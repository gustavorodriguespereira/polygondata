from shapely.geometry import shape
from shapely.geometry import Polygon
import json
from area import area
from geojson import Polygon
import geodaisy.converters as convert
import geojson

if __name__ == '__main__':
    print('PyCharm')

    with open('data/f67cfebf-963e-4ff3-a9a3-560bb3324943.json') as file:
        raw_json = json.load(file)

    for feature in raw_json['features']:
        polygon_geometry = feature['geometry']
        polygon_area = area(polygon_geometry)
        key = 'area'
        value = polygon_area

        dict = {key: value}
        feature.update(dict)
        # print(raw_json)

    for feature in raw_json['features']:
        geom = feature['geometry']
        centroid = shape(geom).centroid
        centroid = centroid.__geo_interface__
        feature['geometry'] = centroid

    print(raw_json)
    with open('data/updated_point_data.json', 'w') as file:
        raw_json = json.dump(raw_json, file)