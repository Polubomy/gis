import pprint
import unittest
import create_place

class test_create_place(unittest.TestCase):

    def test_place_valid(self):
        data_1 = {
            'title': 'Test_1',
            'lat': 55.028254,
            'lon': 82.918501,
            'color': 'BLUE'
        }

        response_data = create_place.create_place(data_1)
        pprint.pprint(response_data)

        self.assertEqual(response_data['title'], 'Test_1')
        self.assertEqual(response_data['lat'], 55.028254)
        self.assertEqual(response_data['lon'], 82.918501)
        self.assertEqual(response_data['color'], 'BLUE')

    def test_invalid_title(self):
        data_2 = {
            'title': '',
            'lat': 55.028254,
            'lon': 82.918501,
            'color': 'BLUE'
        }

        response_data = create_place.create_place(data_2)
        pprint.pprint(response_data)

        self.assertEqual(response_data['title'], '')
        self.assertEqual(response_data['lat'], 55.028254)
        self.assertEqual(response_data['lon'], 82.918501)
        self.assertEqual(response_data['color'], 'BLUE')

    def test_invalid_lat(self):
        data_3 = {
            'title': 'Test_3',
            'lat': 91,
            'lon': 82.918501,
            'color': 'BLUE'
        }

        response_data = create_place.create_place(data_3)
        pprint.pprint(response_data)

        self.assertEqual(response_data['title'], 'Test_3')
        self.assertEqual(response_data['lat'], 91)
        self.assertEqual(response_data['lon'], 82.918501)
        self.assertEqual(response_data['color'], 'BLUE')

    def test_invalid_lon(self):
        data_4 = {
            'title': 'Test_4',
            'lat': 55.028254,
            'lon': 181,
            'color': 'BLUE'
        }

        response_data = create_place.create_place(data_4)
        pprint.pprint(response_data)

        self.assertEqual(response_data['title'], 'Test_4')
        self.assertEqual(response_data['lat'], 55.028254)
        self.assertEqual(response_data['lon'], 82.918501)
        self.assertEqual(response_data['color'], 'BLUE')

    def test_invalid_color(self):
        data_5 = {
            'title': 'Test_5',
            'lat': 55.028254,
            'lon': 82.918501,
            'color': 'Invalid'
        }

        response_data = create_place.create_place(data_5)
        pprint.pprint(response_data)

        self.assertEqual(response_data['title'], 'Test_5')
        self.assertEqual(response_data['lat'], 55.028254)
        self.assertEqual(response_data['lon'], 82.918501)
        self.assertEqual(response_data['color'], 'Invalid')

    def test_invalid_without_color(self):
        data_6 = {
            'title': 'Test_6',
            'lat': 55.028254,
            'lon': 82.918501,
        }

        response_data = create_place.create_place(data_6)
        pprint.pprint(response_data)

        self.assertEqual(response_data['title'], 'Test_6')
        self.assertEqual(response_data['lat'], 55.028254)
        self.assertEqual(response_data['lon'], 82.918501)
        self.assertEqual(response_data['color'], None)

if __name__ == '__main__':
    unittest.main()