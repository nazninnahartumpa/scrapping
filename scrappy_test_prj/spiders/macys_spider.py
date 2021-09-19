import scrapy
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import urljoin
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def configure_driver():
    # Add additional Options to the webdriver
    chrome_options = Options()
    # add the argument and make the browser Headless.
    chrome_options.add_argument("--headless")
    # Instantiate the Webdriver: Mention the executable path of the webdriver you have downloaded
    # For linux/Mac
    # driver = webdriver.Chrome(options = chrome_options)
    # For windows
    # path=r"F:\\Coding\scrapy\scraping_selenium\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=r"E:\\test_scrapy\scrappy_test_prj\scrappy_test_prj\\chromedriver.exe", options = chrome_options)
    return driver


def get_driver():
    # initialize options
    PROXY = "192.168.1.38"
    options = webdriver.ChromeOptions()
    # pass in headless argument to options
    options.add_argument('--headless')
    # options.add_argument('--proxy-server=%s' % PROXY)
    # initialize driver
    # driver = webdriver.Remote(
    #             command_executor='http://192.168.1.40:4445/wd/hub',
    #             desired_capabilities=DesiredCapabilities.CHROME
    # )

    driver = webdriver.Remote(
        command_executor='http://192.168.1.35:4446/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME
    )
    return driver


class MacysSpider(scrapy.Spider):
    name = "macys"

    allowed_domains = ['macys.com']

    start_urls = ['https://www.macys.com/shop/mens-clothing/mens-jackets-coats?id=3763&cm_sp=c2_1111INT_catsplash_men-_-row1-_-image_coats-%26-jackets&edge=hybrid']

    def __init__(self):
        self.driver = get_driver()
       

    def parse(self, response):
        # Step 1: Go to pluralsight.com, category section with selected search keyword
        url = response.url
        self.driver.get(url)

        link_tag_list = self.driver.find_elements_by_xpath('//div[@class="productDescription"]//a')
        print('link_tag_list', link_tag_list)
        url_list = [link.get_attribute("href") for link in link_tag_list[:4]]
        print('url_list', url_list)


        for single_url in url_list:
            self.driver.get(single_url)
            time.sleep(1)
            # print('single_url', single_url)

            # scrape title 
            # title = self.driver.find_element_by_xpath('//meta[@name="keywords"]//@content').text
            # print('title', title)

            # # scrape brand 
            # brand = self.driver.find_element_by_xpath('//div[@data-auto="product-title"]//h4//a').text
            # print('brand', brand)

            # scrape descriptions
            descriptions = self.driver.find_element_by_xpath('//div[@data-el="product-details"]//ul').text
            print('descriptions', descriptions)

            # # scrape price 
            # price = self.driver.find_element_by_xpath('//div[@class="price"]').text
            # print('price', price)

            # # scrape image
            # image_list = self.driver.find_elements_by_xpath('//div[@class="scroller-wrp"]//ul//li//picture//img')
            # image = [link.get_attribute("src") for link in image_list]
            # print('image', image)

            # # scrape rating_count
            # rating_count = self.driver.find_element_by_xpath('//*[@data-type="reviews"]').text
            # print('rating_count', rating_count)

            # scrape review
            # review_list = self.driver.find_elements_by_xpath('//*[@itemprop="reviewBody"]//div')
            # review = [review.text for review in review_list]

            #scrape review
            # try:
            #     element = self.driver.find_element_by_xpath('//div[@data-test-id="reviewContainer"]//div[9]//a//span')
            #     self.driver.execute_script("arguments[0].click();", element)
            #     time.sleep(1)
            #     review_list = self.driver.find_elements_by_xpath('//*[@itemprop="reviewBody"]//div')
            #     review = [review.text for review in review_list]
            # except:
            #     pass


            
            
            
            
            # print('store_product_id', store_product_id)
            
            # print('rating', rating)
            # print('review', review)
            

  
    


       

