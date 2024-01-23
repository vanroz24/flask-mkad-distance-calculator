# app/mkad_distance_calculator/routes.py
from flask import Blueprint, jsonify
from geopy import distance, geocoders
from shapely.geometry import Point, Polygon
import logging
from config import API_KEY

MDCalculator = Blueprint('MDCalculator', __name__, url_prefix='/mkad')

Yandex_API = geocoders.Yandex(API_KEY)

mkad_polygon_coordinates = [
    (55.911431, 37.582629),
    (55.895984, 37.640014),
    (55.893297, 37.702181),
    (55.823367, 37.836079),
    (55.710812, 37.838470),
    (55.695532, 37.828063),
    (55.655540, 37.838470),
    (55.572484, 37.671949),
    (55.596064, 37.506468),
    (55.743703, 37.367006),
    (55.790642, 37.372210),
    (55.803540, 37.387821),
    (55.844552, 37.390943),
    (55.867967, 37.404473),
    (55.887274, 37.486693),
    (55.904818, 37.527283),
]

mkad_polygon = Polygon(mkad_polygon_coordinates)

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@MDCalculator.route('/calculate_distance/<end_address>', methods=['GET'])
def calculate_distance(end_address):
    """Calculate the distance between the given address and MKAD."""
    try:
        end_location = Yandex_API.geocode(end_address, lang="en")

        if end_location:
            end_point = Point(end_location.latitude, end_location.longitude)

            if end_point.within(mkad_polygon):
                logging.info('Address is inside MKAD: %s', end_address)
                return jsonify({'message': 'Address is inside MKAD'})
            
            nearest_mkad_point = min(
                mkad_polygon_coordinates,
                key=lambda mkad_point: distance.distance(mkad_point, end_point.coords).kilometers
            )

            start_point = Point(nearest_mkad_point[0], nearest_mkad_point[1])

            distance_km = distance.distance(start_point.coords, end_point.coords).kilometers

            logging.info('Calculated distance for %s: %f km', end_address, distance_km)

            return jsonify({'distance_km': distance_km})
        
        else:
            logging.error('Location not found for address: %s', end_address)
            return jsonify({'error': 'Location not found'}), 404
        
    except Exception as e:
        logging.error('Error while processing request: %s', str(e))
        return jsonify({'error': str(e)}), 500


@MDCalculator.route('/')
def get_mkad():
    """Get the coordinates of MKAD."""
    try:
        formatted_mkad_points = [{'latitude': lat, 'longitude': lon} for lat, lon in mkad_polygon_coordinates]
        return jsonify({'mkad_points': formatted_mkad_points})
    
    except Exception as e:
        logging.error('Error while retrieving MKAD points: %s', str(e))
        return jsonify({'error': str(e)}), 500
