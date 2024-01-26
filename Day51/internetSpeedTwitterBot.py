from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

PROMISED_DOWN = 100
PROMISED_UP = 10
TWITTER_EMAIL = "email"
TWITTER_PASSWORD = "password"


class InternetSpeedTwitterBot:

    def __init__(self):
        self.real_down = None
        self.real_up = None
        self.driver = webdriver.Chrome()
        self.PROMISED_DOWN = 100
        self.PROMISED_UP = 10
        self.SPEED_TEST_URL = "https://www.speedtest.net/"

    def get_internet_speed(self):
        self.driver.get(self.SPEED_TEST_URL)
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        sleep(40)
        self.real_down = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        self.real_up = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)

    def tweet_at_provider(self, email, password):
        pass


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD)
