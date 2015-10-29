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
		
		# He also sees some placeholder text for the search bar, and a nav
		# bar to navigate to other parts of the website
		inputbox = self.browser.find_element_by_id('inputLarge')
		self.assertEqual(
				inputbox.get_attribute('placeholder'),
				'Enter A Search Term'
		)
		navbar_search = self.browser.find_element_by_id('nav-search').text
		navbar_random = self.browser.find_element_by_id('nav-random').text
		navbar_top = self.browser.find_element_by_id('nav-top').text		
		self.assertIn('Search', navbar_search)
		self.assertIn('Favorites', navbar_random)
		self.assertIn('Top 10', navbar_top)
		
		self.fail('finish me!')
		
if __name__ == '__main__':
    unittest.main(warnings='ignore')