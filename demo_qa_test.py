from pathlib import Path

from selene import be, browser, have
from selenium.webdriver.chrome.options import Options


def test_demo_qa():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    browser.config.driver_options = options

    browser.open("https://demoqa.com/automation-practice-form")

    browser.element("#RightSide_Advertisement").execute_script("element.remove()")
    browser.element("footer").execute_script("element.remove()")
    browser.element("#fixedban").execute_script("element.remove()")

    browser.element("#firstName").type("Aleksei")
    browser.element("#lastName").type("Vasilev")
    browser.element("#userEmail").type("kardahur@gmail.com")
    browser.element("#gender-radio-1").element("..").click()
    browser.element("#userNumber").type("3579432695")
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").element(
        'option[value="7"]'
    ).click()
    browser.element(".react-datepicker__year-select").element(
        'option[value="1989"]'
    ).click()
    browser.element(".react-datepicker__day.react-datepicker__day--009").click()
    browser.element("#subjectsInput").type("Computer").press_enter()
    browser.element("#hobbies-checkbox-1").element("..").click()
    browser.element("#uploadPicture").set_value(str(Path("img/1.jpg").resolve()))
    browser.element("#currentAddress").type("Another str. 11")
    browser.element("#state").click()
    browser.element("#stateCity-wrapper").element('.//*[text()="NCR"]').click()
    browser.element("#city").click()
    browser.element("#stateCity-wrapper").element('.//*[text()="Delhi"]').click()
    browser.element("#submit").click()

    # Asserts

    browser.element("#example-modal-sizes-title-lg").should(be.visible).should(
        have.text("Thanks for submitting the form")
    )
    browser.element(".table-responsive").element(
        './/*[text()="Student Name"]/following-sibling::*[1]'
    ).should(have.text("Aleksei Vasilev"))
    browser.element(".table-responsive").element(
        './/*[text()="Student Email"]/following-sibling::*[1]'
    ).should(have.text("kardahur@gmail.com"))
    browser.element(".table-responsive").element(
        './/*[text()="Gender"]/following-sibling::*[1]'
    ).should(have.text("Male"))
    browser.element(".table-responsive").element(
        './/*[text()="Mobile"]/following-sibling::*[1]'
    ).should(have.text("3579432695"))
    browser.element(".table-responsive").element(
        './/*[text()="Date of Birth"]/following-sibling::*[1]'
    ).should(have.text("09 August,1989"))
    browser.element(".table-responsive").element(
        './/*[text()="Subjects"]/following-sibling::*[1]'
    ).should(have.text("Computer Science"))
    browser.element(".table-responsive").element(
        './/*[text()="Hobbies"]/following-sibling::*[1]'
    ).should(have.text("Sports"))
    browser.element(".table-responsive").element(
        './/*[text()="Picture"]/following-sibling::*[1]'
    ).should(have.text("1.jpg"))
    browser.element(".table-responsive").element(
        './/*[text()="Address"]/following-sibling::*[1]'
    ).should(have.text("Another str. 11"))
    browser.element(".table-responsive").element(
        './/*[text()="State and City"]/following-sibling::*[1]'
    ).should(have.text("NCR Delhi"))
