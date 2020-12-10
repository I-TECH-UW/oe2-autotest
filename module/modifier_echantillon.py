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

class ModifierEchantillon(unittest.TestCase):

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
    def test_action(self):
        driver = self.driver
        self.gotoreasonexisting()
        action = ActionChains(driver)
        """Click on the Admin tab => Gestion des Tests in the left hand menu """
        firstLevelMenu = driver.find_element_by_id("menu_administration")
        action.move_to_element(firstLevelMenu).perform()
        firstLevelMenu.click()
        time.sleep(5)
        driver.find_element_by_link_text("Test Management").click()
        """rename  existing sample types"""
        driver.find_element_by_xpath("//input[@value='Rename Existing Sample Types']").click()
        time.sleep(2)
        """click on test section that you would like  change"""
        driver.find_element_by_xpath("//input[@value='Plasma']").click()
        time.sleep(5)
        """enter the word or phrase word english or french"""
        lab = driver.find_element_by_name("nameEnglish")
        lab.send_keys('Plasma')
        time.sleep(2)
        fr = driver.find_element_by_name("nameFrench")
        fr.send_keys('Plasma')
        """click on save """
        driver.find_element_by_xpath("//input[@value='Save']").click()
        time.sleep(2)
        """click on accept """
        driver.find_element_by_xpath("//input[@value='Accept']").click()
        time.sleep(2)
        """repeat step 2-5"""
        # firstLevelMenu = driver.find_element_by_id("menu_administration")
        # firstLevelMenu.click()
        # time.sleep(5)
        # driver.find_element_by_link_text("Test Management").click()
        # driver.find_element_by_xpath("//input[@value='Rename Existing Sample Types']").click()
        driver.find_element_by_xpath("//input[@value='Plasma']").click()
        time.sleep(2)
        lab = driver.find_element_by_name("nameEnglish")
        lab.send_keys('Plasma')
        time.sleep(2)
        fr = driver.find_element_by_name("nameFrench")
        fr.send_keys('Plasma')
        time.sleep(2)
        """click on save """
        driver.find_element_by_xpath("//input[@value='Save']").click()
        """ click on reject"""
        driver.find_element_by_xpath("//input[@value='Reject']").click()
        time.sleep(2)
        """click on cancel"""
        driver.find_element_by_xpath("//input[@value='Cancel']").click()
        time.sleep(2)

    def tearDown(self):
       self.driver.close()
       self.driver.quit()