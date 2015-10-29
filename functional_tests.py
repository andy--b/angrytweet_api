from selenium import webdriver
import unittest
import sys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class NavigationTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
		
	def tearDown(self):
		self.browser.quit()
	
	def testNavigation(self):
		# Andy opens up a cool new website he has heard about
		self.browser.get('http://localhost:8000')

		# He notices the page title and header mention mean tweets
		self.assertIn('Meanest Tweet', self.browser.title)
		header_text = self.browser.find_element_by_id('header-text').text
		self.assertIn('WELCOME TO THE MEAN TWEETS', header_text)
		
		self.fail('finish me!')
		
if __name__ == '__main__':
    unittest.main(warnings='ignore')