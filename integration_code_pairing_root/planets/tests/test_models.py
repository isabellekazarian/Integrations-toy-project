from django.test import TestCase
from planets.models import Planet

class PlanetTestCase(TestCase):
    def setUp(self):
        super().setUp()

    def test_planet_to_dict_no_id(self):
        p = Planet(
            id=1,
            planet_id=2,
            name='Test Planet',
            diameter=123456,
            rotation_period=1,
            orbital_period=365,
            gravity='1',
            population=6000000,
            climate='tundra,desert,rainforest',
            terrain='flat',
            surface_water=8
        )
        p_dict = p.to_dict()
        self.assertEqual(p.id, 1)
        self.assertNotIn('id', p_dict)
    
    def test_planet_to_dict(self):
        input_dict = {
            'planet_id': 2,
            'name': 'Test Planet',
            'diameter': 123456,
            'rotation_period': 1,
            'orbital_period': 365,
            'gravity': 1,
            'population': 6000000,
            'climate': 'tundra,desert,rainforest',
            'terrain': 'flat',
            'surface_water': 8
        }

        expected_dict = {
            'planet_id': 2,
            'name': 'Test Planet',
            'diameter': 123456 * .6214,
            'rotation_period': 1,
            'orbital_period': 365,
            'gravity': 1,
            'population': 6000000,
            'climate': 'tundra,desert,rainforest',
            'terrain': 'flat',
            'surface_water': 8
        }

        p = Planet(id=1, **input_dict)
        p_dict = p.to_dict()

        self.assertEqual(p.id, 1)
        self.assertEqual(p_dict, expected_dict)