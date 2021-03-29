from selenium import webdriver
import time
import re
import sys
import json

class Driver:
    def __init__(self):
        # Opening JSON conf file
        f = open('conf.json',)
  
        # returns JSON object as 
        # a dictionary
        data = json.load(f)
  
        # Closing file
        f.close()

        browser = data["browser"]
        print "Browser used is ", browser

        if browser == "Firefox":
            self.driver = webdriver.Firefox()
        if browser == "Chrome":
            self.driver = webdriver.Chrome()

    def get(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def find_element_by_id(self, id):
        element = self.driver.find_element_by_id(id)
        return element

    def check_if_headings_in_contents(self, id):
        status = 0
        # - Find the <ul> tag
        ul_elem = self.driver.find_element_by_xpath("//div[@id='toc']//ul")
        # Find all <li> elements under <ul>
        items = ul_elem.find_elements_by_tag_name("li")
        for item in items:
            found = 0
            span = item.find_element_by_class_name("toctext")
            text = span.text
            text1 = re.sub("\s", "_", text)
            list_helements = self.driver.find_elements_by_tag_name("h2")
            for hlem in list_helements:
                try:
                    hlem.find_element_by_id(text1)
                    found = 1
                    break
                except:
                    pass
            if found == 0:
                print("No heading found with text {}" . format(text))
                status = 1
        if (status):
            return 1
        return 0

    def check_hlinks_in_contents(self, id):
        status = 0
        # - Find the <ul> tag
        ul_elem = self.driver.find_element_by_xpath("//div[@id='toc']//ul")
        # Find all <li> elements under <ul>
        items = ul_elem.find_elements_by_tag_name("li")
        for item in items:
            found = 0
            span = item.find_element_by_class_name("toctext")
            text = span.text
            anchorElement = item.find_element_by_tag_name("a")
            href = anchorElement.get_attribute("href")
            try:
                anchorElement.click()
            except:
                print("Unable to click {}" . format(href))
                status = 1
        if (status):
            return 1
        return 0

    def check_personified(self, text1, text2):
        status = 0
        # - Find the <ul> tag
        ul_elem = self.driver.find_element_by_xpath("//div[@class='div-col']//ul")
        items = ul_elem.find_elements_by_tag_name("li")
        for item in items:
            anchorElement = item.find_element_by_tag_name("a")
            href = anchorElement.get_attribute("href")
            if (href):
                match = re.search(text1, href)
                if match:
                    try:
                        anchorElement.click()
                        self.driver.get(href)
                        ul_elem1 = self.driver.find_element_by_xpath("//div[@id='toc']/ul")
                        items_1 = ul_elem1.find_elements_by_tag_name("li")
                        for item in items_1:
                            anchorElement = item.find_element_by_tag_name("a")
                            href = anchorElement.get_attribute("href")
                            if (href):
                                text3 = re.sub("\s", "_", text2)
                                match = re.search(text3, href)
                                if match:
                                    try:
                                        anchorElement.click()
                                        break
                                    except:
                                        print("Unable to click {}" . format(href))
                                        status = 1
                                        break
                                else:
                                    continue
                        break
                    except:
                        print("Unable to click {}" . format(href))
                        status = 1
                        break
        if (status):
            return 1
        return 0

    def print_test_status(self, status, testname):
        if (status):
            print("Test {} Failed" . format(testname))
        else:
            print("Test {} Passed" . format(testname))


