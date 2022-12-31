from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest

from livinesh_guvi_project2.web_elements import AdminPage


class AdminTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        driver = cls.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = AdminPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

    def test_validate_employee_profile_tabs(self):
        driver = self.driver
        pim = AdminPage(driver)
        pim.click_admin_tab()
        pim.validate_all_elements_present()
        pim.validate_search_box()
        pim.validate_lowercase_uppercase()

    def test_drop_down_admin_page(self):
        driver = self.driver
        pim = AdminPage(driver)
        pim.click_admin_tab()
        pim.validate_all_elements_present()
        pim.validate_user_role_drop_down()
        pim.validate_user_status()

    def test_add_new_employee(self):
        driver = self.driver
        pim = AdminPage(driver)
        pim.click_pim()
        pim.click_add()
        pim.enter_first_name("Livinesh")
        pim.enter_last_name("Sastha")
        pim.toggle_switch()
        pim.enter_new_username()
        pim.enter_new_password()
        pim.enter_confirm_password()
        pim.click_save()
        expected_text = "Employee List"
        assert WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, "//a[text() = 'Employee List']"), expected_text))

    def test_validate_employee_tabs(self):
        driver = self.driver
        pim = AdminPage(driver)
        pim.click_pim()
        pim.click_add()
        pim.enter_first_name("Livinesh")
        pim.enter_last_name("Sastha")
        pim.toggle_switch()
        pim.enter_new_username()
        pim.enter_new_password()
        pim.enter_confirm_password()
        pim.click_save()
        expected_text = "Employee List"
        assert WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, "//a[text() = 'Employee List']"), expected_text))
        pim.validate_employee_profile_tab()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
