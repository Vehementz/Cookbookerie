from selenium import webdriver


def get_drivers():
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

def main():
    driver = get_drivers()
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    return element.text
    # element = driver.find_element_by_xpath("/html/body/div[1]/div/h1[1]")



print (main())

#### SOME DIFFERENTS THINGS CAN HELP 

# pip3 install webdriver-manager
# sudo apt install chromium-chromedriver
# pip install -U selenium
