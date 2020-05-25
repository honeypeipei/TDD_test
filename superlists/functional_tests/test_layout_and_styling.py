from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import WebDriverException 
import unittest
import time
# import sys
import os
from unittest import skip
from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):

	def test_layout_and_styling(self):
		self.browser.get(self.live_server_url)
		self.browser.set_window_size(1024,768)
		#she starts a new list and sees the input is nicely
		#centered there too
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('testing')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(3)
		self.wait_for_row_in_list_table('1: testing')
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(
			inputbox.location['x'] + inputbox.size['width'] /2,
			512,
			delta = 10
		)
