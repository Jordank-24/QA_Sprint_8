import helpers
import data
from pages import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")


    def test_set_route(self, routes_page):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert routes_page.get_from() == data.ADDRESS_FROM
        assert routes_page.get_to() == data.ADDRESS_TO

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        phone_number = '+1 123 123 12 12'
        assert self.page.fill_phone_input(phone_number)

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        assert self.page.click_call_taxi_button()
        assert self.page.select_supportive_plan()

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        assert self.page.fill_card_input()

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        assert self.page.fill_comment_input()

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert self.page.select_blanket_input()
        assert self.page.select_handkerchief_input()

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert self.page.fill_icecream_input(quantity=2)

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        assert self.page.is_car_search_modal_displayed() is True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
