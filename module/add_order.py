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

class OrderEntry(unittest.TestCase):

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
        print('Connected')

    def goToAddOrderPage(self):
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_sample']")
        action.move_to_element(firstLevelMenu).perform()
        # Getting to the submenu: Add Order, and clicking on it to go to the Add order form appears
        secondLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_sample_add']")
        secondLevelMenu.click()
    
    @api.assert_capture()
    def test_01_goToOrder(self):
        "This method allows us to test the order entries"
        # Getting to the main menu :Order
        driver = self.driver
        self.goToAddOrderPage()
        # Asserting that that the Add order form appears
        assert "Test Request" in driver.page_source
        time.sleep(10)
        driver.close()

    @api.assert_capture()
    def test_02_orderNumber(self):
        """ Order number """
        self.goToAddOrderPage()
        driver = self.driver
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "labNo"))
        )
        #Access number is mandatory
        mandatory = driver.find_element_by_xpath(
            "//div[@id='orderDisplay']/table/tbody/tr/td/table/tbody/tr[1]/td/span").get_attribute('class')
        self.assertEqual(mandatory, 'requiredlabel')
        # Enter accession Number in manually
        accession_number_field = driver.find_element_by_id("labNo")
        accession_number_field.clear()
        accession_number_field.send_keys('1234519000029')
        time.sleep(3)
        # a. Asserting the text we entered
        self.assertEqual(accession_number_field.get_attribute('value'), '1234519000029')
        #alert appears if format is not in the correct 9-digit format
        accession_number_field.clear()
        accession_number_field.send_keys('BETA119000047')
        driver.find_element_by_id('receivedTime').click()
        time.sleep(5)
        WebDriverWait(driver, 10).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.accept()
        self.assertEqual(accession_number_field.get_attribute('class'), 'text error')
        time.sleep(5)
        # Click Generate
            #1. Clearing the text field et generting values
        accession_number_field.clear()
        driver.find_element_by_class_name("textButton").click()
            #Checking that the accession number is automatically generated in the correct 9-digit numeric format
        time.sleep(7)
        generated_value = accession_number_field.get_attribute('value')
        # Checking that the generated number is a digit
        is_digit = generated_value.isdigit()
        self.assertIs(is_digit, True)

        time.sleep(10)
        driver.close()

    @api.assert_capture()
    def test_03_requestReceivedDate(self):
        """Request and Received Date"""
        self.goToAddOrderPage()
        driver = self.driver
        action = ActionChains(driver)
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "requestDate"))
        )
        # View page Request Date and Received Date Default to the current date
        request_date_field = driver.find_element_by_id("requestDate")
        received_date_field = driver.find_element_by_id("receivedDateForDisplay")
        request_date_field_content = request_date_field.get_attribute('value')
        received_date_field_content = received_date_field.get_attribute('value')
        date = str(datetime.datetime.now().strftime("%d/%m/%Y"))
            # Asserting that the request and received date are default to the current date
        self.assertEqual(request_date_field_content, date)
        self.assertEqual(received_date_field_content, date)

        # Both request and received date are mendatory
        required_request_date = driver.find_element_by_xpath(
            "//div[@id='orderDisplay']/table/tbody/tr/td/table/tbody/tr[2]/td/span").get_attribute('class')
        required_received_date = driver.find_element_by_xpath(
            "//div[@id='orderDisplay']/table/tbody/tr/td/table/tbody/tr[3]/td/span").get_attribute('class')
        self.assertEqual(required_request_date, 'requiredlabel')
        self.assertEqual(required_received_date, 'requiredlabel')

        # Alert appears if not entered in the correct DD/MM/YYYY format.
        request_date_field.clear()
        request_date_field.send_keys('09-02/2019')
        received_date_field.click()
        time.sleep(3)
        incorect_format_alert = request_date_field.get_attribute('class')
        # Asserting that after we send bad format, the alert apears
        self.assertEqual(incorect_format_alert, 'required error')
        time.sleep(4)

        # Alert appears if date is in the future )
        request_date_field.clear()
        next_day = (datetime.datetime.now()+ timedelta(days=1)).strftime("%d/%m/%Y")
        request_date_field.send_keys(next_day)
        received_date_field.click()
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(4)
        future_date_alert = request_date_field.get_attribute('class')
        time.sleep(4)
        self.assertEqual(future_date_alert, 'required error')

        # Enter correct date in the RequestDate and ReceivedDate
        request_date_field.clear()
        received_date_field.clear()
        privious_day_correct_date = (datetime.datetime.now() - timedelta(days=1)).strftime("%d/%m/%Y")
        request_date_field.send_keys(privious_day_correct_date)
        received_date_field.send_keys(privious_day_correct_date)

    @api.assert_capture()
    def test_04_receptionTime(self):
        """ Reception Time"""
        self.goToAddOrderPage()
        driver = self.driver
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "receivedTime"))
        )
        reception_time_field = driver.find_element_by_id("receivedTime")
        received_date_field = driver.find_element_by_id("receivedDateForDisplay")
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

    @api.assert_capture()
    def test_05_siteName(self):
        """ Site Name"""
        self.goToAddOrderPage()
        driver = self.driver
        # Enter the site name
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "requesterId"))
        )
        select = driver.find_element_by_id('requesterId')
        select.click()
        time.sleep(4)
        all_options = select.find_elements_by_tag_name("option")
        n = 0
        for option in all_options[1:]:
            if n == 5:
                break
            option.click()
            time.sleep(3)
            n = n + 1
        # The site name is mandatory
        site_name_required = driver.find_element_by_xpath("//div[@id='orderDisplay']/table/tbody/tr/td/table/tbody/tr[6]/td/span").get_attribute('class')
        self.assertEqual(site_name_required, 'requiredlabel')
        time.sleep(3)
        # Field accept text
        # Drop down menu displays with previous entries
        select.click()
        time.sleep(4)
        # Selection programm from drop down menu
        program_select = driver.find_element_by_id('sampleOrderItems.program')
        program_select.click()
        time.sleep(4)
        # Correct program options appear and can be selected
        program_options = program_select.find_elements_by_tag_name("option")
        for option in program_options[1:]:
            option.click()
            time.sleep(3)

    @api.assert_capture()
    def test_06_requestName(self):
        """ Request's name"""
        self.goToAddOrderPage()
        driver = self.driver
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "providerLastNameID"))
        )
        # Requester's Last Name is mandatory
        last_name_required = driver.find_element_by_xpath(
            "//div[@id='orderDisplay']/table/tbody/tr/td/table/tbody/tr[10]/td/span").get_attribute('class')
        self.assertEqual(last_name_required, 'requiredlabel')
        # Enter Requester's Last Name
        last_name_value = driver.find_element_by_id("providerLastNameID")
        last_name_value.send_keys("SADIO")
            # Field accepts text
        self.assertEqual(last_name_value.get_attribute('value'), "SADIO")
        # Enter First Name
        first_name_value = driver.find_element_by_id("sampleOrderItems.providerFirstName")
        first_name_value.send_keys("Aliou")
            # Field accepts text
        self.assertEqual(first_name_value.get_attribute('value'), "Aliou")

    @api.assert_capture()
    def test_07_requesterPhoneFaxEmail(self):
        """ Request phone Phone, Fax, Email"""
        self.goToAddOrderPage()
        driver = self.driver
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "providerWorkPhoneID"))
        )
        action = ActionChains(driver)
        # Enter telephone in incorrect format (1. alpha, 2. alpha numeric, 3. without spaces or punctuation, etc.)
        phone_number = driver.find_element_by_id("providerWorkPhoneID")

        phone_number.send_keys("+225-23-24-00")
        time.sleep(3)
        fax_number = driver.find_element_by_id("providerFaxID")
        fax_number.click()
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')
        time.sleep(3)

        alert = driver.switch_to.alert
        alert.accept()
        # Gives alert if format is not (dd)dddd-dd(alpha, alphanumeric, without spaces or punctuation (), -, et)
        self.assertEqual(phone_number.get_attribute('class'), "text error")
        phone_number.clear()
        time.sleep(5)

        # Enter Telephone number in correct format
        phone_number.send_keys("+225-33-45-87-88")
        fax_number.click()
        time.sleep(3)
        # Accepts correct format
        self.assertNotEqual(driver.find_element_by_id("providerWorkPhoneID").get_attribute('class'), "text error")

        # Enter Fax number
        fax_number = driver.find_element_by_id("providerFaxID")
        fax_number.send_keys("682737882")
        fax_number.click()
        time.sleep(3)
        # Accepts correct format
        #self.assertNotEqual(driver.find_element_by_id("providerFaxID").get_attribute('class'), "text error")
        # Enter email address
        email = driver.find_element_by_id("providerEmailID")
        email.clear()
        email.send_keys("sadioaliou5gmail.com")
        fax_number.click()
        time.sleep(5)
        # Accepts correct format
        self.assertEqual(email.get_attribute('class'), "text")

    @api.assert_capture()
    def test_08_paymentFields(self):
        """ Payment fields"""
        self.goToAddOrderPage()
        driver = self.driver
        action = ActionChains(driver)
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "sampleOrderItems.paymentOptionSelection"))
        )
        # Select payement status from drop down menu
        select = driver.find_element_by_id('sampleOrderItems.paymentOptionSelection')
        select.click()
        time.sleep(2)
        all_options = select.find_elements_by_tag_name("option")
        for option in all_options[1:]:
            option.click()
            time.sleep(3)
            # All payement options appear
            # Can select correct opttion from menu
        # CONFIGURABLE ITEM: Enter billing/URAP number
        admin_menu = driver.find_element_by_id('menu_administration')
        admin_menu.click()
        WebDriverWait(driver, 20).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')
        time.sleep(3)

        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(5)
        order_entry_conf = driver.find_element_by_xpath("//a[@href='/OpenElis/SampleEntryConfigMenu.do']")
        order_entry_conf.click()

        billing_ref_num = driver.find_element_by_id("selectedIDs2")
        billing_ref_num.click()
        time.sleep(2)
        edit = driver.find_element_by_id("edit")
        edit.click()
        time.sleep(5)
        true = driver.find_element_by_id("value1")
        true.click()
        time.sleep(2)
        save = driver.find_element_by_name("save")
        save.click()
        time.sleep(5)
        self.goToAddOrderPage()
        urap_number =driver.find_element_by_id("billingReferenceNumber")
        urap_number.send_keys("HFH4234D")
        time.sleep(3)
        self.assertEqual(urap_number.get_attribute("value"), "HFH4234D")

        # Field accepts text

    @api.assert_capture()
    def test_09_addSamples(self):
        """" Add samples Tests"""
        # Sample addition is mandatory
        driver = self.driver
        self.goToAddOrderPage()
        sample_addition_mandatory = driver.find_element_by_xpath(
            "//input[@id='samplesSectionId']/following-sibling::span[1]").get_attribute('class')
        print(sample_addition_mandatory)
        self.assertEqual(sample_addition_mandatory, 'requiredlabel')

        #CLick on + buttton next to Sample
        button_next_click = driver.find_element_by_id("samplesSectionId")
        button_next_click.click()
                #Sample + expands form
        sample_form_apear = driver.find_element_by_id("sampleTypeSelect")
        self.assertEqual(sample_form_apear.get_attribute('id'), 'sampleTypeSelect')

        #Click on drop-down list
        # Select payement status from drop down menu
            # Sample types display in drop-down list
        select = driver.find_element_by_id('sampleTypeSelect')
        select.click()
        time.sleep(4)
            # Sample types are correct(Biopsie, Plasma, Sang Total, Scotch Test Anal, Selles, Serum, Urines, Varie)
        all_options = select.find_elements_by_tag_name("option")
        i = 0
        t = ['Serum', ' Plasma', ' Urines', ' Sang total', ' DBS', ' Dry Tube', ' EDTA Tube']
        for option in all_options[1:]:
            self.assertIn(option.text, t)

            #Select a sample Type from the drop-down list.
        for option in all_options[1:]:
            option.click()
            break

        #Select sample  Condition form drop-down list.
        select_condition = driver.find_element_by_id('asmSelect0')
        select_condition.click()
        time.sleep(3)
        condition_option = select_condition.find_elements_by_tag_name("option")
        n = 0
        for option in condition_option[1:]:
            option.click()
            n = n + 1
            if n == 4:
                break
        time.sleep(2)
        #Click Remove
        remove_button = driver.find_element_by_id('removeButton_1')
        remove_button.click()

        #Click Remove all
        time.sleep(4)
        remove_all_button = driver.find_element_by_xpath("//input[@value='Remove All']")
        time.sleep(3)

        #Re-add samples
        time.sleep(3)
        for option in all_options[1:]:
            option.click()
        time.sleep(5)
        driver.close()

    @api.assert_capture()
    def test_10_collectionDate(self):
        """ Collection date tests"""
        driver = self.driver
        self.goToAddOrderPage()
        button_next_click = driver.find_element_by_id("samplesSectionId")
        button_next_click.click()
        select = driver.find_element_by_id('sampleTypeSelect')
        select.click()
        time.sleep(4)
        all_options = select.find_elements_by_tag_name("option")
        for option in all_options[1:]:
            option.click()
            break
        time.sleep(4)
        #Enter Date In incorrect format (1. alpha, 2. alpha numeric, 3. without /, 4. other)
        collection_date = driver.find_element_by_id('collectionDate_1')
        collection_date.clear()
        collection_date.send_keys('25/24/2138')
            #Text field hightlighted in red if date is not in the correct DD/MM/YYYY format.
        driver.find_element_by_id('collectionTime_1').click()
        time.sleep(7)
        self.assertEqual(collection_date.get_attribute("class"), "text error")
        time.sleep(4)
        #Enter Date in the future (1. tomorrow's date, 2. next month , 3. in 100 years)
        collection_date.clear()
        next_day = (datetime.datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
        collection_date.send_keys(next_day)
        driver.find_element_by_id('collectionTime_1').click()
        time.sleep(7)
            #Pop-up alert appears if date is in the future.
        WebDriverWait(driver, 2).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.accept()
        self.assertEqual(collection_date.get_attribute("class"), "text error")
        #Enter correct date in Collection Date filed.
            #Date can be changed manually (field accepts text and saves at the end).
        time.sleep(10)
        collection_date.clear()
        collection_date.send_keys(datetime.datetime.now().strftime("%d/%m/%Y"))
        time.sleep(5)
        driver.close()

    @api.assert_capture()
    def test_11_collectionTime(self):
        """ Collection Time tests"""
        driver = self.driver
        self.goToAddOrderPage()
        button_next_click = driver.find_element_by_id("samplesSectionId")
        button_next_click.click()
        select = driver.find_element_by_id('sampleTypeSelect')
        select.click()
        time.sleep(4)
        all_options = select.find_elements_by_tag_name("option")
        for option in all_options[1:]:
            option.click()
            break
        #Enter time in incorrect format(1. non-numeric, 2. extra digits, etc)
        time.sleep(4)
        collection_time = driver.find_element_by_id('collectionTime_1')
        collection_time.clear()
        collection_time.send_keys('A207FG8888')
        time.sleep(4)
            #Rejects non-numeric entries, additional digits, etc
        self.assertEqual(collection_time.get_attribute('value'), '20:78')
        time.sleep(3)
        collection_time.clear()
        #Enter time as HHMM
        collection_time.send_keys('2030')
        time.sleep(4)
            #Automatically corrects straight numeric entry to proper format HH:MM
        self.assertEqual(collection_time.get_attribute('value'), '20:30')
        time.sleep(3)
        collection_time.clear()
        #Enter time as HH:MM
        collection_time.send_keys('20:30')
            #Field accepts correct format
        self.assertEqual(collection_time.get_attribute('value'), '20:30')
        time.sleep(3)
        #Enter name in Collector Name field
        collector_name = driver.find_element_by_name('collector')
        collector_name.clear()
        collector_name.send_keys('Aliou SADIO')
        time.sleep(3)
            #Field accepts text
        self.assertEqual(collector_name.get_attribute('value'), 'Aliou SADIO')

    @api.assert_capture()
    def test_12_availableTestsPanels(self):
        """Available Tests & Panels"""
        driver = self.driver
        self.goToAddOrderPage()
        button_next_click = driver.find_element_by_id("samplesSectionId")
        button_next_click.click()
        select = driver.find_element_by_id('sampleTypeSelect')
        select.click()
        time.sleep(4)
        all_options = select.find_elements_by_tag_name("option")
        for option in all_options[1:]:
            option.click()
            break
        time.sleep(4)
        #Tests entry is marked mandatory.
        marked_mandatory = driver.find_element_by_xpath("//table[@id='samplesAddedTable']/tbody/tr/th/span[@class='requiredlabel']").get_attribute('class')
        self.assertEqual(marked_mandatory, 'requiredlabel')

        #Check checkbox next to test name
        checke_checkbox = driver.find_element_by_id('test_0')
        checke_checkbox.click()
        time.sleep(4)
            #Checkbox sticks, test name appears under Tests box.
        self.assertEqual(driver.find_element_by_id('tests_1').get_attribute('value'), 'GPT/ALAT')

            #For sample Varied, when you check test name, the specimen type becomes mandatory
            #Correct sample types appear in the varied drop-down menus and can be selected

        #Uncheck checkbox next to test name
        checke_checkbox.click()
        time.sleep(4)
            #Name disapears from Testsbox.
        self.assertEqual(driver.find_element_by_id('tests_1').get_attribute('value'), '')

        #Check checkbox next to panel name
        checke_panel_checkbox = driver.find_element_by_id('panel_0')
        checke_panel_checkbox.click()
        time.sleep(4)
            #All applicable panel tests under Available Tests are automatically selected and these tests apear in the Testsbox.
        #Uncheck checkbox next to panel name
        checke_panel_checkbox.click()
            #Deselects all panel tests (checkboxes clear under Panels and applicable Avalable Test; test names disapear from Tests box)
        #Enter text in Testsbox
            #Text cannot be added to the Testsbox.
        #Delete text from Testsbox
            #Text cannot be deleted from Testsbox

    def sampleAndTestDetails(self):
        """ Sample and test details"""
        driver = self.driver
        #view menus and lists and compare to test catalog
            #Correct sample types appear
            #Correct tests and panels appear for each sample type
            #Correct sample conditions are listed.

    @api.assert_capture()
    def test_13_patient_search(self):
        driver = self.driver
        self.goToAddOrderPage()
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "searchCriteria"))
        )
        #Patient information form is marked mandatory
        patient_information_mandatory = driver.find_element_by_xpath(
            "//td/input[@id='orderSectionId']/following-sibling::span[1]").get_attribute('class')
        self.assertEqual(patient_information_mandatory, "requiredlabel")

        #Expand Patient information form by clicking the + button next to Patien
        patient_section_id = driver.find_element_by_xpath("//td/input[@id='orderSectionId']")
        patient_section_id.click()
        time.sleep(5)
            #Patient search appear
        search_appear = driver.find_element_by_xpath("//h2[contains(text(),'Search')]").text
        self.assertEqual(search_appear, "Search")


        select = driver.find_element_by_id('searchCriteria')
        all_options = select.find_elements_by_tag_name("option")
        search_value_field = driver.find_element_by_id("searchValue")
        #Search button deactivated until search criteria (Last name, First name, Patient identication code, Accession Number
        i = 1
        for option in all_options[1:]:
            option.click()
            search_value_field.clear()
            search_value_field.send_keys('test %s' % i)
            search_button_field = driver.find_element_by_id("searchButton")
            disabled = search_button_field.get_attribute("disabled")
            # self.assertIsNone(disabled)
            i += 1
            time.sleep(1)

        # Search BY LAST NAME
        search_by_last_name = all_options[1]
        search_by_last_name.click()
        search_value_field.clear()
        search_value_field.send_keys('SADIO')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        time.sleep(3)

        # Search BY LASTNAME WITH ACCENT
        search_value_field.clear()
        search_value_field.send_keys('éhemba')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        time.sleep(3)

        # Search BY FIRST NAME
        search_by_first_name = all_options[2]
        search_by_first_name.click()
        search_value_field.clear()
        search_value_field.send_keys('Aliou')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        time.sleep(3)

        # Search BY FIRST NAME WITH ACCENT
        search_value_field.clear()
        search_value_field.send_keys('Jérémie')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        time.sleep(3)

        # Search BY LASTNAME FIRSTNAME
        search_by_first_last_name = all_options[3]
        search_by_first_last_name.click()
        search_value_field.clear()
        search_value_field.send_keys('SADIO,Aliou')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        time.sleep(3)

        # Search BY LASTNAME FIRSTNAME WITH ACCENT
        search_value_field.clear()
        search_value_field.send_keys('émilie,Sémédo')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        time.sleep(3)

        # Search BY LASTNAME FIRSTNAME OMIT COMMA
        search_value_field.clear()
        search_value_field.send_keys('émilie Sémédo')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        time.sleep(3)

        # Search BY PATIENT IDENTIFIANT CODE USING SUBJECT NUMBER
        search_by_patient_identifiant_code = all_options[4]
        search_by_patient_identifiant_code.click()
        search_value_field.clear()
        search_value_field.send_keys('201507D9P')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        time.sleep(3)

        # Search BY PATIENT IDENTIFIANT CODE USING IDENTIFIANT NUMBER
        search_value_field.clear()
        search_value_field.send_keys('201507D33')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        time.sleep(3)

        #Click New Patient: Patient information form clear
        driver.find_element_by_xpath("//input[@value='New Patient']").click()

    @api.assert_capture()
    def test_14_patient_searchpatient_information(self):
        """Commentaire test"""
        self.goToAddOrderPage()
        driver = self.driver

        #Initializing data
        ###############################################################
        driver.find_element_by_class_name("textButton").click()
        # Enter the site name
        select = driver.find_element_by_id('requesterId')
        select.click()
        all_options = select.find_elements_by_tag_name("option")
        for option in all_options[1:]:
            option.click()
            break
        time.sleep(3)
        last_name_value = driver.find_element_by_id("providerLastNameID")
        last_name_value.send_keys("SADIO")
        # CLick on + buttton next to Sample
        button_next_click = driver.find_element_by_id("samplesSectionId")
        button_next_click.click()
        time.sleep(5)
        select = driver.find_element_by_id('sampleTypeSelect')
        select.click()
        time.sleep(1)
        all_options2 = select.find_elements_by_tag_name("option")
        for option in all_options2[1:]:
            option.click()
            break
        time.sleep(2)
        check_panel_checkbox = driver.find_element_by_id('panel_0')
        check_panel_checkbox.click()
        ########################################################################################

        #Going to the patients
        patient_section_id = driver.find_element_by_xpath("//td/input[@id='orderSectionId']")
        patient_section_id.click()
        time.sleep(5)

        #Enter data into text fields

        subject_number_field = driver.find_element_by_id("subjectNumberID")
        national_id_field = driver.find_element_by_id("nationalID")
        last_name_field = driver.find_element_by_id("lastNameID")
        first_name_field = driver.find_element_by_id("firstNameID")
        street_field = driver.find_element_by_id("streetID")
        commune_field = driver.find_element_by_id("communeID")
        town_field = driver.find_element_by_id("cityID")
        phone_field = driver.find_element_by_id("patientPhone")
        birth_date_field = driver.find_element_by_id("dateOfBirthID")
        age_field = driver.find_element_by_id("age")
        specify_field = driver.find_element_by_id("nationalityOtherId")
        gender_field = driver.find_element_by_id("genderID")
        save_button_field = driver.find_element_by_id("saveButtonId")
        health_region_field = driver.find_element_by_id("healthRegionID")
        health_district_field = driver.find_element_by_id("healthDistrictID")

        subject_number_field.send_keys("201807D9P")
        national_id_field.send_keys("201507D35")
        last_name_field.send_keys("SADIO")
        first_name_field.send_keys("Aliou")
        street_field.send_keys("New York city, street 3334")
        commune_field.send_keys("Grand yoff")
        town_field.send_keys("Dakar")
        phone_field.send_keys("+225-33-65-78-23")
        birth_date_field.send_keys("25/07/1992")
        specify_field.send_keys("American")

        gender_field.click()
        time.sleep(1)
        all_gender = gender_field.find_elements_by_tag_name("option")
        for option in all_gender[1:]:
            option.click()
            break

        #Alert is given if Subject Number is already in use
        subject_number_field.clear()
        subject_number_field.send_keys("201507D9P")
        time.sleep(7)
        national_id_field.click()
        time.sleep(5)

        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(4)
        disabled = save_button_field.get_attribute("disabled")
        self.assertTrue(disabled)
        subject_number_field.clear()
        subject_number_field.send_keys("201807D9P")
        time.sleep(3)
        national_id_field.click()
        time.sleep(7)
        not_disabled = save_button_field.get_attribute("disabled")
        self.assertIsNone(not_disabled)

        # Alert is given if Identification number is already in use
        time.sleep(5)
        national_id_field.clear()
        national_id_field.send_keys("201507D33")
        time.sleep(3)
        subject_number_field.click()
        time.sleep(5)
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(4)
        disabled2 = save_button_field.get_attribute("disabled")
        self.assertTrue(disabled2)

        national_id_field.clear()
        national_id_field.send_keys("201507D35")
        time.sleep(3)
        subject_number_field.click()
        time.sleep(5)
        not_disabled2 = save_button_field.get_attribute("disabled")
        self.assertIsNone(not_disabled2)

        #Phone number gives alert if not in correct format
        phone_field.clear()
        phone_field.send_keys("38283838")
        time.sleep(5)
        subject_number_field.click()
        time.sleep(4)
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.accept()

        phone_field.clear()
        phone_field.send_keys("+225-33-65-78-23")
        subject_number_field.click()

        health_region_field.click()
        time.sleep(5)
        all_health_region = health_region_field.find_elements_by_tag_name("option")
        n3 = 0
        for option in all_health_region[1:]:
            if n3 == 5:
                break
            option.click()
            time.sleep(4)
            health_district_field.click()
            n3 = n3 + 1
            time.sleep(4)

        #Alert appears if the date format is not respected: alert does not appear but there's a mark
        birth_date_field.clear()
        birth_date_field.send_keys("03-02/1990")
        time.sleep(4)
        subject_number_field.click()
        time.sleep(4)
        self.assertEqual(
            driver.find_element_by_id("patientProperties.birthDateForDisplayMessage").get_attribute("class"),
            "badmessage")

        next_day = (datetime.datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
        birth_date_field.clear()
        time.sleep(3)
        birth_date_field.send_keys(next_day)
        subject_number_field.click()
        time.sleep(4)
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')
        time.sleep(2)

        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(4)

        birth_date_field.send_keys("25/07/1992")

        time.sleep(4)
        #Delete Date of Birth and enter Age
        birth_date_field.clear()
        time.sleep(4)
        age_field.send_keys("25")
        time.sleep(4)
        town_field.click()
        this_year = int(datetime.datetime.now().strftime("%Y"))
        date_of_birth = str(this_year - 25)

        self.assertEqual(birth_date_field.get_attribute("value"), "xx/xx/"+date_of_birth)

        # Alert apearts if age is -1 99 100 and >100
        test_value = [-1, 99, 100, randint(100, 200)]
        for value in test_value:
            birth_date_field.click()
            age_field.clear()
            age_field.send_keys(value)
            phone_field.click()
            bad_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "patientProperties.ageMessage"))
            )
            assert True if bad_message else False

    @api.assert_capture()
    def test_15_overallPage(self):
        self.goToAddOrderPage()
        driver = self.driver
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "requesterId"))
        )
        #Leave mandatory field without data
        ###############################################################
        driver.find_element_by_class_name("textButton").click()
        # Enter the site name
        select = driver.find_element_by_id('requesterId')
        select.click()
        all_options = select.find_elements_by_tag_name("option")
        for option in all_options[1:]:
            option.click()
            break
        time.sleep(3)
        last_name_value = driver.find_element_by_id("providerLastNameID")
        last_name_value.send_keys("SADIO")
        # CLick on + buttton next to Sample
        button_next_click = driver.find_element_by_id("samplesSectionId")
        button_next_click.click()
        time.sleep(5)
        select = driver.find_element_by_id('sampleTypeSelect')
        select.click()
        time.sleep(1)
        all_options2 = select.find_elements_by_tag_name("option")
        for option in all_options2[1:]:
            option.click()
            break
        time.sleep(2)
        check_panel_checkbox = driver.find_element_by_id('panel_0')
        check_panel_checkbox.click()
        ########################################################################################

        # Going to the patients
        patient_section_id = driver.find_element_by_xpath("//td/input[@id='orderSectionId']")
        patient_section_id.click()
        time.sleep(5)

        # Enter data into text fields

        subject_number_field = driver.find_element_by_id("subjectNumberID")
        national_id_field = driver.find_element_by_id("nationalID")
        last_name_field = driver.find_element_by_id("lastNameID")
        first_name_field = driver.find_element_by_id("firstNameID")
        street_field = driver.find_element_by_id("streetID")
        commune_field = driver.find_element_by_id("communeID")
        town_field = driver.find_element_by_id("cityID")
        phone_field = driver.find_element_by_id("patientPhone")
        birth_date_field = driver.find_element_by_id("dateOfBirthID")
        age_field = driver.find_element_by_id("age")
        specify_field = driver.find_element_by_id("nationalityOtherId")
        gender_field = driver.find_element_by_id("genderID")
        health_region_field = driver.find_element_by_id("healthRegionID")
        health_district_field = driver.find_element_by_id("healthDistrictID")

        subject_number_field.send_keys("201807D9P4F")
        national_id_field.send_keys("2015076SF35")
        last_name_field.send_keys("SADIO")
        first_name_field.send_keys("Aliou")
        street_field.send_keys("New York city, street 3334")
        commune_field.send_keys("Grand yoff")
        town_field.send_keys("Dakar")
        phone_field.send_keys("+225-33-65-78-23")

        specify_field.send_keys("American")
        gender_field.click()
        all_gender = gender_field.find_elements_by_tag_name("option")
        for option in all_gender[1:]:
            option.click()
            break
        time.sleep(5)

        #Complete all mandatory fields
        birth_date_field.send_keys("25/07/1992")
        time.sleep(4)

        for option in all_gender[1:]:
            option.click()
            time.sleep(3)

        #Click Cancel
        time.sleep(5)
        birth_date_field.click()
        time.sleep(4)
        cancel_button = driver.find_element_by_xpath("//input[@value='Cancel']")
        cancel_button.click()


        #Click Stay on Page
        WebDriverWait(driver, 12).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')
        time.sleep(2)

        alert = driver.switch_to.alert
        alert.dismiss()
        time.sleep(4)
        #Click  Save
        save_button_field = driver.find_element_by_id("saveButtonId")
        save_button_field.click()
        #Return to Patient Add/Modify Page
        time.sleep(4)
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "menu_sample"))
        )
        self.goToAddOrderPage()
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "requesterId"))
        )

        driver.find_element_by_class_name("textButton").click()
        time.sleep(3)
        driver.find_element_by_xpath("//input[@value='Cancel']").click()


        WebDriverWait(driver, 12).until(EC.alert_is_present(),
                                        'Timed out waiting for PA creation ' +
                                        'confirmation popup to appear.')
        time.sleep(2)

        alert = driver.switch_to.alert
        # Click Cancel, then click Leave Page
        alert.accept()
        time.sleep(7)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()