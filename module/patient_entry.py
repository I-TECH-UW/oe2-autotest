import time
import unittest
from random import randint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import api


class PatientEntry(unittest.TestCase):

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

   @api.assert_capture()
   def test_01_patient_search(self):
       driver = self.driver
       action = ActionChains(driver)
       firstLevelMenu = driver.find_element(By.ID, "menu_patient")
       action.move_to_element(firstLevelMenu).perform()
       secondLevelMenu = driver.find_element(By.ID,'menu_patient_add_or_edit')
       action.move_to_element(secondLevelMenu).perform()
       secondLevelMenu.click()
           
       page_title = driver.find_element(By.XPATH, "//td/h1").text
       assert page_title == "Add/Modify Patient"

       select = driver.find_element_by_id('searchCriteria')
       all_options = select.find_elements_by_tag_name("option")
       search_value_field = driver.find_element(By.ID,"searchValue")
       i = 1
       for option in all_options[1:]:
          print("Value is: %s" % option.get_attribute("value"), type(option.get_attribute("value")))
          option.click()
          
          search_value_field.clear()
          search_value_field.send_keys('test %s' %i)

          search_button_field = driver.find_element(By.ID,"searchButton")
          disabled = search_button_field.get_attribute("disabled")
          #self.assertIsNone(disabled)
          i+=1
          time.sleep(1)

       #Search BY LASTNAME
       search_by_last_name = all_options[1]
       search_by_last_name.click()
       search_value_field.clear()
       search_value_field.send_keys('McGee')
       search_button_field = driver.find_element(By.ID,"searchButton")
       search_button_field.click()
       time.sleep(1)

       #Search BY LASTNAME WITH ACCENT
       search_value_field.clear()
       search_value_field.send_keys('wélé')
       search_button_field = driver.find_element(By.ID,"searchButton")
       search_button_field.click()
       time.sleep(1)

       #Search BY FIRSTNAME
       search_by_first_name = all_options[2]
       search_by_first_name.click()
       search_value_field.clear()
       search_value_field.send_keys('Foxy')
       search_button_field = driver.find_element(By.ID,"searchButton")
       search_button_field.click()
       time.sleep(1)

       #Search BY FIRSTNAME WITH ACCENT
       search_value_field.clear()
       search_value_field.send_keys('élimane')
       search_button_field = driver.find_element(By.ID,"searchButton")
       search_button_field.click()
       time.sleep(1)

       #Search BY LASTNAME FIRSTNAME
       search_by_first_last_name = all_options[3]
       search_by_first_last_name.click()
       search_value_field.clear()
       search_value_field.send_keys('McGee,Foxy')
       search_button_field = driver.find_element(By.ID,"searchButton")
       search_button_field.click()
       time.sleep(1)

       #Search BY LASTNAME FIRSTNAME WITH ACCENT
       search_value_field.clear()
       search_value_field.send_keys('wélé,élimane')
       search_button_field = driver.find_element(By.ID,"searchButton")
       search_button_field.click()
       time.sleep(1)

       #Search BY LASTNAME FIRSTNAME OMIT COMMA
       search_value_field.clear()
       search_value_field.send_keys('wélé élimane')
       search_button_field = driver.find_element(By.ID,"searchButton")
       search_button_field.click()
       time.sleep(1)

       #Search BY PATIENT IDENTIFIANT CODE USING SUBJECT NUMBER
       search_by_patient_identifiant_code = all_options[4]
       search_by_patient_identifiant_code.click()
       search_value_field.clear()
       search_value_field.send_keys('12345')
       search_button_field = driver.find_element(By.ID,"searchButton")
       search_button_field.click()
       time.sleep(1)

       #Search BY PATIENT IDENTIFIANT CODE USING IDENTIFIANT NUMBER
       search_value_field.clear()
       search_value_field.send_keys('987')
       search_button_field = driver.find_element(By.ID,"searchButton")
       search_button_field.click()
       time.sleep(1)
       
        
       time.sleep(5)
       

   
   @api.assert_capture()
   def test_02_patient_information(self):
       """Commentaire test"""
       driver = self.driver
       action = ActionChains(driver)
       firstLevelMenu = driver.find_element(By.ID, "menu_patient")
       action.move_to_element(firstLevelMenu).perform()
       secondLevelMenu = driver.find_element(By.ID,'menu_patient_add_or_edit')
       action.move_to_element(secondLevelMenu).perform()
       secondLevelMenu.click()
     
       page_title = driver.find_element(By.XPATH, "//td/h1").text
       assert page_title == "Add/Modify Patient"

       #No READONLY ALL FIELDS
       assert "readonly='readonly'" not in driver.page_source

       #Subject Number date of birth, gender sex are mandatory 
       save_button_id = driver.find_element(By.ID,"saveButtonId")
       disabled = save_button_id.get_attribute("disabled")
       self.assertTrue(disabled)

       subject_number_id = driver.find_element(By.ID, "subjectNumberID")
       subject_number_id.clear()
       subject_number_id.send_keys('SN345')

       date_of_birth_id = driver.find_element(By.ID, "dateOfBirthID")
       date_of_birth_id.clear()
       date_of_birth_id.send_keys('10/10/2000')

       
       select = driver.find_element_by_id('genderID')
       gender_options = select.find_elements_by_tag_name("option")
       gender_options[1].click()

       disabled = save_button_id.get_attribute("disabled")
       self.assertIsNone(disabled)

       #Subject Number is unique and disable save button if configured
       subject_number_id.clear()
       subject_number_id.send_keys('SN123')
       date_of_birth_id.clear()
       date_of_birth_id.send_keys('10/10/2000')
       WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

       alert = driver.switch_to.alert
       alert.accept()
       
       save_button_id = driver.find_element(By.ID,"saveButtonId")
       disabled = save_button_id.get_attribute("disabled")
       self.assertTrue(disabled)

       #Phone number Invalid format
       patient_phone = driver.find_element(By.ID, "patientPhone")
       patient_phone.send_keys('771111111')
       date_of_birth_id.click()
       WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

       alert = driver.switch_to.alert
       alert.accept()
       time.sleep(3)
       incorect_format_alert = patient_phone.get_attribute('class')
       self.assertEqual(incorect_format_alert,' error')

       #healthRegionID
       select = driver.find_element_by_id('healthRegionID')
       
       all_region = select.find_elements_by_tag_name("option")
       for region in all_region:
          region.click()
          time.sleep(1)
          select_district = driver.find_element_by_id('healthDistrictID')
          all_district_by_region = select_district.find_elements_by_tag_name("option")
          for district in all_district_by_region:
              district.click()
       #Alert Message appears if DOM is not correct format
       dof_value = ['aa/bb/cccc', 'a1/b2/2000', '10102000']
       for value in dof_value:
           date_of_birth_id.clear()
           date_of_birth_id.send_keys(value)
           patient_phone.click()
           bad_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "patientProperties.birthDateForDisplayMessage"))
           )
           assert True if bad_message else False

       #Alert Appears if the date is in the future
       dof_value = ['06/10/2019', '04/11/2019', '04/09/2119']
       for value in dof_value:
           date_of_birth_id.clear()
           date_of_birth_id.send_keys(value)
           patient_phone.click()
           WebDriverWait(driver, 5).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

           alert = driver.switch_to.alert
           alert.accept()
           #time.sleep(2)
           bad_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "patientProperties.birthDateForDisplayMessage"))
           )
           
           assert True if bad_message else False

       #Automatically Fills correct age when DOT is filled
       date_of_birth_id.clear()
       date_of_birth_id.send_keys('01/01/2000')
       patient_phone.click()
       time.sleep(5)
       age = driver.find_element(By.ID,"age")
       age.click()
       self.assertEqual(age.get_attribute('value'), '19')

       #DOB is left blank and age is filled, gives DOB of xx/xx/AAAA with correct year
       date_of_birth_id.clear()
       age.clear()
       age.send_keys(20)
       date_of_birth_id.click()
       self.assertEqual(date_of_birth_id.get_attribute('value'), 'xx/xx/1999')

       #Alert apearts if age is -1 99 100 and >100
       test_value = [-1, 99, 100, randint(100, 200)]
       for value in test_value:
           date_of_birth_id.clear()
           age.clear()
           age.send_keys(value)
           patient_phone.click()
           bad_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "patientProperties.ageMessage"))
           )
           
           #assert True if bad_message else False

       #Sex options are displayed drop-down list (Male, Female)
       test_list = ['1 = Male', '2 = Female']
       for option in gender_options[1:]:
           option.click()
           self.assertIn(option.text, test_list)

       #Sex option is required
           
       
       
           
   @api.assert_capture()
   def test_03_overall_page(self):
       """Commentaire test"""
       driver = self.driver
       action = ActionChains(driver)
       firstLevelMenu = driver.find_element(By.ID, "menu_patient")
       action.move_to_element(firstLevelMenu).perform()
       secondLevelMenu = driver.find_element(By.ID,'menu_patient_add_or_edit')
       action.move_to_element(secondLevelMenu).perform()
       secondLevelMenu.click()

       #Save button desactivate until all mandatory fields are filled
       save_button_id = driver.find_element(By.ID,"saveButtonId")

        #Subject number id is not filled
       subject_number_id = driver.find_element(By.ID, "subjectNumberID")
       subject_number_id.clear()


       date_of_birth_id = driver.find_element(By.ID, "dateOfBirthID")
       date_of_birth_id.clear()
       date_of_birth_id.send_keys('10/10/2000')

       
       select = driver.find_element_by_id('genderID')
       gender_options = select.find_elements_by_tag_name("option")
       gender_options[1].click()

       disabled = save_button_id.get_attribute("disabled")
       self.assertTrue(disabled)
       
         #DOB is not filled
       subject_number_id.clear()
       subject_number_id.send_keys('SN12345')


       date_of_birth_id.clear()

       gender_options[1].click()

       disabled = save_button_id.get_attribute("disabled")
       self.assertTrue(disabled)
         #Gender is not filled
       subject_number_id.clear()
       subject_number_id.send_keys('SN12345')


       date_of_birth_id.clear()
       date_of_birth_id.send_keys('01/01/1999')

       gender_options[0].click()

       disabled = save_button_id.get_attribute("disabled")
       self.assertTrue(disabled)

       #Save button actived if all mandatory fields are filled
       subject_number_id.clear()
       subject_number_id.send_keys('SN123477'+str(randint(100,1000)))


       date_of_birth_id.clear()
       date_of_birth_id.send_keys('01/01/1959')

       gender_options[1].click()

       disabled = save_button_id.get_attribute("disabled")
       self.assertIsNone(disabled)

       #Cancel Button
       cancel_button_id = driver.find_element(By.ID,"cancelButtonId")
       cancel_button_id.click()
       WebDriverWait(driver, 5).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

       alert = driver.switch_to.alert
       print(dir(alert))
       alert.dismiss()

       #Save Button
       time.sleep(3)
       #save_button_id.click()
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
   def test_04_verification(self):
       driver = self.driver
       action = ActionChains(driver)
       firstLevelMenu = driver.find_element(By.ID, "menu_sample")
       action.move_to_element(firstLevelMenu).perform()
       secondLevelMenu = driver.find_element(By.ID,'menu_sample_add')
       action.move_to_element(secondLevelMenu).perform()
       secondLevelMenu.click()

       patient_section_id = driver.find_element(By.XPATH, "//td/input[@id='orderSectionId']")
       patient_section_id.click()
       time.sleep(5)
       select = driver.find_element_by_id('searchCriteria')
       all_options = select.find_elements_by_tag_name("option")
       search_value_field = driver.find_element(By.ID,"searchValue")

       #Search BY LASTNAME
       search_by_last_name = all_options[1]
       search_by_last_name.click()
       search_value_field.clear()
       search_value_field.send_keys('wélé')
       search_button_field = driver.find_element(By.ID,"searchButton")
       search_button_field.click()

       time.sleep(5)

   def tearDown(self):
       self.driver.close()
       self.driver.quit()
