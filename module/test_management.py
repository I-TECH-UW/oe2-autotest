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


class TestManagment(unittest.TestCase):

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
    def test_01_management_test(self):
        # Click on the Admin tab => Test Management in the left hand menu
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_administration")
        firstLevelMenu.click()
        time.sleep(5)
        continue_link = driver.find_element_by_link_text('Test Management').click()
        time.sleep(5)

    @api.assert_capture()
    def test_02_existing_test(self):
        # Click on Rename Existing Test Names
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_administration")
        action.move_to_element(firstLevelMenu).perform()
        firstLevelMenu.click()
        time.sleep(3)
        link_test = driver.find_element_by_link_text('Test Management').click()
        time.sleep(3)
        button_renameName = driver.find_element_by_xpath("//input[@value='Rename existing test names'][@type='button']")
        button_renameName.click()
        time.sleep(3)
        button_test = driver.find_element_by_xpath("//input[@value='Bioline(Plasma)'][@type='button']")
        button_test.click()
        time.sleep(3)
        champ_test_EN = driver.find_element_by_xpath("//input[@name='nameEnglish'][@type='text']")
        champ_test_EN.clear()
        champ_test_EN.send_keys('AmylaseENG')
        time.sleep(2)
        champ_test_FR = driver.find_element_by_xpath("//input[@name='nameFrench'][@type='text']")
        champ_test_FR.clear()
        champ_test_FR.send_keys('AmylaseFR')
        time.sleep(2)
        champ_testReport_EN = driver.find_element_by_xpath("//input[@name='reportNameEnglish'][@type='text']")
        champ_testReport_EN.clear()
        champ_testReport_EN.send_keys('AmylaseReportENG')
        time.sleep(2)
        champ_testReport_FR = driver.find_element_by_xpath("//input[@name='reportNameFrench'][@type='text']")
        champ_testReport_FR.clear()
        champ_testReport_FR.send_keys('AmylaseReportFR')
        time.sleep(2)
        button_save = driver.find_element_by_xpath("//input[@value='Save'][@type='button']")
        button_save.click()
        time.sleep(2)
        button_accept = driver.find_element_by_xpath("//input[@value='Accept'][@type='button']")
        button_accept.click()
        time.sleep(5)

        # Repeat Step 15-18
        button_retest = driver.find_element_by_xpath("//input[@value='Lymphocytes (Abs)(Sang total)'][@type='button']")
        button_retest.click()
        time.sleep(3)
        champ_retest_EN = driver.find_element_by_xpath("//input[@name='nameEnglish'][@type='text']")
        champ_retest_EN.clear()
        champ_retest_EN.send_keys('LymphocytesENG')
        time.sleep(2)
        champ_retest_FR = driver.find_element_by_xpath("//input[@name='nameFrench'][@type='text']")
        champ_retest_FR.clear()
        champ_retest_FR.send_keys('LymphocytesFR')
        time.sleep(3)
        champ_retestReport_EN = driver.find_element_by_xpath("//input[@name='reportNameEnglish'][@type='text']")
        champ_retestReport_EN.clear()
        champ_retestReport_EN.send_keys('LymphocytesReportENG')
        time.sleep(3)
        champ_retestReport_FR = driver.find_element_by_xpath("//input[@name='reportNameFrench'][@type='text']")
        champ_retestReport_FR.clear()
        champ_retestReport_FR.send_keys('LymphocytesReportFR')
        time.sleep(3)
        button_resave = driver.find_element_by_xpath("//input[@value='Save'][@type='button']")
        button_resave.click()
        time.sleep(3)
        button_reject = driver.find_element_by_xpath("//input[@value='Reject'][@type='button']")
        button_reject.click()
        time.sleep(3)
        button_cancel = driver.find_element_by_xpath("//input[@value='Cancel'][@type='button']")
        button_cancel.click()
        time.sleep(3)
        button_finished = driver.find_element_by_xpath("//input[@value='Finished'][@type='button']")
        button_finished.click()
        time.sleep(5)

    @api.assert_capture()
    def test_03_user_session(self):
        # def setUp(self):
        #     self.driver = webdriver.Firefox()
        #     # self.driver = webdriver.Chrome()
        #     self.driver.get('http://test.openelisci.org')
        #     self.conneting()
        #     # self.validation()
        #
        # def conneting(self):
        #     driver = self.driver
        #     username_field = driver.find_element(By.ID, "loginName")
        #     username_field.clear()
        #     username_field.send_keys('niang')
        #     password_field = driver.find_element(By.ID, "password")
        #     password_field.clear()
        #     password_field.send_keys('Passer123!')
        #     button = driver.find_element(By.ID, "submitButton")
        #     button.click()

        # Click on Order => Add Order tab.
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_sample")
        action.move_to_element(firstLevelMenu).perform()
        firstLevelMenu.click()
        secondLevelMenu = driver.find_element_by_id("menu_sample_add")
        action.move_to_element(secondLevelMenu).perform()
        secondLevelMenu.click()
        time.sleep(5)

        # modifyLocate
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_sample")
        action.move_to_element(firstLevelMenu).perform()
        time.sleep(3)
        secondLevelMenu = driver.find_element_by_id("menu_sample_edit")
        secondLevelMenu.click()
        time.sleep(5)
        select_search_by = driver.find_element_by_id('searchCriteria')
        options_search_by = select_search_by.find_elements_by_tag_name("option")
        options_search_by[5].click()
        time.sleep(3)
        search_value = driver.find_element(By.ID, "searchValue")
        search_value.clear()
        search_value.send_keys('1234519000198')
        time.sleep(3)
        search_button = driver.find_element(By.ID, "searchButton")
        search_button.click()
        time.sleep(7)
        #self.assertIn("Glucose", driver.page_source)
        self.assertIn("Glycémie", driver.page_source)

        # Click on Workplan/By Test Type
        # Click on Workplan/By Test Type
        # Click on Print Workplan
        driver = self.driver
        action = ActionChains(driver)
        thirdLevelMenu = driver.find_element_by_id("menu_workplan")
        action.move_to_element(thirdLevelMenu).perform()
        time.sleep(2)
        fourthLevelMenu = driver.find_element_by_id("menu_workplan_test")
        fourthLevelMenu.click()
        select = driver.find_element_by_id('testName')
        all_options = select.find_elements_by_tag_name("option")
        all_options[28].click()
        time.sleep(3)
        button_print = driver.find_element_by_xpath("//button[@name='print'][@type='button']")
        button_print.click()
        time.sleep(5)

        # Click on Workplan/By Panel and select the test panel with the test ordered
        # Click on Print Workplan
        driver = self.driver
        action = ActionChains(driver)
        menuWorkplan = driver.find_element_by_id("menu_workplan")
        action.move_to_element(menuWorkplan).perform()
        menuWorkplan.click()
        time.sleep(2)
        menuWorkplanPanel = driver.find_element_by_id("menu_workplan_panel")
        menuWorkplanPanel.click()
        select = driver.find_element_by_id('testName')
        all_options = select.find_elements_by_tag_name("option")
        all_options[1].click()
        time.sleep(3)
        button_print = driver.find_element_by_xpath("//button[@name='print'][@type='button']")
        button_print.click()
        time.sleep(5)

        # Click on Workplan/By Unit
        # Click on Print Workplan
        driver = self.driver
        action = ActionChains(driver)
        menuWorkplan = driver.find_element_by_id("menu_workplan")
        action.move_to_element(menuWorkplan).perform()
        menuWorkplan.click()
        time.sleep(2)
        menuWorkplanUnit = driver.find_element_by_id("menu_workplan_bench")
        menuWorkplanUnit.click()
        select = driver.find_element_by_id('testSectionId')
        all_options = select.find_elements_by_tag_name("option")
        all_options[5].click()
        time.sleep(3)
        button_print = driver.find_element_by_xpath("//button[@name='print'][@type='button']")
        button_print.click()
        time.sleep(5)

        # Click on Results=> Enter by Unit
        driver = self.driver
        action = ActionChains(driver)
        menuResults = driver.find_element_by_id("menu_results")
        action.move_to_element(menuResults).perform()
        menuResults.click()
        time.sleep(2)
        menuResultsUnit = driver.find_element_by_id("menu_results_logbook")
        action.move_to_element(menuResultsUnit).perform()
        menuResultsUnit.click()
        select = driver.find_element_by_id('testSectionId')
        all_options = select.find_elements_by_tag_name("option")
        all_options[5].click()
        time.sleep(5)

        # Click on Results=> Search=> By Patient
        driver = self.driver
        action = ActionChains(driver)
        menuResults = driver.find_element_by_id("menu_results")
        action.move_to_element(menuResults).perform()
        menuResults.click()
        time.sleep(3)
        menuResultsSearch = driver.find_element_by_id("menu_results_search")
        action.move_to_element(menuResultsSearch).perform()
        menuResultsSearch.click()
        time.sleep(5)
        menuResultsPatient = driver.find_element_by_id("menu_results_patient")
        action.move_to_element(menuResultsPatient).perform()
        menuResultsPatient.click()
        time.sleep(3)
        select = driver.find_element_by_id('searchCriteria')
        all_options = select.find_elements_by_tag_name("option")
        all_options[1].click()
        time.sleep(3)
        champ = driver.find_element(By.ID, "searchValue")
        champ.send_keys("1234519000198")
        time.sleep(3)
        button_search = driver.find_element(By.ID, "searchButton")
        button_search.click()
        time.sleep(5)

        # Click on Results=> Search=> by Accession Number
        driver = self.driver
        action = ActionChains(driver)
        menuResults = driver.find_element_by_id("menu_results")
        action.move_to_element(menuResults).perform()
        menuResults.click()
        time.sleep(3)
        menuResultsSearch = driver.find_element_by_id("menu_results_search")
        action.move_to_element(menuResultsSearch).perform()
        menuResultsSearch.click()
        time.sleep(5)
        menuResultsSearchAccessNumber = driver.find_element_by_id("menu_results_accession")
        action.move_to_element(menuResultsSearchAccessNumber).perform()
        menuResultsSearchAccessNumber.click()
        time.sleep(3)
        champ_accession = driver.find_element(By.ID, "searchAccessionID")
        champ_accession.send_keys("1234519000002")
        time.sleep(3)
        button_accession_number = driver.find_element(By.ID, "retrieveTestsID")
        button_accession_number.click()
        time.sleep(5)

        # Click on Results=> Search=> by Test, Date, or Status.  Select by Test Name.
        # Click on Get Tests for Status
        driver = self.driver
        action = ActionChains(driver)
        menuResults = driver.find_element_by_id("menu_results")
        action.move_to_element(menuResults).perform()
        menuResults.click()
        time.sleep(3)
        menuResultsSearch = driver.find_element_by_id("menu_results_search")
        action.move_to_element(menuResultsSearch).perform()
        menuResultsSearch.click()
        time.sleep(5)
        menuResultsSearchTestStatus = driver.find_element_by_id("menu_results_status")
        action.move_to_element(menuResultsSearchTestStatus).perform()
        menuResultsSearchTestStatus.click()
        time.sleep(3)
        select_test = driver.find_element_by_id('selectedTest')
        all_options = select_test.find_elements_by_tag_name("option")
        all_options[33].click()
        time.sleep(3)
        button_get_test = driver.find_element_by_xpath("//button[@name='searchButton'][@type='button']")
        button_get_test.click()
        time.sleep(5)

        # Click on Results=> Search=> by Test, Date, or Status.  Select by Reception Date
        # Click on Get Tests for Status
        driver = self.driver
        action = ActionChains(driver)
        menuResults = driver.find_element_by_id("menu_results")
        action.move_to_element(menuResults).perform()
        menuResults.click()
        time.sleep(3)
        menuResultsSearch = driver.find_element_by_id("menu_results_search")
        action.move_to_element(menuResultsSearch).perform()
        menuResultsSearch.click()
        time.sleep(5)
        menuResultsSearchTestStatus = driver.find_element_by_id("menu_results_status")
        action.move_to_element(menuResultsSearchTestStatus).perform()
        menuResultsSearchTestStatus.click()
        received_field = driver.find_element(By.ID, "recievedDate")
        received_field.clear()
        received_field.send_keys('04/09/2019')
        time.sleep(3)
        #button_get_test = driver.find_element_by_link_text('Get Tests For Status')
        button_get_test = driver.find_element_by_xpath("//button[@name='searchButton'][@type='button']")
        button_get_test.click()
        time.sleep(5)

        # Select each Analysis Status, then click Get Tests for Status
        driver = self.driver
        action = ActionChains(driver)
        menuResults = driver.find_element_by_id("menu_results")
        action.move_to_element(menuResults).perform()
        menuResults.click()
        time.sleep(3)
        menuResultsSearch = driver.find_element_by_id("menu_results_search")
        action.move_to_element(menuResultsSearch).perform()
        menuResultsSearch.click()
        time.sleep(5)
        menuResultsSearchTestStatus = driver.find_element_by_id("menu_results_status")
        action.move_to_element(menuResultsSearchTestStatus).perform()
        menuResultsSearchTestStatus.click()
        select_analysis = driver.find_element_by_id('selectedAnalysisStatus')
        all_options = select_analysis.find_elements_by_tag_name("option")
        all_options[1].click()
        time.sleep(3)
        button_get_test = driver.find_element_by_xpath("//button[@name='searchButton'][@type='button']")
        button_get_test.click()
        time.sleep(5)

       # Click on Validation=> Unit Type
        driver = self.driver
        action = ActionChains(driver)
        menuValidation = driver.find_element_by_id("menu_resultvalidation")
        menuValidation.click()
        time.sleep(3)
        select_unit_type = driver.find_element_by_id('testSectionId')
        all_options = select_unit_type.find_elements_by_tag_name("option")
        all_options[5].click()
        time.sleep(3)
        self.assertIn("Glucose(Plasma)", driver.page_source)
        time.sleep(5)


        # Click on Reports => Patient Status Report
        driver = self.driver
        action = ActionChains(driver)
        firstMenuReport = driver.find_element_by_id("menu_reports")
        action.move_to_element(firstMenuReport).perform()
        time.sleep(3)
        secondMenuReport = driver.find_element_by_id("menu_reports_routine")
        action.move_to_element(secondMenuReport).perform()
        time.sleep(3)
        thirdMenuReport = driver.find_element_by_id("menu_reports_status_patient")
        action.move_to_element(thirdMenuReport).perform()
        time.sleep(3)
        fourthMenuReport = driver.find_element_by_id("menu_reports_status_patient.classique")
        fourthMenuReport.click()
        time.sleep(5)

        # lick on Reports => Summary of All Tests
        driver = self.driver
        action = ActionChains(driver)
        firstMenuReport = driver.find_element_by_id("menu_reports")
        action.move_to_element(firstMenuReport).perform()
        time.sleep(3)
        secondMenuReport = driver.find_element_by_id("menu_reports_routine")
        action.move_to_element(secondMenuReport).perform()
        time.sleep(3)
        thirdMenuReport = driver.find_element_by_id("menu_reports_aggregate")
        action.move_to_element(thirdMenuReport).perform()
        time.sleep(3)
        fourthMenuReport = driver.find_element_by_id("menu_reports_aggregate_all")
        fourthMenuReport.click()
        time.sleep(5)

        # Click on Reports=>Management Reports=>Activity Report by Test
        driver = self.driver
        action = ActionChains(driver)
        firstMenuReport = driver.find_element_by_id("menu_reports")
        action.move_to_element(firstMenuReport).perform()
        time.sleep(3)
        secondMenuReport = driver.find_element_by_id("menu_reports_routine")
        action.move_to_element(secondMenuReport).perform()
        time.sleep(3)
        thirdMenuReport = driver.find_element_by_id("menu_reports_management")
        action.move_to_element(thirdMenuReport).perform()
        time.sleep(3)
        fourthMenuReport = driver.find_element_by_id("menu_reports_activity")
        action.move_to_element(fourthMenuReport).perform()
        time.sleep(3)
        fifthMenuReport = driver.find_element_by_id("menu_activity_report_test")
        fifthMenuReport.click()
        time.sleep(5)

        # Click on Reports => Patient Status Report
        driver = self.driver
        action = ActionChains(driver)
        firstMenuReport = driver.find_element_by_id("menu_reports")
        action.move_to_element(firstMenuReport).perform()
        time.sleep(3)
        secondMenuReport = driver.find_element_by_id("menu_reports_routine")
        action.move_to_element(secondMenuReport).perform()
        time.sleep(3)
        thirdMenuReport = driver.find_element_by_id("menu_reports_status_patient")
        action.move_to_element(thirdMenuReport).perform()
        time.sleep(3)
        fourthMenuReport = driver.find_element_by_id("menu_reports_status_patient.classique")
        fourthMenuReport.click()
        time.sleep(3)
        field_from = driver.find_element(By.ID, "accessionDirect")
        field_from.clear()
        field_from.send_keys('1234500000012')
        time.sleep(3)
        field_to = driver.find_element(By.ID, "highAccessionDirect")
        field_to.clear()
        field_to.send_keys('1234500000019')
        time.sleep(3)
        button_generate = driver.find_element_by_xpath("//input[@value='Generate printable version'][@type='button']")
        button_generate.click()
        time.sleep(5)

        # Click on Reports=>Management Reports=>Audit Trail
        driver = self.driver
        action = ActionChains(driver)
        firstMenuReport = driver.find_element_by_id("menu_reports")
        action.move_to_element(firstMenuReport).perform()
        time.sleep(3)
        secondMenuReport = driver.find_element_by_id("menu_reports_routine")
        action.move_to_element(secondMenuReport).perform()
        time.sleep(3)
        thirdMenuReport = driver.find_element_by_id("menu_reports_management")
        action.move_to_element(thirdMenuReport).perform()
        time.sleep(3)
        fourthMenuReport = driver.find_element_by_id("menu_reports_auditTrail")
        fourthMenuReport.click()
        time.sleep(5)

    @api.assert_capture()
    def test_04_activation(self):
        # Click on Order => Add Order tab. Open the Sample section and open the Sample Type Xdrop down menu.
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_sample")
        action.move_to_element(firstLevelMenu).perform()
        firstLevelMenu.click()
        time.sleep(3)
        secondLevelMenu = driver.find_element_by_id("menu_sample_add")
        action.move_to_element(secondLevelMenu).perform()
        secondLevelMenu.click()
        time.sleep(3)
        button_plus = driver.find_element(By.ID, "samplesSectionId")
        button_plus.click()
        time.sleep(3)
        button_drop_down = driver.find_element(By.ID, "sampleTypeSelect")
        button_drop_down.click()
        time.sleep(5)

        # Click on Admin=> Test Management=> Activate/Deactivate tests
        driver = self.driver
        action = ActionChains(driver)
        admin_menu = driver.find_element_by_id("menu_administration")
        admin_menu.click()
        time.sleep(3)
        link_testManagement = driver.find_element_by_link_text('Test Management').click()
        time.sleep(3)
        link_activ_desactiv = driver.find_element_by_xpath("//input[@value='Activate/Deactivate tests'][@type='button']").click()
        time.sleep(5)

        # Deselect all Plasma tests
        driver.find_element_by_xpath("//input[@value='3'][@type='checkbox']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@value='53'][@type='checkbox']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@value='49'][@type='checkbox']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@value='32'][@type='checkbox']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@value='44'][@type='checkbox']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@value='51'][@type='checkbox']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@value='40'][@type='checkbox']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@value='56'][@type='checkbox']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@value='41'][@type='checkbox']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@value='47'][@type='checkbox']").click()
        time.sleep(3)

        # Scroll down and click Next
        driver.find_element_by_xpath("//input[@value='Save'][@type='button']").click()
        time.sleep(3)

        # driver.find_element_by_xpath("//input[@value='Next'][@type='button']").click()
        # time.sleep(3)
        #
        # driver.find_element_by_xpath("//input[@value='Previous'][@type='button']").click()
        # time.sleep(3)
        #
        # driver.find_element_by_xpath("//input[@value='Next'][@type='button']").click()
        # time.sleep(3)

        # Click Accept
        driver.find_element_by_xpath("//input[@value='Accept'][@type='button']").click()
        time.sleep(5)

        # Click on Order => Add Order tab. Open the Sample section and open the Sample Type Xdrop down menu.
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_sample")
        action.move_to_element(firstLevelMenu).perform()
        time.sleep(3)
        secondLevelMenu = driver.find_element_by_id("menu_sample_add")
        secondLevelMenu.click()
        time.sleep(3)
        button_plus = driver.find_element(By.ID, "samplesSectionId")
        button_plus.click()
        time.sleep(3)
        button_drop_down = driver.find_element(By.ID, "sampleTypeSelect")
        button_drop_down.click()
        time.sleep(5)

        # Click Cancel
        button_cancel = driver.find_element(By.ID, "cancelButtonId")
        button_cancel.click()
        time.sleep(5)

        # Click on Reports=>Management Reports=>Audit Trail
        driver = self.driver
        action = ActionChains(driver)
        firstMenuReport = driver.find_element_by_id("menu_reports")
        action.move_to_element(firstMenuReport).perform()
        firstMenuReport.click()
        time.sleep(5)
        secondMenuReport = driver.find_element_by_id("menu_reports_routine")
        action.move_to_element(secondMenuReport).perform()
        secondMenuReport.click()
        time.sleep(5)
        thirdMenuReport = driver.find_element_by_id("menu_reports_management")
        action.move_to_element(thirdMenuReport).perform()
        thirdMenuReport.click()
        time.sleep(5)
        fourthMenuReport = driver.find_element_by_id("menu_reports_auditTrail")
        action.move_to_element(fourthMenuReport).perform()
        fourthMenuReport.click()
        time.sleep(5)

        # Click on Order => Add Order tab. Open the Sample section and open the Sample Type drop down menu.
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_sample")
        action.move_to_element(firstLevelMenu).perform()
        firstLevelMenu.click()
        time.sleep(3)
        secondLevelMenu = driver.find_element_by_id("menu_sample_add")
        action.move_to_element(secondLevelMenu).perform()
        secondLevelMenu.click()
        time.sleep(3)
        button_plus = driver.find_element(By.ID, "samplesSectionId")
        button_plus.click()
        time.sleep(3)
        button_drop_down = driver.find_element(By.ID, "sampleTypeSelect")
        button_drop_down.click()
        time.sleep(5)


    def tearDown(self):
        self.driver.close()
        self.driver.quit()