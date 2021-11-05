from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

driver.get(
    'https://github.com/')

driver.implicitly_wait(3)

sign_up = driver.find_element_by_class_name('btn-mktg')
sign_up.click()

sign_in = driver.find_element_by_class_name('color-fg-on-emphasis')
sign_in.click()
driver.implicitly_wait(10)
login_input = driver.find_element_by_id('login_field')
password_input = driver.find_element_by_id('password')
submit_button = driver.find_element_by_class_name('js-sign-in-button')
driver.implicitly_wait(10)
login_input.send_keys('mogobanyamwaro@gmail.com')
password_input.send_keys('dOUGLAS@2019')
password_input.send_keys(Keys.ENTER)
