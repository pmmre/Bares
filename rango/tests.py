from django.test import TestCase
import unittest
from django.test.client import Client
from django.core.urlresolvers import reverse

# Create your tests here.
class TestStringMethods(unittest.TestCase):

	def test_index(self):
		"""
			Comprobamos que la pagina index funciona mandandole
			una peticion get y comprobando que el codigo de 
			respuesta es correcto (200)
		"""	

		c = Client()

		respose = c.get(reverse('index'))
		self.assertEqual(respose.status_code,200)


	def test_about(self):
		"""
		 	Comprobamos que la pagina about funciona mandandole
		 	una peticion get y comprobando que el codigo de 
		 	respuesta es correcto (200)
		"""	
		c = Client()
		
		respose = c.get(reverse('about'))
		self.assertEqual(respose.status_code,200)



if __name__ == '__main__':
	unittest.main()