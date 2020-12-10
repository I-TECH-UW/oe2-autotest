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

class Validation(unittest.TestCase):

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
    def test_01_validation(self):
        # the validation by Unit Type page displays
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_resultvalidation")
        action.move_to_element(firstLevelMenu).perform()
        firstLevelMenu.click()
        time.sleep(5)
        self.assertIn("Unit Type", driver.page_source)
        # bad_message = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, "menu_resultvalidation")))

        # tests display with Lab order Number, Test name, result ans result reference
        select = driver.find_element_by_id('testSectionId')
        all_options = select.find_elements_by_tag_name("option")
        all_options[1].click()
        time.sleep(4)

        # results notes display with date ans time stamp (notes entered on results page)
        self.assertIn("Prior Notes", driver.page_source)
        time.sleep(4)

        # Field only accepts 9 characters in the order but the field can contain 13 characters
        select2 = driver.find_element_by_id('testSectionId')
        all_options2 = select2.find_elements_by_tag_name("option")
        all_options2[2].click()
        lab_number = driver.find_element_by_id("labnoSearch")
        lab_number.send_keys('zzzzzzzzzzzzzzzzzzzzzzz')
        time.sleep(4)

        # page goes to order number; order is highlighted in yellow
        valeur = driver.find_element_by_xpath("//td[@colspan='3']").text
        champ = driver.find_element(By.ID, "labnoSearch")
        champ.clear()
        champ.send_keys(valeur)
        clear_button = driver.find_element_by_xpath("//input[@value='Search'][@type='button']")
        clear_button.click()
        time.sleep(4)

        # if order number does not exist, message "Order not found" appears
        champ2 = driver.find_element(By.ID, "labnoSearch")
        champ2.clear()
        champ2.send_keys('1234519000003')
        clear_button = driver.find_element_by_xpath("//input[@value='Search'][@type='button']")
        clear_button.click()
        self.assertIn("Order number not found", driver.page_source)
        time.sleep(4)

        # Red flag displayed next to test
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_resultvalidation")
        action.move_to_element(firstLevelMenu).perform()
        firstLevelMenu.click()
        self.assertIn("Unit Type", driver.page_source)
        select2 = driver.find_element_by_id('testSectionId')
        all_options2 = select2.find_elements_by_tag_name("option")
        all_options2[1].click()
        time.sleep(2)
        self.assertIn("	White Blood Cells", driver.page_source)
        self.assertIn("Non Conformity", driver.page_source)
        time.sleep(3)

        # All results are checked "Save"
        # All results de-checked "Save"
        # Check Save all results again
        # Uncheck selected tests.
        # Uncheck Retest all results.
        # Check Retest all results again.
        # Uncheck selected tests.
        # driver = self.driver
        # action = ActionChains(driver)
        # firstLevelMenu = driver.find_element_by_id("menu_resultvalidation")
        # action.move_to_element(firstLevelMenu).perform()
        # firstLevelMenu.click()
        # self.assertIn("Unit Type", driver.page_source)
        # select2 = driver.find_element_by_id('testSectionId')
        # all_options2 = select2.find_elements_by_tag_name("option")
        # all_options2[1].click()
        check_button = driver.find_element(By.ID, "selectAllAccept")
        check_button.click()
        time.sleep(3)
        check_button = driver.find_element(By.ID, "selectAllAccept")
        check_button.click()
        time.sleep(3)
        check_button = driver.find_element(By.ID, "selectAllAccept")
        check_button.click()
        time.sleep(3)
        check_button = driver.find_element(By.ID, "selectAllAccept")
        check_button.click()
        time.sleep(3)
        check_button = driver.find_element(By.ID, "selectAllReject")
        check_button.click()
        time.sleep(3)
        check_button = driver.find_element(By.ID, "selectAllReject")
        check_button.click()
        time.sleep(3)
        check_button = driver.find_element(By.ID, "selectAllReject")
        check_button.click()
        time.sleep(3)
        check_button = driver.find_element(By.ID, "selectAllReject")
        check_button.click()
        time.sleep(3)

    @api.assert_capture()
    def test_02_overallPage(self):
       #Triggers message, "this page is asking you to confirm that you want to leave-data you have entered may not be saved?"
       driver = self.driver
       action = ActionChains(driver)
       firstLevelMenu = driver.find_element_by_id("menu_resultvalidation")
       action.move_to_element(firstLevelMenu).perform()
       firstLevelMenu.click()
       time.sleep(5)
       self.assertIn("Unit Type", driver.page_source)
       select = driver.find_element_by_id('testSectionId')
       all_options = select.find_elements_by_tag_name("option")
       all_options[2].click()

       check_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "sampleAccepted_2"))
       )
       check_button.click()
    
       cancel_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "cancelButtonId"))
       )
       cancel_button.click()
       WebDriverWait(driver, 10).until(EC.alert_is_present(), 'Timed out waiting for PA creation ' + 'confirmation popup to appear.')
       alert = driver.switch_to.alert
       alert.dismiss()
       

       # Pop-up message asks you to confirm that you have indicated action (Save or Retest) for all items you wish to validate
       save_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "saveButtonId"))
       )
       save_button.click()
       WebDriverWait(driver, 10).until(EC.alert_is_present(), 'Timed out waiting for PA creation ' + 'confirmation popup to appear.')
       alert = driver.switch_to.alert
       alert.accept()
       time.sleep(5)

       # Pull up Validation page again
       # Enter a validation for another result
       # Click Cancel button: Triggers message "Are you sure you want to navigate away without saving?"
       # Click "Leave Page" in cancel message: Returned to home page
       driver = self.driver
       action = ActionChains(driver)
       firstLevelMenu = driver.find_element_by_id("menu_resultvalidation")
       action.move_to_element(firstLevelMenu).perform()
       firstLevelMenu.click()
       time.sleep(3)
       self.assertIn("Unit Type", driver.page_source)
       select = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "testSectionId"))
       )
       all_options = select.find_elements_by_tag_name("option")
       all_options[1].click()
       check_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "sampleAccepted_2"))
       )
       check_button.click()
       time.sleep(2)
       cancel_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "cancelButtonId"))
       )
       cancel_button.click()
       WebDriverWait(driver, 10).until(EC.alert_is_present(), 'Timed out waiting for PA creation ' + 'confirmation popup to appear.')
       alert = driver.switch_to.alert
       alert.accept()
       time.sleep(5)

    @api.assert_capture()
    def test_03_verification(self):
        # Generate Patient Status Report for the accession number.
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_reports")
        action.move_to_element(firstLevelMenu).perform()
        secondLevelMenu = driver.find_element_by_id("menu_reports_routine")
        action.move_to_element(secondLevelMenu).perform()
        time.sleep(2)
        thirdLevelMenu = driver.find_element_by_id("menu_reports_status_patient")
        action.move_to_element(thirdLevelMenu).perform()
        time.sleep(2)
        fourthLevelMenu = driver.find_element_by_id("menu_reports_status_patient.classique")
        action.move_to_element(fourthLevelMenu).perform()
        time.sleep(2)
        fourthLevelMenu.click()
        lab_number = driver.find_element(By.ID, "accessionDirect")
        lab_number.clear()
        lab_number.send_keys('1234500000012')
        time.sleep(2)
        button_generate = driver.find_element_by_xpath("//input[@name='printNew'][@type='button']")
        button_generate.click()
        time.sleep(5)

        # Go to Workplan --> By Test Type: Retest tests appear on workplan for that accession number.
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_workplan")
        action.move_to_element(firstLevelMenu).perform()
        time.sleep(3)
        secondLevelMenu = driver.find_element_by_id("menu_workplan_test")
        action.move_to_element(secondLevelMenu).perform()
        secondLevelMenu.click()
        self.assertIn("Test Type", driver.page_source)
        select = driver.find_element_by_id('testName')
        all_options = select.find_elements_by_tag_name("option")
        all_options[19].click()
        time.sleep(5)

        # Go to Workplan --> By Panel Type: Retest panels appear on workplan for that accession number.
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_workplan")
        action.move_to_element(firstLevelMenu).perform()
        time.sleep(3)
        secondLevelMenu = driver.find_element_by_id("menu_workplan_panel")
        action.move_to_element(secondLevelMenu).perform()
        secondLevelMenu.click()
        self.assertIn("Panel Type", driver.page_source)
        select = driver.find_element_by_id('testName')
        all_options = select.find_elements_by_tag_name("option")
        all_options[1].click()
        time.sleep(5)

        # Go to Workplan --> By Unit, Serology-Immunology: Retest panels appear on workplan for that accession number.
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_workplan")
        action.move_to_element(firstLevelMenu).perform()
        time.sleep(3)
        secondLevelMenu = driver.find_element_by_id("menu_workplan_bench")
        action.move_to_element(secondLevelMenu).perform()
        secondLevelMenu.click()
        self.assertIn("Unit Type", driver.page_source)
        select1 = driver.find_element_by_id('testSectionId')
        all_options1 = select1.find_elements_by_tag_name("option")
        all_options1[3].click()
        time.sleep(2)
        select2 = driver.find_element_by_id('testSectionId')
        all_options2 = select2.find_elements_by_tag_name("option")
        all_options2[1].click()
        time.sleep(2)
        select3 = driver.find_element_by_id('testSectionId')
        all_options3 = select3.find_elements_by_tag_name("option")
        all_options3[2].click()
        time.sleep(2)
        select4 = driver.find_element_by_id('testSectionId')
        all_options4 = select4.find_elements_by_tag_name("option")
        all_options4[5].click()
        time.sleep(2)
        select5 = driver.find_element_by_id('testSectionId')
        all_options5 = select5.find_elements_by_tag_name("option")
        all_options5[6].click()
        time.sleep(5)



    def tearDown(self):
        self.driver.close()
        self.driver.quit()