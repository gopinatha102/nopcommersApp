import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.AddcustomerPage import Addcustomer
from time import sleep
from Utillties.readproperties import ReadConfig
from Utillties.customLogger import LogGen
import string
import random


class Test_003_Addcustomer:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getuseremail()
    password = ReadConfig.getpassword()

    logger = LogGen.loggen()


    @pytest.mark.sanity
    def test_Addcustomer(self, setup):
        self.logger.info("*******************test_003_Addcustomer********************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*******************Login  sucessful*****************")

        self.logger.info("*********************Started Add Customer Test**************")

        self.addcust = Addcustomer(self.driver)
        self.addcust.ClickonCustomersMenu()
        self.addcust.ClickOnSubCustomerMenu()
        self.addcust.ClickOnAddNew()

        self.logger.info("************Provied Customer Infomation***********")

        self.email = random_generator() +"@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setpassword("test123")
        self.addcust.setFirstName("Gopi")
        self.addcust.setLastName("natha")
        self.addcust.setGender("Male")
        self.addcust.setDob("7/05/2015")
        self.addcust.setCompanyName("GPS")
        self.addcust.setTaxExempt()
        self.addcust.setNewsLetter("Test store 2")
        self.addcust.setTaxExempt()
        self.addcust.setMangerVenoder("Vendor 1")
        self.addcust.setAdimeCommint("this is testing........")
        self.addcust.ClickonSave()

        self.logger.info("*************Save The Customer Information*********")

        self.logger.info("******Add Customer Validation Stated*******")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if "The new customer has been added successfully." in self.msg:
            assert True
            self.logger.info("**********Add custome Test case paased*******")
        else:
            self.driver.save_screenshot(
                r"C:\Users\PAVAN KUMARA\PycharmProjects\nopcommerceApp\Screenshots\screenshot3" + "AddnewCustomer.png")
            self.logger.info("**********Add custome Test case Failed*******")
            assert False

        self.driver.close()
        self.logger.info("**********Ending Add custome**************")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
