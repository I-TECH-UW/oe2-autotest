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

class RenamExistingMeasure(unittest.TestCase):

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
        #
        # testname=driver.find_element_by_xpath("//input[@value='Rename existing test names']")
        # testname.click()
        # time.sleep(4)
        # rename=driver.find_element_by_xpath("//input[@value='Albumin(Urines)']")
        # rename.click()
        # time.sleep(4)
        # correcteng = driver.find_element_by_xpath("//input[@name='nameEnglish'][@type='text']")
        #
        # time.sleep(4)
        # correcteng.send_keys('Albumin')
        # correctfr =driver.find_element_by_xpath("//input[@name='nameFrench'][@type='text']")
        #
        # correctfr.send_keys('Albumine')
        # correctengr = driver.find_element_by_xpath("//input[@name='reportNameEnglish'][@type='text']")
        #
        # correctengr.send_keys('Albumin')
        # correctfrr =  driver.find_element_by_xpath("//input[@name='reportNameFrench'][@type='text']")
        #
        # correctfrr.send_keys('Albumine')
        #
        # driver.find_element_by_xpath("//input[@value='Save']").click()
        # driver.find_element_by_xpath("//input[@value='Accept']").click()
        #
        #
        # """rename existing panels """
        # firstLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_administration']")
        # firstLevelMenu.click()
        # time.sleep(5)
        # driver.find_element_by_link_text("Test Management").click()
        # driver.find_element_by_xpath("//input[@value='Rename Existing Panels']").click()
        # time.sleep(5)
        # driver.find_element_by_xpath("//input[@value='NFS']").click()
        # time.sleep(5)
        # lab = driver.find_element_by_name("nameEnglish")
        # lab.send_keys('NFS')
        # time.sleep(2)
        # fr = driver.find_element_by_name("nameFrench")
        # time.sleep(2)
        # fr.send_keys('NFS')
        # time.sleep(2)
        # driver.find_element_by_xpath("//input[@value='Save']").click()
        # time.sleep(2)
        # driver.find_element_by_xpath("//input[@value='Accept']").click()
        # """rename existing simple type """
        # firstLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_administration']")
        # firstLevelMenu.click()
        # time.sleep(5)
        # driver.find_element_by_link_text("Test Management").click()
        # driver.find_element_by_xpath("//input[@value='Rename Existing Sample Types']").click()
        # driver.find_element_by_xpath("//input[@value='Plasma']").click()
        # time.sleep(5)
        # lab = driver.find_element_by_name("nameEnglish")
        # lab.send_keys('Plasma')
        # time.sleep(2)
        # fr = driver.find_element_by_name("nameFrench")
        # fr.send_keys('Plasma')
        # driver.find_element_by_xpath("//input[@value='Save']").click()
        # time.sleep(2)
        # driver.find_element_by_xpath("//input[@value='Accept']").click()
        # time.sleep(2)
        # """rename existing test sections """
        # firstLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_administration']")
        # firstLevelMenu.click()
        # time.sleep(5)
        # driver.find_element_by_link_text("Test Management").click()
        # driver.find_element_by_xpath("//input[@value='Rename Existing Test Sections']").click()
        # driver.find_element_by_xpath("//input[@value='Hematology']").click()
        # WebDriverWait(driver, 5).until(EC.alert_is_present(),
        #                                'Timed out waiting for PA creation ' +
        #                                'confirmation popup to appear.')
        # alert = driver.switch_to.alert
        # alert.accept()
        #
        # labtest = driver.find_element_by_name("nameEnglish")
        # time.sleep(2)
        # labtest.send_keys('Hematology')
        # time.sleep(2)
        # frtest = driver.find_element_by_name("nameFrench")
        # frtest.send_keys('Hematologie')
        # driver.find_element_by_xpath("//input[@value='Save']").click()
        # time.sleep(2)
        # driver.find_element_by_xpath("//input[@value='Accept']").click()
        # time.sleep(2)
        """rename existing test unit of measure entries """
        # firstLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_administration']")
        # firstLevelMenu.click()
        # time.sleep(5)
        # driver.find_element_by_link_text("Test Management").click()
        driver.find_element_by_xpath("//input[@value='Rename Existing Unit of Measure Entries']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@value='ppl']").click()
        labtest = driver.find_element_by_name("nameEnglish")
        time.sleep(2)
        labtest.send_keys('ppl')
        driver.find_element_by_xpath("//input[@value='Save']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@value='Accept']").click()
        time.sleep(2)
        # """View test catalog"""
        # firstLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_administration']")
        # firstLevelMenu.click()
        # time.sleep(5)
        # driver.find_element_by_link_text("Test Management").click()
        # driver.find_element_by_xpath("//input[@value='View Test Catalog']").click()
        # time.sleep()
        # """add new tests"""
        # firstLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_administration']")
        # firstLevelMenu.click()
        # time.sleep(5)
        # driver.find_element_by_link_text("Test Management").click()
        # driver.find_element_by_xpath("//input[@value='Add new tests']").click()
        # time.sleep()
        """click on reject"""
        # firstLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_administration']")
        # firstLevelMenu.click()
        # time.sleep(5)
        # driver.find_element_by_link_text("Test Management").click()
        # driver.find_element_by_xpath("//input[@value='Rename Existing Unit of Measure Entries']").click()
        # time.sleep(2)
        driver.find_element_by_xpath("//input[@value='ppl']").click()
        labtest = driver.find_element_by_name("nameEnglish")
        time.sleep(2)
        labtest.send_keys('ppl')
        driver.find_element_by_xpath("//input[@value='Save']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@value='Reject']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@value='Cancel']").click()
        time.sleep(2)
        """"click on Finished"""
        driver.find_element_by_xpath("//input[@value='Finished']").click()
        time.sleep(2)


    def tearDown(self):
       self.driver.close()
       self.driver.quit()