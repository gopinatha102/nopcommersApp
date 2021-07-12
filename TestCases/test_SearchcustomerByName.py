import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.AddcustomerPage import Addcustomer
from PageObjects.SearchcustomerPage import Searchcustomer
from time import sleep
from Utillties.readproperties import ReadConfig
from Utillties.customLogger import LogGen
from Utillties import Xlutile
import time


class Test_SearchcustomerByemail_004:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getuseremail()
    password = ReadConfig.getpassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchcustomerByName(self, setup):
        self.logger.info("***********************searchCustomerByName*****************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("*****************Login Sucessful*******************")

        self.logger.info("*****************Starting Search CustomerByName*************")

        self.addcust = Addcustomer(self.driver)
        self.addcust.ClickonCustomersMenu()
        self.addcust.ClickOnSubCustomerMenu()


        # ***************************Here Using Search Customer By Name********************************
        self.logger.info("******************Searching Customer By Name*********************")
        searchcust = Searchcustomer(self.driver)
        searchcust.setFirstname("Victoria")
        searchcust.setLastname("Terces")
        searchcust.ClickSearch()
        time.sleep(5)
        status =searchcust.SearchCustomerByname("Victoria Terces")
        assert True==status
        self.logger.info("*********Test_SearchcustomerByname_005 Finished*****************")
        self.driver.close()
