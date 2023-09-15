import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {}
desired_caps['platformName'] = 'Android'
#desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'OPPO F11'
desired_caps['app'] = ('C:/Users/mohammad.daanish/Desktop/Mobile_ApplicationTestes/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

element = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")

for x in element:
    print(x.text)

for x in element:
    button = x.text
    if button == 'ZOOM':
        x.click()
        print("Zoom Clicked Successfully")
        break
time.sleep(3)
driver.quit()