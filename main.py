"""Tinder bot swipe like and dislike 3 times automatically . I've not added Matching concept coz i'm not lucky 
to get a match .If you use firefox driver manually click allow location which pop up (top of the page) 
becuase this does not comes handy in developer tools.Script fb_login.py enter your email and password for logging
in Facebook"""

#Import
from selenium import webdriver
from time import sleep
from fb_login import email_id,password

#code
class Tinder():
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path="driver path")
    
    def opentinder(self):
        self.driver.get("https://tinder.com/")

    def login(self):
        sleep(5)
        fb_login = self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/div[2]")
        fb_login.click()
        #switch windows
        base_window = self.driver.window_handles[0]
        popup_window = self.driver.window_handles[1]
        # new popup window
        self.driver.switch_to.window(popup_window)
        sleep(1.2)
        fb_email = self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(email_id)
        fb_pass = self.driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
        fb_loin_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]').click()
        #Back to normal window
        self.driver.switch_to.window(base_window)
        # wait and allow location
        sleep(1.8)
        allow_location = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]').click()
        sleep(9.5)
        not_intersted_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[2]').click()
    
    def swipe_like(self):
        sleep(1)
        swipe_right = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]").click()

    def swipe_dislike(self):
        sleep(0.3)
        swipe_left = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]").click()

    def auto_swipes(self):
        quit_loop = True
        while quit_loop:
            for like_three_times in range(1,4):
                self.swipe_like()
                sleep(1)
                self.swipe_dislike()
            quit_swiping = input("press Any button to continue -- Continue ,q -- to Quit from swiping! ")
            if quit_swiping == "q":
                print("Stopped")
                quit_loop = False

#execution
tinder = Tinder()
tinder.opentinder()
tinder.login()
tinder.auto_swipes()
