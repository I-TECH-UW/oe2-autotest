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

class Reports(unittest.TestCase):

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

    def goToPatientReports(self):
        driver = self.driver
        action = ActionChains(driver)

        firstLevelMenu = driver.find_element_by_id("menu_reports")
        action.move_to_element(firstLevelMenu).perform()

        # Getting to the submenu: Add Order, and clicking on it to go to the Add order form appears
        secondLevelMenu = driver.find_element_by_id('menu_reports_routine')
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "menu_reports_routine"))
        )
        action.move_to_element(secondLevelMenu).perform()

        thirdLevelMenu = driver.find_element_by_id('menu_reports_status_patient')
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "menu_reports_status_patient"))
        )
        action.move_to_element(thirdLevelMenu).perform()

        fourthLevelMenu = driver.find_element_by_id('menu_reports_status_patient.classique')
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "menu_reports_status_patient.classique"))
        )
        fourthLevelMenu.click()

        time.sleep(4)

    def goToAgregateReports(self):
        driver = self.driver
        action = ActionChains(driver)

        firstLevelMenu = driver.find_element_by_id("menu_reports")
        action.move_to_element(firstLevelMenu).perform()

        # Getting to the submenu: Add Order, and clicking on it to go to the Add order form appears
        secondLevelMenu = driver.find_element_by_id('menu_reports_routine')

        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "menu_reports_routine"))
        )
        action.move_to_element(secondLevelMenu).perform()

        thirdLevelMenu = driver.find_element_by_id('menu_reports_aggregate')
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "menu_reports_aggregate"))
        )

        action.move_to_element(thirdLevelMenu).perform()

        fourthLevelMenu = driver.find_element_by_id('menu_reports_aggregate_hiv')
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "menu_reports_aggregate_hiv"))
        )
        fourthLevelMenu.click()

        time.sleep(4)

    def goToResultsByOrder(self):
        driver = self.driver
        action = ActionChains(driver)

        firstLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_results']")
        action.move_to_element(firstLevelMenu).perform()

        # Getting to the submenu: Add Order, and clicking on it to go to the Add order form appears
        secondLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_results_search']")

        action.move_to_element(secondLevelMenu).perform()

        thirdLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_results_accession']")

        action.move_to_element(thirdLevelMenu).perform()

        fourthLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_results_accession']")

        fourthLevelMenu.click()

        time.sleep(4)

    def goToAddOrderPage(self):
        time.sleep(4)
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_sample")
        action.move_to_element(firstLevelMenu).perform()
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "menu_sample_add"))
        )
        # Getting to the submenu: Add Order, and clicking on it to go to the Add order form appears
        secondLevelMenu = driver.find_element_by_id('menu_sample_add')
        secondLevelMenu.click()

    def goToResumeTests(self):
        driver = self.driver
        action = ActionChains(driver)

        firstLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports']")
        action.move_to_element(firstLevelMenu).perform()

        # Getting to the submenu: Add Order, and clicking on it to go to the Add order form appears
        secondLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports_routine']")

        action.move_to_element(secondLevelMenu).perform()

        thirdLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports_aggregate']")

        action.move_to_element(thirdLevelMenu).perform()

        fourthLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports_aggregate_all']")

        fourthLevelMenu.click()

        time.sleep(4)

    def goToActivityReportByTest(self):
        driver = self.driver
        action = ActionChains(driver)

        firstLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports']")
        action.move_to_element(firstLevelMenu).perform()

        # Getting to the submenu: Add Order, and clicking on it to go to the Add order form appears
        secondLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports_routine']")

        action.move_to_element(secondLevelMenu).perform()

        thirdLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports_management']")

        action.move_to_element(thirdLevelMenu).perform()

        fourthLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports_activity']")
        action.move_to_element(fourthLevelMenu).perform()

        fithLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_activity_report_test']")

        fithLevelMenu.click()

        time.sleep(4)

    def goToactivityReportByPanel(self):
        driver = self.driver
        action = ActionChains(driver)

        firstLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports']")
        action.move_to_element(firstLevelMenu).perform()

        # Getting to the submenu: Add Order, and clicking on it to go to the Add order form appears
        secondLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports_routine']")

        action.move_to_element(secondLevelMenu).perform()

        thirdLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports_management']")

        action.move_to_element(thirdLevelMenu).perform()

        fourthLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports_activity']")
        action.move_to_element(fourthLevelMenu).perform()

        fithLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_activity_report_panel']")

        fithLevelMenu.click()

        time.sleep(4)
    def goToactivityReportByUnit(self):
        driver = self.driver
        action = ActionChains(driver)

        firstLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports']")
        action.move_to_element(firstLevelMenu).perform()

        # Getting to the submenu: Add Order, and clicking on it to go to the Add order form appears
        secondLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports_routine']")

        action.move_to_element(secondLevelMenu).perform()

        thirdLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports_management']")

        action.move_to_element(thirdLevelMenu).perform()

        fourthLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports_activity']")
        action.move_to_element(fourthLevelMenu).perform()

        fithLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_activity_report_bench']")

        fithLevelMenu.click()

        time.sleep(4)

    def goToactivityReportByPanel(self):
        driver = self.driver
        action = ActionChains(driver)

        firstLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports']")
        action.move_to_element(firstLevelMenu).perform()

        # Getting to the submenu: Add Order, and clicking on it to go to the Add order form appears
        secondLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports_routine']")

        action.move_to_element(secondLevelMenu).perform()

        thirdLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports_management']")

        action.move_to_element(thirdLevelMenu).perform()

        fourthLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports_activity']")
        action.move_to_element(fourthLevelMenu).perform()

        fithLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_activity_report_panel']")

        fithLevelMenu.click()

        time.sleep(4)
    def goToReportNonConformityByDate(self):
        driver = self.driver
        action = ActionChains(driver)

        firstLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports']")
        action.move_to_element(firstLevelMenu).perform()

        # Getting to the submenu: Add Order, and clicking on it to go to the Add order form appears
        secondLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports_study']")

        action.move_to_element(secondLevelMenu).perform()

        thirdLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports_nonconformity.study']")

        action.move_to_element(thirdLevelMenu).perform()

        fourthLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports_nonconformity_date.study']")

        fourthLevelMenu.click()

        time.sleep(4)

    def goToReportNonConformityByUnitReason(self):
        driver = self.driver
        action = ActionChains(driver)

        firstLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports']")
        action.move_to_element(firstLevelMenu).perform()

        # Getting to the submenu: Add Order, and clicking on it to go to the Add order form appears
        secondLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports_study']")

        action.move_to_element(secondLevelMenu).perform()

        thirdLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports_nonconformity.study']")

        action.move_to_element(thirdLevelMenu).perform()

        fourthLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports_nonconformity_section.study']")

        fourthLevelMenu.click()

        time.sleep(4)

    def goToReportExportCSV(self):
        driver = self.driver
        action = ActionChains(driver)

        firstLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports']")
        action.move_to_element(firstLevelMenu).perform()

        # Getting to the submenu: Add Order, and clicking on it to go to the Add order form appears
        secondLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports_routine']")

        action.move_to_element(secondLevelMenu).perform()

        thirdLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_reports_export_routine']")

        thirdLevelMenu.click()

        time.sleep(4)

    @api.assert_capture()
    def test_01_patientReport(self):
        driver = self.driver
        self.goToPatientReports()
        # Enter single lab number  in the left  lab number parameter field
        lab_number_1 = driver.find_element_by_id("accessionDirect")
        lab_number_1.send_keys("1234500000012")
        time.sleep(5)

        # Conserving the context of the drive
        firstTab = self.driver

        # Click generate printable Report
        print_button = driver.find_element_by_name("printNew")
        print_button.click()
        time.sleep(5)

        # Make the driver stay on the first tab
        self.driver = firstTab
        # Enter parameter: a range of lab numbers
        lab_number_1.clear()
        lab_number_2 = driver.find_element_by_id("highAccessionDirect")

        lab_number_1.send_keys("1234500000012")
        time.sleep(3)
        lab_number_2.send_keys("1234519000117")
        time.sleep(3)

        print_button.click()

        time.sleep(3)
        # Make the driver stay on the first tab
        self.driver = firstTab
        # Enter parameter Patient id
        lab_number_1.clear()
        lab_number_2.clear()
        patient_id = driver.find_element_by_id("patientNumberDirect")
        patient_id.send_keys("201507D10P")
        time.sleep(10)
        print_button.click()

        time.sleep(10)

    @api.assert_capture()
    def test_02_hivTestResume(self):
        driver = self.driver

        self.goToAgregateReports()

        # Enter parameters with date mm/jj/aaaa using day (jj) above 12
        start_date = driver.find_element_by_id("lowerDateRange")
        end_date = driver.find_element_by_id("upperDateRange")
        time.sleep(4)

        start_date.send_keys("25/13/2013")
        end_date.send_keys("25/14/2017")
        time.sleep(5)
        # Conserving the context of the drive
        firstTab = self.driver

        # Click Generate Printable Report
        print_button = driver.find_element_by_name("printNew")
        print_button.click()
        time.sleep(5)

        # Make the driver stay on the first tab
        self.driver = firstTab
        # Enter parameters with invalid year
        start_date.clear()
        end_date.clear()

        start_date.send_keys("25/10/F5")
        end_date.send_keys("25/14/5F")

        #Click Generate Printable Report

        print_button.click()
        time.sleep(5)

        #Enter parameters jjmmaaa (ddmmyyyy)
        self.driver = firstTab
        start_date.clear()
        end_date.clear()


        start_date.send_keys("25102012")
        time.sleep(3)
        end_date.send_keys("20102016")
        firstTab = self.driver
        time.sleep(4)
        print_button.click()
        #Date is formatted automatically
        self.driver = firstTab
        self.assertEqual(driver.find_element_by_id("lowerDateRange").get_attribute("value"), "25/10/2012")
        self.assertEqual(driver.find_element_by_id("upperDateRange").get_attribute("value"), "20/10/2016")

        #Click Generate Printable Report (for testing purposes, keep the report open!)

        time.sleep(10)

        #Enter an order for HIV tests (VIH rapide, CD4, etc.). Note the patient sex and age.
        #Uncomment if you want to add


        """""
        self.goToAddOrderPage()
        # Initializing data
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
        last_name_value.send_keys("KOUADJO")
        First_name_value = driver.find_element_by_id("sampleOrderItems.providerFirstName")
        First_name_value.send_keys("Rébéca")

        #Selecting a programm
        programm = driver.find_element_by_id('sampleOrderItems.program')
        all_programms = programm.find_elements_by_tag_name("option")
        all_programms[1].click()


        # CLick on + buttton next to Sample
        button_next_click = driver.find_element_by_id("samplesSectionId")
        button_next_click.click()
        time.sleep(5)
        select = driver.find_element_by_id('sampleTypeSelect')
        select.click()
        time.sleep(1)
        all_options2 = select.find_elements_by_tag_name("option")[2].click()

        time.sleep(2)
        check_panel_checkbox = driver.find_element_by_id('test_1')
        check_panel_checkbox.click()

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
        save_button_field = driver.find_element_by_id("saveButtonId")
        health_region_field = driver.find_element_by_id("healthRegionID")
        health_district_field = driver.find_element_by_id("healthDistrictID")

        subject_number_field.send_keys("201905D9P")
        national_id_field.send_keys("203507D35")
        last_name_field.send_keys("SAGNA")
        first_name_field.send_keys("Abdoulay")
        street_field.send_keys("New York city, street 3334")
        commune_field.send_keys("Grand yoff")
        town_field.send_keys("Dakar")
        phone_field.send_keys("+225-33-65-78-23")
        birth_date_field.send_keys("25/07/1992")
        specify_field.send_keys("American")

        gender_field.click()
        time.sleep(1)
        all_gender = gender_field.find_elements_by_tag_name("option")[1].click()
        time.sleep(10)

        driver.find_element_by_id("saveButtonId").click()
        """""

        self.goToResultsByOrder()
        lab_no = driver.find_element_by_id("searchAccessionID")
        lab_no.send_keys("1234519000162")
        time.sleep(4)
        get_test = driver.find_element_by_id("retrieveTestsID")
        get_test.click()

        select_result = driver.find_element_by_id("resultId_1")
        all_gender = select_result.find_elements_by_tag_name("option")[2].click()
        time.sleep(5)

        self.goToAgregateReports()

        # Enter parameters with date mm/jj/aaaa using day (jj) above 12
        start_date = driver.find_element_by_id("lowerDateRange")
        end_date = driver.find_element_by_id("upperDateRange")
        time.sleep(4)

        start_date.send_keys("25/13/2013")
        end_date.send_keys("25/14/2017")
        time.sleep(5)

        # Click Generate Printable Report
        print_button = driver.find_element_by_name("printNew")
        print_button.click()
        time.sleep(10)

    @api.assert_capture()
    def test_03_resumeTests(self):
        # Go to Reports--> Aggregate Reports--> Resume des Tests VIH
        driver = self.driver
        self.goToResumeTests()

        #Enter parameters with date mm/jj/aaaa using day (jj) above 12
        # Enter parameters with date mm/jj/aaaa using day (jj) above 12
        start_date = driver.find_element_by_id("lowerDateRange")
        end_date = driver.find_element_by_id("upperDateRange")
        time.sleep(4)

        start_date.send_keys("25/13/2013")
        end_date.send_keys("25/14/2017")
        time.sleep(5)
        # Conserving the context of the drive
        firstTab = self.driver

        # Click Generate Printable Report
        print_button = driver.find_element_by_name("printNew")
        print_button.click()
        time.sleep(5)

        # Make the driver stay on the first tab
        self.driver = firstTab
        # Enter parameters with invalid year
        start_date.clear()
        end_date.clear()

        start_date.send_keys("25/10/F5")
        end_date.send_keys("25/14/5F")

        # Click Generate Printable Report

        print_button.click()
        time.sleep(5)

        # Enter parameters jjmmaaa (ddmmyyyy)
        self.driver = firstTab
        start_date.clear()
        end_date.clear()

        start_date.send_keys("25102012")
        time.sleep(3)
        end_date.send_keys("20102016")
        firstTab = self.driver
        time.sleep(4)
        print_button.click()
        # Date is formatted automatically
        self.driver = firstTab
        self.assertEqual(driver.find_element_by_id("lowerDateRange").get_attribute("value"), "25/10/2012")
        self.assertEqual(driver.find_element_by_id("upperDateRange").get_attribute("value"), "20/10/2016")

        #Enter an order for at least one test for each lab unit
        #Enter results for some of the tests ordered; validate some as needed
        #Generate the Résumé de Tous les Tests report again, including today's date
        driver = firstTab
        start_date.clear()
        end_date.clear()
        time.sleep(5)
        start_date.send_keys("25/05/2007")
        time.sleep(3)
        today = datetime.datetime.now().strftime("%d/%m/%Y")
        end_date.send_keys(today)
        time.sleep(4)
        print_button.click()
        time.sleep(10)

    @api.assert_capture()
    def test_04_confirmationTestReport(self):
        driver = self.driver
        self.goToResumeTests()

        # Enter parameters with date mm/jj/aaaa using day (jj) above 12
        # Enter parameters with date mm/jj/aaaa using day (jj) above 12
        start_date = driver.find_element_by_id("lowerDateRange")
        end_date = driver.find_element_by_id("upperDateRange")
        time.sleep(4)

        start_date.send_keys("25/13/2013")
        end_date.send_keys("25/14/2017")
        time.sleep(5)
        # Conserving the context of the drive
        firstTab = self.driver

        # Click Generate Printable Report
        print_button = driver.find_element_by_name("printNew")
        print_button.click()
        time.sleep(5)

        # Make the driver stay on the first tab
        self.driver = firstTab
        # Enter parameters with invalid year
        start_date.clear()
        end_date.clear()

        start_date.send_keys("25/10/F5")
        end_date.send_keys("25/14/5F")

        # Click Generate Printable Report

        print_button.click()
        time.sleep(5)

        # Enter parameters jjmmaaa (ddmmyyyy)
        self.driver = firstTab
        start_date.clear()
        end_date.clear()

        start_date.send_keys("25102012")
        time.sleep(3)
        end_date.send_keys("20102016")
        firstTab = self.driver
        time.sleep(4)
        print_button.click()
        # Date is formatted automatically
        self.driver = firstTab
        self.assertEqual(driver.find_element_by_id("lowerDateRange").get_attribute("value"), "25/10/2012")
        self.assertEqual(driver.find_element_by_id("upperDateRange").get_attribute("value"), "20/10/2016")


    @api.assert_capture()
    def test_05_activityReportByTest(self):
        driver = self.driver
        # Go to Reports--> Aggregate Reports--> Rapport d'Activité--> Par Test
        self.goToActivityReportByTest()

        # Enter parameters with date mm/jj/aaaa using day (jj) above 12
        start_date = driver.find_element_by_id("lowerDateRange")
        end_date = driver.find_element_by_id("upperDateRange")
        time.sleep(4)

        start_date.send_keys("25/13/2013")
        end_date.send_keys("25/14/2017")
        time.sleep(3)

        #Select  test from drop-down list
        test_type_select = driver.find_element_by_id("selectList")
        select_all_option = test_type_select.find_elements_by_tag_name("option")[3].click()

        time.sleep(5)
        # Conserving the context of the drive
        firstTab = self.driver

        # Click Generate Printable Report
        print_button = driver.find_element_by_name("printNew")
        print_button.click()
        time.sleep(5)

        # Make the driver stay on the first tab
        self.driver = firstTab

        # Enter parameters with invalid year
        start_date.clear()
        end_date.clear()

        start_date.send_keys("25/10/F5")
        end_date.send_keys("25/14/5F")

        # Click Generate Printable Report

        print_button.click()
        time.sleep(5)

        # Enter parameters jjmmaaa (ddmmyyyy)
        self.driver = firstTab
        start_date.clear()
        end_date.clear()

        start_date.send_keys("25052007")
        time.sleep(3)
        end_date.send_keys("18092019")
        firstTab = self.driver
        time.sleep(4)
        print_button.click()
        # Date is formatted automatically
        self.driver = firstTab
        self.assertEqual(driver.find_element_by_id("lowerDateRange").get_attribute("value"), "25/05/2007")
        self.assertEqual(driver.find_element_by_id("upperDateRange").get_attribute("value"), "18/09/2019")
        time.sleep(10)

    @api.assert_capture()
    def test_06_activityReportByPanel(self):
        driver = self.driver
        self.goToactivityReportByPanel()

        # Enter parameters with date mm/jj/aaaa using day (jj) above 12
        start_date = driver.find_element_by_id("lowerDateRange")
        end_date = driver.find_element_by_id("upperDateRange")
        time.sleep(4)

        start_date.send_keys("25/13/2013")
        end_date.send_keys("25/14/2017")
        time.sleep(3)

        # Select  test from drop-down list
        test_type_select = driver.find_element_by_id("selectList")
        select_all_option = test_type_select.find_elements_by_tag_name("option")[1].click()

        time.sleep(5)
        # Conserving the context of the drive
        firstTab = self.driver

        # Click Generate Printable Report
        print_button = driver.find_element_by_name("printNew")
        print_button.click()
        time.sleep(5)

        # Make the driver stay on the first tab
        self.driver = firstTab

        # Enter parameters with invalid year
        start_date.clear()
        end_date.clear()

        start_date.send_keys("25/10/F5")
        end_date.send_keys("25/14/5F")

        # Click Generate Printable Report

        print_button.click()
        time.sleep(5)

        # Enter parameters jjmmaaa (ddmmyyyy)
        self.driver = firstTab
        start_date.clear()
        end_date.clear()

        start_date.send_keys("25052007")
        time.sleep(3)
        end_date.send_keys("18092019")
        firstTab = self.driver
        time.sleep(4)
        print_button.click()
        # Date is formatted automatically
        self.driver = firstTab
        self.assertEqual(driver.find_element_by_id("lowerDateRange").get_attribute("value"), "25/05/2007")
        self.assertEqual(driver.find_element_by_id("upperDateRange").get_attribute("value"), "18/09/2019")
        time.sleep(10)

    @api.assert_capture()
    def test_07_activityReportByUnit(self):
        driver = self.driver
        self.goToactivityReportByUnit()

        # Enter parameters with date mm/jj/aaaa using day (jj) above 12
        start_date = driver.find_element_by_id("lowerDateRange")
        end_date = driver.find_element_by_id("upperDateRange")
        time.sleep(4)

        start_date.send_keys("25/13/2013")
        end_date.send_keys("25/14/2017")
        time.sleep(3)

        # Select  test from drop-down list
        test_type_select = driver.find_element_by_id("selectList")
        select_all_option = test_type_select.find_elements_by_tag_name("option")[1].click()

        time.sleep(5)
        # Conserving the context of the drive
        firstTab = self.driver

        # Click Generate Printable Report
        print_button = driver.find_element_by_name("printNew")
        print_button.click()
        time.sleep(5)

        # Make the driver stay on the first tab
        self.driver = firstTab

        # Enter parameters with invalid year
        start_date.clear()
        end_date.clear()

        start_date.send_keys("25/10/F5")
        end_date.send_keys("25/14/5F")

        # Click Generate Printable Report

        print_button.click()
        time.sleep(5)

        # Enter parameters jjmmaaa (ddmmyyyy)
        self.driver = firstTab
        start_date.clear()
        end_date.clear()

        start_date.send_keys("25052007")
        time.sleep(3)
        end_date.send_keys("18092019")
        firstTab = self.driver
        time.sleep(4)
        print_button.click()
        # Date is formatted automatically
        self.driver = firstTab
        self.assertEqual(driver.find_element_by_id("lowerDateRange").get_attribute("value"), "25/05/2007")
        self.assertEqual(driver.find_element_by_id("upperDateRange").get_attribute("value"), "18/09/2019")
        time.sleep(10)

    @api.assert_capture()
    def test_08_reportNonConformityByDate(self):
        driver = self.driver
        self.goToReportNonConformityByDate()

        # Enter parameters with date mm/jj/aaaa using day (jj) above 12
        start_date = driver.find_element_by_id("lowerDateRange")
        end_date = driver.find_element_by_id("upperDateRange")
        time.sleep(4)

        start_date.send_keys("25/13/2013")
        end_date.send_keys("25/14/2017")
        time.sleep(3)

        # Conserving the context of the drive
        firstTab = self.driver

        # Click Generate Printable Report
        print_button = driver.find_element_by_name("printNew")
        print_button.click()
        time.sleep(5)

        # Make the driver stay on the first tab
        self.driver = firstTab

        # Enter parameters with invalid year
        start_date.clear()
        end_date.clear()

        start_date.send_keys("25/10/F5")
        end_date.send_keys("25/14/5F")

        # Click Generate Printable Report

        print_button.click()
        time.sleep(5)

        # Enter parameters jjmmaaa (ddmmyyyy)
        self.driver = firstTab
        start_date.clear()
        end_date.clear()

        start_date.send_keys("25052007")
        time.sleep(3)
        end_date.send_keys("18092019")
        firstTab = self.driver
        time.sleep(4)
        print_button.click()
        # Date is formatted automatically
        self.driver = firstTab
        self.assertEqual(driver.find_element_by_id("lowerDateRange").get_attribute("value"), "25/05/2007")
        self.assertEqual(driver.find_element_by_id("upperDateRange").get_attribute("value"), "18/09/2019")
        time.sleep(10)

    @api.assert_capture()
    def test_09_reportNonConformityByUnitReason(self):
        driver = self.driver
        self.goToReportNonConformityByUnitReason()

        # Enter parameters with date mm/jj/aaaa using day (jj) above 12
        start_date = driver.find_element_by_id("lowerDateRange")
        end_date = driver.find_element_by_id("upperDateRange")
        time.sleep(4)

        start_date.send_keys("25/13/2013")
        end_date.send_keys("25/14/2017")
        time.sleep(3)

        # Conserving the context of the drive
        firstTab = self.driver

        # Click Generate Printable Report
        print_button = driver.find_element_by_name("printNew")
        print_button.click()
        time.sleep(5)

        # Make the driver stay on the first tab
        self.driver = firstTab

        # Enter parameters with invalid year
        start_date.clear()
        end_date.clear()

        start_date.send_keys("25/10/F5")
        end_date.send_keys("25/14/5F")

        # Click Generate Printable Report

        print_button.click()
        time.sleep(5)

        # Enter parameters jjmmaaa (ddmmyyyy)
        self.driver = firstTab
        start_date.clear()
        end_date.clear()

        start_date.send_keys("25052007")
        time.sleep(3)
        end_date.send_keys("18092019")
        firstTab = self.driver
        time.sleep(4)
        print_button.click()
        # Date is formatted automatically
        self.driver = firstTab
        self.assertEqual(driver.find_element_by_id("lowerDateRange").get_attribute("value"), "25/05/2007")
        self.assertEqual(driver.find_element_by_id("upperDateRange").get_attribute("value"), "18/09/2019")
        time.sleep(10)

    @api.assert_capture()
    def test_10_test_reportExportCSV(self):
        driver = self.driver
        self.goToReportExportCSV()

        # Enter parameters with date mm/jj/aaaa using day (jj) above 12
        start_date = driver.find_element_by_id("lowerDateRange")
        end_date = driver.find_element_by_id("upperDateRange")
        time.sleep(4)

        start_date.send_keys("25/13/2013")
        end_date.send_keys("25/14/2017")
        time.sleep(3)

        # Conserving the context of the drive
        firstTab = self.driver

        # Click Generate Printable Report
        print_button = driver.find_element_by_name("printNew")
        print_button.click()
        time.sleep(5)

        # Make the driver stay on the first tab
        self.driver = firstTab

        # Enter parameters with invalid year
        start_date.clear()
        end_date.clear()

        start_date.send_keys("25/10/F5")
        end_date.send_keys("25/14/5F")

        # Click Generate Printable Report

        print_button.click()
        time.sleep(5)

        # Enter parameters jjmmaaa (ddmmyyyy)
        self.driver = firstTab
        start_date.clear()
        end_date.clear()

        start_date.send_keys("25052007")
        time.sleep(3)
        end_date.send_keys("18092019")
        firstTab = self.driver
        time.sleep(4)
        print_button.click()
        # Date is formatted automatically
        self.driver = firstTab
        self.assertEqual(driver.find_element_by_id("lowerDateRange").get_attribute("value"), "25/05/2007")
        self.assertEqual(driver.find_element_by_id("upperDateRange").get_attribute("value"), "18/09/2019")
        time.sleep(10)

    def goToAudit(self):
        driver = self.driver
        action = ActionChains(driver)

        firstLevelMenu = driver.find_element_by_id("menu_reports")
        action.move_to_element(firstLevelMenu).perform()

        # Getting to the submenu: Add Order, and clicking on it to go to the Add order form appears
        secondLevelMenu = driver.find_element_by_id('menu_reports_study')

        action.move_to_element(secondLevelMenu).perform()

        thirdLevelMenu = driver.find_element_by_id('menu_reports_auditTrail.study')

        thirdLevelMenu.click()

        time.sleep(4)   

    @api.assert_capture()
    def test_11_audit(self):
        driver = self.driver

        #Go to Reports--> Examen d'Audit
        self.goToAudit()
        #Enter parameters with incorrect lab number format (e.g. 13000111)
        lab_no = driver.find_element_by_id("accessionNumberSearch")
        lab_no.send_keys('12345000')
        button = driver.find_element_by_xpath("//input[@value='View Report']")
        #Click Rechercher
        button.click()
        time.sleep(5)
        #Enter parameters with correct lab number format (e.g. 13000111)
        lab_no = driver.find_element_by_id("accessionNumberSearch")
        lab_no.clear()
        button = driver.find_element_by_xpath("//input[@value='View Report']")
        lab_no.send_keys('1234500000012')
        time.sleep(3)
        #Click Rechercher
        button.click()
        time.sleep(4)

        #Modify text field
        street = driver.find_element_by_id("streetID")
        street.send_keys('Khar yalla 56')

        time.sleep(3)

        #Select filter from drop-down list (Montrer)
        select_filter = driver.find_element_by_id("filterByType")
        all_options = select_filter.find_elements_by_tag_name("option")
        for option in all_options:
            option.click()
            time.sleep(2)

        time.sleep(4)
        #Click Reset
        reset = driver.find_element_by_xpath("//button")
        reset.click()
        time.sleep(5)

    def goToModifyOrderPage(self):
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_sample']")
        action.move_to_element(firstLevelMenu).perform()
        # Getting to the submenu: Add Order, and clicking on it to go to the Add order form appears
        secondLevelMenu = driver.find_element_by_xpath("//li/a[@id='menu_sample_edit']")
        secondLevelMenu.click()

    def test_12_verification(self):
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
        search_by_lab_no = all_options[5]
        search_by_lab_no.click()
        search_value_field.send_keys('1234519000117')
        search_button_field = driver.find_element_by_id("searchButton")
        search_button_field.click()
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "sampleTypeSelect"))
        )

        #Change the patient or order information OR add a result and validate OR generate patient report

            # Click on drop-down Sample Type list
        select = driver.find_element_by_id('sampleTypeSelect')

        # Adding a sample type

        all_options = select.find_elements_by_tag_name("option")
        option = all_options[2]
        option.click()
        time.sleep(3)
        check_checkbox = driver.find_element_by_id('test_0')
        check_checkbox.click()
            #Save the result
        save_button = driver.find_element_by_id("saveButtonId")
        save_button.click()
        time.sleep(7)

        #Checking result in the audit Trail report
        self.goToAudit()
            # Enter parameters with correct lab number format (e.g. 13000111)
        lab_no = driver.find_element_by_id("accessionNumberSearch")
        lab_no.clear()
        button = driver.find_element_by_xpath("//input[@value='View Report']")
        lab_no.send_keys('1234519000117')
        time.sleep(3)
            # Click Rechercher
        button.click()
        time.sleep(10)



    def tearDown(self):
       self.driver.close()
       self.driver.quit()