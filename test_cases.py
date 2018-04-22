import unittest
from selenium import webdriver
class SearchEmail(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Chrome()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        inst.driver.get('http://www.gmail.com')
        inst.driver.title

    def test_login_and_search_email(self):
        driver.find_element_by_class_name("whs0nd zHQkBf").send_keys("some_gmail_account")
        driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
        driver.implicitly_wait(30)
        driver.find_element_by_name("password").send_keys("some_password")
        driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
        driver.find_element_by_class_name('J-Ke n0').click()
        first_list = self.driver.find_elements_by_class_name('r')
        self.assertTrue(len(first_list) > 0)

    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()
