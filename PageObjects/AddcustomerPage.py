import email
import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver


class Addcustomer:
    # Add Customer Page
    lnkAddcustomer_Main_Menu_Xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p"
    lnkAddcustomer_Sub_Menu_Xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    btnAddNewc_Xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a/i"
    txtEmail_Xpath = "//*[@id='Email']"
    txtpassword_Xpath = "//*[@id='Password']"
    txtFirstName_Xpath = "//*[@id='FirstName']"
    txtLastName_Xpath = "//*[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDob_Xpath = "//*[@id='DateOfBirth']"
    txtCompanyName_Xpath = "//*[@id='Company']"
    clickTaxEXempt_Xpath = "//*[@id='IsTaxExempt']"
    txtcustomerRole_Xpath = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div/input"
    drpmgrofVendor_Xpath = "//*[@id='VendorId']"
    clickActive_Xpath = "//*[@id='Active']"
    txtAdminComment_Xpath = "//*[@id='AdminComment']"
    lnkcustomerRole_Xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[2]"
    lstitemsAdministrators_Xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[1]"
    lstitemsformModerator_Xpath = "//*[@id='fcc83820-2c7c-4a7c-870c-02779c978593']"
    lstitemsGueste_Xpath = "//*[@id='fcc83820-2c7c-4a7c-870c-02779c978593']"
    lstitemsRegister_Xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[4]"
    lstitemsVendor_Xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[5]"
    clickMange_NOVendors_Xpath = "//*[@id='VendorId']/option[1]_"
    clickMange_Vendors1_Xpath = "//*[@id='VendorId']/option[2]"
    clickMange_Vendors2_Xpath = "//*[@id='VendorId']/option[3]"
    btnSave_Xpath = "/html/body/div[3]/div[1]/form/div[1]/div/button[1]"
    Newsletter_Xpath = "//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div"
    clicknewsletteryourstroe_Xpath="//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[1]"
    clicknewsletteteststroe2_Xpath="//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[2]"

    def __init__(self, driver):
        self.driver = driver

    def ClickonCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnkAddcustomer_Main_Menu_Xpath).click()

    def ClickOnSubCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkAddcustomer_Sub_Menu_Xpath).click()

    def ClickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btnAddNewc_Xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_Xpath).send_keys(email)

    def setpassword(self, password):
        self.driver.find_element_by_xpath(self.txtpassword_Xpath).send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element_by_xpath(self.txtFirstName_Xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_xpath(self.txtLastName_Xpath).send_keys(lname)

    def setDob(self, Dob):
        self.driver.find_element_by_xpath(self.txtDob_Xpath).send_keys(Dob)

    def setCompanyName(self, CompanyName):
        self.driver.find_element_by_xpath(self.txtCompanyName_Xpath).send_keys(CompanyName)

    def setAdimeCommint(self, Admincommints):
        self.driver.find_element_by_xpath(self.txtAdminComment_Xpath).send_keys(Admincommints)

    def ClickonSave(self):
        self.driver.find_element_by_xpath(self.btnSave_Xpath).click()

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.txtcustomerRole_Xpath).click()
        time.sleep(3)

        if role == "Register":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemsRegister_Xpath)

        elif role == "Administrators":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemsAdministrators_Xpath)
        elif role == "Gueste":
            # Here user can be Registed or Gueste ,only one
            time.sleep(3)
            self.driver.find_element_by_xpath("/*[@id='SelectedCustomerRoleIds_listbox']/li[4]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemsGueste_Xpath)

        elif role == "Register":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemsRegister_Xpath)

        elif role == 'Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemsVendor_Xpath)

        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemsGueste_Xpath)

        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setMangerVenoder(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drpmgrofVendor_Xpath))
        drp.select_by_visible_text(value)

    def setNewsLetter(self, value, gender=None):
        #drp = Select(self.driver.find_element_by_xpath(self.Newsletter_Xpath))
        #drp.select_by_visible_text(value)
        self.driver.find_element_by_xpath(self.Newsletter_Xpath).click()
        if value == "Test store 2":
            self.driver.find_element_by_xpath(self.clicknewsletteteststroe2_Xpath).click()
        elif gender == "Your store name":
            self.driver.find_element_by_xpath(self.clicknewsletteryourstroe_Xpath).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setGender(self, gender):

        if gender == "Male":
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender == "Female":
            self.driver.find_element_by_id(self.rdFemaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setTaxExempt(self):
        self.driver.find_element_by_xpath(self.clickTaxEXempt_Xpath).click
