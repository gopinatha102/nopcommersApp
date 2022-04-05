#main branch
import pytest
# from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.AddcustomerPage import Addcustomer
from PageObjects.SearchcustomerPage import Searchcustomer
# from time import sleep
from Utillties.readproperties import ReadConfig
from Utillties.customLogger import LogGen
# from Utillties import Xlutile
import time
# import unittest


class Test_SearchcustomerByemail_004:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getuseremail()
    password = ReadConfig.getpassword()

    logger = LogGen.loggen()

    # logger.info("*********************logger****************")

    @pytest.mark.regression
    def test_searchcustomerByemail(self, setup):
        self.logger.info("***********************searchCustomerByEmail*****************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("*****************Login Successfully*******************")

        self.logger.info("*****************Starting Search CustomerByEmail***************")

        self.addcust = Addcustomer(self.driver)
        self.addcust.ClickonCustomersMenu()
        self.addcust.ClickOnSubCustomerMenu()

        self.logger.info("******************Searching Customer By EmailID*********************")
        # ***************************Here using Search Customer By Email********************
        searchcust = Searchcustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.ClickSearch()
        time.sleep(3)
        status = searchcust.SearchCustomerByEmail("victoria_victoria@nopCommerce.com")
        print(status)
        assert True == status
        self.logger.info("*********Test_Search customer By email_004 Finished*****************")
        self.driver.close()
