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
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

import api

class WorkPlans(unittest.TestCase):

   def setUp(self):
       #self.driver = webdriver.Firefox()
       self.driver = webdriver.Chrome()
       self.driver.get('http://test.openelisci.org')
       self.conneting()
       
   
   def conneting(self):
       driver = self.driver
       username_field = driver.find_element(By.ID,"loginName")
       username_field.clear()
       username_field.send_keys('admin')
       password_field = driver.find_element(By.ID,"password")
       password_field.clear()
       password_field.send_keys('adminADMIN!')
       submit_button = driver.find_element(By.ID, 'submitButton')
       submit_button.click()

   @api.assert_capture()
   def test_01_work_plan_by_test(self):
       driver = self.driver
       action = ActionChains(driver)
       firstLevelMenu = driver.find_element(By.ID, "menu_workplan")
       action.move_to_element(firstLevelMenu).perform()
       secondLevelMenu = driver.find_element(By.ID,'menu_workplan_test')
       action.move_to_element(secondLevelMenu).perform()
       secondLevelMenu.click()

       
       select_test_name = driver.find_element_by_id('testName')
       all_options = select_test_name.find_elements_by_tag_name("option")
       number_of_test = len(all_options[1:])
       all_options[1].click()
       results_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "resultsDiv"))
       )
       assert True if results_div else False

       #View work plan select form
         #All known order are display and total number of tests is correct
       number_of_test = 5
       for i in range(1, number_of_test):
           select_test_name = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "testName"))
           )
           all_options = select_test_name.find_elements_by_tag_name("option")
           all_options[i].click()

           results_div = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "resultsDiv"))
           )

           if not 'No appropriate tests were found.' in driver.page_source:
               #If result is found
               
               
               select_test_name = driver.find_element_by_xpath('//div[@id="resultsDiv"]/table/tbody')
               all_tr = select_test_name.find_elements_by_tag_name("tr")
               i=0
               for tr in all_tr:
                   if 'oddRow' in tr.get_attribute('class') or 'evenRow' in tr.get_attribute('class'):
                       #Count number of result
                       i+=1
               tests_line = 'Total tests = '+str(i)
               self.assertIn(tests_line, driver.page_source)

               i=0
               for tr in all_tr:
                   
                   if 'oddRow' in tr.get_attribute('class') or 'evenRow' in tr.get_attribute('class'):
                       all_td = tr.find_elements_by_tag_name("td")
                       
                       #Assertion number display correctly in workplan form
                       accession_number = all_td[2].text
                       if accession_number:
                          assert len(accession_number) >= 9

                       #Receive date and reception time display correctly in workplan form
                       
                       receive_datetime_str = all_td[5].text
                       if receive_datetime_str:
                           receive_datetime = datetime.strptime(receive_datetime_str, '%d/%m/%Y %H:%M')
                           self.assertEqual(type(receive_datetime), datetime)

                       #//img[contains(@src,'nonconforming')]
                       non_conforming = driver.find_element_by_xpath('//img[contains(@src,"nonconforming")]')
                       assert True if non_conforming else False

                       #Check checkbox
                       included_check = driver.find_element(By.ID, "includedCheck_"+str(i)) # first line id="includedCheck_0"
                       checkbox = included_check.get_attribute('type')
                       self.assertEqual(checkbox, 'checkbox')
                       

                       #Click on workplan
                       ### Workplan appears in a new tab
                       ### Checkbox was ticked is not appear on a printable workplan
                       ### All other appear
                       ### Workplan display information correctly
                       ### Configurable print patient information
                       ### Configurable display space to write result ans techID
                       print_workplan = driver.find_element(By.ID, "print")
                       if randint(0,1):
                           try:
                               included_check.click()
                           except ElementClickInterceptedException:
                               print('no clickable')
                       try:
                           print_workplan.click()
                       except ElementClickInterceptedException:
                           print('no clickable')
                       
                       i+=1

   @api.assert_capture()
   def test_02_work_plan_by_panel(self):
       driver = self.driver
       action = ActionChains(driver)
       firstLevelMenu = driver.find_element(By.ID, "menu_workplan")
       action.move_to_element(firstLevelMenu).perform()
       secondLevelMenu = driver.find_element(By.ID,'menu_workplan_panel')
       action.move_to_element(secondLevelMenu).perform()
       secondLevelMenu.click()

       
       select_test_name = driver.find_element_by_id('testName')
       all_options = select_test_name.find_elements_by_tag_name("option")
       number_of_test = len(all_options[1:])
       all_options[1].click()
       results_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "resultsDiv"))
       )
       assert True if results_div else False

       #View work plan select form
         #All known order are display and total number of tests is correct
       #number_of_test = 3
       for i in range(1, number_of_test):
           select_test_name = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "testName"))
           )
           all_options = select_test_name.find_elements_by_tag_name("option")
           all_options[i].click()

           results_div = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "resultsDiv"))
           )

           if not 'No appropriate tests were found.' in driver.page_source:
               #If result is found
               
               
               select_test_name = driver.find_element_by_xpath('//div[@id="resultsDiv"]/table/tbody')
               all_tr = select_test_name.find_elements_by_tag_name("tr")
               i=0
               for tr in all_tr:
                   if 'oddRow' in tr.get_attribute('class') or 'evenRow' in tr.get_attribute('class'):
                       #Count number of result
                       i+=1
               tests_line = 'Total tests = '+str(i)
               self.assertIn(tests_line, driver.page_source)

               i=0
               for tr in all_tr:
                   
                   if 'oddRow' in tr.get_attribute('class') or 'evenRow' in tr.get_attribute('class'):
                       all_td = tr.find_elements_by_tag_name("td")
                       
                       #Assertion number display correctly in workplan form
                       accession_number = all_td[1].text
                       assert True if len(accession_number) >= 9 or len(accession_number) == 0 else False

                       #Receive date and reception time display correctly in workplan form
                       receive_datetime_str = all_td[6].text
                       receive_datetime = datetime.strptime(receive_datetime_str, '%d/%m/%Y %H:%M')
                       self.assertEqual(type(receive_datetime), datetime)

                       #//img[contains(@src,'nonconforming')]
                       non_conforming = driver.find_element_by_xpath('//img[contains(@src,"nonconforming")]')
                       assert True if non_conforming else False

                       #Check checkbox
                       included_check = driver.find_element(By.ID, "includedCheck_"+str(i)) # first line id="includedCheck_0"
                       checkbox = included_check.get_attribute('type')
                       self.assertEqual(checkbox, 'checkbox')
                       

                       #Click on workplan
                       ### Workplan appears in a new tab
                       ### Checkbox was ticked is not appear on a printable workplan
                       ### All other appear
                       ### Workplan display information correctly
                       ### Configurable print patient information
                       ### Configurable display space to write result ans techID
                       print_workplan = driver.find_element(By.ID, "print")
                       if randint(0,1):
                           try:
                               included_check.click()
                           except ElementClickInterceptedException:
                               print('no clickable')
                       try:
                           print_workplan.click()
                       except ElementClickInterceptedException:
                           print('no clickable')
                           
                       i+=1
                   
   @api.assert_capture()
   def test_03_work_plan_by_unit(self):
       driver = self.driver
       action = ActionChains(driver)
       firstLevelMenu = driver.find_element(By.ID, "menu_workplan")
       action.move_to_element(firstLevelMenu).perform()
       secondLevelMenu = driver.find_element(By.ID,'menu_workplan_bench')
       action.move_to_element(secondLevelMenu).perform()
       secondLevelMenu.click()

       
       select_test_name = driver.find_element_by_id('testSectionId')
       all_options = select_test_name.find_elements_by_tag_name("option")
       number_of_test = len(all_options[1:])
       all_options[1].click()
       main_form = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "mainForm"))
       )
       assert True if main_form else False

       #View work plan select form
         #All known order are display and total number of tests is correct
       #number_of_test = 3
       for i in range(1, number_of_test):
           select_test_name = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "testSectionId"))
           )
           all_options = select_test_name.find_elements_by_tag_name("option")
           all_options[i].click()

           result = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//table/tbody/tr[4]"))
           )

           if not 'No appropriate tests were found.' in driver.page_source:
               #If result is found
               
               
               select_test_name = driver.find_element_by_xpath('//table/tbody/tr[4]/td/table/tbody')
               all_tr = select_test_name.find_elements_by_tag_name("tr")
               i=0
               for tr in all_tr:
                   if 'oddRow' in tr.get_attribute('class') or 'evenRow' in tr.get_attribute('class'):
                       #Count number of result
                       i+=1
               tests_line = 'Total tests = '+str(i)
               self.assertIn(tests_line, driver.page_source)

               i=0
               for tr in all_tr:
                   
                   if 'oddRow' in tr.get_attribute('class') or 'evenRow' in tr.get_attribute('class'):
                       all_td = tr.find_elements_by_tag_name("td")
                       
                       #Assertion number display correctly in workplan form
                       accession_number = all_td[1].text
                       if accession_number:
                          assert True if len(accession_number) >= 9 or len(accession_number) == 0 else False

                       #Receive date and reception time display correctly in workplan form
                       receive_datetime_str = all_td[6].text
                       receive_datetime = datetime.strptime(receive_datetime_str, '%d/%m/%Y %H:%M')
                       self.assertEqual(type(receive_datetime), datetime)

                       #//img[contains(@src,'nonconforming')]
                       non_conforming = driver.find_element_by_xpath('//img[contains(@src,"nonconforming")]')
                       assert True if non_conforming else False

                       #Check checkbox
                       included_check = driver.find_element(By.ID, "includedCheck_"+str(i)) # first line id="includedCheck_0"
                       checkbox = included_check.get_attribute('type')
                       self.assertEqual(checkbox, 'checkbox')
                       

                       #Click on workplan
                       ### Workplan appears in a new tab
                       ### Checkbox was ticked is not appear on a printable workplan
                       ### All other appear
                       ### Workplan display information correctly
                       ### Configurable print patient information
                       ### Configurable display space to write result ans techID
                       print_workplan = driver.find_element(By.ID, "print")
                       if randint(0,1):
                           try:
                               included_check.click()
                           except ElementClickInterceptedException:
                               print('no clickable')
                       try:
                           print_workplan.click()
                       except ElementClickInterceptedException:
                           print('no clickable')
                       
                       i+=1

   @api.assert_capture()
   def test_04_verification(self):
       driver = self.driver
       action = ActionChains(driver)
       firstLevelMenu = driver.find_element(By.ID, "menu_results")
       action.move_to_element(firstLevelMenu).perform()
       secondLevelMenu = driver.find_element(By.ID,'menu_results_logbook')
       action.move_to_element(secondLevelMenu).perform()
       secondLevelMenu.click()

       select_test_name = driver.find_element_by_id('testSectionId')
       all_options = select_test_name.find_elements_by_tag_name("option")
       all_options[1].click()
       reflex_select = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "reflexSelect"))
       )
       assert True if reflex_select else False

       #Add result test
       input_field = driver.find_elements(By.XPATH, "//tr[@id='row_1']/td[@id='cell_1']/textarea[@id='results_1']")
       input_field[0].clear()
       input_field[0].send_keys('40')
       
       save_button_id = driver.find_elements(By.ID, "saveButtonId")
       save_button_id[0].click()

       #successMsg
       success_msg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "successMsg"))
       )
       assert  'Save was successful' == success_msg.text and 'color: seagreen;' in success_msg.get_attribute('style')

       #By Test Type: Test no longer appears on workplan
       action = ActionChains(driver)
       firstLevelMenu = driver.find_element(By.ID, "menu_workplan")
       action.move_to_element(firstLevelMenu).perform()
       secondLevelMenu = driver.find_element(By.ID,'menu_workplan_test')
       action.move_to_element(secondLevelMenu).perform()
       secondLevelMenu.click()

       
       select_test_name = driver.find_element_by_id('testName')
       all_options = select_test_name.find_elements_by_tag_name("option")
       all_options[16].click()
       results_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "resultsDiv"))
       )
       assert True if results_div else False
       
       assert '1234519000002' not in driver.page_source
       
       #By Panel Type: Test no longer appears on workplan
       action = ActionChains(driver)
       firstLevelMenu = driver.find_element(By.ID, "menu_workplan")
       action.move_to_element(firstLevelMenu).perform()
       secondLevelMenu = driver.find_element(By.ID,'menu_workplan_panel')
       action.move_to_element(secondLevelMenu).perform()
       secondLevelMenu.click()

       
       select_test_name = driver.find_element_by_id('testName')
       all_options = select_test_name.find_elements_by_tag_name("option")
       all_options[3].click()
       results_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "resultsDiv"))
       )
       assert True if results_div else False

       assert '1234519000002' not in driver.page_source

       
       #By Unit Type: Test no longer appears on workplan
       action = ActionChains(driver)
       firstLevelMenu = driver.find_element(By.ID, "menu_workplan")
       action.move_to_element(firstLevelMenu).perform()
       secondLevelMenu = driver.find_element(By.ID,'menu_workplan_bench')
       action.move_to_element(secondLevelMenu).perform()
       secondLevelMenu.click()

       
       select_test_name = driver.find_element_by_id('testSectionId')
       all_options = select_test_name.find_elements_by_tag_name("option")
       all_options[4].click()
       main_form = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "mainForm"))
       )
       assert True if main_form else False

       assert '1234519000002' not in driver.page_source
       
       


       
       time.sleep(5)

   def tearDown(self):
       self.driver.close()
       self.driver.quit()