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

class Ordonnances(unittest.TestCase):

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
        driver.find_element_by_id("menu_sample").click()
    
    @api.assert_capture()
    def test_01_action(self):
        driver = self.driver
        self.gotoreasonexisting()
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_sample")
        action.move_to_element(firstLevelMenu).perform()
        time.sleep(2)
        secondLevelMenu = driver.find_element_by_id("menu_sample_batch_entry")
        action.move_to_element(secondLevelMenu).perform()
        secondLevelMenu.click()
        time.sleep(2)
        # firstLevelMenu = driver.find_element_by_id("menu_administration")
        # action.move_to_element(firstLevelMenu).perform()
        # firstLevelMenu.click()
        # time.sleep(5)
        # driver.find_element_by_link_text("Test Management").click()
        # """rename  existing sample types"""
        # driver.find_element_by_xpath("//input[@value='Rename Existing Sample Types']").click()
        # time.sleep(2)
    
    @api.assert_capture()
    def test_02_current_received(self):
        driver = self.driver
        self.gotoreasonexisting()
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_sample")
        action.move_to_element(firstLevelMenu).perform()
        time.sleep(2)
        secondLevelMenu = driver.find_element_by_id("menu_sample_batch_entry")
        action.move_to_element(secondLevelMenu).perform()
        secondLevelMenu.click()
        time.sleep(2)
        dat2 = driver.find_element_by_id("receivedDateForDisplay")
        dat2.clear()
        dat2.send_keys('jj/hh/aaaajj')
        driver.find_element_by_id("receivedTime").click()
        """enter date in the future"""
        dat2 = driver.find_element_by_id("receivedDateForDisplay")
        dat2.clear()
        next_day = (datetime.datetime.now()+ timedelta(days=1)).strftime("%d/%m/%Y")
        dat2.send_keys(next_day)
        driver.find_element_by_id("receivedTime").click()
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')
            alert = driver.switch_to.alert
            alert.accept()
            assert  True
        except:
            assert False
        time.sleep(5)

    @api.assert_capture()
    def test_03_add_samples(self):
        driver = self.driver
        self.gotoreasonexisting()
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_sample")
        action.move_to_element(firstLevelMenu).perform()
        time.sleep(2)
        secondLevelMenu = driver.find_element_by_id("menu_sample_batch_entry")
        action.move_to_element(secondLevelMenu).perform()
        secondLevelMenu.click()
        time.sleep(2)
        select_panel_type= driver.find_element_by_id("sampleTypeSelect")
        options_panel_type = select_panel_type.find_elements_by_tag_name("option")
        options_panel_type[2].click()
        time.sleep(3)
        driver.find_element_by_id("panel_0").click()
        time.sleep(5)

    @api.assert_capture()
    def test_04_configure(self):
        driver = self.driver
        self.gotoreasonexisting()
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_sample")
        action.move_to_element(firstLevelMenu).perform()
        time.sleep(2)
        secondLevelMenu = driver.find_element_by_id("menu_sample_batch_entry")
        action.move_to_element(secondLevelMenu).perform()
        secondLevelMenu.click()
        time.sleep(2)
        select_panel_type = driver.find_element_by_id("sampleTypeSelect")
        options_panel_type = select_panel_type.find_elements_by_tag_name("option")
        options_panel_type[2].click()
        time.sleep(3)
        driver.find_element_by_id("panel_0").click()
        time.sleep(5)
        """In Barcode Method, select On-Demand"""
        select_panel_type = driver.find_element_by_id("methodId")
        options_panel_type = select_panel_type.find_elements_by_tag_name("option")
        options_panel_type[0].click()
        time.sleep(3)
        driver.find_element_by_id("psuedoFacilityID").click()
        abc = driver.find_element_by_xpath("//select[@id='requesterId']/following-sibling::input[1]")
        abc.send_keys("102 - CSU KONAHIRI")
        time.sleep(2)
        driver.find_element_by_id("nextButtonId").click()

    @api.assert_capture()
    def test_05_batch(self):
        driver = self.driver
        self.gotoreasonexisting()
        action = ActionChains(driver)
        self.test_04_configure()
        driver.find_element_by_id("saveButtonId").click()
        WebDriverWait(driver, 5).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')
        alert = driver.switch_to.alert
        alert.accept()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()