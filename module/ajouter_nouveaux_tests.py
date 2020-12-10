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


class AjouterNouveauxTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome()
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
    def test_01_action(self):
        # Click on the Admin tab => Gestion des Tests in the left hand menu
        # Click on Ajouter de nouveaux Tests
        # Tick the box next to afficher le guide
        # Click on the Ordonnance menu tab and select Ajuter Ordonnance
        # Click on the + next to Type de test
        # Select the Type d'echantillon that you created the added the new test to
        # Look for the Nom du Test that you added, which will be listed under Tests Disponibles in the position in the list that you placed it in
        # Repeat for any other Type d'echantillon that you assigned the new Nom du Test to.
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_administration")
        action.move_to_element(firstLevelMenu).perform()
        firstLevelMenu.click()
        time.sleep(3)
        continue_link = driver.find_element_by_link_text('Test Management').click()
        time.sleep(3)
        button_new_test = driver.find_element_by_xpath("//input[@value='Add new tests'][@type='button']")
        button_new_test.click()
        time.sleep(3)
        button_check = driver.find_element_by_xpath("//input[@onchange='guideSelection(this)'][@type='checkbox']")
        button_check.click()
        time.sleep(3)
        english_test = driver.find_element(By.ID, "testNameEnglish")
        english_test.clear()
        english_test.send_keys('sickle cell disease'+str(randint(0, 1000)))
        time.sleep(3)
        frensh_test = driver.find_element(By.ID, "testNameFrench")
        frensh_test.clear()
        frensh_test.send_keys('Drepanocytose'+str(randint(0, 1000)))
        time.sleep(3)
        select1 = driver.find_element_by_id('testUnitSelection')
        all_options1 = select1.find_elements_by_tag_name("option")
        all_options1[1].click()
        time.sleep(3)
        select2 = driver.find_element_by_id('asmSelect0')
        all_options2 = select2.find_elements_by_tag_name("option")
        all_options2[1].click()
        time.sleep(3)
        select3 = driver.find_element_by_id('resultTypeSelection')
        all_options3 = select3.find_elements_by_tag_name("option")
        all_options3[1].click()
        time.sleep(3)
        button_copy_test_name = driver.find_element_by_xpath("//input[@value='Copy from Test Name'][@type='button']")
        button_copy_test_name.click()
        time.sleep(3)
        select4 = driver.find_element_by_id('uomSelection')
        all_options4 = select4.find_elements_by_tag_name("option")
        all_options4[1].click()
        time.sleep(3)
        button_next1 = driver.find_element_by_xpath("//input[@value='Next'][@type='button']")
        button_next1.click()
        time.sleep(3)
        select5 = driver.find_element_by_id('asmSelect1')
        all_options5 = select5.find_elements_by_tag_name("option")
        all_options5[1].click()
        time.sleep(3)
        source_element = driver.find_element_by_xpath("//li[@value='1']")
        destination_element = driver.find_element_by_xpath("//li[@value='31']")
        actionChains = ActionChains(driver)
        actionChains.drag_and_drop(source_element, destination_element).perform()
        time.sleep(3)
        button_next2 = driver.find_element_by_xpath("//input[@value='Next'][@type='button']")
        button_next2.click()
        time.sleep(3)
        button_accept = driver.find_element_by_xpath("//input[@value='Accept'][@type='button']")
        button_accept.click()
        time.sleep(5)

        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_sample")
        action.move_to_element(firstLevelMenu).perform()
        time.sleep(3)
        # thirdLevelMenu = driver.find_element_by_id("menu_sample_add")
        thirdLevelMenu = driver.find_element_by_link_text('Add Order')
        # action.move_to_element(thirdLevelMenu).perform()
        thirdLevelMenu.click()
        time.sleep(3)
        #button_sample = driver.find_element_by_xpath("//input[@name='showHide'][@type='button']")
        button_sample = driver.find_element(By.ID, "samplesSectionId")
        button_sample.click()
        time.sleep(3)
        select5 = driver.find_element_by_id('sampleTypeSelect')
        all_options6 = select5.find_elements_by_tag_name("option")
        all_options6[1].click()
        time.sleep(3)
        button_check1 = driver.find_element_by_id("test_16")
        button_check1.click()
        time.sleep(3)
        button_check2 = driver.find_element_by_id("test_15")
        button_check2.click()
        time.sleep(5)

        # Repeat for any other Type d'echantillon that you assigned the new Nom du Test to.
        select = driver.find_element_by_id('sampleTypeSelect')
        all_options = select.find_elements_by_tag_name("option")
        all_options[1].click()
        check_id = driver.find_element_by_id('select_2')
        check_id.click()
        time.sleep(5)
        button_check2 = driver.find_element_by_id('test_19')
        button_check2.click()
        time.sleep(5)






    def tearDown(self):
        self.driver.close()
        self.driver.quit()