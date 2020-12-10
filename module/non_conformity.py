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

class NonConformity(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.connecting()

    def connecting(self):
        "This method allows us to connect to the site"
        driver = self.driver
        driver.get('http://test.openelisci.org')
        name = driver.find_element_by_id("loginName")
        name.clear()
        name.send_keys('admin')
        time.sleep(2)
        password=driver.find_element_by_id("password")
        password.clear()
        password.send_keys('adminADMIN!')
        time.sleep(2)
        button = driver.find_element_by_id("submitButton")
        button.click()

    def gotononcoformity(self):
        driver = self.driver
        driver.find_element_by_id("menu_nonconformity").click()

    @api.assert_capture()
    def test_01_searchvalue(self):
        driver = self.driver
        self.gotononcoformity()
        buttonsearch = driver.find_element_by_id("searchButtonId")
        disabled2 = buttonsearch.get_attribute("disabled")
        self.assertFalse(disabled2)
        """correct format """
        lab1 = driver.find_element_by_id("searchId")
        lab1.send_keys('1234519000107')
        time.sleep(4)
        buttonsearch.click()
        time.sleep(4)
        """ incorrect format"""
        driver = self.driver
        buttonsearch = driver.find_element_by_id("searchButtonId")
        lab2 = driver.find_element_by_id("searchId")
        lab2.send_keys('0123ab6789')
        time.sleep(4)
        buttonsearch.click()
        """format incorrect """
        buttonsearch = driver.find_element_by_id("searchButtonId")
        lab3 = driver.find_element_by_id("searchId")
        lab3.send_keys('1234519000107')
        time.sleep(4)
        buttonsearch.click()

    @api.assert_capture()
    def test_02_form(self):
        driver = self.driver
        self.gotononcoformity()
        buttonsearch = driver.find_element_by_id("searchButtonId")
        lab3 = driver.find_element_by_id("searchId")
        lab3.send_keys('1234519000107')
        time.sleep(4)
        buttonsearch.click()
        """ comparison between the date of the machine and the date field """
        date = driver.find_element_by_id("date1")
        dateform=date.get_attribute("value")
        today = datetime.datetime.now().strftime("%d/%m/%Y")
        self.assertEqual(today,dateform)
        """change of date"""
        date.clear()
        date.send_keys('1/07/2019')
        """incorrect format for the date """
        date.clear()
        date.send_keys('13/9/19')
        time.sleep(4)
        nationalid = driver.find_element_by_id("nationalId")
        nationalid.click()
        date.clear()
        """ enter date in future"""
        time.sleep(5)
        next_day = (datetime.datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
        date.send_keys(next_day)
        """ pescriber information displays(site name,lastname ,firstname,adrees ...)"""
        select = driver.find_element_by_id('site')
        select.click()
        time.sleep(4)
        all_options = select.find_elements_by_tag_name("option")
        time.sleep(4)
        lab1 = driver.find_element_by_id("requesterSampleID")
        lab1.send_keys('azerty')
        lab1 = driver.find_element_by_id("providerLastNameID")
        lab1.send_keys('azerty')
        lab1 = driver.find_element_by_id("providerFirstNameID")
        lab1.send_keys('azerty')
        lab1 = driver.find_element_by_id("providerStreetAddress")
        lab1.send_keys('azerty')
        lab1 = driver.find_element_by_id("providerCity")
        lab1.send_keys('azerty')
        lab1 = driver.find_element_by_id("providerCommune")
        lab1.send_keys('azerty')
        lab1 = driver.find_element_by_id("providerWorkPhoneID")
        lab1.send_keys('+225-00-00-00-00')
        """  correct simple type appear drop down list and can be selected"""
        select = driver.find_element_by_id('qaEvent0')
        select.click()
        time.sleep(4)
        all_options = select.find_elements_by_tag_name("option")
        time.sleep(4)
        for option in all_options[1:]:
            option.click()
        """  correct refusal reason appear drop down list and can be selected"""
        select1 = driver.find_element_by_id('sampleType0')
        select.click()
        time.sleep(4)
        all_options = select.find_elements_by_tag_name("option")
        time.sleep(4)
        for option in all_options[1:]:
            option.click()
        """ """
        self.assertEqual(driver.find_element_by_id('section0').get_attribute("class"),"qaEventElement")
        """correct units apprear in the drop down menu """
        select = driver.find_element_by_id('section0')
        select.click()
        time.sleep(2)
        all_options = select.find_elements_by_tag_name("option")
        for option in all_options[1:]:
            option.click()
        time.sleep(2)
        """  enter name in field name"""
        lab1 = driver.find_element_by_id("author0")
        lab1.send_keys('azerty')
        time.sleep(2)
        """ enter text  in Note """
        lab1 = driver.find_element_by_id("note0")
        lab1.send_keys('azerty')
        """no button remove"""
        """ new sub from opens """
        select = driver.find_element_by_id('addButtonId')
        select.click()
        time.sleep(4)
        """ enter text in comments field"""
        lab1 = driver.find_element_by_id("comment")
        lab1.send_keys('azerty aaaaaaaaaaaaaaaaaaaaaaaaaaa qqqqqqqqqqqqqqqqqqqqqqqqqqq zzzzzzzzzzzzzzz')
    
    @api.assert_capture()
    def test_03_overallpage(self):
        driver = self.driver
        self.gotononcoformity()
        buttonsearch = driver.find_element_by_id("searchButtonId")
        lab3 = driver.find_element_by_id("searchId")
        lab3.send_keys('1234519000117')
        time.sleep(4)
        buttonsearch.click()
        """ leave mandatory field without data """
        select = driver.find_element_by_id('qaEvent0')
        all_options = select.find_elements_by_tag_name("option")
        for option in all_options[1:]:
            option.click()
            break
        time.sleep(4)
        buttonsave = driver.find_element_by_id("saveButtonId")
        disabled2 = buttonsave.get_attribute("disabled")
        self.assertTrue(disabled2)
        """ complete all mandatory"""
        select = driver.find_element_by_id('sampleType0')
        all_options = select.find_elements_by_tag_name("option")
        for option in all_options[1:]:
            option.click()
            break
        time.sleep(4)
        buttonsave = driver.find_element_by_id("saveButtonId")
        disabled2 = buttonsave.get_attribute("disabled")
        self.assertTrue(disabled2)
        time.sleep(4)
        """ click cancel """
        buttoncancel= driver.find_element_by_id("cancelButtonId")
        buttoncancel.click()
        time.sleep(4)
        """there is no confirmation message when you click on cancel"""
        # buttonsave= driver.find_element_by_id("saveButtonId")
        # buttonsave.click()
        time.sleep(4)
        """click add"""
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_patient")
        action.move_to_element(firstLevelMenu).perform()
        time.sleep(4)
        secondLevelMenu = driver.find_element_by_id('menu_patient_add_or_edit')
        action.move_to_element(secondLevelMenu).perform()
        secondLevelMenu.click()
        time.sleep(4)
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, "cancelButtonId")))
        buttoncancel= driver.find_element_by_id("cancelButtonId")
        buttoncancel.click()
        """return to home"""
        driver.find_element_by_id("menu_nonconformity").click()
    

    @api.assert_capture()
    def test_04_verification(self):
        driver = self.driver
        self.gotononcoformity()
        """  go to results page and look up accession number"""
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_results")
        action.move_to_element(firstLevelMenu).perform()
        time.sleep(4)
        secondLevelMenu = driver.find_element_by_id('menu_results_search')
        action.move_to_element(secondLevelMenu).perform()
        thirdLevelMenu= driver.find_element_by_id('menu_results_accession')
        thirdLevelMenu.click()
        results = driver.find_element_by_id("searchAccessionID")
        results.send_keys('1234500000012')
        driver.find_element_by_id("retrieveTestsID").click()
        """ go to validation page and look up accession number"""
        driver.find_element_by_id("menu_resultvalidation").click()
        result = driver.find_element_by_id("testSectionId")
        result.click()
        all_options = result.find_elements_by_tag_name("option")
        for option in all_options[1:]:
            option.click()
            break
        results = driver.find_element_by_id("labnoSearch")
        results.send_keys('1234519000002')
        time.sleep(2)
        buttonrech = driver.find_element_by_xpath("//input[@value='Search']")
##        [@type='button']
        buttonrech.click()
        """ generate workplan  by test for thant accession number """
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_workplan")
        action.move_to_element(firstLevelMenu).perform()
        secondLevelMenu = driver.find_element_by_id('menu_workplan_test')
        action.move_to_element(secondLevelMenu).perform()
        secondLevelMenu.click()
        bytest=driver.find_element_by_id("testName")
        all_options = bytest.find_elements_by_tag_name("option")
        for option in all_options[1:]:
            option.click()
            break

        """ generate workplan  by unit for thant accession number """

        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_workplan")
        action.move_to_element(firstLevelMenu).perform()

        secondLevelMenu = driver.find_element_by_id('menu_workplan_bench')
        action.move_to_element(secondLevelMenu).perform()

        secondLevelMenu.click()
        bytunit = driver.find_element_by_id("testSectionId")
        all_options = bytunit.find_elements_by_tag_name("option")
        for option in all_options[1:]:
            option.click()
            break
        """ generate workplan  by panel for thant accession number """
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_workplan")
        action.move_to_element(firstLevelMenu).perform()
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "menu_workplan"))
        )
        secondLevelMenu = driver.find_element_by_id('menu_workplan_panel')
        action.move_to_element(secondLevelMenu).perform()
        secondLevelMenu.click()
        bytunit = driver.find_element_by_id("testName")
        all_options = bytunit.find_elements_by_tag_name("option")
        for option in all_options[1:]:
            option.click()
            break
        """generate non conformity report by date"""
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_reports")
        action.move_to_element(firstLevelMenu).perform()
        secondLevelMenu = driver.find_element_by_id('menu_reports_routine')
        action.move_to_element(secondLevelMenu).perform()
        thirdLevelMenu = driver.find_element_by_id('menu_reports_management')
        action.move_to_element(thirdLevelMenu).perform()
        fourLevelMenu = driver.find_element_by_id('menu_reports_nonconformity')
        action.move_to_element(fourLevelMenu).perform()
        fiveLevelMenu = driver.find_element_by_id('menu_reports_nonconformity_date')
        #action.move_to_element(fiveLevelMenu).perform()
        fiveLevelMenu.click()
        time.sleep(2)
        datestart = driver.find_element_by_id('lowerDateRange')
        datestart.send_keys("12/09/2019")
        dateend = driver.find_element_by_id('upperDateRange')
        dateend.send_keys("12/09/2019")
        time.sleep(2)
        btn = driver.find_element_by_class_name('btn')
        btn.click()
        time.sleep(2)
        """generate non conformity report by unit and reason"""
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_reports")
        action.move_to_element(firstLevelMenu).perform()
        secondLevelMenu = driver.find_element_by_id('menu_reports_routine')
        action.move_to_element(secondLevelMenu).perform()
        thirdLevelMenu = driver.find_element_by_id('menu_reports_management')
        action.move_to_element(thirdLevelMenu).perform()
        fourLevelMenu = driver.find_element_by_id('menu_reports_nonconformity')
        action.move_to_element(fourLevelMenu).perform()
        fiveLevelMenu = driver.find_element_by_id('menu_reports_nonconformity_section')
        fiveLevelMenu.click()
        datestart = driver.find_element_by_id('lowerDateRange')
        datestart.send_keys("13/09/2019")
        dateend = driver.find_element_by_id('upperDateRange')
        dateend.send_keys("04/09/2019")
        time.sleep(2)
        btn = driver.find_element_by_class_name('btn')
        btn.click()
        time.sleep(2)
        """ generate audit trail report for that lab number  """
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_reports")
        action.move_to_element(firstLevelMenu).perform()
        secondLevelMenu = driver.find_element_by_id('menu_reports_routine')
        action.move_to_element(secondLevelMenu).perform()
        thirdLevelMenu = driver.find_element_by_id('menu_reports_management')
        action.move_to_element(thirdLevelMenu).perform()
        fourLevelMenu = driver.find_element_by_id('menu_reports_auditTrail')
        fourLevelMenu.click()
        audittrail = driver.find_element_by_id('accessionNumberSearch')
        audittrail.send_keys("1234500000012")
        bout = driver.find_element_by_class_name('btn')
        bout.click()
        """ generate patient report lab number  """
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_reports")
        action.move_to_element(firstLevelMenu).perform()
        secondLevelMenu = driver.find_element_by_id('menu_reports_routine')
        action.move_to_element(secondLevelMenu).perform()
        thirdLevelMenu = driver.find_element_by_id('menu_reports_status_patient')
        action.move_to_element(thirdLevelMenu).perform()
        thirdLevelMenu.click()
        audittrail = driver.find_element_by_id('accessionDirect')
        audittrail.send_keys("1234500000012")
        audittrail = driver.find_element_by_id('highAccessionDirect')
        audittrail.send_keys("1234500000018")
        audittrail = driver.find_element_by_id('patientNumberDirect')
        audittrail.send_keys("1234500000021")
        bout = driver.find_element_by_class_name('btn')
        bout.click()

    def tearDown(self):
       self.driver.close()
       self.driver.quit()