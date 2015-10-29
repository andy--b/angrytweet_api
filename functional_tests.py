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
		
		# He notices the page title and header mention mean search results
		self.assertIn('Search Results', self.browser.title)
		header_text = self.browser.find_element_by_id('header-text').text
		self.assertIn('SEARCH RESULTS', header_text)
		
		# Navbar is still present on this new page
		testNavBar(self)
		
		# He sees a mention of Bacon in uppercase.
		search_term = self.browser.find_element_by_id('search-result-term').text
		self.assertIn('BACON', search_term)
		
		# He sees a tweet, refreshes the page, and sees the same tweet
		tweet_text = self.browser.find_element_by_id('result-tweet-text').text
		self.browser.refresh()
		self.assertEqual(tweet_text, 
						 self.browser.find_element_by_id('result-tweet-text').text)
		
		# Since this is the first of the results list, he sees no "previous" button
		self.assertEqual(0, len(self.browser.find_elements_by_id('result-previous')))
		
		# He sees a next button, hits it, and sees a different tweet-text
		next_button = self.browser.find_element_by_id('result-next')
		next_button.click()
		self.assertNotEqual(tweet_text, 
						 self.browser.find_element_by_id('result-tweet-text').text)
						 
		# Satisfied with his awesome bacon search, Andy now goes to the top 10 page
		navbar_top = self.browser.find_element_by_id('nav-top')
		navbar_top.click()
		
		# He notices the page title and header mention mean search results
		self.assertIn('Top Tweets of All Time', self.browser.title)
		header_text = self.browser.find_element_by_id('header-text').text
		self.assertIn('TOP TWEETS OF ALL TIME', header_text)
		
		# Navbar is still present on this new page
		testNavBar(self)
		
		# He sees 10 top tweets, each inside a jumbotron
		self.assertEqual(10,
						 len(self.browser.find_elements_by_class_name('jumbotron')))
		
		# Finally, he navigates to the random tweet section of the website
		navbar_random = self.browser.find_element_by_id('nav-random')
		navbar_random.click()
		
		# Navbar is still present on this new page
		testNavBar(self)
		
		# He sees a tweet
		self.assertEqual(1,
						 len(self.browser.find_elements_by_class_name('jumbotron')))
						 
		# He likes this tweet, but not enough to vote. He wants another
		tweet_text = self.browser.find_element_by_id('random-tweet-text').text
		another_button = self.browser.find_element_by_id('random-another-btn')
		another_button.click()
		
		# He sees another tweet, still has a navbar
		testNavBar(self)
		self.assertNotEqual(tweet_text,
							self.browser.find_element_by_id('random-tweet-text').text)
		
if __name__ == '__main__':
    unittest.main(warnings='ignore')