# NYC Development Site PPZFA Predictor

A machine learning model that predicts Price Per Zoning Floor Area (PPZFA) for development sites in NYC, trained on actual market transactions. The model analyzes basic site characteristics and zoning parameters to estimate land values.

## What This Model Actually Does

### Core Function
Predicts PPZFA based on:
```python
Required Inputs:
- BOROUGH (e.g., 'MANHATTAN')
- NEIGHBORHOOD (e.g., 'SOHO')
- LOT AREA (in square feet)
- LOT FRONTAGE (in feet)
- LOT TYPE (e.g., 'INTERIOR')
- ZONING 1 (e.g., 'M1-5/R10')
- BASE FAR (e.g., 12.0)

Optional Inputs:
- ZONING 2
- OVERLAY 1
- OVERLAY 2
- SPECIAL DISTRICT (e.g., 'SNX')
- MIH/VIH
```

### Outputs
```python
Results = {
    'ppzfa': Predicted price per buildable SF
    'total_value': ppzfa * lot_area * base_far
    'confidence_level': 'High'/'Medium'/'Low'
    'warnings': List of any data validation warnings
}
```

## Quick Start

1. **Installation**
```bash
git clone https://github.com/yourusername/nyc-development-land-ml.git
cd nyc-development-land-ml
pip install -r requirements.txt
```

2. **Data Setup**
- Place TRANSACTIONS-PT.csv in the `data/` directory
- Note: Data file not included in repository for privacy

3. **Usage Example**
```python
site_data = {
    'BOROUGH': 'MANHATTAN',
    'NEIGHBORHOOD': 'SOHO',
    'LOT AREA': 4026,
    'LOT FRONTAGE': 51.75,
    'LOT TYPE': 'INTERIOR',
    'ZONING 1': 'M1-5/R10',
    'ZONING 2': 'NONE',
    'OVERLAY 1': 'NONE',
    'OVERLAY 2': 'NONE',
    'SPECIAL DISTRICT': 'SNX',
    'MIH/VIH': 'MIH',
    'BASE FAR': 12.0
}

prediction = predictor.make_prediction(site_data)
print(f"Predicted PPZFA: ${prediction['ppzfa']:.2f}")
print(f"Total Value: ${prediction['total_value']:,.2f}")
print(f"Confidence Level: {prediction['confidence_level']}")
```

## Key Features

### Data Validation
- Checks if inputs are within historical ranges
- Flags unusual or outlier values
- Provides confidence scoring based on input validity

### Value Calculation
- Predicts PPZFA based on trained data
- Calculates total site value using:
  - Predicted PPZFA
  - Lot area
  - Base FAR

### Machine Learning
- Random Forest algorithm
- Feature importance analysis
- Cross-validation
- Outlier detection

## Important Notes

### Model Limitations
- Predictions based solely on provided input parameters
- Does not consider:
  - Current market conditions
  - Recent zoning changes
  - Site-specific constraints
  - Development costs
  - Construction feasibility

### Professional Usage
This tool should be used as one of many inputs in a comprehensive site analysis, alongside:
- Professional appraisals
- Market research
- Zoning analysis
- Due diligence
- Legal review

## Technical Requirements
- Python 3.8+
- pandas
- numpy
- scikit-learn

## Repository Structure
```
nyc-development-land-ml/
├── data/                   # Place TRANSACTIONS-PT.csv here
├── notebooks/             # Analysis examples
├── src/                   # Core model code
├── tests/                # Test suite
└── docs/                 # Documentation
```

## License & Usage Restrictions
```
© 2024 Panithi Tawethipong
All Rights Reserved.

This model provides estimated values based on historical data.
Results should be verified through professional due diligence.
```

For inquiries:
ptawethi@pratt.edu

---
*Note: This model provides data-driven PPZFA predictions based on basic site characteristics. Results should be used as one of many tools in professional development analysis.*
