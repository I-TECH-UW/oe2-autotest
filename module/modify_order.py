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

class ModifyOrder(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.connecting()

    def connecting(self):
        "This method allows us to connect to the site"
        driver = self.driver
        driver.get('http://test.openelisci.org')
        username_field = driver.find_element_by_id("loginName")
        username_field.clear()
        username_field.send_keys('admin')
        password_field = driver.find_element_by_id("password")
        password_field.clear()
        password_field.send_keys('adminADMIN!')
        submit_button = driver.find_element_by_id('submitButton')
        submit_button.click()


    def goToModifyOrderPage(self):
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_sample']")
        action.move_to_element(firstLevelMenu).perform()
        # Getting to the submenu: Add Order, and clicking on it to go to the Add order form appears
        secondLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_sample_edit']")
        secondLevelMenu.click()

    def goToWorkplanByTestType(self):
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_workplan")
        action.move_to_element(firstLevelMenu).perform()

        secondLevelMenu = driver.find_element_by_id('menu_workplan_test')

        bad_message = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "menu_workplan_test"))
        )
        action.move_to_element(secondLevelMenu).perform()
        secondLevelMenu.click()

    def goToWorkplanByPanelType(self):
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_workplan")
        action.move_to_element(firstLevelMenu).perform()

        secondLevelMenu = driver.find_element_by_id('menu_workplan_panel')

        bad_message = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "menu_workplan_panel"))
        )
        action.move_to_element(secondLevelMenu).perform()
        secondLevelMenu.click()

    def goToWorkplanByUnit(self):
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_workplan")
        action.move_to_element(firstLevelMenu).perform()

        secondLevelMenu = driver.find_element_by_id('menu_workplan_bench')

        bad_message = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "menu_workplan_bench"))
        )
        action.move_to_element(secondLevelMenu).perform()
        secondLevelMenu.click()

    @api.assert_capture()
    def test_01_order_search(self):
        driver = self.driver
        self.goToModifyOrderPage()
        # Asserting that that the Add order form appears
        assert "Search" in driver.page_source

        select = driver.find_element_by_id('searchCriteria')
        all_options = select.find_elements_by_tag_name("option")
        search_value_field = driver.find_element_by_id("searchValue")
        time.sleep(5)


        # Search button deactivated until search criteria is selected and text entered
        table = ["SADIO", "Aliou", "SADIO, Aliou", "201508D10P", "1234519000103"]
        i = 0
        for option in all_options[1:]:
            option.click()
            time.sleep(2)
            search_value_field.clear()
            search_value_field.send_keys(table[i])
            time.sleep(3)
            i += 1

        select.click()

        # Search BY LAST NAME
        search_by_last_name = all_options[1]
        search_by_last_name.click()
        time.sleep(3)
        search_value_field.clear()
        search_value_field.send_keys('SADIO')
        time.sleep(3)
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        time.sleep(5)

        # Search BY LASTNAME WITH ACCENT
        select = driver.find_element_by_id('searchCriteria')
        all_options = select.find_elements_by_tag_name("option")
        search_value_field = driver.find_element_by_id("searchValue")
        search_value_field.clear()
        search_by_last_name_accent = all_options[1]
        search_by_last_name_accent.click()
        time.sleep(4)
        search_value_field.send_keys('éhemba')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        time.sleep(7)

        # Search BY FIRST NAME
        select = driver.find_element_by_id('searchCriteria')
        all_options = select.find_elements_by_tag_name("option")
        search_value_field = driver.find_element_by_id("searchValue")
        search_value_field.clear()
        search_by_first_name = all_options[2]
        search_by_first_name.click()
        search_value_field.send_keys('Aliou')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        time.sleep(7)

        # Search BY FIRST NAME WITH ACCENT
        select = driver.find_element_by_id('searchCriteria')
        all_options = select.find_elements_by_tag_name("option")
        search_value_field = driver.find_element_by_id("searchValue")
        search_value_field.clear()
        search_by_first_name = all_options[2]
        search_by_first_name.click()
        search_value_field.send_keys('Jérémie')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        time.sleep(7)

        # Search BY LASTNAME FIRSTNAME
        select = driver.find_element_by_id('searchCriteria')
        all_options = select.find_elements_by_tag_name("option")
        search_value_field = driver.find_element_by_id("searchValue")
        search_value_field.clear()
        search_by_first_last_name = all_options[3]
        search_by_first_last_name.click()
        search_value_field.send_keys('SADIO,Aliou')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        time.sleep(7)

        # Search BY LASTNAME FIRSTNAME WITH ACCENT
        select = driver.find_element_by_id('searchCriteria')
        all_options = select.find_elements_by_tag_name("option")
        search_value_field = driver.find_element_by_id("searchValue")
        search_value_field.clear()
        search_by_first_last_name = all_options[3]
        search_by_first_last_name.click()
        search_value_field.send_keys('émilie,Sémédo')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        time.sleep(7)

        # Search BY LASTNAME FIRSTNAME OMIT COMMA
        select = driver.find_element_by_id('searchCriteria')
        all_options = select.find_elements_by_tag_name("option")
        search_value_field = driver.find_element_by_id("searchValue")
        search_value_field.clear()
        search_by_first_last_name = all_options[3]
        search_by_first_last_name.click()
        search_value_field.send_keys('émilie Sémédo')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        time.sleep(7)

        # Search BY PATIENT IDENTIFIANT CODE USING SUBJECT NUMBER
        select = driver.find_element_by_id('searchCriteria')
        all_options = select.find_elements_by_tag_name("option")
        search_value_field = driver.find_element_by_id("searchValue")
        search_value_field.clear()
        search_by_first_last_name = all_options[4]
        search_by_first_last_name.click()
        search_value_field.send_keys('201507D10P')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        time.sleep(7)

        # Search BY PATIENT IDENTIFIANT CODE USING IDENTIFIANT NUMBER
        select = driver.find_element_by_id('searchCriteria')
        all_options = select.find_elements_by_tag_name("option")
        search_value_field = driver.find_element_by_id("searchValue")
        search_value_field.clear()
        search_by_first_last_name = all_options[5]
        search_by_first_last_name.click()
        search_value_field.send_keys('1234519000111')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        time.sleep(7)

    @api.assert_capture()
    def test_02_orderInformation(self):
        driver = self.driver
        self.goToModifyOrderPage()

        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "searchCriteria"))
        )
        time.sleep(4)
        #pull up a known order
        select = driver.find_element_by_id('searchCriteria')
        all_options = select.find_elements_by_tag_name("option")
        search_value_field = driver.find_element_by_id("searchValue")
        search_value_field.clear()
        search_by_first_last_name = all_options[5]
        search_by_first_last_name.click()
        search_value_field.send_keys('1234500000012')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        time.sleep(15)

        #Enter incorrect Accession Number

        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "accessionEdit"))
        )
        time.sleep(1)

        accessionEdit = driver.find_element_by_id("accessionEdit")
        accessionEdit.clear()
        accessionEdit.send_keys("313SD455")

        request_date = driver.find_element_by_id("requestDate")
        request_date.click()
        time.sleep(5)

        WebDriverWait(driver, 5).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.dismiss()

        accessionEdit.clear()
        time.sleep(5)
        accessionEdit.send_keys('00000012')

        time.sleep(2)

        request_date.click()
        accessionEdit.clear()
        time.sleep(2)
        #Resusing an existing access number
        accessionEdit.send_keys('19000117')
        request_date.click()
        time.sleep(7)

        WebDriverWait(driver, 5).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')

        alert = driver.switch_to.alert
        print(dir(alert), alert.text)
        alert.dismiss()

        # Text box highlighted in red entry is not in the correct DD/MM/YYYY format.
        request_date_field = driver.find_element_by_id("requestDate")
        received_date_field = driver.find_element_by_id("receivedDateForDisplay")

        request_date_field.clear()
        request_date_field.send_keys('09-02/2019')
        received_date_field.click()
        time.sleep(5)
        self.assertEqual(driver.find_element_by_id("requestDate").get_attribute("class"), "required error")

        # Alert appears if date is in the future )
        request_date_field.clear()
        next_day = (datetime.datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
        request_date_field.send_keys(next_day)
        received_date_field.click()
        time.sleep(5)
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(4)
        future_date_alert = request_date_field.get_attribute('class')
        time.sleep(4)
        self.assertEqual(future_date_alert, 'required error')

        #Enter correct date in the order date field
        time.sleep(5)
        request_date_field.clear()
        time.sleep(3)
        request_date_field.send_keys(datetime.datetime.now().strftime("%d/%m/%Y"))

        ##################################################################"""
        #Enter received in incorrect format
        received_date_field.clear()
        received_date_field.send_keys('09-02/2019')
        request_date_field.click()
        time.sleep(5)
        self.assertEqual(driver.find_element_by_id("receivedDateForDisplay").get_attribute("class"), "text required error")

        # Alert appears if date is in the future )
        received_date_field.clear()
        received_date_field.send_keys(next_day)
        request_date_field.click()
        time.sleep(5)
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(4)
        future_date_alert = received_date_field.get_attribute('class')
        time.sleep(4)
        self.assertEqual(future_date_alert, 'text required error')

        # Enter correct date in the order date field
        time.sleep(5)
        received_date_field.clear()
        time.sleep(3)
        received_date_field.send_keys(datetime.datetime.now().strftime("%d/%m/%Y"))
        request_date_field.click()

        time.sleep(5)

        ###############################################################"

        #Reception time
        reception_time_field = driver.find_element_by_id("receivedTime")
        reception_time_field.clear()
        # Enter time in incorrect format
        reception_time_field.send_keys('1d2d77D')
        received_date_field.click()
        time.sleep(3)
        # Result: field rejects non-numeric entries, additional digits, etc, automatically corrects straight numeric ot proper correct format HH:MM
        self.assertEqual(reception_time_field.get_attribute('value'), '12:77')
        # Result: Red alert alert appears if time does not exist on 12 or 24 hour clock
        self.assertEqual(reception_time_field.get_attribute('class'), ' error')
        time.sleep(4)
        reception_time_field.clear()

        # Enter time as HHMM
        reception_time_field.send_keys('1254')
        received_date_field.click()
        time.sleep(3)
        # Automatically corrects straight numeric to proper format HH:MM
        self.assertEqual(reception_time_field.get_attribute('value'), '12:54')
        reception_time_field.clear()
        time.sleep(3)

        # Enter time as HH:MM
        reception_time_field.send_keys('13:54')
        received_date_field.click()
        time.sleep(3)
        # Fields accepts correct format
        self.assertEqual(reception_time_field.get_attribute('value'), '13:54')

        # Enter the site name
        select = driver.find_element_by_id('requesterId')
        select.click()
        time.sleep(3)
        all_options = select.find_elements_by_tag_name("option")
        n = 0
        for option in all_options[1:]:
            if n == 4:
                break
            option.click()
            time.sleep(3)
            n = n + 1

        # Enter new site name
        n = 0
        for option in all_options[1:]:
            if n == 5:
                break
            option.click()
            time.sleep(3)
            n = n + 1

        select.click()
        time.sleep(7)

    @api.assert_capture()
    def test_03_currentTestInformation(self):
        driver = self.driver
        self.goToModifyOrderPage()

        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "searchCriteria"))
        )
        time.sleep(4)
        # pull up a known order
        select = driver.find_element_by_id('searchCriteria')
        all_options = select.find_elements_by_tag_name("option")
        search_value_field = driver.find_element_by_id("searchValue")
        search_value_field.clear()
        search_by_first_last_name = all_options[5]
        search_by_first_last_name.click()
        search_value_field.send_keys('1234500000012')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        time.sleep(15)

        # Enter new collection Date In incorrect format (1. alpha, 2. alpha numeric, 3. without /, 4. other)
        collection_date = driver.find_element_by_name('existingTests[0].collectionDate')
        collection_date.clear()
        collection_date.send_keys('25/24/2138')
        # Text field hightlighted in red if date is not in the correct DD/MM/YYYY format.
        driver.find_element_by_name('existingTests[0].collectionTime').click()
        time.sleep(7)
        self.assertEqual(collection_date.get_attribute("class"), "text  error")
        time.sleep(4)

        # Enter Date in the future (1. tomorrow's date, 2. next month , 3. in 100 years)
        collection_date.clear()
        next_day = (datetime.datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
        collection_date.send_keys(next_day)
        driver.find_element_by_name('existingTests[0].collectionTime').click()
        time.sleep(7)
        # Pop-up alert appears if date is in the future.
        WebDriverWait(driver, 7).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.accept()
        self.assertEqual(collection_date.get_attribute("class"), "text  error")
        # Enter correct date in Collection Date filed.
        time.sleep(10)
        collection_date.clear()
        collection_date.send_keys(datetime.datetime.now().strftime("%d/%m/%Y"))
        time.sleep(5)

        # Enter new collection time in incorrect format(1. non-numeric, 2. extra digits, etc)
        time.sleep(4)
        collection_time = driver.find_element_by_name('existingTests[0].collectionTime')
        collection_time.clear()
        collection_time.send_keys('A207FG8888')
        time.sleep(4)
        # Rejects non-numeric entries, additional digits, etc
        self.assertEqual(collection_time.get_attribute('value'), '20:78')
        time.sleep(3)
        collection_time.clear()

        # Enter time as HHMM
        collection_time.send_keys('2030')
        time.sleep(4)
        # Automatically corrects straight numeric entry to proper format HH:MM
        self.assertEqual(collection_time.get_attribute('value'), '20:30')
        time.sleep(3)
        collection_time.clear()

        # Enter time as HH:MM
        collection_time.send_keys('20:30')
        # Field accepts correct format
        self.assertEqual(collection_time.get_attribute('value'), '20:30')
        time.sleep(3)

        # Click remove sample checkbox
        checke_checkbox = driver.find_element_by_id('existingTests0.removeSample1')
        checke_checkbox.click()
        time.sleep(4)

        # Uncheck remove sample checkbox
        checke_checkbox.click()
        time.sleep(4)
        # Recheck remove sample checkbox
        checke_checkbox.click()

        #Check  delete cancel test
        delete_checke_checkbox = driver.find_element_by_name('existingTests[1].canceled')
        delete_checke_checkbox.click()
        time.sleep(3)
        # Uncheck  delete cancel test
        delete_checke_checkbox.click()
        time.sleep(3)
        #Recheck delete cancel test
        delete_checke_checkbox.click()

        time.sleep(4)

    @api.assert_capture()
    def test_04_availableTestInformation(self):
        driver = self.driver
        self.goToModifyOrderPage()

        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "searchCriteria"))
        )
        time.sleep(4)
        # pull up a known order
        select = driver.find_element_by_id('searchCriteria')
        all_options = select.find_elements_by_tag_name("option")
        search_value_field = driver.find_element_by_id("searchValue")
        search_value_field.clear()
        search_by_first_last_name = all_options[5]
        search_by_first_last_name.click()
        search_value_field.send_keys('1234500000012')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "possibleTests0.add1"))
        )

        #Check box next to several tests
        check_field = driver.find_element_by_id("possibleTests0.add1")
        check_field.click()
        time.sleep(10)

    #@api.assert_capture()
    def test_05_addOrder(self):
        driver = self.driver
        self.goToModifyOrderPage()

        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "searchCriteria"))
        )
        time.sleep(4)
        # pull up a known order
        select = driver.find_element_by_id('searchCriteria')
        all_options = select.find_elements_by_tag_name("option")
        search_value_field = driver.find_element_by_id("searchValue")
        search_value_field.clear()
        search_by_first_last_name = all_options[5]
        search_by_first_last_name.click()
        search_value_field.send_keys('1234500000012')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        time.sleep(15)

        #Click on drop-down Sample Type list
        select = driver.find_element_by_id('sampleTypeSelect')
        select.click()
        time.sleep(3)

        #Adding and highlightin sample type

        all_options = select.find_elements_by_tag_name("option")
        for option in all_options[1:]:
            option.click()
            time.sleep(4)

        #Click remove sample
        remove = driver.find_element_by_id('removeButton_1')
        remove.click()
        WebDriverWait(driver, 10).until(EC.alert_is_present(), 'Timed out waiting for PA creation ' + 'confirmation popup to appear.')
        alert = driver.switch_to.alert
        alert.accept()

        #Click remove all
        remove_all_button = driver.find_element_by_xpath("//input[@value='Remove All']")
        remove_all_button.click()
        WebDriverWait(driver, 10).until(EC.alert_is_present(), 'Timed out waiting for PA creation ' + 'confirmation popup to appear.')
        alert = driver.switch_to.alert
        alert.accept()
        

        #Re-add sample

        for option in all_options[1:]:
            option.click()
            time.sleep(4)

        time.sleep(7)

    #@api.assert_capture()
    def test_06_collectionDate(self):
        driver = self.driver
        self.goToModifyOrderPage()

        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "searchCriteria"))
        )
        time.sleep(4)
        # pull up a known order
        select = driver.find_element_by_id('searchCriteria')
        all_options = select.find_elements_by_tag_name("option")
        search_value_field = driver.find_element_by_id("searchValue")
        search_value_field.clear()
        search_by_first_last_name = all_options[5]
        search_by_first_last_name.click()
        search_value_field.send_keys('1234500000012')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        time.sleep(15)

        # Click on drop-down Sample Type list
        select = driver.find_element_by_id('sampleTypeSelect')

        # Adding a sample type

        all_options = select.find_elements_by_tag_name("option")
        for option in all_options[1:]:
            option.click()
            break
        time.sleep(4)

        # Enter Date In incorrect format (1. alpha, 2. alpha numeric, 3. without /, 4. other)
        collection_date = driver.find_element_by_id('collectionDate_1')
        collection_date.clear()
        collection_date.send_keys('25/24/2138')

        # Text field hightlighted in red if date is not in the correct DD/MM/YYYY format.
        driver.find_element_by_id('collectionDate_0').click()
        time.sleep(7)
        self.assertEqual(collection_date.get_attribute("class"), "text  error")
        time.sleep(4)

        # Enter Date in the future (1. tomorrow's date, 2. next month , 3. in 100 years)
        collection_date.clear()
        next_day = (datetime.datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
        collection_date.send_keys(next_day)
        driver.find_element_by_id('collectionDate_0').click()
        time.sleep(7)
        # Pop-up alert appears if date is in the future.
        WebDriverWait(driver, 2).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.accept()
        self.assertEqual(collection_date.get_attribute("class"), "text  error")
        # Enter correct date in Collection Date filed.
        # Date can be changed manually (field accepts text and saves at the end).
        time.sleep(10)
        collection_date.clear()
        collection_date.send_keys(datetime.datetime.now().strftime("%d/%m/%Y"))
        time.sleep(5)

    #@api.assert_capture()
    def test_07_collectionTime(self):
        driver = self.driver
        self.goToModifyOrderPage()

        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "searchCriteria"))
        )
        time.sleep(4)
        # pull up a known order
        select = driver.find_element_by_id('searchCriteria')
        all_options = select.find_elements_by_tag_name("option")
        search_value_field = driver.find_element_by_id("searchValue")
        search_value_field.clear()
        search_by_first_last_name = all_options[5]
        search_by_first_last_name.click()
        search_value_field.send_keys('1234500000012')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        time.sleep(15)

        # Click on drop-down Sample Type list
        select = driver.find_element_by_id('sampleTypeSelect')

        # Adding a sample type

        all_options = select.find_elements_by_tag_name("option")
        for option in all_options[1:]:
            option.click()
            break
        time.sleep(4)

        # Enter time in incorrect format(1. non-numeric, 2. extra digits, etc)
        time.sleep(4)
        collection_time = driver.find_element_by_id('collectionTime_1')
        collection_time.clear()
        collection_time.send_keys('A207FG8888')
        time.sleep(4)
        # Rejects non-numeric entries, additional digits, etc
        self.assertEqual(collection_time.get_attribute('value'), '20:78')
        time.sleep(3)
        collection_time.clear()

        # Enter time as HHMM
        collection_time.send_keys('2030')
        time.sleep(4)
        # Automatically corrects straight numeric entry to proper format HH:MM
        self.assertEqual(collection_time.get_attribute('value'), '20:30')
        time.sleep(3)
        collection_time.clear()

        # Enter time as HH:MM
        collection_time.send_keys('20:30')

        time.sleep(7)

    @api.assert_capture()
    def test_08_addTests(self):
        driver = self.driver
        self.goToModifyOrderPage()

        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "searchCriteria"))
        )
        time.sleep(4)
        # pull up a known order
        select = driver.find_element_by_id('searchCriteria')
        all_options = select.find_elements_by_tag_name("option")
        search_value_field = driver.find_element_by_id("searchValue")
        search_value_field.clear()
        search_by_first_last_name = all_options[5]
        search_by_first_last_name.click()
        search_value_field.send_keys('1234500000012')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        time.sleep(15)

        # Click on drop-down Sample Type list
        select = driver.find_element_by_id('sampleTypeSelect')

        # Adding a sample type

        all_options = select.find_elements_by_tag_name("option")
        option1 = all_options[1].click()

        # Tests entry is marked mandatory.
        marked_mandatory = driver.find_element_by_xpath(
            "//table[@id='samplesAddedTable']/tbody/tr/th/span[@class='requiredlabel']").get_attribute('class')
        self.assertEqual(marked_mandatory, 'requiredlabel')
        # Test Selection (Available Tests) appears for each sample type.

        # Test names are spelled correctly.
        # Check checkbox next to test name
        time.sleep(5)
        checke_checkbox = driver.find_element_by_id('test_0')
        checke_checkbox.click()
        time.sleep(4)
        # Checkbox sticks, test name appears under Tests box.
        self.assertEqual(driver.find_element_by_id('tests_1').get_attribute('value'), 'GOT/ASAT')

        # Uncheck checkbox next to test name
        checke_checkbox.click()
        time.sleep(4)
        # Name disapears from Testsbox.
        self.assertEqual(driver.find_element_by_id('tests_1').get_attribute('value'), '')

        # Check checkbox next to panel name
        checke_panel_checkbox = driver.find_element_by_id('panel_0')
        checke_panel_checkbox.click()
        time.sleep(7)
        # All applicable panel tests under Available Tests are automatically selected and these tests apear in the Testsbox.
        # Uncheck checkbox next to panel name
        checke_panel_checkbox.click()

    #@api.assert_capture()
    def test_09_overallPage(self):
        driver = self.driver
        self.goToModifyOrderPage()

        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "searchCriteria"))
        )
        time.sleep(4)
        # pull up a known order
        select = driver.find_element_by_id('searchCriteria')
        all_options = select.find_elements_by_tag_name("option")
        search_value_field = driver.find_element_by_id("searchValue")
        search_value_field.clear()
        search_by_first_last_name = all_options[5]
        search_by_first_last_name.click()
        search_value_field.send_keys('1234519000117')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        time.sleep(15)

        # Click on drop-down Sample Type list
        select = driver.find_element_by_id('sampleTypeSelect')

        # Adding a sample type

        all_options = select.find_elements_by_tag_name("option")
        option1 = all_options[1].click()

        time.sleep(4)

        #Leave mandatory field without data: save button is deactivated
        save_button_field = driver.find_element_by_id("saveButtonId")
        disabled = save_button_field.get_attribute("disabled")
        self.assertTrue(disabled)

        #Complete all mandatory fields: save button activated
        check_checkbox = driver.find_element_by_id('test_0')
        time.sleep(5)
        check_checkbox.click()
        time.sleep(7)

        save_button_field = driver.find_element_by_id("saveButtonId")
        disabled = save_button_field.get_attribute("disabled")
        self.assertFalse(disabled)
        time.sleep(7)

        #CLick Cancel
        cancel_button = driver.find_element_by_id("cancelButtonId")
        cancel_button.click()
        time.sleep(5)

        #Click stay on the page
        WebDriverWait(driver, 120).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.dismiss()

        time.sleep(10)

        #Click save
            #Let's select test result for delation :
        checke_checkbox_deleation = driver.find_element_by_name("existingTests[0].canceled")
        checke_checkbox_deleation.click()
        time.sleep(5)

        driver.find_element_by_id("saveButtonId").click()


        #Accepting the message: You are about to permanently delete a test and its result
        WebDriverWait(driver, 120).until(EC.alert_is_present(),
                                         'Timed out waiting for PA creation ' +
                                         'confirmation popup to appear.')

        time.sleep(5)

        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(5)

        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "successMsg"))
        )

        self.assertEqual(driver.find_element_by_id("successMsg").text, "Save was successful")
        time.sleep(7)

        cancel_button = driver.find_element_by_id("cancelButtonId")
        cancel_button.click()
        time.sleep(10)

    @api.assert_capture()
    def test_10_verification(self):
        driver = self.driver

        # Generate workplan by test
        self.goToWorkplanByTestType()

        select_test_type = driver.find_element_by_id("testName")
        bad_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "testName"))
        )
        all_type_options = select_test_type.find_elements_by_tag_name("option")

        time.sleep(5)
        option = all_type_options[4].click()

        time.sleep(5)

        bad_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "print"))
        )
        print_workplan_button = driver.find_element_by_id("print")
        print_workplan_button.click()
        time.sleep(15)

        ##################################################################################################################

        # Generate workplan by Panel
        self.goToWorkplanByPanelType()

        select_panel_type = driver.find_element_by_id("testName")
        bad_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "testName"))
        )
        all_panel_type_options = select_panel_type.find_elements_by_tag_name("option")

        time.sleep(5)

        for option in all_panel_type_options[1:]:
            option.click()
            break
        time.sleep(5)

        bad_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "print"))
        )
        print_panel_workplan_button = driver.find_element_by_id("print")
        print_panel_workplan_button.click()
        time.sleep(15)

        ###############################################################################################################################

        # Generate workplan by Unit
        self.goToWorkplanByUnit()

        select_unit_type = driver.find_element_by_id("testSectionId")
        bad_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "testSectionId"))
        )
        all_unit_type_options = select_unit_type.find_elements_by_tag_name("option")

        time.sleep(5)

        for option in all_unit_type_options[1:]:
            option.click()
            break
        time.sleep(5)

        bad_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "print"))
        )
        print_unit_workplan_button = driver.find_element_by_id("print")
        print_unit_workplan_button.click()
        time.sleep(15)

    def tearDown(self):
       self.driver.close()
       self.driver.quit()