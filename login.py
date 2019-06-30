from  selenium import webdriver
from selenium.webdriver.common.by import By
import yaml
import time
import unittest

# links = driver.find_elements(*locator_result)
# for link in links:
#     print(link.text)
# driver.quit()
# yaml.lo
# /html/body/div[4]/div[2]/form/ul/li[5]/input[2]
class  TestBaiDu(unittest.TestCase):
    url = 'https://www.baidu.com/'
    locator_kw = (By.CSS_SELECTOR, '#kw')
    locator_su = (By.CSS_SELECTOR, '#su')
    locator_result = (By.XPATH,'//div[contains(@class,"result")]/h3/a')
    link = '深蓝'
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
    def test_search_0(self):
            # self.driver.find_element(*self.locator_new).click()
        self.driver.find_element(*self.locator_kw).send_keys("深蓝")
        self.driver.find_element(*self.locator_su).click()
        time.sleep(3)
        result_0 = self.driver.title
        # print(self.driver.title)
        self.assertEqual('深蓝',result_0,msg='PASS')
        self.driver.quit()

    def test_search_1(self):
        self.driver.find_element(*self.locator_kw).send_keys("美国")
        self.driver.find_element(*self.locator_su).click()
        time.sleep(3)
        result_1 = self.driver.title
        self.assertIn('美国_百度搜索',result_1,'Pass')
        time.sleep(3)
        self.driver.quit()

    #     self.driver.quit()
if __name__ == '__main__':
    unittest.main()



