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


class GestionTypes(unittest.TestCase):

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
   def test_01_action(self):
       driver = self.driver
       action = ActionChains(driver)
       firstLevelMenu = driver.find_element(By.ID, "menu_administration")
       action.move_to_element(firstLevelMenu).perform()
       secondLevelMenu = driver.find_element(By.ID,'menu_administration_test_management')
       action.move_to_element(secondLevelMenu).perform()
       secondLevelMenu.click()

       time.sleep(3)
       page_source = driver.page_source

       #Test Management page appears, "Spelling corrections" and "Organisation des Tests" 
       assert 'Test Management' in page_source and \
              'Spelling corrections' in page_source and \
              'est Organization' in page_source

       #
       manage_sample_type =  manage_sample_type =  WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='Manage Sample Types']"))
       )
       manage_sample_type.click()

       time.sleep(3)
       page_source = driver.page_source

       assert 'Create New Sample Type' in page_source and \
              'Set Sample Type Order' in page_source and \
              'Test Assignment' in page_source

   @api.assert_capture()
   def test_02_create_new_sample_type(self):
       driver = self.driver
       action = ActionChains(driver)
       firstLevelMenu = driver.find_element(By.ID, "menu_administration")
       action.move_to_element(firstLevelMenu).perform()
       secondLevelMenu = driver.find_element(By.ID,'menu_administration_test_management')
       action.move_to_element(secondLevelMenu).perform()
       secondLevelMenu.click()

       #Click on Create New Sample Type: An Editer page opens with blank text boxes in English and French under the title "New Sample Type"
       manage_sample_type =  WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='Manage Sample Types']"))
       )
       manage_sample_type.click()
       
       create_new_sample_type =  WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='Create New Sample Type']"))
       )
       create_new_sample_type.click()

       assert 'Create New Sample Type' in driver.page_source

       #Enter only a name in English and click Suivant: A popup saying "Tous les champs sont obligatoires" will appear
       sample_type_english_name =  WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "sampleTypeEnglishName"))
       )
       sample_type_english_name.clear()
       sample_type_english_name.send_keys('Test English')
       next_button = driver.find_element(By.XPATH, "//input[@value='Next']")
       next_button.click()
       WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

       alert = driver.switch_to.alert
       alert.accept()

       #Enter only a name in French and click Suivant: A popup saying "Tous les champs sont obligatoires" will appear
       sample_type_french_name =  WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "sampleTypeFrenchName"))
       )
       sample_type_english_name.clear()
       sample_type_french_name.clear()
       sample_type_french_name.send_keys('Test French')
       next_button = driver.find_element(By.XPATH, "//input[@value='Next']")
       next_button.click()
       WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

       alert = driver.switch_to.alert
       alert.accept()

       #Enter a name in the English text box and a name in the French text box.  Click Suivant.
       ##A new page appears where you can accept or reject the new name(s).
       sample_type_english_name.clear()
       sample_type_english_name.send_keys('Test English '+str(randint(0,1000)))
       sample_type_french_name.clear()
       sample_type_french_name.send_keys('Test French '+str(randint(0,1000)))
       next_button.click()
       page_source = driver.page_source
       assert 'Accept' in page_source and \
              'Reject' in page_source

       #Click Accepter:A new Editer page will appear
       accept_button = driver.find_element(By.XPATH, "//input[@value='Accept']")
       accept_button.click()
       sample_type_english_name =  WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "sampleTypeEnglishName"))
       )
       sample_type_french_name =  WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "sampleTypeFrenchName"))
       )

       assert 'Create New Sample Type' in driver.page_source

       #Click on Precedent:You will return to the main Creer un nouveau type d'chantillon page
       time.sleep(3)
       previous_button =  WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='Previous']"))
       )
       
       previous_button.click()
       page_source = driver.page_source

       assert 'Manage Sample Types' in page_source
              

       #Click on Creer un nouveau type d'chantillon:Confirm that the new name you entered appears below "Inactive Sample Types. Assign tests to activate."
       create_new_sample_type =  WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='Create New Sample Type']"))
       )
       
       create_new_sample_type.click()

       #Click on Precedent: You will return to the main Gerer de unites des tests page
       previous_button =  WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='Previous']"))
       )
       
       previous_button.click()
       assert 'Manage Sample Types' in driver.page_source
       

       time.sleep(5)

   @api.assert_capture()
   def test_03_set_sample_type_order(self):
       driver = self.driver
       action = ActionChains(driver)
       firstLevelMenu = driver.find_element(By.ID, "menu_administration")
       action.move_to_element(firstLevelMenu).perform()
       secondLevelMenu = driver.find_element(By.ID,'menu_administration_test_management')
       action.move_to_element(secondLevelMenu).perform()
       secondLevelMenu.click()

       #Click on Create New Sample Type: An Editer page opens with blank text boxes in English and French under the title "New Sample Type"
       manage_sample_type =  WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='Manage Sample Types']"))
       )
       manage_sample_type.click()
       
       set_sample_type_order =  WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='Set Sample Type Order']"))
       )
       set_sample_type_order.click()

       #Select one of the Sample Types with your mouse pointer.
       #Hold the mouse button down and you will be able to move your selection up and down in the list order
       #Release the mouse button when your selection is in where you want the name to appear in the list order
       #Selected name stays were you place it.
       ul = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//ul[@class='sortable ui-sortable']"))
       )
       all_li = ul.find_elements_by_tag_name("li")
       action = ActionChains(driver)
       action.drag_and_drop(all_li[1], all_li[5]).perform()

       #Click Suivant: A verification page appears with the name where you placed it
       next_button = driver.find_element(By.XPATH, "//input[@value='Next']")
       next_button.click()
       page_source = driver.page_source
       assert 'Accept' in page_source and \
              'Reject' in page_source

       #Click Accept
       accept_button = driver.find_element(By.XPATH, "//input[@value='Accept']")
       accept_button.click()

       #Click Previous
       previous_button =  WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='Previous']"))
       )
       
       previous_button.click()
       page_source = driver.page_source

       assert 'Manage Sample Types' in page_source
       

   @api.assert_capture()
   def test_04_test_assignment(self):
       driver = self.driver
       action = ActionChains(driver)
       firstLevelMenu = driver.find_element(By.ID, "menu_administration")
       action.move_to_element(firstLevelMenu).perform()
       secondLevelMenu = driver.find_element(By.ID,'menu_administration_test_management')
       action.move_to_element(secondLevelMenu).perform()
       secondLevelMenu.click()

       #Click on Attribuer des tests a un type d'echantillon: A page with the list of tests assigned to each Unite d'analyse will appear
       manage_sample_type =  WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='Manage Sample Types']"))
       )
       manage_sample_type.click()
       
       test_assignment =  WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='Test Assignment']"))
       )
       test_assignment.click()
       time.sleep(3)

       #Click on one of the tests: An Editer page will appear and the test you selected will be listed as "Test: _______" above a dropdown menu.
       driver.find_element(By.XPATH, "//input[@value='Amylase(Plasma)']").click()
       page_source = driver.page_source
       assert 'Amylase(Plasma)' in page_source

       #Try to click on the Suivant button: disable
       next_button = driver.find_element(By.XPATH, "//input[@value='Next']")
       disabled = next_button.get_attribute('disabled')
       self.assertTrue(disabled)

       #Select an option from the dropdown menu: Option selected is shown in the dropdown and the Suivant button becomes active
       select = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "sampleTypeSelection"))
       )
       all_options = select.find_elements_by_tag_name("option")
       all_options[1].click()
       next_button = driver.find_element(By.XPATH, "//input[@value='Next']")
       next_button.click()

       #Click Accept
       accept_button = driver.find_element(By.XPATH, "//input[@value='Accept']")
       accept_button.click()
       
       
       
  
       

       
       

   def tearDown(self):
       self.driver.close()
       self.driver.quit()

