import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from dotenv import load_dotenv
load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


tinder_url = "https://app.100daysofpython.dev/services/tindog/u/zbrNIWI_LnwXJGTok_CM2dgazmXuhGBM"
EMAIL_ADDRESS = os.environ["EMAIL_ADDRESS"]
PASSWORD_ADDRESS = os.environ["PASSWORD_ADDRESS"]


driver = webdriver.Chrome(chrome_options)
driver.get(tinder_url)

original_window = driver.current_window_handle

wait = WebDriverWait(driver, 3)

login_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "tindog-login-pill")))
login_btn.click()

facebook_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-facebark")))
facebook_btn.click()

for handle in driver.window_handles:
    if handle != original_window:
        driver.switch_to.window(handle)
        break

driver.switch_to.window(driver.window_handles[-1])


email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
email_input.send_keys(EMAIL_ADDRESS)

password_input = wait.until(EC.presence_of_element_located((By.ID, "pass")))
password_input.send_keys(PASSWORD_ADDRESS)

facebook_login = driver.find_element(By.XPATH, value='/html/body/div[2]/div/form/button')
facebook_login.click()

driver.switch_to.window(original_window)
driver.switch_to.window(driver.window_handles[0])

allow_btn = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn-primary")))
allow_btn.click()

time.sleep(2)
notification = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/form/button[1]")))
notification.click()

accept_cookies = driver.find_element(By.XPATH, value="/html/body/main/div/div/form/button")
accept_cookies.click()

for n in range(20):
    time.sleep(1)
    try:
        like_button = driver.find_element(By.CLASS_NAME, value='btn-like')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            driver.find_element(By.CSS_SELECTOR, value='.match-popup a').click()
        except NoSuchElementException:
            time.sleep(2)
    except NoSuchElementException:
        time.sleep(2)

driver.quit()

