# Development Environment Setup

## Prerequisites
- Python 3.8 or higher
- Git (for version control)
- Your TRANSACTIONS-PT.csv data file

## Local Setup Steps

1. Clone the repository
```bash
git clone https://github.com/yourusername/nyc-development-land-ml.git
cd nyc-development-land-ml
```

2. Create virtual environment
```bash
# Create venv
python -m venv venv

# Activate venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

3. Install requirements
```bash
pip install -r requirements.txt
```

4. Data Setup
- Place your TRANSACTIONS-PT.csv file in the `data/` directory

5. Test the installation
```bash
python src/main.py
```

## Example Input
```
Enter BOROUGH: MANHATTAN
Enter NEIGHBORHOOD: SOHO
Enter LOT AREA (in square feet): 4026
Enter LOT FRONTAGE (in feet): 51.75
Enter LOT TYPE: INTERIOR
Enter ZONING 1: M1-5/R10
Enter ZONING 2 (or press Enter if none): 
Enter OVERLAY 1 (or press Enter if none): 
Enter OVERLAY 2 (or press Enter if none): 
Enter SPECIAL DISTRICT (or press Enter if none): SNX
Enter MIH/VIH: MIH
Enter BASE FAR: 12
```

## Troubleshooting
- If you get a "file not found" error, check if TRANSACTIONS-PT.csv is in the data/ directory
- For package errors, try: `pip install --upgrade -r requirements.txt`
- Make sure your Python version is 3.8 or higher: `python --version`
