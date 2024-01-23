# Flask MKAD Distance Calculator

This Flask web application calculates the distance between a given address and the Moscow Ring Road (MKAD). It also provides functionality to check if an address is inside MKAD and retrieve MKAD coordinates.

## Features

- Calculate the distance between an input address and MKAD.
- Check if an address is inside MKAD.
- Retrieve the coordinates of MKAD.

## Getting Started

### Prerequisites

- Python 3.x
- Yandex API Key (See [Yandex Geocoder API](https://yandex.com/dev/maps/geocoder/))

### Setup

1. Clone the repository:
```
git clone https://github.com/your-username/flask-mkad-distance-calculator.git
cd flask-mkad-distance-calculator
```

2. Create a virtual environment (optional but recommended):
```
python -m venv .venv
source venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Add your Yandex API key in config.py

5. Run the application:
```
python run.py
```
The app will be available at http://localhost:5000

## Usage
### Calculate Distance

```
curl http://localhost:5000/mkad/calculate_distance/Saratov
```

### Get MKAD Coordinates
```
curl http://localhost:5000/mkad/
```

## Testing
Run the tests using pytest:

```
pytest
```

The tests cover scenarios of checking if an address is inside MKAD, calculating distances, and handling invalid addresses.

## Logging
Application logs are stored in app.log