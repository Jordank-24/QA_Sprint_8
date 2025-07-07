import helpers
import data
from pages import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options

@classmethod
def setup_class(cls):
    options = Options()
    options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
    cls.driver = webdriver.Chrome(options=options)
    cls.page = UrbanRoutesPage(cls.driver)

    if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
        print("Connected to the Urban Routes server")
        cls.driver.get(data.URBAN_ROUTES_URL)
    else:
        print("Cannot connect to Urban Routes. Check the server is on and still running")


        cls.driver.get(data.URBAN_ROUTES_URL)

    def test_set_route(self):
        self.page.set_from_address('East 2nd Street, 601')
        self.page.set_to_address('1300 1st St')

    def test_fill_phone_number(self):
        phone_number = '+1 123 123 12 12'
        self.page.fill_phone_input(phone_number)  # Assuming the method requires a phone number

    def test_select_plan(self):
        self.page.click_call_taxi_button()
        self.page.select_supportive_plan()

    def test_fill_card(self):
        self.page.fill_card_input()

    def test_comment_for_driver(self):
        self.page.fill_comment_input()

    def test_order_blanket_and_handkerchiefs(self):
        self.page.select_blanket_input()
        self.page.select_handkerchief_input()

    def test_order_2_ice_creams(self):
        self.page.fill_icecream_input(quantity=2)

    def test_car_search_model_appears(self):
        assert self.page.is_car_search_modal_displayed() is True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


