import json
from django.urls import reverse
from django.test import TestCase
from django.core.management import call_command
from accounts.models import Person

class PersonModelTestCase(TestCase):
    fixtures = ['people_data.json']
    
    def test_gen_frequency_returns_dict(self):
        freq = Person.gen_frequency('sexo')
        self.assertIsInstance(freq, dict)

    def test_gen_distribution_returns_dist(self):
        dist = Person.gen_distribution('sexo')
        acc = sum(dist.values())
        self.assertIsInstance(dist, dict)
        self.assertAlmostEqual(acc, 1)

class PersonViewTestCase(TestCase):
    fixtures = ['people_data.json']

    def test_get_olders_returns_n(self):
        response = self.client.get(reverse('olders', args=[5]))
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(content), 5)

    def test_get_youngers_returns_n(self):
        response = self.client.get(reverse('youngers', args=[5]))
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(content), 5)
    
    def test_get_gender_distribution_returns_gender(self):
        response = self.client.get(reverse('gender_dist'))
        content = json.loads(response.content)
        content = list(content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content, ['Masculino', 'Feminino'])
    
    def test_get_bloodtype_frequency_is_dict(self):
        response = self.client.get(reverse('bloodtype_freq'))
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(content, dict)
    
    def test_get_person_by_cpf_returns_nothing(self):
        response = self.client.get(reverse('person_by_cpf', args=["?"]))
        content = json.loads(response.content)
        self.assertEqual(content, [])

    def test_get_people_returns_list(self):
        response = self.client.get(reverse('people'))
        content = json.loads(response.content)
        self.assertIsInstance(content, list)

    def test_get_people_by_name_returns_nothing(self):
        path = reverse('people_by_name') + '?q=!'
        response = self.client.get(path)
        content = json.loads(response.content)
        print(content)
        self.assertEqual(content, [])

# References
# https://docs.djangoproject.com/en/3.2/topics/testing/overview/
# https://docs.djangoproject.com/en/3.2/intro/tutorial05/