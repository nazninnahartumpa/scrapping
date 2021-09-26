import scrapy
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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
    driver = webdriver.Chrome(executable_path=r"D:\\scraping\\scrapping\\chromedriver.exe", options = chrome_options)
    return driver


class MedexSpider(scrapy.Spider):
    name = "medex"

    allowed_domains = ['medex.com.bd']

    # start_urls = ['https://medex.com.bd/brands']

    def __init__(self):
        self.driver = configure_driver()
       

    def parse(self, response):
        # Step 1: Go to pluralsight.com, category section with selected search keyword
        # url = response.url
        # self.driver.get(url)

        for i in range(1, 6):
            url = f"https://medex.com.bd/brands?page={i}"
            self.driver.get(url)

            product_link_list = self.driver.find_elements_by_xpath('//*[@id="ms-block"]/section/div/div[2]/div/a')
            url_list = [link.get_attribute("href") for link in product_link_list]
            print('url_list', url_list)

        # scrape read more
        # try:
        #     element = self.driver.find_element_by_xpath('//a[@aria-label="Next »"]')
        #     self.driver.execute_script("arguments[0].click();", element)
        #     print('element', element)
        #     time.sleep(5)
        #     if element:
        #         time.sleep(5)
        #         try:
        #             product_link_list = self.driver.find_elements_by_xpath('//*[@id="ms-block"]/section/div/div[2]/div/a')
        #             url_list = [link.get_attribute("href") for link in product_link_list]
        #             print('url_list', url_list)
        #         except:
        #             pass
        #     else:
        #         product_link_list = self.driver.find_elements_by_xpath('//*[@id="ms-block"]/section/div/div[2]/div/a')
        #         url_list = [link.get_attribute("href") for link in product_link_list]
        #         print('else url_list', url_list)

        #     # description = self.driver.find_element_by_xpath('//*[@id="product-detail-modal"]//div[@class="pi-pdpmainbody"]').text
        # except NoSuchElementException:
        #     pass

        # product_link_list = self.driver.find_elements_by_xpath('//*[@id="ms-block"]/section/div/div[2]/div/a')
        # url_list = [link.get_attribute("href") for link in product_link_list]
        # print('url_list', url_list)
        
        # for single_url in url_list:
        #     self.driver.get(single_url)
        #     time.sleep(1)

        #     # scrape drug name
        #     Name = self.driver.find_element_by_xpath('//h1/span[2]').text
        #     print('Name', Name)

        #     # scrape generic name
        #     Generic_Name = self.driver.find_element_by_xpath('//*[@title="Generic Name"]//a').text
        #     print('Generic Name', Generic_Name)

        #     # scrape Strength
        #     Strength = self.driver.find_element_by_xpath('//*[@title="Strength"]').text
        #     print('Strength', Strength)

        #     # scrape Dosage Form
        #     Dosage_Form = self.driver.find_element_by_xpath('//*[@title="Dosage Form"]').text
        #     print('Dosage_Form', Dosage_Form)

        #     # scrape price
        #     Price = self.driver.find_element_by_xpath('//*[@class="package-container"]').text
        #     print('Price', Price)

        #     # # scrape Manufactured by
        #     # Pharmacy = self.driver.find_element_by_xpath('//*[@title="Manufactured by"]//a').text
        #     # print('Pharmacy', Pharmacy)

        #     # scrape Manufactured by
        #     Pharmacy  = self.driver.find_element_by_xpath('//*[@title="Manufactured by"]//a').text
        #     print('Pharmacy', Pharmacy)

        #     # scrape Indications
        #     Indications  = self.driver.find_element_by_xpath('//*[@id="indications"]/following-sibling::div').text
        #     print('Indications', Indications)

        #     # scrape Description
        #     try:
        #         Description  = self.driver.find_element_by_xpath('//*[@id="description"]//following-sibling::div').text
        #         print('Description', Description)
        #     except:
        #         Description = ''

        #     # scrape Pharmacology
        #     Pharmacology  = self.driver.find_element_by_xpath('//*[@id="mode_of_action"]/following-sibling::div').text
        #     print('Pharmacology', Pharmacology)


        #     # scrape Dosage & Administration
        #     Dosage_Administration  = self.driver.find_element_by_xpath('//*[@id="dosage"]/following-sibling::div').text
        #     print('Dosage_Administration', Dosage_Administration)

        #     # scrape Interaction
        #     Interaction  = self.driver.find_element_by_xpath('//*[@id="interaction"]/following-sibling::div').text
        #     print('Interaction', Interaction)

        #     # scrape Contraindications
        #     Contraindications  = self.driver.find_element_by_xpath('//*[@id="contraindications"]/following-sibling::div').text
        #     print('Contraindications', Contraindications)

        #     # scrape Side_Effects
        #     Side_Effects  = self.driver.find_element_by_xpath('//*[@id="side_effects"]/following-sibling::div').text
        #     print('Side_Effects', Side_Effects)

        #     # scrape Pregnancy_Lactation
        #     Pregnancy_Lactation  = self.driver.find_element_by_xpath('//*[@id="pregnancy_cat"]/following-sibling::div').text
        #     print('Pregnancy_Lactation', Pregnancy_Lactation)

        #     # scrape Precautions_Warnings
        #     Precautions_Warnings  = self.driver.find_element_by_xpath('//*[@id="precautions"]/following-sibling::div').text
        #     print('Precautions_Warnings', Precautions_Warnings)

        #     # scrape Therapeutic_Class
        #     Therapeutic_Class  = self.driver.find_element_by_xpath('//*[@id="drug_classes"]/following-sibling::div').text
        #     print('Therapeutic_Class', Therapeutic_Class)

        #     # scrape Storage_Conditions
        #     Storage_Conditions  = self.driver.find_element_by_xpath('//*[@id="storage_conditions"]/following-sibling::div').text
        #     print('Storage_Conditions', Storage_Conditions)


            

            # # scrape price
            # price = self.driver.find_element_by_xpath('//*[@class="product-price__wrapper"]//div').text

            # # scrape image
            # image_list = self.driver.find_elements_by_xpath('//*[@id="ColorwayDiv"]//img')
            # image = [link.get_attribute("src") for link in image_list]

            # # scrape rating count
            # # rating_count_list = self.driver.find_elements_by_xpath('//*[@id="RightRail"]//button').get_attribute('aria-controls')
            # # rating_count = [rating_count.text for rating_count in rating_count_list]

            # # scrape review
            # try:
            #     element = self.driver.find_element_by_xpath('//*[@id="RightRail"]//button[@aria-controls="accordion-panel-3"]//div//h3')
            #     self.driver.execute_script("arguments[0].click();", element)
            #     time.sleep(1)
            #     review_list = self.driver.find_elements_by_xpath('//*[@id="accordion-panel-3"]//div//div')
            #     review = [review.text for review in review_list]
            #     # print(rating)
            # except NoSuchElementException:
            #     pass

            # # ratings = self.driver.find_elements_by_xpath('//div[@id="accordion-panel-3"]//div[@class="product-review mb10-sm"]//p[@class="d-sm-ib pl4-sm"]')[0]
            # # ratings = [rating.text for rating in rating_list]

            # # sku_list = self.driver.find_elements_by_xpath('//*[contains(text(), "SKU")]')
            # # sku_number = [sku.text for sku in sku_list]
            # # review_list = self.driver.find_elements_by_xpath('//*[@itemprop="reviewBody"]//div[@class="WP-z XP-z"]')
            # # review = [review.text for review in review_list]
            
            # # rating_count = self.driver.find_element_by_xpath('//*[@id="overview"]//span[@class="zP-z"][1]').text


            # print('title', title)
            # # print('brand', brand)
            # print('description', description)
            # print('price', price)
            # # print('sku_number', sku_number)
            # print('image', image)
            # print('review', review)
            # print('rating_count', rating_count)


    

