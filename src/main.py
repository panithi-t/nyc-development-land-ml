from predictor import OptimizedRealEstatePredictor

def main():
    predictor = OptimizedRealEstatePredictor()
    
    print("Loading and training the model...")
    try:
        predictor.train_model()
        print("\nModel is ready for predictions!")
        
        while True:
            user_input = predictor.get_user_input()
            prediction = predictor.make_prediction(user_input)
            
            print("\n=== Prediction Results ===")
            print(f"Predicted PPZFA: ${prediction['ppzfa']:.2f}")
            print(f"Total Value: ${prediction['total_value']:,.2f}")
            print(f"Confidence Level: {prediction['confidence_level']}")
            
            if prediction['warnings']:
                print("\nWarnings:")
                for warning in prediction['warnings']:
                    print(f"- {warning}")
            
            if input("\nWould you like to make another prediction? (yes/no): ").lower() != 'yes':
                break
                
        print("\nThank you for using the Real Estate Value Predictor!")
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        print("Please ensure the dataset file is available and try again.")

if __name__ == "__main__":
    main()
