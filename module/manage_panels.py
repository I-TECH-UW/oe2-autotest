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

class ManagePanels(unittest.TestCase):

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

    @api.assert_capture()
    def test_01(self):
        # Click on the Admin tab => Gestion des Tests in the left hand menu
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_administration")
        firstLevelMenu.click()
        time.sleep(3)
        link_test = driver.find_element_by_link_text('Test Management').click()
        time.sleep(3)
        button_renameName = driver.find_element_by_xpath("//input[@value='Manage Panels'][@type='button']")
        button_renameName.click()
        time.sleep(5)

    @api.assert_capture()
    def test_02createNewPanel(self):
        # Click on Create New Panel
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_administration")
        firstLevelMenu.click()
        time.sleep(3)
        link_test = driver.find_element_by_link_text('Test Management').click()
        time.sleep(3)
        button_renameName = driver.find_element_by_xpath("//input[@value='Manage Panels'][@type='button']")
        button_renameName.click()
        time.sleep(3)
        button_newPanel = driver.find_element_by_xpath("//input[@value='Create New Panel'][@type='button']")
        button_newPanel.click()
        time.sleep(3)
        champ_englishName = driver.find_element(By.ID, "panelEnglishName")
        champ_englishName.clear()
        champ_englishName.send_keys('hemoglobin' + str(randint(0, 1000)))
        time.sleep(3)
        button_next = driver.find_element_by_xpath("//input[@value='Next'][@type='button']")
        button_next.click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.alert_is_present(), 'Timed out waiting for PA creation ' + 'confirmation popup to appear.')
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(3)
        champ_englishName.clear()
        time.sleep(3)
        champ_frenchName = driver.find_element(By.ID, "panelFrenchName")
        champ_frenchName.clear()
        champ_frenchName.send_keys('hémoglobine' + str(randint(0, 1000)))
        time.sleep(3)
        button_next = driver.find_element_by_xpath("//input[@value='Next'][@type='button']")
        button_next.click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.alert_is_present(), 'Timed out waiting for PA creation ' + 'confirmation popup to appear.')
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(3)
        champ_frenchName.clear()
        time.sleep(3)
        champ_englishName.send_keys('hemoglobin' + str(randint(0, 1000)))
        time.sleep(3)
        champ_frenchName.send_keys('hémoglobine' + str(randint(0, 1000)))
        time.sleep(3)
        button_next = driver.find_element_by_xpath("//input[@value='Next'][@type='button']")
        button_next.click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.alert_is_present(), 'Timed out waiting for PA creation ' + 'confirmation popup to appear.')
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(3)
        select_sample_type = driver.find_element_by_id('sampleTypeId')
        options_sample_type = select_sample_type.find_elements_by_tag_name("option")
        options_sample_type[1].click()
        time.sleep(3)
        button_next = driver.find_element_by_xpath("//input[@value='Next'][@type='button']")
        button_next.click()
        time.sleep(3)
        button_accept = driver.find_element_by_xpath("//input[@value='Accept'][@type='button']")
        button_accept.click()
        time.sleep(3)
        button_previous = driver.find_element_by_xpath("//input[@value='Previous'][@type='button']")
        button_previous.click()
        time.sleep(3)
        button_newPanel = driver.find_element_by_xpath("//input[@value='Create New Panel'][@type='button']")
        button_newPanel.click()
        time.sleep(3)
        button_previous = driver.find_element_by_xpath("//input[@value='Previous'][@type='button']")
        button_previous.click()
        time.sleep(5)

    @api.assert_capture()
    def test_03setsampleTypeOrder(self):
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_administration")
        firstLevelMenu.click()
        time.sleep(3)
        link_test = driver.find_element_by_link_text('Test Management').click()
        time.sleep(3)
        button_renameName = driver.find_element_by_xpath("//input[@value='Manage Panels'][@type='button']")
        button_renameName.click()
        time.sleep(3)
        button_newPanel = driver.find_element_by_xpath("//input[@value='Set Panel Order'][@type='button']")
        button_newPanel.click()
        time.sleep(3)
        source_element = driver.find_element_by_xpath("//li[@value='1']")
        destination_element = driver.find_element_by_xpath("//li[@value='4']")
        actionChains = ActionChains(driver)
        actionChains.drag_and_drop(source_element, destination_element).perform()
        time.sleep(3)
        button_next = driver.find_element_by_xpath("//input[@value='Next'][@type='button']")
        button_next.click()
        time.sleep(3)
        button_accept = driver.find_element_by_xpath("//input[@value='Accept'][@type='button']")
        button_accept.click()
        time.sleep(3)
        button_previous = driver.find_element_by_xpath("//input[@value='Previous'][@type='button']")
        button_previous.click()
        time.sleep(5)


    def test_04testTypeEchantillon(self):
        driver = self.driver
        action = ActionChains(driver)
        firstLevelMenu = driver.find_element_by_id("menu_administration")
        firstLevelMenu.click()
        time.sleep(3)
        link_test = driver.find_element_by_link_text('Test Management').click()
        time.sleep(3)
        button_renameName = driver.find_element_by_xpath("//input[@value='Manage Panels'][@type='button']")
        button_renameName.click()
        time.sleep(3)
        button_newPanel = driver.find_element_by_xpath("//input[@value='Test Assignment'][@type='button']")
        button_newPanel.click()
        time.sleep(3)
        select_panel_type = driver.find_element_by_class_name('required')
        options_panel_type = select_panel_type.find_elements_by_tag_name("option")
        options_panel_type[5].click()
        time.sleep(3)
        availale_test = driver.find_element(By.ID, "option_9")
        availale_test.click()
        time.sleep(3)
        inferieur = driver.find_element(By.ID, "button2")
        inferieur.click()
        time.sleep(3)
        inferieur = driver.find_element(By.ID, "button2")
        inferieur.click()
        time.sleep(6)
        inferieur = driver.find_element(By.ID, "button1")
        inferieur.click()
        time.sleep(6)
        button_save = driver.find_element_by_xpath("//input[@value='Save'][@type='button']")
        button_save.click()
        self.assertIn("Save was successful", driver.page_source)
        time.sleep(5)
        link_test = driver.find_element_by_xpath("//input[@value='Test Management'][@type='button']").click()
        time.sleep(5)








    def tearDown(self):
        self.driver.close()
        self.driver.quit()