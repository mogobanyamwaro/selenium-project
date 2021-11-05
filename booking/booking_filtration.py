from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_values):
        star_filtration_box = self.driver.find_element_by_class_name(
            '_962ef834c')
        star_child_elements = star_filtration_box.find_elements_by_css_selector(
            '*')
        print(star_child_elements)
        for star_value in star_values:
            for star_element in star_child_elements:
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value}':
                    star_element.click()
