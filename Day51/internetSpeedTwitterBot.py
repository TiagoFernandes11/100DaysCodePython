from selenium import webdriver
from selenium.webdriver import Keys
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
        sleep(45)
        self.real_down = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        self.real_up = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)

    def tweet_at_provider(self, email, password):
        self.login_at_twitter(email, password)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]'
                                           '/div/div/div/div').send_keys(f"Should be: {PROMISED_UP}Mbs upload and {PROMISED_DOWN}Mbs download."
                                                                         f"\nAnd it is {self.real_up}Mbs upload and {self.real_down}Mbs download.")
        sleep(2)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]'
                                 '/div/div/div/div').send_keys(Keys.ENTER)

        pass

    def login_at_twitter(self, email, password):
        self.driver.get("https://twitter.com/login")
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(email)
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(password)
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD)
