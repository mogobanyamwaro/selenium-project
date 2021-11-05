from selenium import webdriver
import booking.constants as const
from booking.booking_filtration import BookingFiltration


class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_to):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]')
        currency_element.click()

        selected_currency_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element_by_id('ss')
        search_field.clear()
        search_field.send_keys(place_to_go)
        first_result = self.find_element_by_css_selector('li[data-i="0"]')
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"]')
        check_in_element.click()
        check_out_element = self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"]')
        check_out_element.click()

    def select_adults(self, count=1):
        selection_element = self.find_element_by_id('xp__guests__toggle')
        selection_element.click()

        while True:
            decrease_adults_elements = self.find_element_by_css_selector(
                'button[aria-label="Decrease number of Adults"]')
            decrease_adults_elements.click()
            adults_value_element = self.find_element_by_id('group_adults')
            adults_value = adults_value_element.get_attribute('value')
            if int(adults_value) == 1:
                break

        increase_button_element = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]')

        for _ in range(count-1):
            increase_button_element.click()

    def click_search(self):
        search_button = self.find_element_by_css_selector(
            'button[type="submit"')
        search_button.click()

    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        # filtration.apply_star_rating(3, 5, 4)
