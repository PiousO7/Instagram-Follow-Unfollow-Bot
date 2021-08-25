from selenium import webdriver
import os
from dotenv import load_dotenv
import time

load_dotenv()


class FollowBot:
    def __init__(self):

        self.chrome_driver_path = "E:\Softwares\Chrome Driver (python prject)/chromedriver.exe"

        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)

        self.driver.get("https://www.instagram.com/accounts/login/?next=%2Flogin%2F&source=desktop_nav")

        time.sleep(3)
        self.username = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        self.username.send_keys(os.getenv("USER_ID"))

        self.password_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        self.password_input.send_keys(os.getenv("PASSWORD"))

        self.login_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
        self.login_button.click()

        time.sleep(3)
        # EXAMPLE INSTAGRAM ACCOUNT TO FOLLOW
        self.driver.get("https://www.instagram.com/chefsteps/")

        time.sleep(3)
        self.followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        self.followers.click()
        time.sleep(3)

        time.sleep(2)
        keep_following = True
        while keep_following:
            self.follow_button = self.driver.find_elements_by_css_selector(".sqdOP.L3NKy.y3zKF")
            for i in self.follow_button:
                i.click()
            time.sleep(2)
            self.scr1 = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", self.scr1)
            time.sleep(2)
