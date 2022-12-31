from telnetlib import EC

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AdminPage:
    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_name = "username"
        self.password_textbox_name = "password"
        self.login_button_xpath = "//button[@type='submit']"
        self.admin_tab_xpath = "//span[text() = 'Admin']"
        self.all_tab_xpath = "//ul[@class = 'oxd-main-menu']/li/a/span"
        self.search_box_xpath = "//input[@placeholder = 'Search']"
        self.user_management_xpath = "//span[text() = 'User Management ']"
        self.users_xpath = "//a[text() = 'Users']"
        self.user_role_drop_down_xpath = "//label[text() = 'User Role']//../following-sibling::div/div/div/div/i"
        self.user_role_drop_down_list_admin_xpath = "//div[@role = 'option']/span[text() = 'Admin']"
        self.user_role_drop_down_list_ESS_xpath = "//div[@role = 'option']/span[text() = 'ESS']"
        self.user_status_drop_down_xpath = "//label[text() = 'Status']//../following-sibling::div/div/div/div/i"
        self.user_status_drop_down_list_enabled_xpath = "//span[text() = 'Enabled']"
        self.user_status_drop_down_list_disabled_xpath = "//span[text() = 'Disabled']"
        self.status_drop_down_xpath = "//label[text() = 'Status']//../following-sibling::div/div/div/div/i"
        self.status_drop_down_list_xpath = ""
        self.pim_tab_xpath = "//span[text() = 'PIM']"
        self.add_button_xpath = "//button[text() = ' Add ']"
        self.first_name_textbox_xpath = "//input[@placeholder = 'First Name']"
        self.last_name_textbox_xpath = "//input[@placeholder = 'Last Name']"
        self.toggle_switch_xpath = "//span[@class = 'oxd-switch-input oxd-switch-input--active --label-right']"
        self.new_username_xpath = "//label[text() = 'Username']//../following-sibling::div/input"
        self.new_password_xpath = "//label[text() = 'Password']//../following-sibling::div/input"
        self.confirm_password_xpath = "//label[text() = 'Confirm Password']//../following-sibling::div/input"
        self.status_enable_xpath = "//label[text() = 'Enabled']/span"
        self.save_button_xpath = "//button[text() = ' Save ']"
        self.username_already_exist_xpath = "//span[text() = 'Username already exists']"
        self.employee_profile_tab_data = "//div[@role = 'tablist']"
        self.contact_details_tab_xpath = "//a[text() = 'Contact Details']"
        self.street1_xpath = "//label[text() = 'Street 1']//../following-sibling::div/input"
        self.city_xpath = "//label[text() = 'City']//../following-sibling::div/input"
        self.state_xpath = "//label[text() = 'State/Province']//../following-sibling::div/input"
        self.postal_code_xpath = "//label[text() = 'Zip/Postal Code']//../following-sibling::div/input"
        self.mobile_xpath = "//label[text() = 'Mobile']//../following-sibling::div/input"
        self.work_email_xpath = "//label[text() = 'Work Email']//../following-sibling::div/input"
        self.nationality_icon_xpath = "//label[text() = 'Country']//../following-sibling::div/div/div/div/i"
        self.nationality_drop_down = "//div[@role = 'listbox']"
        self.contact_details_save_xpath = "//button[text() = ' Save ']"
        self.emergency_contacts_tab_xpath = "//a[text() = 'Emergency Contacts']"
        self.emergency_contacts_name = "//label[text() = 'Name']//../following-sibling::div/input"
        self.emergency_contacts_relation = "//label[text() = 'Relationship']//../following-sibling::div/input"
        self.emergency_contacts_mobile = "//label[text() = 'Mobile']//../following-sibling::div/input"
        self.emergency_contacts_save_xpath = "//button[text() = ' Save ']"
        self.emergency_contacts_add = "//h6[text() = 'Assigned Emergency Contacts']/following-sibling::button"
        self.dependents_tab_xpath = "//a[text() = 'Dependents']"
        self.dependents_add_xpath = "//h6[text() = 'Assigned Dependents']/following-sibling::button"
        self.dependents_name_xpath = "//label[text() = 'Name']//../following-sibling::div/input"
        self.dependents_relationship_xpath = "//label[text() = 'Relationship']//../following-sibling::div/div/div/div/i"
        self.dependents_relation_drop_down_option_xpath = "//span[text() = 'Other']"
        self.dependents_please_specify_xpath = "//label[text() = 'Please Specify']//../following-sibling::div/input"
        self.dependents_dob_xpath = "//label[text() = 'Date of Birth']//../following-sibling::div/div/div/input"
        self.dependents_save_xpath = "//label[text() = 'Date of Birth']//..//..//..//..//../following-sibling::div/button[text() = ' Save ']"
        self.job_tab_xpath = "//a[text() = 'Job']"
        self.job_joined_date_xpath = "//label[text() = 'Joined Date']//../following-sibling::div/div/div/input"
        self.job_title_drop_down_xpath = "//label[text() = 'Job Title']//../following-sibling::div/div/div/div/i"
        self.job_title_option_xpath = "//span[text() = 'Chief Financial Officer']"
        self.job_category_drop_down_xpath = "//label[text() = 'Job Category']//../following-sibling::div/div/div/div/i"
        self.job_category_option_xpath = "//span[text() = 'Officials and Managers']"
        self.job_sub_unit_drop_down_xpath = "//label[text() = 'Sub Unit']//../following-sibling::div/div/div/div/i"
        self.job_sub_unit_option_xpath = "//span[text() = 'Development']"
        self.job_location_drop_down_xpath = "//label[text() = 'Location']//../following-sibling::div/div/div/div/i"
        self.job_location_option_xpath = "//span[text() = 'New York Sales Office']"
        self.job_toggle_switch_xpath = "//span[@class = 'oxd-switch-input oxd-switch-input--active --label-right']"
        self.job_contract_start_date_xpath = "//label[text() = 'Contract Start Date']//../following-sibling::div/div/div/input"
        self.job_contract_end_date_xpath = "//label[text() = 'Contract End Date']//../following-sibling::div/div/div/input"
        self.job_save_xpath = "//button[text() = ' Save ']"
        self.job_employment_status_drop_down_xpath = "//label[text() = 'Employment Status']//../following-sibling::div/div/div/div/i"
        self.job_employment_status_option_xpath = "//span[text() = 'Full-Time Permanent']"
        self.job_terminate_employment_xpath = "//button[text() = ' Terminate Employment ']"
        self.job_terminate_date_xpath = "//label[text() = 'Termination Date']//../following-sibling::div/div/div/input"
        self.job_terminate_reason_drop_down_xpath = "//label[text() = 'Termination Reason']//../following-sibling::div/div/div/div[@class = 'oxd-select-text-input']"
        self.job_terminate_reason_option_xpath = "//span[text() = 'Laid-off']"
        self.job_terminate_save_xpath = "//p[text() = 'Terminate Employment']//../following-sibling::form/div/button[text() = ' Save ']"
        self.job_activate_employment_xpath = "//button[text() = ' Activate Employment ']"
        self.salary_component_xpath = "//label[text() = 'Salary Component']//../following-sibling::div/input"
        self.salary_component_pay_grade_drop_down_xpath = "//label[text() = 'Pay Grade']//../following-sibling::div/div/div/div/i"
        self.salary_component_pay_grade_option_xpath = "//span[text() = 'Grade 2']"
        self.salary_component_pay_frequency_drop_down_xpath = "//label[text() = 'Pay Frequency']//../following-sibling::div/div/div/div/i"
        self.salary_component_pay_frequency_option_xpath = "//span[text() = 'Monthly']"
        self.salary_component_currency_drop_down_xpath = "//label[text() = 'Currency']//../following-sibling::div/div/div/div/i"
        self.salary_component_currenc_option_xpath = "//span[text() = 'United States Dollar']"
        self.salary_tab_xpath = "//a[text() = 'Salary']"
        self.salary_component_add_xpath = "//h6[text() = 'Assigned Salary Components']/following-sibling::button"
        self.salary_component_amount_xpath = "//label[text() = 'Amount']//../following-sibling::div/input"
        self.salary_component_switch_xpath = "//span[@class = 'oxd-switch-input oxd-switch-input--active --label-right']"
        self.salary_component_account_number_xpath = "//label[text() = 'Account Number']//../following-sibling::div/input"
        self.salary_component_account_type_drop_down_xpath = "//label[text() = 'Account Type']//../following-sibling::div/div/div/div/i"
        self.salary_component_account_type_option_xpath = "//span[text() = 'Savings']"
        self.salary_component_routing_number_xpath = "//label[text() = 'Routing Number']//../following-sibling::div/input"
        self.salary_component_ddd_amount_xpath = "//label[text() = 'Routing Number']//..//..//../following-sibling::div/div/div/label[text() = 'Amount']//../following-sibling::div/input"
        self.salary_component_save_xpath = "//button[text() = ' Save ']"
        self.tax_exemption_tab_xpath = "//a[text() = 'Tax Exemptions']"
        self.personal_details_tab_xpath = "//a[text() = 'Personal Details']"
        self.license_number_xpath = "//label[contains(text(), 'License Number')]//../following-sibling::div/input"
        self.license_expiry_date_xpath = "//label[contains(text(), 'License Expiry Date')]//../following-sibling::div/div/div/input"
        self.date_of_birth = "//label[contains(text(), 'Date of Birth')]//../following-sibling::div/div/div/input"
        self.gender_choose_xpath = "//input[@type = 'radio' and @value = '1']"
        self.personal_details_marital_status_drop_down_xpath = "//label[text() = 'Marital Status']//../following-sibling::div/div/div/div/i"
        self.personal_details_marital_status_option_xpath = "//span[text() = 'Married']"
        self.personal_details_nationality_drop_down_xpath = "//label[text() = 'Nationality']//../following-sibling::div/div/div/div/i"
        self.personal_details_nationality_option_list_xpath = "//div[@role = 'listbox']"
        self.submit_button_xpath = "//p[text() = ' * Required']/following-sibling::button"
        self.personal_details_dob_drop_down_year_xpath = "//div[@class = 'oxd-calendar-selector-year-selected']/i"
        self.personal_details_dob_option_list_year_xpath = "//div[@class = 'oxd-calendar-selector-year-selected']/following-sibling::ul"
        self.submit_button_xpath = "//p[text() = ' * Required']/following-sibling::button"
        self.personal_details_dob_drop_down_month_xpath = "//div[@class = 'oxd-calendar-selector-month-selected']/i"
        self.personal_details_dob_option_list_month_xpath = "//div[@class = 'oxd-calendar-selector-month-selected']/following-sibling::ul"
        self.personal_details_dob_date_xpath = "//div[text() = '20']"
        self.employee_termination_validate_xpath = "//p[text() = '(Past Employee)']"

    def enter_username(self, username):
        self.driver.find_element(By.NAME, self.username_textbox_name).clear()
        self.driver.find_element(By.NAME, self.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_textbox_name).clear()
        self.driver.find_element(By.NAME, self.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def click_pim(self):
        self.driver.find_element(By.XPATH, self.pim_tab_xpath).click()

    def click_add(self):
        self.driver.find_element(By.XPATH, self.add_button_xpath).click()

    def enter_first_name(self, first_name):
        self.driver.find_element(By.XPATH, self.first_name_textbox_xpath).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.XPATH, self.last_name_textbox_xpath).send_keys(last_name)

    def toggle_switch(self):
        self.driver.find_element(By.XPATH, self.toggle_switch_xpath).click()

    def enter_new_username(self):
        self.driver.find_element(By.XPATH, self.new_username_xpath).click()
        self.driver.find_element(By.XPATH, self.new_username_xpath).send_keys('Sastha')
        expected_msg = "Username already exists"
        msg = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located
                                              ((By.XPATH, self.username_already_exist_xpath))).text
        if msg == expected_msg:
            self.driver.find_element(By.XPATH, self.new_username_xpath).send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
            self.driver.find_element(By.XPATH, self.new_username_xpath).send_keys('Livinesh')

    def enter_new_password(self):
        self.driver.find_element(By.XPATH, self.new_password_xpath).click()
        self.driver.find_element(By.XPATH, self.new_password_xpath).send_keys('Livinesh04@')

    def enter_confirm_password(self):
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).click()
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).send_keys('Livinesh04@')

    def click_save(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()

    def validate_employee_profile_tab(self):
        expected_elements = ['Personal Details\nContact Details\nEmergency '
                             'Contacts\nDependents\nImmigration\nJob\nSalary\nTax '
                             'Exemptions\nReport-to\nQualifications\nMemberships']
        actual_elements = []
        profile_elements = self.driver.find_elements(By.XPATH, self.employee_profile_tab_data)
        for element in profile_elements:
            actual_elements.append(element.text)
            print(actual_elements)

        assert expected_elements == actual_elements

    def click_contact_details_tab(self):
        self.driver.find_element(By.XPATH, self.contact_details_tab_xpath).click()

    def enter_street1(self, street1):
        self.driver.find_element(By.XPATH, self.street1_xpath).click()
        self.driver.find_element(By.XPATH, self.street1_xpath).send_keys(street1)
        element1 = self.driver.find_element(By.XPATH, self.street1_xpath).is_displayed()
        print(element1)

    def enter_city(self, city):
        self.driver.find_element(By.XPATH, self.city_xpath).click()
        self.driver.find_element(By.XPATH, self.city_xpath).send_keys(city)
        element2 = self.driver.find_element(By.XPATH, self.city_xpath).is_displayed()
        print(element2)

    def enter_state(self, state):
        self.driver.find_element(By.XPATH, self.state_xpath).click()
        self.driver.find_element(By.XPATH, self.state_xpath).send_keys(state)
        element3 = self.driver.find_element(By.XPATH, self.state_xpath).is_displayed()
        print(element3)

    def enter_postal_code(self, postal_code):
        self.driver.find_element(By.XPATH, self.postal_code_xpath).click()
        self.driver.find_element(By.XPATH, self.postal_code_xpath).send_keys(postal_code)
        element4 = self.driver.find_element(By.XPATH, self.postal_code_xpath).is_displayed()
        print(element4)

    def choose_country(self, country):
        self.driver.find_element(By.XPATH, self.nationality_icon_xpath).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.nationality_drop_down)))
        nation_list = self.driver.find_elements(By.XPATH, self.nationality_drop_down)
        for nation in nation_list:
            if country == nation.text:
                print(nation.text)
                nation.click()
            break
        element5 = self.driver.find_element(By.XPATH, "//span[text() = 'India']").is_displayed()
        print(element5)

    def enter_mobile(self, mobile):
        self.driver.find_element(By.XPATH, self.mobile_xpath).click()
        self.driver.find_element(By.XPATH, self.mobile_xpath).send_keys(mobile)
        element6 = self.driver.find_element(By.XPATH, self.mobile_xpath).is_dispalyed()
        print(element6)

    def enter_work_email(self, work_email):
        self.driver.find_element(By.XPATH, self.work_email_xpath).click()
        self.driver.find_element(By.XPATH, self.work_email_xpath).send_keys(work_email)
        element7 = self.driver.find_element(By.XPATH, self.work_email_xpath).is_displayed()
        print(element7)

    def click_contact_details_save(self):
        self.driver.find_element(By.XPATH, self.contact_details_save_xpath).click()

    def validate_contact_details(self):
        self.driver.find_element(By.XPATH, self.street1_xpath).is_displayed()
        self.driver.find_element(By.XPATH, self.city_xpath).is_displayed()
        self.driver.find_element(By.XPATH, self.state_xpath).is_displayed()
        self.driver.find_element(By.XPATH, self.postal_code_xpath).is_displayed()
        self.driver.find_element(By.XPATH, "//span[text() = 'India']").is_displayed()
        self.driver.find_element(By.XPATH, self.mobile_xpath).is_dispalyed()
        self.driver.find_element(By.XPATH, self.work_email_xpath).is_displayed()

    def click_emergency_contact_tab(self):
        self.driver.find_element(By.XPATH, self.emergency_contacts_tab_xpath).click()

    def click_emergency_contact_add_button(self):
        self.driver.find_element(By.XPATH, self.emergency_contacts_add).click()

    def enter_emergency_contact_name(self, name):
        self.driver.find_element(By.XPATH, self.emergency_contacts_name).click()
        self.driver.find_element(By.XPATH, self.emergency_contacts_name).send_keys(name)
        element1 = self.driver.find_element(By.XPATH, self.emergency_contacts_name)
        print(element1)

    def enter_emergency_contact_relation(self, relationship):
        self.driver.find_element(By.XPATH, self.emergency_contacts_relation).click()
        self.driver.find_element(By.XPATH, self.emergency_contacts_relation).send_keys(relationship)
        element2 = self.driver.find_element(By.XPATH, self.emergency_contacts_relation)
        print(element2)

    def enter_emergency_contacts_mobile(self, mobile):
        self.driver.find_element(By.XPATH, self.emergency_contacts_mobile).click()
        self.driver.find_element(By.XPATH, self.emergency_contacts_mobile).send_keys(mobile)
        element3 = self.driver.find_element(By.XPATH, self.emergency_contacts_mobile).is_displayed()
        print(element3)

    def click_emergency_contacts_save(self):
        self.driver.find_element(By.XPATH, self.emergency_contacts_save_xpath).click()

    def click_dependent_tab(self):
        self.driver.find_element(By.XPATH, self.dependents_tab_xpath).click()

    def click_dependent_add_button(self):
        self.driver.find_element(By.XPATH, self.dependents_add_xpath).click()

    def enter_dependent_name(self, name):
        self.driver.find_element(By.XPATH, self.dependents_name_xpath).click()
        self.driver.find_element(By.XPATH, self.dependents_name_xpath).send_keys(name)
        element1 = self.driver.find_element(By.XPATH, self.dependents_name_xpath).is_displayed()
        print(element1)

    def select_dependents_relationship(self, relation):
        self.driver.find_element(By.XPATH, self.dependents_relationship_xpath).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.dependents_relation_drop_down_option_xpath)))
        self.driver.find_element(By.XPATH, self.dependents_relation_drop_down_option_xpath).click()
        self.driver.find_element(By.XPATH, self.dependents_please_specify_xpath).click()
        self.driver.find_element(By.XPATH, self.dependents_please_specify_xpath).send_keys(relation)
        element2 = self.driver.find_element(By.XPATH, self.dependents_please_specify_xpath).is_displayed()
        print(element2)

    def enter_dependents_dob(self, dob):
        self.driver.find_element(By.XPATH, self.dependents_dob_xpath).click()
        self.driver.find_element(By.XPATH, self.dependents_dob_xpath).send_keys(dob)
        element3 = self.driver.find_element(By.XPATH, self.dependents_dob_xpath).is_displayed()
        print(element3)

    def click_dependents_save(self):
        self.driver.find_element(By.XPATH, self.dependents_save_xpath).click()

    def click_job_tab(self):
        self.driver.find_element(By.XPATH, self.job_tab_xpath).click()

    def enter_job_joined_date(self, date):
        date_element = self.driver.find_element(By.XPATH, self.job_joined_date_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(date_element).click(date_element).perform()
        actions.move_to_element(date_element).send_keys(date).perform()


    def select_job_title(self):
        self.driver.find_element(By.XPATH, self.job_title_drop_down_xpath).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.job_title_option_xpath)))
        self.driver.find_element(By.XPATH, self.job_title_option_xpath).click()


    def select_job_category(self):
        self.driver.find_element(By.XPATH, self.job_category_drop_down_xpath).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.job_category_option_xpath)))
        self.driver.find_element(By.XPATH, self.job_category_option_xpath).click()


    def select_job_sub_unit(self):
        self.driver.find_element(By.XPATH, self.job_sub_unit_drop_down_xpath).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.job_sub_unit_option_xpath)))
        self.driver.find_element(By.XPATH, self.job_sub_unit_option_xpath).click()


    def select_job_location(self):
        self.driver.find_element(By.XPATH, self.job_location_drop_down_xpath).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.job_location_option_xpath)))
        self.driver.find_element(By.XPATH, self.job_location_option_xpath).click()

    def select_job_employment_status(self):
        self.driver.find_element(By.XPATH, self.job_employment_status_drop_down_xpath).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.job_employment_status_option_xpath)))
        self.driver.find_element(By.XPATH, self.job_employment_status_option_xpath).click()


    def click_job_toggle_switch(self):
        self.driver.find_element(By.XPATH, self.job_toggle_switch_xpath).click()

    def enter_job_contract_start_date(self, start_date):
        self.driver.find_element(By.XPATH, self.job_contract_start_date_xpath).click()
        self.driver.find_element(By.XPATH, self.job_contract_start_date_xpath).send_keys(start_date)


    def enter_job_contract_end_date(self, end_date):
        self.driver.find_element(By.XPATH, self.job_contract_end_date_xpath).click()
        self.driver.find_element(By.XPATH, self.job_contract_end_date_xpath).send_keys(end_date)


    def click_job_save(self):
        self.driver.find_element(By.XPATH, self.job_save_xpath).click()

    def click_employee_termination(self):
        self.driver.find_element(By.XPATH, self.job_terminate_employment_xpath).click()

    def enter_employee_termination_date(self):
        self.driver.find_element(By.XPATH, self.job_terminate_date_xpath).click()
        self.driver.find_element(By.XPATH, "//div[text() = '15']").click()

    def select_employee_termination_reason(self):
        reason = self.driver.find_element(By.XPATH, self.job_terminate_reason_drop_down_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(reason).click(reason).perform()
        #
        self.driver.find_element(By.XPATH, self.job_terminate_reason_option_xpath).click()

    def click_employee_termination_save(self):
        self.driver.find_element(By.XPATH, self.job_terminate_save_xpath).click()

    def validate_employee_termination(self):
        employee_termination = self.driver.find_element(By.XPATH, self.employee_termination_validate_xpath).is_displayed()
        if employee_termination == 'true':
            print("termination is successful")

    def click_activate_employee(self):
        self.driver.find_element(By.XPATH, self.job_activate_employment_xpath).click()

    def validate_employee_activation(self):
        employee_termination = self.driver.find_element(By.XPATH,
                                                        self.employee_termination_validate_xpath).is_displayed()
        if employee_termination == 'false':
            print("Activation is successful")


    def click_salary_tab(self):
        self.driver.find_element(By.XPATH, self.salary_tab_xpath).click()

    def click_salary_component_add(self):
        self.driver.find_element(By.XPATH, self.salary_component_add_xpath).click()

    def enter_salary_component(self, salary_component):
        self.driver.find_element(By.XPATH, self.salary_component_xpath).click()
        self.driver.find_element(By.XPATH, self.salary_component_xpath).send_keys(salary_component)

    def select_pay_grade(self):
        self.driver.find_element(By.XPATH, self.salary_component_pay_grade_drop_down_xpath).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.salary_component_pay_grade_option_xpath)))
        self.driver.find_element(By.XPATH, self.salary_component_pay_grade_option_xpath).click()


    def select_pay_frequency(self):
        self.driver.find_element(By.XPATH, self.salary_component_pay_frequency_drop_down_xpath).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.salary_component_pay_frequency_option_xpath)))
        self.driver.find_element(By.XPATH, self.salary_component_pay_frequency_option_xpath).click()


    def select_currency(self):
        self.driver.find_element(By.XPATH, self.salary_component_currency_drop_down_xpath).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.salary_component_currenc_option_xpath)))
        self.driver.find_element(By.XPATH, self.salary_component_currenc_option_xpath).click()


    def enter_amount(self, amount):
        self.driver.find_element(By.XPATH, self.salary_component_amount_xpath).click()
        self.driver.find_element(By.XPATH, self.salary_component_amount_xpath).send_keys(amount)


    def click_salary_component_switch(self):
        self.driver.find_element(By.XPATH, self.salary_component_switch_xpath).click()

    def enter_account_number(self, account_number):
        self.driver.find_element(By.XPATH, self.salary_component_account_number_xpath).click()
        self.driver.find_element(By.XPATH, self.salary_component_account_number_xpath).send_keys(account_number)


    def select_account_type(self):
        self.driver.find_element(By.XPATH, self.salary_component_account_type_drop_down_xpath).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.salary_component_account_type_option_xpath)))
        self.driver.find_element(By.XPATH, self.salary_component_account_type_option_xpath).click()


    def enter_routing_number(self, routing_number):
        self.driver.find_element(By.XPATH, self.salary_component_routing_number_xpath).click()
        self.driver.find_element(By.XPATH, self.salary_component_routing_number_xpath).send_keys(routing_number)


    def enter_salary_component_ddd_amount(self, ddd_amount):
        self.driver.find_element(By.XPATH, self.salary_component_ddd_amount_xpath).click()
        self.driver.find_element(By.XPATH, self.salary_component_routing_number_xpath).send_keys(ddd_amount)


    def click_salary_component_save(self):
        self.driver.find_element(By.XPATH, self.salary_component_save_xpath).click()

    def click_personal_details_tab(self):
        self.driver.find_element(By.XPATH, self.personal_details_tab_xpath).click()

    def enter_license_number(self, license_number):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.license_number_xpath)))
        element = self.driver.find_element(By.XPATH, self.license_number_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click(element).perform()
        actions.move_to_element(element).send_keys(license_number).perform()

    def enter_license_expiry_date(self, expiry_date):
        self.driver.find_element(By.XPATH, self.license_expiry_date_xpath).click()
        self.driver.find_element(By.XPATH, self.license_expiry_date_xpath).send_keys(expiry_date)

    def select_nationality(self, nation):
        self.driver.find_element(By.XPATH, self.personal_details_nationality_drop_down_xpath).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.personal_details_nationality_option_list_xpath)))
        #self.driver.find_element(By.XPATH, "//span[text() = 'Indian']").click()
        nation_list = self.driver.find_elements(By.XPATH, self.personal_details_nationality_option_list_xpath)
        for item in nation_list:
            if nation == item.text:
                item.click()
            break

    def select_marital_status(self):
        element = self.driver.find_element(By.XPATH, self.personal_details_marital_status_drop_down_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click(element).perform()
        #WebDriverWait(self.driver, 10).until(
            #expected_conditions.presence_of_element_located(
               # (By.XPATH, self.personal_details_marital_status_option_xpath)))
        self.driver.find_element(By.XPATH, self.personal_details_marital_status_option_xpath).click()

    def enter_date_of_birth(self, dob):
        date = self.driver.find_element(By.XPATH, self.date_of_birth)
        actions = ActionChains(self.driver)
        actions.move_to_element(date).click(date).perform()
        actions.send_keys(dob).perform()
        #self.driver.find_element(By.XPATH, self.date_of_birth).send_keys(dob)
        #
        # self.driver.find_element(By.XPATH, self.personal_details_dob_date_xpath).click()

    def select_gender(self):
        self.driver.find_element(By.XPATH, self.gender_choose_xpath).click()

    def click_personal_details_save(self):
        self.driver.find_element(By.XPATH, self.submit_button_xpath).click()

    def click_admin_tab(self):
        self.driver.find_element(By.XPATH, self.admin_tab_xpath).click()

    def validate_all_elements_present(self):
        expected_menu_elements = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard',
                                  'Directory', 'Maintenance', 'Buzz']
        menu_elements = self.driver.find_elements(By.XPATH, self.all_tab_xpath)
        actual_menu_elements = []
        for menu in menu_elements:
            actual_menu_elements.append(menu.text)

        assert expected_menu_elements == actual_menu_elements

    def validate_search_box(self):
        search = self.driver.find_element(By.XPATH, self.search_box_xpath).is_displayed()
        print(search)

    def validate_lowercase_uppercase(self):
        expected_menu_elements = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard',
                                  'Directory', 'Maintenance', 'Buzz']
        search_box = self.driver.find_element(By.XPATH, self.search_box_xpath)
        for item in expected_menu_elements:
            search_box.send_keys(item.lower())
            assert self.driver.find_element(By.XPATH, self.all_tab_xpath).text == item
            search_box.send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)

        for item in expected_menu_elements:
            search_box.send_keys(item.upper())
            assert self.driver.find_element(By.XPATH, self.all_tab_xpath).text == item
            search_box.send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)

    def validate_user_role_drop_down(self):
        self.driver.find_element(By.XPATH, self.user_role_drop_down_xpath).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.user_role_drop_down_list_admin_xpath)))
        element1 = self.driver.find_element(By.XPATH, self.user_role_drop_down_list_admin_xpath).is_displayed()
        print(element1)
        element2 = self.driver.find_element(By.XPATH, self.user_role_drop_down_list_ESS_xpath).is_displayed()
        print(element2)

    def validate_user_status(self):
        self.driver.find_element(By.XPATH, self.user_status_drop_down_xpath).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.user_status_drop_down_list_enabled_xpath)))
        element1 = self.driver.find_element(By.XPATH, self.user_status_drop_down_list_enabled_xpath).is_displayed()
        print(element1)
        element2 = self.driver.find_element(By.XPATH, self.user_status_drop_down_list_disabled_xpath).is_displayed()
        print(element2)


