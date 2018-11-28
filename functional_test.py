from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('My To-Do List', header_text)
      
    inputbox = self.browser.find_element_by_id('id_new_item')
    self.assertEqual(
      inputbox.get_attribute('placeholder'),
      'Enter a to-do item'
    )
    #Type in box to enter new todo item
    inputbox.send_keys('Buy peacock feathers')

    #Hit enter updates page with input
    inputbox.send_keys(keys.ENTER)
    time.sleep(1)
    
    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertTrue(
      any(row.text == '1: Buy peacock feathers' for row in rows)
    )

    #Text box remains for new item
    self.fail('Finish the test!')

#Make project specific url and remember lsit

#Notify user as to the url

if __name__ == '__main__':
  unittest.main()