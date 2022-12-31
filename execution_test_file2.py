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

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.job_joined_details_xpath = None

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
        pim = AdminPage(driver)
        pim.click_pim()
        pim.click_add()
        pim.enter_first_name("Livinesh")
        pim.enter_last_name("Sastha")
        pim.click_save()

    def test_personal_details(self):
        driver = self.driver
        pim = AdminPage(driver)
        pim.click_personal_details_tab()
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "//label[contains(text(), 'License Number')]//../following-sibling::div/input")))
        pim.enter_license_number("23456")
        pim.enter_license_expiry_date("2023-10-20")
        pim.select_nationality("Indian")
        pim.select_marital_status()
        pim.enter_date_of_birth("1999-11-20")
        pim.select_gender()
        pim.click_personal_details_save()

    def test_contact_details(self):
        driver = self.driver
        pim = AdminPage(driver)
        pim.click_contact_details_tab()
        pim.enter_street1("Periyar street")
        pim.enter_city("Erode")
        pim.enter_state("TamilNadu")
        pim.enter_postal_code("638001")
        pim.choose_country("India")
        pim.enter_mobile("8344595899")
        pim.enter_work_email("livinesh@gmail.com")
        pim.click_contact_details_save()

    def test_emergency_contacts(self):
        driver = self.driver
        pim = AdminPage(driver)
        pim.click_emergency_contact_tab()
        pim.click_emergency_contact_add_button()
        pim.enter_emergency_contact_name("Sharmatha")
        pim.enter_emergency_contact_relation("Mother")
        pim.enter_emergency_contacts_mobile("9488875755")
        pim.click_emergency_contacts_save()

    def test_dependents(self):
        driver = self.driver
        pim = AdminPage(driver)
        pim.click_dependent_tab()
        pim.click_dependent_add_button()
        pim.enter_dependent_name('Sharmatha')
        pim.select_dependents_relationship('Mother')
        pim.enter_dependents_dob('1970-05-12')
        pim.click_dependents_save()

    def test_job_details(self):
        driver = self.driver
        pim = AdminPage(driver)
        pim.click_job_tab()
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "//label[text() = 'Joined Date']//../following-sibling::div/div/div/input")))
        pim.enter_job_joined_date('2020-11-21')
        pim.select_job_title()
        pim.select_job_category()
        pim.select_job_sub_unit()
        pim.select_job_location()
        pim.select_job_employment_status()
        pim.click_job_toggle_switch()
        pim.enter_job_contract_start_date('2020-12-21')
        pim.enter_job_contract_end_date('2023-11-21')
        pim.click_job_save()

    def test_job_terminate_details(self):
        driver = self.driver
        pim = AdminPage(driver)
        pim.click_job_tab()
        pim.click_employee_termination()
        pim.enter_employee_termination_date()
        pim.select_employee_termination_reason()
        pim.click_employee_termination_save()
        pim.validate_employee_termination()

    def test_job_activate_employment(self):
        driver = self.driver
        pim = AdminPage(driver)
        pim.click_job_tab()
        pim.click_employee_termination()
        pim.enter_employee_termination_date()
        pim.select_employee_termination_reason()
        pim.click_employee_termination_save()
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "//button[text() = ' Activate Employment ']")))
        pim.click_activate_employee()
        pim.validate_employee_activation()

    def test_salary_component(self):
        driver = self.driver
        pim = AdminPage(driver)
        pim.click_salary_tab()
        pim.click_salary_component_add()
        pim.enter_salary_component("abcd")
        pim.select_pay_grade()
        pim.select_pay_frequency()
        pim.select_currency()
        pim.enter_amount("45000")
        pim.click_salary_component_switch()
        pim.enter_account_number("2343464567")
        pim.select_account_type()
        pim.enter_routing_number("55677778")
        pim.enter_salary_component_ddd_amount("46000")
        pim.click_salary_component_save()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
