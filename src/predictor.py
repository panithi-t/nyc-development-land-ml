import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

class OptimizedRealEstatePredictor:
    def __init__(self, data_path="TRANSACTIONS-PT.csv"):
        self.data_path = data_path
        self.pipeline = None
        self.numeric_features = ['LOT AREA', 'LOT FRONTAGE', 'BASE FAR']
        self.categorical_features = ['BOROUGH', 'NEIGHBORHOOD', 'LOT TYPE',
                                   'ZONING 1', 'ZONING 2', 'OVERLAY 1', 'OVERLAY 2', 
                                   'SPECIAL DISTRICT', 'MIH/VIH']
        self.features = self.numeric_features + self.categorical_features
        
        # Store feature importance
        self.feature_importance = None
        
        # Store training data statistics
        self.data_stats = {}
        
    def train_model(self):
        try:
            # Load the dataset
            print("Loading data...")
            data = pd.read_csv(self.data_path)
            print(f"Loaded {len(data)} samples")
            
            # Store data statistics for validation
            for col in self.numeric_features:
                data[col] = pd.to_numeric(data[col], errors='coerce')
                self.data_stats[col] = {
                    'median': data[col].median(),
                    'mean': data[col].mean(),
                    'std': data[col].std(),
                    'min': data[col].min(),
                    'max': data[col].max()
                }
                data[col] = data[col].fillna(data[col].median())
                
            for col in self.categorical_features:
                data[col] = data[col].fillna('NONE')
                self.data_stats[col] = {
                    'unique_values': list(data[col].unique())
                }
            
            # Store PPZFA statistics
            self.data_stats['PPZFA'] = {
                'mean': data['PPZFA'].mean(),
                'std': data['PPZFA'].std(),
                'min': data['PPZFA'].min(),
                'max': data['PPZFA'].max()
            }
            
            # Prepare features and target
            X = data[self.features]
            y = data['PPZFA']
            
            # Create optimized preprocessing pipeline
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', StandardScaler(), self.numeric_features),
                    ('cat', OneHotEncoder(handle_unknown='ignore'), self.categorical_features)
                ]
            )
            
            # Create and train pipeline with optimized Random Forest
            self.pipeline = Pipeline([
                ('preprocessor', preprocessor),
                ('model', RandomForestRegressor(
                    n_estimators=200,          # More trees for better stability
                    max_depth=None,            # Allow full depth for complex patterns
                    min_samples_split=2,       # Default split criterion
                    min_samples_leaf=1,        # Default leaf criterion
                    max_features='sqrt',       # Recommended for regression
                    n_jobs=-1,                 # Use all CPU cores
                    random_state=42,           # For reproducibility
                    bootstrap=True,            # Enable bootstrapping
                    oob_score=True             # Calculate out-of-bag score
                ))
            ])
            
            # Train the model
            print("Training model...")
            self.pipeline.fit(X, y)
            
            # Calculate feature importance
            self.calculate_feature_importance()
            
            # Print model information
            rf_model = self.pipeline.named_steps['model']
            print("\nModel Information:")
            print(f"Out-of-bag Score: {rf_model.oob_score_:.3f}")
            print(f"Number of Trees: {rf_model.n_estimators}")
            
            print("\nTop 10 Most Important Features:")
            for feature, importance in self.feature_importance[:10]:
                print(f"{feature}: {importance:.3f}")
            
            print("\nValue Ranges in Training Data:")
            print(f"PPZFA: ${self.data_stats['PPZFA']['min']:.2f} to ${self.data_stats['PPZFA']['max']:.2f}")
            for feature in self.numeric_features:
                print(f"{feature}: {self.data_stats[feature]['min']:.2f} to {self.data_stats[feature]['max']:.2f}")
            
            return True
            
        except Exception as e:
            print(f"Error details: {str(e)}")
            raise Exception(f"Error training model: {str(e)}")
            
    def calculate_feature_importance(self):
        """Calculate and store feature importance scores"""
        if self.pipeline is None:
            return
            
        # Get feature names after preprocessing
        numeric_features = self.numeric_features
        categorical_features = self.pipeline.named_steps['preprocessor'].named_transformers_['cat'].get_feature_names_out(self.categorical_features)
        all_features = list(categorical_features) + numeric_features
        
        # Get importance scores
        importances = self.pipeline.named_steps['model'].feature_importances_
        
        # Combine and sort
        self.feature_importance = sorted(zip(all_features, importances), key=lambda x: x[1], reverse=True)

    def validate_input(self, input_data):
        """Validate input data against training data statistics"""
        warnings = []
        
        for feature in self.numeric_features:
            value = input_data[feature].iloc[0]
            stats = self.data_stats[feature]
            
            if value < stats['min']:
                warnings.append(f"{feature} ({value}) is below training data minimum ({stats['min']:.2f})")
            elif value > stats['max']:
                warnings.append(f"{feature} ({value}) is above training data maximum ({stats['max']:.2f})")
            elif abs(value - stats['mean']) > 3 * stats['std']:
                warnings.append(f"{feature} ({value}) is more than 3 standard deviations from mean")
                
        return warnings

    def get_user_input(self):
        print("\n=== Real Estate Value Predictor ===")
        print("\nPlease provide the following information:")
        
        try:
            input_data = {
                'BOROUGH': input("Enter BOROUGH: ").upper(),
                'NEIGHBORHOOD': input("Enter NEIGHBORHOOD: ").upper(),
                'LOT AREA': float(input("Enter LOT AREA (in square feet): ") or 0),
                'LOT FRONTAGE': float(input("Enter LOT FRONTAGE (in feet): ") or 0),
                'LOT TYPE': input("Enter LOT TYPE: ").upper(),
                'ZONING 1': input("Enter ZONING 1: ").upper(),
                'ZONING 2': input("Enter ZONING 2 (or press Enter if none): ").upper() or "NONE",
                'OVERLAY 1': input("Enter OVERLAY 1 (or press Enter if none): ").upper() or "NONE",
                'OVERLAY 2': input("Enter OVERLAY 2 (or press Enter if none): ").upper() or "NONE",
                'SPECIAL DISTRICT': input("Enter SPECIAL DISTRICT (or press Enter if none): ").upper() or "NONE",
                'MIH/VIH': input("Enter MIH/VIH: ").upper(),
                'BASE FAR': float(input("Enter BASE FAR: ") or 0)
            }
            
            return pd.DataFrame([input_data])
                
        except ValueError as e:
            raise ValueError(f"Invalid input: {str(e)}")

    def make_prediction(self, user_input):
        try:
            # Validate input
            warnings = self.validate_input(user_input)
            
            # Make prediction
            predicted_ppzfa = self.pipeline.predict(user_input)[0]
            
            # Calculate confidence based on input validation
            confidence_level = "High"
            if len(warnings) == 1:
                confidence_level = "Medium"
            elif len(warnings) > 1:
                confidence_level = "Low"
            
            # Calculate total value
            lot_area = user_input['LOT AREA'].values[0]
            base_far = user_input['BASE FAR'].values[0]
            base_zfa = lot_area * base_far
            total_value = predicted_ppzfa * base_zfa
            
            return {
                'ppzfa': predicted_ppzfa,
                'total_value': total_value,
                'confidence_level': confidence_level,
                'warnings': warnings
            }
        except Exception as e:
            raise Exception(f"Error making prediction: {str(e)}")
