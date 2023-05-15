from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# write the automation scripts for the following pages:
# Login Page & Home Page 
# Cover all the possible functional testing scenarios.
# Note:- Any value of username/password is valid to log in the application
class Loginpage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.XPATH, "//input[@id = 'username']")
        self.password = (By.XPATH, "//input[@id = 'password']")
        self.login = (By.XPATH, "//button[@id ='log-in']")
        self.amount_header =(By.XPATH, '//th[@id = "amount"]')
        self.amount = (By.XPATH, '//table[@id = "transactionsTable"]')

    def _username(self,username):
        self.driver.find_element(*self.username).send_keys(username)
        sleep(1)
    def _password(self,password):
        self.driver.find_element(*self.password).send_keys(password)
        sleep(1)
    def _login(self):
        self.driver.find_element(*self.login).click()
        sleep(1)
    def _amount_header(self):
        self.driver.find_element(*self.amount_header).click()
        sleep(3)
    def _amount(self):
        self.driver.find_element(*self.amount).click()
        sleep(2)
    
class Testlogin:
    def login_method(self):
        self.driver = webdriver.Chrome("G:\@PYTHON@\Selenium\Selenium pratice\chromedriver")
        self.driver.get("https://sakshingp.github.io/assignment/login.html")

    def input(self):
        login_page = Loginpage(self.driver)
        login_page._username("testuse")
        login_page._password("testpass")
        login_page._login()
        login_page._amount_header()
        login_page._amount()
        sleep(4)

if __name__ == "__main__":
    input = Testlogin()
    input.login_method()
    input.input()

# Home Page
# After successful login into the application, click the AMOUNT header in the transaction table and
# check the values are sorted.
_sorted = sorted('//span[@class = "text-success"] to //span[@class = "text-danger"]')
if input == _sorted:
    print("Values are sorted in descending order")
else:
    print("Values are sorted in ascending order")
sleep(1)






