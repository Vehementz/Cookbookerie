
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt


def get_drvier():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com")
    return driver


def clean_text(text):
    """ Extract only the temperature from text"""
    output = float(text.split(": ")[1])
    return output


def write_file(temperaturetext):
    """Write input text into a text file"""
    filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.text"
    with open(filename, 'w') as file:
        file.write(temperaturetext)


def main():
    driver = get_drvier()
    while True:
        time.sleep(2)
        print(driver.current_url)
        temperaturetext = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]").text
        temperaturetext = str(clean_text(temperaturetext))
        write_file(temperaturetext)

print(main())


# SOME DIFFERENTS THINGS CAN HELP

# pip3 install webdriver-manager
# sudo apt install chromium-chromedriver
# pip install -U selenium
