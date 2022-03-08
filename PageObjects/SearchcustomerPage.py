from selenium import webdriver
class Searchcustomer:
    txtEmail_id="SearchEmail"
    txtFirstname_id="SearchFirstName"
    txtlastName_id="SearchLastName"
    txtCompanyName_id="SearchCompany"
    btnSearach_id="search-customers"

    tblSearchResulte_xpath="//*[@id='customers-grid']"
    table_xpath= "//table[@id='customers-grid']"
    tableRows_xpath="//table[@id='customers-grid']/tbody/tr"
    tableColumns_xpath="//table[@id='customers-grid']/tbody/tr/td"



    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element_by_id(self.txtEmail_id).clear()
        self.driver.find_element_by_id(self.txtEmail_id).send_keys(email)

    def setFirstname(self,fname):
        self.driver.find_element_by_id(self. txtFirstname_id).clear()
        self.driver.find_element_by_id(self. txtFirstname_id).send_keys(fname)

    def setLastname(self, lname):
        self.driver.find_element_by_id(self.txtlastName_id).clear()
        self.driver.find_element_by_id(self.txtlastName_id).send_keys(lname)

    def ClickSearch(self):
        self.driver.find_element_by_id(self.btnSearach_id).click()

    def getNoofRows(self):
        Rows=len(self.driver.find_elements_by_xpath(self.tableRows_xpath))
        print("Number of Rows :",Rows)
        return Rows


    def getNoofColumns(self):
        Columes=len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))
        print("Number of columes:",Columes)
        return

    def SearchCustomerByEmail(self, email):
        flage =False
        for r in range(1,self.getNoofRows()+1):
            table=self.driver.find_element_by_xpath(self.table_xpath)
            emailid=table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text

            if emailid==email:
                flage=True
                break
        return flage

    def SearchCustomerByname(self,Name):
        flage=False
        for r in range(1,self.getNoofRows()+1):
            table=self.driver.find_element_by_xpath(self.table_xpath)
            name=table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            print("**********************name*****************",name)
            print("************************Name**************",Name)

            if name == Name:
                return True
                break
        return flage

