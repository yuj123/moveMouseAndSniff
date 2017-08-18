import unittest
import logging
from move_sniff import *
import os
import sys

from selenium import webdriver
from selenium.webdriver import ActionChains

class SimpleTestCase(unittest.TestCase):
	snapshot_file = "./snapshot.png"
	template_file = "./small.png"
	result_file   = "./result.png"
	myFunc = "myFunc2"
	myVar = "myvar2"

	@classmethod
	def setUpClass(cls):
		cls.logger = logging.getLogger( "SimpleTestCase" )
	
		# create a new Firefox session
		cls.driver = webdriver.Firefox()
		cls.driver.implicitly_wait(5)
		cls.driver.maximize_window()
		
		# navigate to the application home page
		cls.driver.get("https://github.com/yuj123/moveMouseAndSniff")
		
	def __locate_to_screen(self):
		self.driver.get_screenshot_as_file(self.snapshot_file) 
		return locate_to_screen(self.snapshot_file, self.template_file, self.result_file)	

	def __mouseOver(self, elem):
		builder = ActionChains(self.driver);
		builder.move_to_element(elem).perform();
		
	def test_locate_to_screen(self):
		self.logger.debug("-------------- test_locate_to_screen - begin --------------")

		x, y = self.__locate_to_screen()
		
		self.assertTrue(x > 0)
		self.assertTrue(y > 0)
		self.assertTrue(os.path.exists(self.result_file))
		
		self.logger.debug( "The center point of the sub-image is located at (%d, %d)" % (x, y) )
		
		self.logger.debug("-------------- test_locate_to_screen - end --------------")
		
	def test_move_mouse_to_pos_and_sniff(self):
		self.logger.debug("-------------- test_move_mouse_to_pos_and_sniff - begin --------------")
		
		# 1. capture mouse move event
		capture_mouse_move(self.driver, self.myFunc, self.myVar)
		
		# check mouse position
		self.logger.debug("mouse position before fist move=%s" % str(check_mouse_pos(self.driver, self.myVar)))
		
		# 2. move mouse to an arbitary element to initial the mouse coordinate
		elem = self.driver.find_element_by_tag_name("div")
		self.__mouseOver(elem)
		
		# check mouse position
		self.logger.debug("mouse position of first move=%s" % check_mouse_pos(self.driver, self.myVar),)
		
		# 3. locate to the center of sub-image
		spot = self.__locate_to_screen()
		x = spot[0]
		y = spot[1]
		elem2 = move_mouse_to_pos_and_sniff(self.driver, x, y, self.myVar)
		self.logger.debug("mouse position of second move=%s" % check_mouse_pos(self.driver, self.myVar),)	
		
		self.logger.debug("Resulted element=%s" % elem2)
		self.logger.debug("element text=%s" % elem2.get_attribute("innerText"))
		self.logger.debug("element css=%s" % elem2.get_attribute("className"))
		
		self.logger.debug("-------------- test_move_mouse_to_pos_and_sniff - end --------------")
	
	def test_move_mouse_to_pos_multiply(self):
		self.logger.debug("-------------- test_move_mouse_to_pos_multiply - start --------------")
	
		# 1. capture mouse move event
		capture_mouse_move(self.driver)
		
		# check mouse position
		self.logger.debug("mouse position before fist move=%s" % str(check_mouse_pos(self.driver)))
		
		# 2. move mouse to an arbitary element to initial the mouse coordinate
		elem = self.driver.find_element_by_tag_name("div")
		self.__mouseOver(elem)
		
		# 3. first move 
		move_mouse_to_pos(self.driver, 50, 50)
		self.logger.debug("mouse position before first move=%s" % str(check_mouse_pos(self.driver)))
		self.logger.debug("Resulted element css=%s" % sniff(self.driver).get_attribute("className"))
		
		# 4. second move
		move_mouse_to_pos(self.driver, 50, 100)
		self.logger.debug("mouse position before second move=%s" % str(check_mouse_pos(self.driver)))	
		self.logger.debug("Resulted element css=%s" % sniff(self.driver).get_attribute("className"))

		self.logger.debug("-------------- test_move_mouse_to_pos_multiply - end --------------")		
		
		
	
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
		
if __name__ == "__main__":
	logging.basicConfig( stream=sys.stdout )
	logging.getLogger( "SimpleTestCase" ).setLevel( logging.DEBUG )
	unittest.main()
		