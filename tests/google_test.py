from time import sleep


def test_google(driver):
    driver.get('https://www.google.com')

    sleep(10)
