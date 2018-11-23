from selenium import webdriver
import unittest

# browser = webdriver.Firefox()

# browser.get('http://localhost:8000')

# assert 'My To-Do List' in browser.title

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
	    self.browser = webdriver.Firefox()
		
	def tearDown(self):
	    self.browser.quit()
		
	def test_can_start_list_and_retrieve_it_later(self):
	    self.browser.get('http://localhost:8000')
	    self.assertIn('My To-Do List', self.browser.title)
	    self.fail('Finish the test!')

#Type in box to enter new todo item

#Hit enter updates page with input

#Text box remains for new item

#Make project specific url and remember lsit

#Notify user as to the url

if __name__ == '__main__':
  unittest.main()