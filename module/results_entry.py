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


class ResultsEntry(unittest.TestCase):

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
   def test_01_accessing_result_entry(self):
       driver = self.driver

       #Enter by unit 
       action = ActionChains(driver)
       firstLevelMenu = driver.find_element(By.ID, "menu_results")
       action.move_to_element(firstLevelMenu).perform()
       secondLevelMenu = driver.find_element(By.ID,'menu_results_logbook')
       action.move_to_element(secondLevelMenu).perform()
       secondLevelMenu.click()

       #Search page appears
       search_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchDiv"))
       )
       assert True if search_div else False
       
       #All unit name display correectly in drop down menu
       #Can select unit from drop down menu and direct to enter page
       select = driver.find_element_by_id('testSectionId')
       all_options = select.find_elements_by_tag_name("option")
       number_of_test = len(all_options[1:])
       for i in range(1, number_of_test):
           select = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "testSectionId"))
           )
           all_options = select.find_elements_by_tag_name("option")
           all_options[i].click()
    
       #Search : by patient
       action = ActionChains(driver)
       
       firstLevelMenu = driver.find_element(By.ID, "menu_results")
       action.move_to_element(firstLevelMenu).perform()
       
       secondLevelMenu = driver.find_element(By.ID,'menu_results_search')
       action.move_to_element(secondLevelMenu).perform()

       thirdLevelMenu = driver.find_element(By.ID,'menu_results_patient')
       action.move_to_element(thirdLevelMenu).perform()
       
       thirdLevelMenu.click()

       #Search page appears
       search_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchDiv"))
       )
       assert True if search_div else False

       #Search : by Order
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
       assert True if search_div and 'Lab No' in driver.page_source else False

       #Search : by Test Name
       action = ActionChains(driver)
       
       firstLevelMenu = driver.find_element(By.ID, "menu_results")
       action.move_to_element(firstLevelMenu).perform()
       
       secondLevelMenu = driver.find_element(By.ID,'menu_results_search')
       action.move_to_element(secondLevelMenu).perform()

       thirdLevelMenu = driver.find_element(By.ID,'menu_results_status')
       action.move_to_element(thirdLevelMenu).perform()
       
       thirdLevelMenu.click()

       #Search page appears
       search_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchDiv"))
       )
       assert True if search_div and \
              'Date' in driver.page_source and \
              'Test' in driver.page_source and \
              'Status' in driver.page_source \
              else False
       
   @api.assert_capture()
   def test_02_searching_for_test_result_entry_forms(self):
       driver = self.driver
       action = ActionChains(driver)
       
       firstLevelMenu = driver.find_element(By.ID, "menu_results")
       action.move_to_element(firstLevelMenu).perform()
       
       secondLevelMenu = driver.find_element(By.ID,'menu_results_search')
       action.move_to_element(secondLevelMenu).perform()

       thirdLevelMenu = driver.find_element(By.ID,'menu_results_patient')
       action.move_to_element(thirdLevelMenu).perform()
       
       thirdLevelMenu.click()

       #Search page appears
       search_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchDiv"))
       )
       assert True if search_div else False

       #Search button deactivited until search criteria selected and input text entered 
       search_list = ['SOW','ALIOU', 'ALIOU,wélé', 'HT7823728', '1234517000003']
       select = driver.find_element_by_id('searchCriteria')
       all_options = select.find_elements_by_tag_name("option")
       search_value_field = driver.find_element(By.ID,"searchValue")
       i = 0
       for option in all_options[1:]:
          option.click()
          
          search_value_field.clear()
          search_value_field.send_keys(search_list[i])

          search_button_field = driver.find_element(By.ID,"searchButton")
          disabled = search_button_field.get_attribute("disabled")
          self.assertIsNone(disabled)
          i+=1
          time.sleep(1)

       #Drop down menu displays correct search criteria
       test_list = [
           '1. Last name',
           '2. First name',
           '3. Last name, First name',
           '4. Patient identification code',
           '5. Lab No',
        ]
       for option in all_options[1:]:
           self.assertIn(option.text.strip(), test_list)

       #Search BY LASTNAME
       search_by_last_name = all_options[1]
       search_by_last_name.click()
       search_value_field.clear()
       search_value_field.send_keys('McGee')
       search_button_field = driver.find_element(By.ID,"searchButton")
       search_button_field.click()
       WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "resultsDiv"))
       )
       no_patient_found = driver.find_element(By.ID,"noPatientFound")
       style = no_patient_found.get_attribute('style')
       self.assertEqual(style, 'display: none;')
       time.sleep(1)
       
       #Page refresh
       select = driver.find_element_by_id('searchCriteria')
       all_options = select.find_elements_by_tag_name("option")
       search_value_field = driver.find_element(By.ID,"searchValue")
       
       #Search BY FIRSTNAME
       search_by_first_name = all_options[2]
       search_by_first_name.click()
       search_value_field.clear()
       search_value_field.send_keys('Foxy')
       search_button_field = driver.find_element(By.ID,"searchButton")
       search_button_field.click()
       WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "resultsDiv"))
       )
       noPatientFound = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "resultsDiv"))
       )
       no_patient_found = driver.find_element(By.ID,"noPatientFound")
       style = no_patient_found.get_attribute('style')
       self.assertEqual(style, 'display: none;')
       time.sleep(5)
       
       #Page refresh
       select = driver.find_element_by_id('searchCriteria')
       all_options = select.find_elements_by_tag_name("option")
       search_value_field = driver.find_element(By.ID,"searchValue")

       #Search BY LASTNAME FIRSTNAME OMIT COMMA
       search_by_first_last_name = all_options[3]
       search_by_first_last_name.click()
       search_value_field.clear()
       search_value_field.send_keys('McGee Foxy')
       search_button_field = driver.find_element(By.ID,"searchButton")
       search_button_field.click()
       WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "resultsDiv"))
       )
       time.sleep(3)
       no_patient_found = driver.find_element(By.ID,"noPatientFound")
       style = no_patient_found.get_attribute('style')
       
       self.assertFalse(style)

       #Page refresh
       select = driver.find_element_by_id('searchCriteria')
       all_options = select.find_elements_by_tag_name("option")
       search_value_field = driver.find_element(By.ID,"searchValue")
       
       #Search BY PATIENT IDENTIFIANT CODE
       search_by_patient_identifiant_code = all_options[4]
       search_by_patient_identifiant_code.click()
       search_value_field.clear()
       search_value_field.send_keys('12345')
       search_button_field = driver.find_element(By.ID,"searchButton")
       search_button_field.click()
       WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "resultsDiv"))
       )
       time.sleep(3)
       noPatientFound = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "resultsDiv"))
       )
       no_patient_found = driver.find_element(By.ID,"noPatientFound")
       style = no_patient_found.get_attribute('style')
       self.assertEqual(style, 'display: none;')
       time.sleep(1)

       
       
       #Page refresh
       select = driver.find_element_by_id('searchCriteria')
       all_options = select.find_elements_by_tag_name("option")
       search_value_field = driver.find_element(By.ID,"searchValue")
       
       #Search BY Accession Number
       search_by_patient_identifiant_code = all_options[5]
       search_by_patient_identifiant_code.click()
       search_value_field.clear()
       search_value_field.send_keys('1234519000002')
       search_button_field = driver.find_element(By.ID,"searchButton")
       search_button_field.click()
       WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "resultsDiv"))
       )
       time.sleep(3)
       noPatientFound = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "resultsDiv"))
       )
       no_patient_found = driver.find_element(By.ID,"noPatientFound")
       style = no_patient_found.get_attribute('style')
       self.assertEqual(style, 'display: none;')
       time.sleep(1)

       #Result -> Search -> By order
       action = ActionChains(driver)
       
       firstLevelMenu = driver.find_element(By.ID, "menu_results")
       action.move_to_element(firstLevelMenu).perform()
       
       secondLevelMenu = driver.find_element(By.ID,'menu_results_search')
       action.move_to_element(secondLevelMenu).perform()

       thirdLevelMenu = driver.find_element(By.ID,'menu_results_accession')
       action.move_to_element(thirdLevelMenu).perform()
       
       thirdLevelMenu.click()

       #Search by accession number
       search_accession_id = driver.find_element(By.ID,"searchAccessionID")
       search_accession_id.clear()
       search_accession_id.send_keys('1234519000002')
       retrieve_tests_id = driver.find_element(By.ID,"retrieveTestsID")
       retrieve_tests_id.click()
       WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "resultsDiv"))
       )
       time.sleep(3)
       results_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "resultsDiv"))
       )
       assert True if results_div else False
       time.sleep(1)


   @api.assert_capture()
   def test_03_results_entry_set_up(self):
           
       #Result -> Search -> By order
       driver = self.driver
       
       action = ActionChains(driver)
       
       firstLevelMenu = driver.find_element(By.ID, "menu_results")
       action.move_to_element(firstLevelMenu).perform()
       
       secondLevelMenu = driver.find_element(By.ID,'menu_results_search')
       action.move_to_element(secondLevelMenu).perform()

       thirdLevelMenu = driver.find_element(By.ID,'menu_results_accession')
       action.move_to_element(thirdLevelMenu).perform()
       
       thirdLevelMenu.click()

       #Search by accession number
       search_accession_id = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchAccessionID"))
       )
       search_accession_id.clear()
       search_accession_id.send_keys('1234519000002')
       retrieve_tests_id = driver.find_element(By.ID,"retrieveTestsID")
       retrieve_tests_id.click()
       WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "resultsDiv"))
       )
       time.sleep(3)
       page_source = driver.page_source

       assert 'Last Name' in page_source and \
              'First Name' in page_source and \
              'Gender' in page_source and \
              'Date of Birth' in page_source and \
              'National ID' in page_source and \
              'Subject Number' in page_source


       action = ActionChains(driver)
       
       firstLevelMenu = driver.find_element(By.ID, "menu_results")
       action.move_to_element(firstLevelMenu).perform()
       
       secondLevelMenu = driver.find_element(By.ID,'menu_results_search')
       action.move_to_element(secondLevelMenu).perform()

       thirdLevelMenu = driver.find_element(By.ID,'menu_results_patient')
       action.move_to_element(thirdLevelMenu).perform()
       
       thirdLevelMenu.click()

       #Search page appears
       search_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchDiv"))
       )

       
       #Search BY Patient
       search_value_field = driver.find_element(By.ID,"searchValue")
       select = driver.find_element_by_id('searchCriteria')
       all_options = select.find_elements_by_tag_name("option")
       search_by_last_name = all_options[1]
       search_by_last_name.click()
       search_value_field.clear()
       search_value_field.send_keys('McGee')
       search_button_field = driver.find_element(By.ID,"searchButton")
       search_button_field.click()
       WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "resultsDiv"))
       )
       time.sleep(3)
       page_source = driver.page_source

       assert 'Last Name' in page_source and \
              'First Name' in page_source and \
              'Gender' in page_source and \
              'Date of Birth' in page_source and \
              'National ID' in page_source and \
              'Subject Number' in page_source
       
       #Enter by unit 
       action = ActionChains(driver)
       firstLevelMenu = driver.find_element(By.ID, "menu_results")
       action.move_to_element(firstLevelMenu).perform()
       secondLevelMenu = driver.find_element(By.ID,'menu_results_logbook')
       action.move_to_element(secondLevelMenu).perform()
       secondLevelMenu.click()

       
       
       #Can select unit from drop down menu:Only test without result display
       
       #i=1
       #do_while = True#Execute before verifing
       #while do_while or 'No appropriate tests were found.' in driver.page_source:
       #     select = WebDriverWait(driver, 10).until(
       #    EC.visibility_of_element_located((By.ID, "testSectionId"))
       #    )
       #    all_options = select.find_elements_by_tag_name("option")
       #    all_options[i].click()
       #    do_while=False
       #    i+=1
       select = WebDriverWait(driver, 10).until(
         EC.visibility_of_element_located((By.ID, "testSectionId"))
       )
       all_options = select.find_elements_by_tag_name("option")
       all_options[1].click()
    
       for i in range(3,5):
           input_field = driver.find_elements(By.XPATH, "//tr[@id='row_%s']/td[@id='cell_%s']/input[@id='results_%s']"%(str(i),str(i),str(i)))
           result = input_field[0].text
           self.assertEqual(result,'')

       page_source = driver.page_source
       #Number of page 
       #Note
       assert 'Notes' in page_source
       #Accession Number with sample extension display
       #Simple Condition display
       #Simple Type display
       assert 'Sample Type' in page_source
       #Name test display(example: 'Serum')
       
       #Display current date
       today = datetime.today().date()
       for i in range(3,5):
           input_field = driver.find_elements(By.XPATH, "//input[@id='testDate_%s']"%(str(i)))
           test_date = input_field[0].get_attribute('value')
           test_date = datetime.strptime(test_date, '%d/%m/%Y').date()
           self.assertEqual(test_date, today)

       #Test date accept text: choose a random field
       input_field = driver.find_elements(By.XPATH, "//input[@id='testDate_%s']"%(str(randint(0,28))))
       input_field[0].clear()
       input_field[0].send_keys('10/09/2019')

       #//img[contains(@src,'nonconforming')]
       non_conforming = driver.find_element_by_xpath('//img[contains(@src,"nonconforming")]')
       assert True if non_conforming else False

       #Enter know accession number in lab no search  field
       lab_no_search = driver.find_element(By.ID,"labnoSearch")
       lab_no_search.clear()
       lab_no_search.send_keys("1234519000215")
       search = driver.find_elements(By.XPATH, "//input[@onclick='pageSearch.doLabNoSearch($(labnoSearch))']")
       search[0].click()
       page_source = driver.page_source
       assert 'background-color: rgb(255, 255, 36);' in page_source

       #Message appears: 'search item not found' if number is not use
       lab_no_search.clear()
       lab_no_search.send_keys("12345190000")
       search[0].click()
       page_source = driver.page_source
       assert 'Order number not found' in page_source

   @api.assert_capture()
   def test_04_entering_test_results(self):
       #Result -> By unit
       driver = self.driver
       action = ActionChains(driver)
       firstLevelMenu = driver.find_element(By.ID, "menu_results")
       action.move_to_element(firstLevelMenu).perform()
       secondLevelMenu = driver.find_element(By.ID,'menu_results_logbook')
       action.move_to_element(secondLevelMenu).perform()
       secondLevelMenu.click()

       
       select = WebDriverWait(driver, 10).until(
           EC.visibility_of_element_located((By.ID, "testSectionId"))
       )
       all_options = select.find_elements_by_tag_name("option")
       all_options[1].click()
       
       #Reference range correct

       #Result can be entered in the field
       for i in range(3,5):
           input_field = driver.find_elements(By.XPATH, "//tr[@id='row_%s']/td[@id='cell_%s']/input[@id='results_%s']"%(str(i),str(i),str(i)))
           input_field[0].clear()
           input_field[0].send_keys(randint(1,10))
           time.sleep(0.5)
           input_field[0].clear()
           
       #Result unit display correctly
       for i in range(3,5):
           test_range_with_unit = driver.find_elements(By.XPATH, "//tr[@id='row_%s']/td[3]"%(str(i)))
           test_range_with_unit = test_range_with_unit[0].text
           unit = driver.find_elements(By.XPATH, "//tr[@id='row_%s']/td[6]"%(str(i)))
           unit = unit[0].text
           assert unit in test_range_with_unit

       #Result convert to correct decimal(rounding, display, ) for the test: exemple first test
       input_field = driver.find_elements(By.XPATH, "//tr[@id='row_3']/td[@id='cell_3']/input[@id='results_3']")
       input_field[0].clear()
       input_field[0].send_keys('8.5')
       input_click = driver.find_elements(By.XPATH, "//tr[@id='row_4']/td[@id='cell_4']/input[@id='results_4']")
       input_click[0].click()
       time.sleep(3)
       input_rouding = input_field[0].get_attribute('value')
       print ('input_rouding', input_rouding)
       time.sleep(3)
       #assert input_rouding == '9'

       #Result Out of range: Yellow Background(rgb(255, 255, 160)
       #Reflesh Result Page
       select = WebDriverWait(driver, 10).until(
           EC.visibility_of_element_located((By.ID, "testSectionId"))
       )
       all_options = select.find_elements_by_tag_name("option")
       all_options[1].click()
       WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

       alert = driver.switch_to.alert
       alert.accept()
       
       input_field = WebDriverWait(driver, 10).until(
           EC.visibility_of_element_located((By.XPATH, "//tr[@id='row_3']/td[@id='cell_3']/input[@id='results_3']"))
       )
       input_field.clear()
       input_field.send_keys('50')
       input_click = driver.find_elements(By.XPATH, "//tr[@id='row_4']/td[@id='cell_4']/input[@id='results_4']")
       input_click[0].click()
       time.sleep(3)
       page_source = driver.page_source
       #assert 'background: rgb(255, 255, 160);' in page_source

       #Result Out of range: Red Background(background: rgb(255, 160, 160);)
       input_field = WebDriverWait(driver, 10).until(
           EC.visibility_of_element_located((By.XPATH, "//tr[@id='row_5']/td[@id='cell_5']/input[@id='results_5']"))
       )
       input_field.clear()
       input_field.send_keys('67')
       input_click = driver.find_elements(By.XPATH, "//tr[@id='row_7']/td[@id='cell_7']/input[@id='results_7']")
       input_click[0].click()
       time.sleep(3)
       page_source = driver.page_source
       #assert 'background: rgb(255, 160, 160);' in page_source
       
       #Click on green add icon note: Note fields displays
       add_icon = driver.find_elements(By.XPATH, "//tr[@id='row_3']/td[9]/img")
       add_icon[0].click()
       page_source = driver.page_source
       note_row = WebDriverWait(driver, 10).until(
           EC.visibility_of_element_located((By.ID, "noteRow_3"))
       )
       style = note_row.get_attribute('style')
       self.assertFalse(style)

       #Enter a text, then click on a arraw icon: notebook appears
       note = driver.find_elements(By.ID, "note_3")
       note[0].clear()
       note[0].send_keys('je suis un test')
       show_hide_button = driver.find_elements(By.ID, "showHideButton_3")
       show_hide_button[0].click()
       note_edit = driver.find_element_by_xpath('//img[contains(@src,"note-edit")]')
       assert True if note_edit else False

       #Enter select list result: go to the Serology-Immunology section
       select = WebDriverWait(driver, 10).until(
           EC.visibility_of_element_located((By.ID, "testSectionId"))
       )
       all_options = select.find_elements_by_tag_name("option")
       all_options[3].click()

       WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

       alert = driver.switch_to.alert
       alert.accept()

       select = WebDriverWait(driver, 10).until(
           EC.visibility_of_element_located((By.ID, "resultId_0"))
       )
       result_list = select.find_elements_by_tag_name("option")
       for result in result_list:
           result.click()

       #Click Checkbox for result automate: check box sticks or unchek sticks
       force_tech_approval1 = driver.find_elements(By.ID, "testResult10.forceTechApproval1")    
       force_tech_approval1[0].click()
       WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

       alert = driver.switch_to.alert
       alert.accept()
       time.sleep(3)
       force_tech_approval1[0].click()
       
   @api.assert_capture()  
   def test_05_overall_page(self):
       #Result -> By unit
       driver = self.driver
       action = ActionChains(driver)
       firstLevelMenu = driver.find_element(By.ID, "menu_results")
       action.move_to_element(firstLevelMenu).perform()
       secondLevelMenu = driver.find_element(By.ID,'menu_results_logbook')
       action.move_to_element(secondLevelMenu).perform()
       secondLevelMenu.click()

       select = WebDriverWait(driver, 10).until(
           EC.visibility_of_element_located((By.ID, "testSectionId"))
       )
       all_options = select.find_elements_by_tag_name("option")
       all_options[1].click()

       #Click cancel: Trigger Message
       for i in range(3,5):
           input_field = driver.find_elements(By.XPATH, "//tr[@id='row_%s']/td[@id='cell_%s']/input[@id='results_%s']"%(str(i),str(i),str(i)))
           input_field[0].clear()
           input_field[0].send_keys(randint(1,100))
           time.sleep(0.5)

       #Cancel Button and stay on page
       cancel_button_id = driver.find_element(By.ID,"cancelButtonId")
       cancel_button_id.click()
       WebDriverWait(driver, 5).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

       alert = driver.switch_to.alert
       alert.dismiss()

       save_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "saveButtonId"))
       )
       save_button.click()

       #successMsg
       success_msg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "successMsg"))
       )
       assert  'Save was successful' == success_msg.text and 'color: seagreen;' in success_msg.get_attribute('style')

       
       #Cancel Button and leave the page
       select = WebDriverWait(driver, 10).until(
           EC.visibility_of_element_located((By.ID, "testSectionId"))
       )
       all_options = select.find_elements_by_tag_name("option")
       all_options[1].click()

       for i in range(3,5):
           input_field = WebDriverWait(driver, 10).until(
              EC.visibility_of_element_located((By.XPATH, "//tr[@id='row_%s']/td[@id='cell_%s']/input[@id='results_%s']"%(str(i),str(i),str(i))))
           )
           input_field.clear()
           input_field.send_keys(randint(1,100))
           time.sleep(0.5)

       cancel_button_id = driver.find_element(By.ID,"cancelButtonId")
       cancel_button_id.click()
       WebDriverWait(driver, 5).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

       alert = driver.switch_to.alert
       alert.accept()

   @api.assert_capture()        
   def test_06_verification(self):
       driver = self.driver
       
       #Result -> Search -> by patient
       action = ActionChains(driver)
       
       firstLevelMenu = driver.find_element(By.ID, "menu_results")
       action.move_to_element(firstLevelMenu).perform()
       
       secondLevelMenu = driver.find_element(By.ID,'menu_results_search')
       action.move_to_element(secondLevelMenu).perform()

       thirdLevelMenu = driver.find_element(By.ID,'menu_results_patient')
       action.move_to_element(thirdLevelMenu).perform()
       
       thirdLevelMenu.click()

       search_value_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchValue"))
       )
       select = driver.find_element_by_id('searchCriteria')
       all_options = select.find_elements_by_tag_name("option")
       search_by_last_name = all_options[1]
       search_by_last_name.click()
       search_value_field.clear()
       search_value_field.send_keys('McGee')
       search_button_field = driver.find_element(By.ID,"searchButton")
       search_button_field.click()
       WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "resultsDiv"))
       )
       time.sleep(3)
       page_source = driver.page_source

       assert 'Last Name' in page_source and \
              'First Name' in page_source and \
              'Gender' in page_source and \
              'Date of Birth' in page_source and \
              'National ID' in page_source and \
              'Subject Number' in page_source

       #Search page appears
       search_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchDiv"))
       )
       assert True if search_div else False

       #Result -> Search -> by Order
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
       
       #Result -> Search -> by Test, Date or Status
       action = ActionChains(driver)
       
       firstLevelMenu = driver.find_element(By.ID, "menu_results")
       action.move_to_element(firstLevelMenu).perform()
       
       secondLevelMenu = driver.find_element(By.ID,'menu_results_search')
       action.move_to_element(secondLevelMenu).perform()

       thirdLevelMenu = driver.find_element(By.ID,'menu_results_status')
       action.move_to_element(thirdLevelMenu).perform()
       
       thirdLevelMenu.click()

       #Search page appears
       search_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchDiv"))
       )
       assert True if search_div else False
       
       #GO TO HOME
       menu_home = driver.find_element(By.ID, "menu_home")
       menu_home.click()

       #Result->By unit
       action = ActionChains(driver)
       firstLevelMenu = driver.find_element(By.ID, "menu_results")
       action.move_to_element(firstLevelMenu).perform()
       secondLevelMenu = driver.find_element(By.ID,'menu_results_logbook')
       action.move_to_element(secondLevelMenu).perform()
       secondLevelMenu.click()

       
       select = WebDriverWait(driver, 10).until(
           EC.visibility_of_element_located((By.ID, "testSectionId"))
       )
       all_options = select.find_elements_by_tag_name("option")
       all_options[1].click()
       
       #Result can be entered in the field
       for i in range(3,5):
           input_field = driver.find_elements(By.XPATH, "//tr[@id='row_%s']/td[@id='cell_%s']/input[@id='results_%s']"%(str(i),str(i),str(i)))
           input_field[0].clear()
           input_field[0].send_keys('31')
           
       save_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "saveButtonId"))
       )
       save_button.click()
       #Reflesh after save
       select = WebDriverWait(driver, 10).until(
           EC.visibility_of_element_located((By.ID, "testSectionId"))
       )
       all_options = select.find_elements_by_tag_name("option")
       all_options[1].click()

       
       #Go to Validation: validate results 
       menu_home = driver.find_element(By.ID, "menu_resultvalidation")
       menu_home.click()

       select = WebDriverWait(driver, 10).until(
           EC.visibility_of_element_located((By.ID, "testSectionId"))
       )
       all_options = select.find_elements_by_tag_name("option")
       all_options[2].click()

       assert 'CD4' in driver.page_source

       select_all_accept = driver.find_elements(By.ID, "selectAllAccept")
       select_all_accept[0].click()
       save_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "saveButtonId"))
       )
       save_button.click()

       WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

       alert = driver.switch_to.alert
       alert.accept()
       
   @api.assert_capture()
   def test_07_accept_as_is_functionality(self):
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

       search_accession_id = WebDriverWait(driver, 10).until(
           EC.visibility_of_element_located((By.ID, "searchAccessionID"))
       )
       search_accession_id.clear()
       search_accession_id.send_keys('1234519000002')
       retrieve_tests_id = driver.find_element(By.ID,"retrieveTestsID")
       retrieve_tests_id.click()

       #Check accept as is box
       force_tech_approval1 = driver.find_elements(By.ID, "testResult1.forceTechApproval1")    
       force_tech_approval1[0].click()
       #Pop up appears: click ok
       WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

       alert = driver.switch_to.alert
       alert.accept()
       time.sleep(3)
       #note field open
       note_row = WebDriverWait(driver, 10).until(
           EC.visibility_of_element_located((By.ID, "note_1"))
       )
       style = note_row.get_attribute('style')
       self.assertFalse(style)

       """

       #enter text
       note = driver.find_elements(By.ID, "note_1")
       note[0].clear()
       note[0].send_keys('je suis un test')

       #Close note box: triange symble transform to note edit
       show_hide_button = driver.find_elements(By.ID, "showHideButton_1")
       show_hide_button[0].click()
       note_edit = WebDriverWait(driver, 10).until(
           EC.visibility_of_element_located((By.XPATH, '//img[contains(@src,"note-edit")]'))
       )
       assert True if note_edit else False

       #Check another 2 result with accept as is: Pop up not appears
       force_tech_approval2 = driver.find_elements(By.ID, "testResult2.forceTechApproval1")    
       force_tech_approval2[0].click()
       force_tech_approval3 = driver.find_elements(By.ID, "testResult3.forceTechApproval1")    
       force_tech_approval3[0].click()

       #Uncheck accept as is for one this result: Note Bloc close
       force_tech_approval3[0].click()
       note_row = driver.find_elements(By.ID, "noteRow_3")
       style = note_row[0].get_attribute('style')
       self.assertEqual(style, 'display: none;')

       #Save Button: Green message display
       save_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "saveButtonId"))
       )
       save_button.click()

       #successMsg
       success_msg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "successMsg"))
       )
       assert  'Save was successful' == success_msg.text and 'color: seagreen;' in success_msg.get_attribute('style')
       """
       
       
   @api.assert_capture()         
   def test_08_verification(self):
       #Go to Validation: validate results
       driver = self.driver
       menu_home = driver.find_element(By.ID, "menu_resultvalidation")
       menu_home.click()

       select = WebDriverWait(driver, 10).until(
           EC.visibility_of_element_located((By.ID, "testSectionId"))
       )
       all_options = select.find_elements_by_tag_name("option")
       all_options[1].click()

       time.sleep(5)

       assert 'je suis un test' in driver.page_source

   @api.assert_capture()  
   def test_09_changing_result(self):
       driver = self.driver

       assert False

       
       
       

       
       
       
       time.sleep(5)

   def tearDown(self):
       self.driver.close()
       self.driver.quit()

