import time

from selene import browser
from pathlib import Path
from selenium.webdriver.chrome.options import Options

def test_demo_qa():
    file_path = Path('img/1.jpg').resolve()

    options = Options()
    options.add_argument('--window-size=1920,1080')
    browser.config.driver_options = options

    browser.open('https://demoqa.com/automation-practice-form')

    browser.element("#RightSide_Advertisement").execute_script('element.remove()')
    browser.element("footer").execute_script('element.remove()')
    browser.element("#fixedban").execute_script('element.remove()')

    browser.element("#firstName").type("Aleksei")
    browser.element("#lastName").type("Vasilev")
    browser.element("#userEmail").type("kardahur@gmail.com")
    browser.element("#gender-radio-1").element("..").click()
    browser.element("#userNumber").type("9054512345")
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").element('option[value="7"]').click()
    browser.element(".react-datepicker__year-select").element('option[value="1989"]').click()
    browser.element(".react-datepicker__day.react-datepicker__day--009").click()
    browser.element("#subjectsInput").type("Computer").press_enter()
    browser.element("#hobbies-checkbox-1").element("..").click()
    browser.element("#uploadPicture").set_value(str(file_path))
    browser.element("#currentAddress").type("Another str. 11")
    browser.element("#state").click()
    browser.element("#stateCity-wrapper").element('.//*[text()="NCR"]').click()
    browser.element("#city").click()
    browser.element("#stateCity-wrapper").element('.//*[text()="Delhi"]').click()
    browser.element('#submit').click()




