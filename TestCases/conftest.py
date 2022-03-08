from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'Chrome':

        driver = webdriver.Chrome(
            executable_path="C:\\Users\\DELL\\PycharmProjects\\DemoProject\\Drivers\\chromedriver.exe")
        # driver=webdriver.Chrome()
        print("Launching Chrome driver")

    elif browser == 'firefox':
        driver = webdriver.Firefox(
            executable_path=r"C:\Users\DELL\PycharmProjects\driver\geckodriver-v0.29.1-win64\geckodriver")
        print("Launching Firefox driver ")

    else:
        driver = webdriver.Ie(executable_path=r"C:\Users\PAVAN KUMARA\PycharmProjects\driver")
        print("Launching Inetenet Exploer ")

    return driver

def pytest_addoption(parser):  # This will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup Methode
    return request.config.getoption("--browser")


######################### Pytest HTML Report##################################
# It is Hook for adding Environment info to HTML Report

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Gopinatha'


# It is Hook for Delete /modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
