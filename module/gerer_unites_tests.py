import time
import unittest
from random import randint
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import api


class GererUnitesTests(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.get('http://test.openelisci.org')
        self.conneting()
        # self.validation()

    def conneting(self):
        driver = self.driver
        username_field = driver.find_element(By.ID, "loginName")
        username_field.clear()
        username_field.send_keys('admin')
        password_field = driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys('adminADMIN!')
        button = driver.find_element(By.ID, "submitButton")
        button.click()
        # time.sleep(5)

    @api.assert_capture()
    def test_01(self):
        # Click on the Admin tab => Gestion des Tests in the left hand menu
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_administration")
        action.move_to_element(firstLevelMenu).perform()
        firstLevelMenu.click()
        continue_link = driver.find_element_by_link_text('Test Management').click()
        time.sleep(5)

        # Click on Gerer de unites des tests
        button_test_unit = driver.find_element_by_xpath("//input[@value='Manage Test Units'][@type='button']")
        button_test_unit.click()
        time.sleep(5)

    @api.assert_capture()
    def test_02_newTestUnit(self):
        # Click on Creer une nouvelle unite d'analyse
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_administration")
        action.move_to_element(firstLevelMenu).perform()
        firstLevelMenu.click()
        time.sleep(3)
        continue_link = driver.find_element_by_link_text('Test Management').click()
        time.sleep(3)
        button_test_unit = driver.find_element_by_xpath("//input[@value='Manage Test Units'][@type='button']")
        button_test_unit.click()
        time.sleep(3)
        button_new_test_unit = driver.find_element_by_xpath("//input[@value='Create New Test Unite'][@type='button']")
        button_new_test_unit.click()
        time.sleep(5)

        # Enter only a name in English and click Suivant
        # click OK
        unit_test_english = driver.find_element(By.ID, "testUnitEnglishName")
        unit_test_english.clear()
        unit_test_english.send_keys('sickle cell disease '+str(randint(1,1000)))
        time.sleep(2)
        button_save = driver.find_element_by_xpath("//input[@value='Save'][@type='button']")
        button_save.click()
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        unit_test_english.clear()
        time.sleep(5)

        # Enter only a name in English and click Suivant
        # click OK
        unit_test_french = driver.find_element(By.ID, "testUnitFrenchName")
        unit_test_french.clear()
        unit_test_french.send_keys('Drépanocytose '+str(randint(1,1000)))
        
        button_save = driver.find_element_by_xpath("//input[@value='Save'][@type='button']")
        button_save.click()
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        unit_test_french.clear()
        time.sleep(5)

        # Enter a name in the English text box and a name in the French text box.  Click Suivant.
        # Click Accepter
        # Click on Precedent
        unit_test_english = driver.find_element(By.ID, "testUnitEnglishName")
        #unit_test_english.clear()
        unit_test_english.send_keys('Test' +str(randint(1,1000)))
        time.sleep(2)
        unit_test_french = driver.find_element(By.ID, "testUnitFrenchName")
        #unit_test_french.clear()
        unit_test_french.send_keys('Test'+str(randint(1,1000)))
        time.sleep(2)
        button_save = driver.find_element_by_xpath("//input[@value='Save'][@type='button']")
        button_save.click()
        
        time.sleep(3)
        button_accepter = driver.find_element_by_xpath("//input[@value='Accept'][@type='button']")
        button_accepter.click()
        time.sleep(3)
        button_cancel = driver.find_element_by_xpath("//input[@value='Cancel'][@type='button']")
        button_cancel.click()
        time.sleep(10)

        # Click on Creer une nouvelle unite d'analyse
        # Click on Precedent
        button_new_test_unit = driver.find_element_by_xpath("//input[@value='Create New Test Unite'][@type='button']")
        button_new_test_unit.click()
        self.assertIn("Test", driver.page_source)
        time.sleep(2)
        button_cancel = driver.find_element_by_xpath("//input[@value='Cancel'][@type='button']")
        button_cancel.click()
        time.sleep(10)

    @api.assert_capture()
    def test_03_analyseOrder(self):
        # Click on Etablir l'ordre des unites d'analyse
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_administration")
        action.move_to_element(firstLevelMenu).perform()
        firstLevelMenu.click()
        time.sleep(3)
        continue_link = driver.find_element_by_link_text('Test Management').click()
        time.sleep(3)
        button_test_unit = driver.find_element_by_xpath("//input[@value='Manage Test Units'][@type='button']")
        button_test_unit.click()
        time.sleep(3)
        button_set_test_unit_order = driver.find_element_by_xpath("//input[@value='Set Test Unit Order'][@type='button']")
        button_set_test_unit_order.click()
        time.sleep(10)
        source_element = driver.find_element_by_xpath("//li[@value='56']")
        destination_element = driver.find_element_by_xpath("//li[@value='58']")
        ##        source_element = driver.find_element_by_tag_name("li")
        ##        destination_element = driver.find_element_by_tag_name("li")
        actionChains = ActionChains(driver)
        actionChains.drag_and_drop(source_element, destination_element).perform()
        time.sleep(5)
        button_next = driver.find_element_by_xpath("//input[@value='Next'][@type='button']")
        button_next.click()
        time.sleep(3)
        button_accept = driver.find_element_by_xpath("//input[@value='Accept'][@type='button']")
        button_accept.click()
        time.sleep(3)
        button_previous = driver.find_element_by_xpath("//input[@value='Previous'][@type='button']")
        button_previous.click()
        time.sleep(10)

    @api.assert_capture()
    def atest_04_assignAnalysis(self):
        # Click on Affecter l'analyse a une unite d'analyse
        # Click on one of the tests
        # Try to click on the Suivant button
        # Select an option from the dropdown menu
        # Click Suivant
        # Click Accepter
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_administration")
        action.move_to_element(firstLevelMenu).perform()
        firstLevelMenu.click()
        time.sleep(3)
        continue_link = driver.find_element_by_link_text('Test Management').click()
        time.sleep(3)
        button_test_unit = driver.find_element_by_xpath("//input[@value='Manage Test Units'][@type='button']")
        button_test_unit.click()
        time.sleep(3)
        button_test_assignment = driver.find_element_by_xpath("//input[@value='Test Assignment'][@type='button']")
        button_test_assignment.click()
        time.sleep(5)
        button_test = driver.find_element_by_xpath("//input[@value='Hemoglobin(Sang total)'][@type='button']")
        button_test.click()
        time.sleep(3)
        self.assertIn("Hemoglobin(Sang total)", driver.page_source)
        time.sleep(3)
        select = driver.find_element_by_id('testSectionSelection')
        all_options = select.find_elements_by_tag_name("option")
        all_options[1].click()
        time.sleep(3)
        button_save = driver.find_element(By.ID, "saveButton")
        button_save.click()
        time.sleep(3)
        button_accept = driver.find_element_by_xpath("//input[@value='Accept'][@type='button']")
        button_accept.click()
        time.sleep(5)



    def tearDown(self):
        self.driver.close()
        self.driver.quit()