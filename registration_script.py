
from time import sleep
import pyautogui
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--lang=en-US')  # Замените 'en-US' на нужный вам язык

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://discord.com/register")
element = driver.find_element(By.TAG_NAME, 'div')

elements = element.find_elements(By.CLASS_NAME, 'authBox-1HR6Ha theme-dark')
inputs = element.find_elements(By.TAG_NAME, 'input')
sleep(2)
username = "fdsaffsd"
for e in inputs:
    match e.get_attribute("name"):
        case "email":
            e.send_keys("dimakhaulin@gmail.com")
        case "global_name":
            e.send_keys("dima")
        case "username":
            e.send_keys(username)
            sleep(3)
            msg_error = driver.find_element(By.CSS_SELECTOR,
                                            "#app-mount > div.appAsidePanelWrapper-ev4hlp > div.notAppAsidePanel-3yzkgB > div.app-3xd6d0 > div > div > div > form > div.centeringWrapper-dGnJPQ > div > div:nth-child(4) > div:nth-child(2) > div > div")
            if "unavailable" in msg_error.text:
                e.send_keys("fdgrovjhewrvowerp")
        case "password":
            e.send_keys("324gerwv")
    match  e.get_attribute("aria-label"):
        case "Year":
            e.send_keys("2000")
        case "Day":
            e.send_keys("12")
        case "Month":
            e.send_keys("May")
            e.send_keys(Keys.RETURN)

def make_cheack():
    driver.implicitly_wait(10)
    driver.maximize_window()
    window_size = driver.get_window_size()
    driver.set_window_position(50, 50)
    driver.set_window_size(600, 800)
    x_percent = 38
    y_percent = 70
    x = (650 * x_percent) // 100
    y = (850 * y_percent) // 100
    pyautogui.moveTo(x, y)
    sleep(0.2)
    pyautogui.click()
    sleep(1)
    driver.save_screenshot(f"screenshot/{username}.png")
    # вывод

submit_button = driver.find_element(By.CSS_SELECTOR,"#app-mount > div.appAsidePanelWrapper-ev4hlp > div.notAppAsidePanel-3yzkgB > div.app-3xd6d0 > div > div > div > form > div.centeringWrapper-dGnJPQ > div > div.marginTop20-2T8ZJx > button"  )
submit_button.click()
sleep(0.5)
make_cheack()

sleep(20)
driver.close()
