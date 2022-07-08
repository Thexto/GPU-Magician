from driver_finder import get_driver
import pickle as rick
from itertools import cycle
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from re import sub
from time import sleep


class Bot(object):
    def __init__(self):
        with open(
            "storage/user_config.pickle", "rb"
        ) as handle:  # opens file containing user settings
            self.config = rick.load(handle)
        with open(
            "storage/user_websites.pickle", "rb"
        ) as handle:  # opens file containing websites
            self.websites = rick.load(handle)
        with open(
            "storage/user_data.pickle", "rb"
        ) as handle:  # opens file containing username and password
            self.user_data = rick.load(handle)
        self.debug = self.config["debug"]
        self.driver = get_driver()

    def check_availability(self):# cycle through items to purchase
        while self.config['items'] > 0:
            self.driver.implicitly_wait(3) # max wait of 3 seconds
            for url, website_data in cycle(self.websites.items()): # loops through items to purchase
                if self.running == False:
                    sleep(5)
                else:
                    try:
                        self.website, price_limit = website_data['website'] , website_data['price']# get website/price data
                        self.driver.get(url)
                        match self.website:
                            case 'Amazon':
                                try:
                                    WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.ID, "buy-now-button")))
                                    site_price = self.driver.find_element(By.CLASS_NAME, 'a-price-whole').get_attribute("innerHTML")
                                    site_price = sub('[^0-9]','', site_price)
                                    if float(site_price) <= float(price_limit): #If the Price Is Right:
                                        self.name = self.driver.find_element(By.ID, 'productTitle').get_attribute("innerHTML")
                                        self.price = site_price
                                        self.amazon_purchase()
                                except: pass       

                            case 'BestBuy':
                                try:
                                    WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button")))
                                    site_price = self.driver.find_element(By.CLASS_NAME,'priceView-hero-price').get_attribute("innerHTML")
                                    site_price = sub('[^0-9_.]','', site_price)
                                    site_price = site_price[0 : int(len(site_price) / 2)]

                                    if float(site_price) <= float(price_limit):
                                        self.name = self.driver.find_element(By.CLASS_NAME, 'heading-5').get_attribute("innerHTML")
                                        self.price = site_price
                                        self.bestbuy_purchase()
                                except: pass
                    except: pass

    def amazon_purchase(self):
        self.driver.implicitly_wait(10)  # waits a max of 10 seconds
        try:
            self.driver.find_element(
                By.ID, "buy-now-button"
            ).click()  # click the buy-now-button
        except:
            pass

        try:
            username = self.user_data["Amazon"]["username"]
            password = self.user_data["Amazon"]["password"]

            sign_in = self.driver.find_element(By.NAME, "email")
            sign_in.click()
            sign_in.send_keys("", username)

            self.driver.find_element(By.ID, "continue").click()

            sign_in = self.driver.find_element(By.NAME, "password")
            sign_in.click()
            sign_in.send_keys("", password)

            self.driver.find_element(By.ID, "signInSubmit").click()
        except:
            print(
                "Sign in failed\nDouble check sign in information\nReport if informtion is correct"
            )
        if self.driver.find_element(By.NAME, "placeYourOrder1"):
            self.debug = self.config["debug"]
            if not self.debug:
                WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.NAME, "placeYourOrder1"))
                ).click()
            else:
                print("Would have purchased")
            self.purchased_item()  # goes to purchased item directly instead of returning true
            # If the function returns false, it just ends and I don't have to do anything else. Big brain logic
        else:
            print("Could not purchase")

    def bestbuy_purchase(self):
        self.driver.implicitly_wait(20)
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart-button").click()
            self.driver.get("https://www.bestbuy.com/cart")
        except:
            pass

        try:
            username = self.user_data["BestBuy"]["username"]
            password = self.user_data["BestBuy"]["password"]
            cvv2 = self.user_data["BestBuy"]["CVV2"]

            self.driver.find_element(
                By.XPATH,
                "/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[4]/div/div/button",
            ).click()

            sign_in = self.driver.find_element(By.XPATH, '//*[@id="fld-e"]')
            type(username)
            sign_in.send_keys("", username)

            sign_in = self.driver.find_element(By.XPATH, '//*[@id="fld-p1"]')
            type(password)
            sign_in.send_keys("", password)

            self.driver.find_element(
                By.XPATH,
                "/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/div/form/div[3]/button",
            ).click()

            self.driver.get("https://www.bestbuy.com/checkout/r/fast-track")

            sign_in = self.driver.find_element(By.XPATH, '//*[@id="cvv"]')
            sign_in.click
            type(cvv2)
            sign_in.send_keys("", cvv2)
        except:
            print("Failed at Bestbuy purchase")
        if self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/div/div[4]/div[3]/div/div[2]/button",
        ):
            self.debug = self.config["debug"]
            if not self.debug:
                self.driver.find_element(
                    By.XPATH,
                    "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/div/div[4]/div[3]/div/div[2]/button",
                ).click()
            else:
                print("Would have purchased")
            self.purchased_item()  # goes to purchased item directly instead of returning true
            # If the function returns false, it just ends and I don't have to do anything else. Big brain logic
        else:
            print("Could not purchase")

    def purchased_item(self):

        date = datetime.now()

        try:  # try to open purchases
            with open("storage/user_purchases.pickle", "rb") as handle:
                purchases = rick.load(handle)
        except:  # make an empty variable to store purchases in
            purchases = []
        if len(self.name) >= 50:  # Limit name length
            self.name = self.name[0:49]
        self.name = self.name.strip()

        # append dictionary with purchase info to list containing all purchase info
        purchases.append(
            {
                "name": self.name,
                "website": self.website,
                "price": self.price,
                "date": date.strftime("%m/%d/%y"),
                "time": date.strftime("%H:%M:%S"),
            }
        )

        with open("storage/user_purchases.pickle", "wb") as handle:
            rick.dump(purchases, handle, protocol=rick.HIGHEST_PROTOCOL)
        self.config["items"] = self.config["items"] - 1
        with open("storage/user_config.pickle", "wb") as handle:
            rick.dump(self.config, handle, protocol=rick.HIGHEST_PROTOCOL)

    def stop_running(self):
        self.running = False

    def start_running(self):
        self.running = True


if __name__ == "__main__":
    Bot().check_availability()
