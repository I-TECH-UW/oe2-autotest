import datetime
from datetime import timedelta
from random import randint
import selenium, time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import api

class ConfigItems(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.connecting()

    def connecting(self):
        "This method allows us to connect to the site"
        driver = self.driver
        driver.get('http://test.openelisci.org')
        name = driver.find_element_by_id("loginName")
        name.clear()
        name.send_keys('admin')
        time.sleep(2)
        password=driver.find_element_by_id("password")
        password.clear()
        password.send_keys('adminADMIN!')
        time.sleep(2)
        button = driver.find_element_by_id("submitButton")
        button.click()

    def gotoreasonexisting(self):
        driver = self.driver
        driver.find_element_by_id("menu_administration").click()

    @api.assert_capture()
    def test_additional(self):
        driver = self.driver
        self.gotoreasonexisting()
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_administration")
        firstLevelMenu.click()
        time.sleep(5)
        driver.find_element_by_link_text("Printed Reports Configuration").click()
        time.sleep(2)
        driver.find_element_by_id("selectedIDs1").click()
        time.sleep(2)
        driver.find_element_by_id("edit").click()
        time.sleep(2)



    def tearDown(self):
        self.driver.close()
        self.driver.quit()