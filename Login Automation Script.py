from selenium import webdriver
from time import sleep

path = "G:\@PYTHON@\Selenium\Selenium pratice\chromedriver"
url = "https://sakshingp.github.io/assignment/login.html"
driver = webdriver.Chrome(path)
sleep(2)
driver.get(url)
sleep(2)
# Login Page
# Cover all the possible functional testing scenarios.
#Enter Value in Username Text field
#Enter all the inputs of username and password  as per test case 
driver.find_element_by_xpath("//input[@id = 'username']").click()
sleep(1)
driver.find_element_by_xpath('//input[@type = "text"]').send_keys("PRADEEP")
sleep(1)
#Enter Value in Password Text field
driver.find_element_by_xpath('//input[@id = "password"]').click()
sleep(2)
driver.find_element_by_xpath('//input[@placeholder = "Enter your password"]').send_keys("AbcdE1234oj2kjk")
sleep(2)
#Click on Remember me Check box
Checkbox = driver.find_element_by_xpath('//input[@class = "form-check-input"]').click()
sleep(2)
#Click on Login botton
log_in = driver.find_element_by_xpath('//button[@id = "log-in"]').click()
# Home Page
# After successful login into the application, click the AMOUNT header in the transaction table and
# check the values are sorted.
amount_header= driver.find_element_by_xpath('//th[@id = "amount"]').click()
sleep(2)
amount = driver.find_element_by_xpath('//table[@id = "transactionsTable"]')
_sorted = sorted('//span[@class = "text-success"] to //span[@class = "text-danger"]')
if amount == _sorted:
    print("Values are sorted in descending order")
else:
    print("Values are sorted in ascending orer")
sleep(2)
#print the Values
_amount = driver.find_element_by_xpath('//table[@id = "transactionsTable"]').text
print(f"The values of Amount Header is {_amount}")
driver.quit()
sleep(3)
