from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.get(
    'https://www.seleniumeasy.com/python')
driver.implicitly_wait(3)
my_element = driver.find_element_by_class_name('easy-breadcrumb_segment')
driver.implicitly_wait(3)
my_element.click()
welcome_to = driver.getPageSource().contains('Welcome to')

print(welcome_to)
WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element(
    # Element filtration
    (BY.CLASS_NAME, 'progress-label'),
    # The exppected text
    'Complete!'
))
