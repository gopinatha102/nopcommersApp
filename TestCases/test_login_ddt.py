import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from time import sleep
from Utillties.readproperties import ReadConfig
from Utillties.customLogger import LogGen
from Utillties import Xlutile
import time


class Test_002_DDT_Login:


    baseUrl = ReadConfig.getApplicationURL()
    path=".//TestData//LoginData.xlsx"
    logger=LogGen.loggen()


    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("Test_002_DDt_Login")
        self.logger.info("verfying Login DDT ")
        self.driver=setup
        self.driver.get(self.baseUrl)

        self.lp=LoginPage(self.driver)
        self.rows=Xlutile.getRowcount(self.path,'Sheet1')
        print("****************************************n************:",self.rows)

        lst_status=[]    #Empty List creating
        for r in range(3,self.rows+1):
            self.user=Xlutile.readData(self.path,'Sheet1', r,1)
            self.password = Xlutile.readData(self.path, 'Sheet1', r, 2)
            self.exp = Xlutile.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(6)
            act_Title = self.driver.title
            expt_Title='Dashboard / nopCommerce administration'

            if act_Title==expt_Title:
                if self.exp=="Pass":
                    self.logger.info("******** Passed************")
                    self.lp.clickLogout()
                    lst_status.append("Pass")

                elif self.exp=="fail":
                    self.logger.info("********Failed************")
                    self.lp.clickLogout()
                    lst_status.append("fail")
            elif act_Title != expt_Title:
                if self.exp == "Pass":
                    self.logger.info("******** Failed************")
                    lst_status.append("fail")
                elif self.exp == 'fail':
                    self.logger.info("********Passed************")
                    lst_status.append("Pass")

        if 'fail' not in  lst_status:
            self.logger.info("**************Login DDT Test Case Passed********************")
            self.driver.close()
            assert True
        else:
            self.logger.info("****************Login DDT Test Case Passed******************")
            self.driver.close()
            assert False

        self.logger.info("**************End of DDT Test Case***************")
        self.logger.info("**************Completed TC_loginDDT***************")






