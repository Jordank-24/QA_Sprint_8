from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    FROM_FIELD = (By.ID, "from")
    TO_FIELD = (By.ID, "to")
    CARD_INPUT = (By.CLASS_NAME, "card-input")
    CALL_TAXI_BUTTON = (By.XPATH, "//button[contains(text(), 'Call a taxi')]")
    SUPPORTIVE_PLAN = (By.XPATH, "//div[contains(text(), 'Supportive')]")
    PHONE_FIELD = (By.ID, "phone")
    COMMENT_FIELD = (By.XPATH, "//div[contains(text(), 'Comment')]")
    BLANKET_FIELD = (By.XPATH, "//div[contains(text(), 'Blanket')]")
    HANDKERCHIEF_FIELD = (By.ID, "handkerchief")
    ICE_CREAM_FIELD = (By.ID, "icecream")
    CAR_SEARCH_MODAL = (By.ID, "search")
    CARD_NUMBER = (By.ID, "number")
    CARD_CODE = (By.ID, "code")

    def __init__(self, driver):
        self.driver = driver
        routes_page = UrbanRoutesPage(self.driver)

    def set_from_address(self, address):
        self.driver.find_element(*self.FROM_FIELD).send_keys(address)

    def set_to_address(self, address):
        self.driver.find_element(*self.TO_FIELD).send_keys(address)

    def get_from_address(self):
        return self.driver.find_element(*self.FROM_FIELD).get_attribute("value")

    def click_call_taxi_button(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(expected_conditions.element_to_be_clickable(self.CALL_TAXI_BUTTON))
        button.click()

    def select_supportive_plan(self):
        self.driver.find_element(*self.SUPPORTIVE_PLAN).click()

    def fill_card_input(self):
        self.driver.find_element(*self.CARD_INPUT).click()
        self.driver.find_element(*self.CARD_NUMBER).send_keys("1234 5678 9100")
        self.driver.find_element(*self.CARD_CODE).send_keys('1111')

    def fill_comment_input(self):
        self.driver.find_element(*self.COMMENT_FIELD).click()
        self.driver.find_element(*self.COMMENT_FIELD).send_keys('Stop at the juice bar, please')

    def get_message_for_driver(self):
        return self.driver.find_element(*self.COMMENT_FIELD).get_property("value")

    def select_blanket_input(self):
        self.driver.find_element(*self.BLANKET_FIELD).click()

    def select_handkerchief_input(self):
        self.driver.find_element(*self.HANDKERCHIEF_FIELD).click()
        return self.driver.find_element(*self.HANDKERCHIEF_FIELD).get_property("checked")

    def fill_icecream_input(self):
        for i in range(2):
            self.driver.find_element(*self.ICE_CREAM_FIELD).click()

    def fill_phone_input(self):
        self.driver.find_element(*self.PHONE_FIELD).click()
        self.driver.find_element(*self.PHONE_FIELD).send_keys('+1 123 123 12 12')

    def is_car_search_modal_displayed(self):
        return self.driver.find_element(*self.CAR_SEARCH_MODAL).is_displayed()
