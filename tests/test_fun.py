import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

from app import create_app,db
import time
MAX_WAIT = 10
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        self.browser.quit()
    
    def test_home(self):
        self.browser.get('http://127.0.0.1:5000/')
        self.assertIn('Black', self.browser.title) 
    

    def test_post(self):
        #register
        self.browser.get('http://127.0.0.1:5000/auth/register')
        self.browser.find_element_by_id('email').send_keys('admin@ad.com')
        self.browser.find_element_by_id('username').send_keys('admin')
        self.browser.find_element_by_id('password').send_keys('admin')
        self.browser.find_element_by_id('password2').send_keys('admin')
        self.browser.find_element_by_id('submit').click()
        
        #login
        self.browser.find_element_by_id('email').send_keys('admin@ad.com')
        self.browser.find_element_by_id('password').send_keys('admin')
        self.browser.find_element_by_id('submit').click()

        #create records
        for i in range(0,60):
            self.browser.find_element_by_id('new').click()
            self.browser.find_element_by_id('title').send_keys('TEST TEST')
            self.browser.find_element_by_id('text').send_keys('TESTTESTESTSTES')
            self.browser.find_element_by_id('submit').click()
        
        time.sleep(3)
        self.browser.find_element_by_id('nexts').click()
        time.sleep(3)
        self.browser.find_element_by_id('notnext').click()
        time.sleep(3)