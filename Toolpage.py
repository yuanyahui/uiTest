from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class Toolpage():
    def __init__(self):
        self.driver = webdriver.Chrome()
    '''定位方式'''

    '''id定位'''
    def byid(self,id):
        ID = (By.id)
        WebDriverWait(self.driver, 30, 0.1).until(EC.presence_of_all_elements_located(ID))
        return self.driver.find_element_by_id()


