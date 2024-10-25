# NYC Development Land Value Prediction Methodology

## Overview
This model predicts Price Per Zoning Floor Area (PPZFA) for development sites in NYC using machine learning, specifically optimized Random Forest regression.

## Core Components

### 1. Input Features

#### Physical Characteristics
- Lot Area (SF)
- Lot Frontage (feet)
- Lot Type (Interior/Corner/Through)

#### Zoning Parameters
- Base FAR
- Zoning District (Primary)
- Zoning District (Secondary)
- Overlay Districts
- Special Districts
- MIH/VIH Designation

#### Location Data
- Borough
- Neighborhood

### 2. Prediction Pipeline

#### Data Preprocessing
```python
- Numeric Features: Standard scaling
  - Lot Area
  - Lot Frontage
  - Base FAR

- Categorical Features: One-hot encoding
  - Borough
  - Neighborhood
  - Zoning Districts
  - Special Districts
```

#### Model Architecture
- Algorithm: Random Forest Regressor
- Trees: 200
- Features: sqrt(n_features)
- Bootstrap: Enabled
- Cross-validation: Out-of-bag score

### 3. Validation System

#### Input Validation
- Range checks against training data
- Statistical outlier detection
- Missing value handling

#### Confidence Scoring
- High: All inputs within normal ranges
- Medium: 1 parameter outside normal range
- Low: Multiple parameters outside ranges

## Prediction Process

1. **Data Input**
   - User provides site characteristics
   - System validates inputs

2. **Processing**
   - Feature scaling
   - Categorical encoding
   - Model prediction

3. **Output Generation**
   - PPZFA prediction
   - Total value calculation
   - Confidence assessment
   - Warning generation

## Usage Considerations

### Strengths
- Based on actual NYC transactions
- Considers zoning parameters
- Built-in validation
- Confidence metrics

### Limitations
- Based on historical data only
- Does not consider:
  - Future market conditions
  - Site-specific constraints
  - Development costs
  - Construction feasibility

## Technical Implementation

```python
# Core prediction flow
prediction = predictor.make_prediction({
    'BOROUGH': borough,
    'NEIGHBORHOOD': neighborhood,
    'LOT_AREA': lot_area,
    'LOT_FRONTAGE': frontage,
    'LOT_TYPE': lot_type,
    'ZONING_1': zoning,
    'BASE_FAR': far
})

# Results include
{
    'ppzfa': predicted_price,
    'total_value': total_site_value,
    'confidence_level': confidence,
    'warnings': validation_warnings
}
```

## Data Sources
- Training data from NYC Department of Finance
- Transaction period: [January 2018 - September 2024]
- Geographic coverage: All NYC boroughs

## Validation Metrics
- Feature importance analysis
- Out-of-bag score validation
- Input range validation
- Statistical outlier detection

---

Note: This methodology document outlines the technical approach. Results should be used as one of many inputs in professional development analysis.
