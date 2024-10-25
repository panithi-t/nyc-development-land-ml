import unittest
import pandas as pd
from src.predictor import OptimizedRealEstatePredictor

class TestPredictor(unittest.TestCase):
    def setUp(self):
        self.predictor = OptimizedRealEstatePredictor()
        
    def test_prediction_format(self):
        """Test if prediction returns correct format"""
        test_input = pd.DataFrame({
            'BOROUGH': ['MANHATTAN'],
            'NEIGHBORHOOD': ['SOHO'],
            'LOT_AREA': [4026],
            'LOT_FRONTAGE': [51.75],
            'LOT_TYPE': ['INTERIOR'],
            'ZONING_1': ['M1-5/R10'],
            'ZONING_2': ['NONE'],
            'OVERLAY_1': ['NONE'],
            'OVERLAY_2': ['NONE'],
            'SPECIAL_DISTRICT': ['SNX'],
            'MIH/VIH': ['MIH'],
            'BASE_FAR': [12.0]
        })
        
        result = self.predictor.make_prediction(test_input)
        
        # Check result structure
        self.assertIn('ppzfa', result)
        self.assertIn('total_value', result)
        self.assertIn('confidence_level', result)
        self.assertIn('warnings', result)
        
        # Check value types
        self.assertIsInstance(result['ppzfa'], float)
        self.assertIsInstance(result['total_value'], float)
        self.assertIsInstance(result['confidence_level'], str)
        self.assertIsInstance(result['warnings'], list)

if __name__ == '__main__':
    unittest.main()
