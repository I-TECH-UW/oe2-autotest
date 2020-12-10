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
from selenium.common.exceptions import NoSuchElementException

import api



class ReferralOut(unittest.TestCase):

   def setUp(self):
       #self.driver = webdriver.Firefox()
       self.driver = webdriver.Chrome()
       self.driver.get('http://test.openelisci.org')
       self.conneting()
       
   def conneting(self):
       driver = self.driver
       username_field = driver.find_element(By.ID,"loginName")
       #print(username_field)
       username_field.clear()
       username_field.send_keys('admin')
       password_field = driver.find_element(By.ID,"password")
       password_field.clear()
       password_field.send_keys('adminADMIN!')
       submit_button = driver.find_element(By.ID, 'submitButton')
       submit_button.click()
       
   def check_exists_by_id(self, ID):
    try:
        self.driver.find_element(By.ID,ID)
    except NoSuchElementException:
        return False
    return True


   @api.assert_capture()
   def test_01_referring_result(self):
       driver = self.driver

       #Search : by Order for known accession number
       action = ActionChains(driver)
       
       firstLevelMenu = driver.find_element(By.ID, "menu_results")
       action.move_to_element(firstLevelMenu).perform()
       
       secondLevelMenu = driver.find_element(By.ID,'menu_results_search')
       action.move_to_element(secondLevelMenu).perform()

       thirdLevelMenu = driver.find_element(By.ID,'menu_results_accession')
       action.move_to_element(thirdLevelMenu).perform()
       
       thirdLevelMenu.click()

       #Search page appears
       search_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchDiv"))
       )
       assert True if search_div else False

       search_accession_id = WebDriverWait(driver, 10).until(
           EC.visibility_of_element_located((By.ID, "searchAccessionID"))
       )
       search_accession_id.clear()
       search_accession_id.send_keys('1234519000002')
       retrieve_tests_id = driver.find_element(By.ID,"retrieveTestsID")
       retrieve_tests_id.click()
       #Referral stick and referral list appears
       is_referral_stick = self.check_exists_by_id('referralId_8')
       is_referral_list = self.check_exists_by_id('referralReasonId_8')
       self.assertTrue(is_referral_stick and is_referral_list)

       #Click on referral stick and drop down list activate
       referral_stick = driver.find_element(By.ID,'referralId_8')
       referral_stick.click()
       referral_list = driver.find_element(By.ID,"referralReasonId_8")
       disabled = referral_list.get_attribute("disabled")
       self.assertIsNone(disabled)

       #Uncheck refferral stick and drop down list deactivate
       referral_stick.click()
       disabled = referral_list.get_attribute("disabled")
       self.assertTrue(disabled)

       #Recheck Referral box
       referral_stick.click()

       #Select a raison
       all_options = referral_list.find_elements_by_tag_name("option")
       all_options[1].click()

       #Click Save Button
       save_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "saveButtonId"))
       )
       save_button.click()


       #successMsg
       success_msg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "successMsg"))
       )
       assert  'Save was successful' == success_msg.text and 'color: seagreen;' in success_msg.get_attribute('style')

       #Reload referral page
       search_accession_id = WebDriverWait(driver, 10).until(
           EC.visibility_of_element_located((By.ID, "searchAccessionID"))
       )
       search_accession_id.clear()
       search_accession_id.send_keys('1234519000002')
       retrieve_tests_id = driver.find_element(By.ID,"retrieveTestsID")
       retrieve_tests_id.click()

       referral_stick = driver.find_element(By.ID,'referralId_9')
       referral_stick.click()
       referral_list = driver.find_element(By.ID,"referralReasonId_9")



       #Select a raison
       all_options = referral_list.find_elements_by_tag_name("option")
       all_options[1].click()

       #Click Save Button
       save_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "saveButtonId"))
       )
       save_button.click()


       #successMsg
       success_msg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "successMsg"))
       )
       assert  'Save was successful' == success_msg.text and 'color: seagreen;' in success_msg.get_attribute('style')



   @api.assert_capture()
   def test_02_referral_page(self):
       driver = self.driver

       #Referred test 
       action = ActionChains(driver)
       firstLevelMenu = driver.find_element(By.ID, "menu_results")
       action.move_to_element(firstLevelMenu).perform()
       secondLevelMenu = driver.find_element(By.ID,'menu_results_referred')
       action.move_to_element(secondLevelMenu).perform()
       secondLevelMenu.click()

       
       
       time.sleep(5)

   def tearDown(self):
       self.driver.close()
       self.driver.quit()

