from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
		# Test navbar on each page
		def testNavBar(self):
			navbar_search = self.browser.find_element_by_id('nav-search').text
			navbar_random = self.browser.find_element_by_id('nav-random').text
			navbar_top = self.browser.find_element_by_id('nav-top').text		
			self.assertIn('Search', navbar_search)
			self.assertIn('Favorites', navbar_random)
			self.assertIn('Top 10', navbar_top)
			
		# Andy opens up a cool new website he has heard about
		self.browser.get('http://localhost:8000')
		self.browser.set_window_size(1024,768)
		
		# He sees a navbar at the top with some options
		testNavBar(self)

		# He notices the page title and header mention mean tweets
		self.assertIn('Meanest Tweet', self.browser.title)
		header_text = self.browser.find_element_by_id('header-text').text
		self.assertIn('WELCOME TO THE MEAN TWEETS', header_text)
		
		# He also sees a search bar, centered, with some placeholder text
		inputbox = self.browser.find_element_by_id('inputLarge')
		self.assertEqual(
				inputbox.get_attribute('placeholder'),
				'Enter A Search Term'
		)
		self.assertAlmostEqual(
			inputbox.location['x'] + inputbox.size['width'] / 2,
			512,
			delta=20
		)
		
		# He enteres the search term "Bacon", which sends him to a new page
		# with a tweet about bacon.
		inputbox.send_keys('Bacon')
		inputbox.send_keys(Keys.ENTER)
		
		# Navbar is still present on this new page
		testNavBar(self)
		
		# He sees a mention of Bacon in uppercase.
		search_term = self.browser.find_element_by_id('search-result-term').text
		self.assertIn('BACON', search_term)
		
		self.fail('finish me!')
		
if __name__ == '__main__':
    unittest.main(warnings='ignore')