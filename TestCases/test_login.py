import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from time import sleep
from Utillties.readproperties import ReadConfig
from Utillties.customLogger import LogGen


class Test_001_Login:


    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getuseremail()
    password = ReadConfig.getpassword()

    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("test_homePageTitle")
        self.logger.info("verfying home page title ")
        self.driver=setup
        self.driver.get(self.baseUrl)
        act_Title=self.driver.title
        if act_Title=='Your store. Login':
            assert True
            self.driver.close()
            self.logger.info("Home page title pass")

        else:
            self.driver.save_screenshot(
                r"C:\Users\DELL\PycharmProjects\nopcommerceApp\Screenshots\screenshot1" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("home page title failed")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("login test ")
        self.logger.info("verfiy login Test ")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title

        if act_title =='Dashboard / nopCommerce administration':
            assert True
            self.logger.info("login test is passed")
            self.driver.close()

        else:
            self.driver.save_screenshot(
                r"C:\Users\DELL\PycharmProjects\nopcommerceApp\Screenshots\screenshot2" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("test case Failed ")
            assert False

