from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import pyautogui
url = "https://web.mobilomsorg.se/Login#company/select"

browser = webdriver.Chrome()
browser.get(url)

def login():
    company_code = "solidcare"
    user = "gijo"
    pass_w = "651019"
    # go in to log in
    # bot = browser.find_element_by_id("comp-jee51bpn6linkElement")
    # bot.click()

    #company_code
    bot = browser.find_element_by_class_name("form-control")
    sleep(2)
    bot.send_keys(company_code)
    bot.send_keys(Keys.ENTER)
    sleep(2)
    bot = browser.find_element_by_name("username")
    bot.send_keys(user)
    bot.send_keys(Keys.TAB, pass_w)
    bot.send_keys(Keys.ENTER)
    sleep(3)

class Scheme():

    def graphics_schedual(self):
        # from start screen to graphics schedual
        bot = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[3]/a")
        bot.click()
        bot = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[3]/ul/li[1]/a")
        bot.click()
        sleep(2)

    def press_date(self):
        browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[1]/div[1]/div[1]/div/div[2]/input").click()
        sleep(1)

    def next_month(self):
        bot = browser.find_element_by_class_name("next")
        bot.click()

    def find_month(self):
        bot = browser.find_element_by_class_name("datepicker-switch")
        month, year = bot.text.split(" ")
        return month, year

    def find_day(self, target_day):
        try:
            tbody = browser.find_element_by_xpath("/html/body/div[17]/div[1]/table/tbody")
            tr = tbody.find_elements_by_tag_name("tr")
            for each_tr in tr:
                td = each_tr.find_elements_by_tag_name("td")
                for each_td in td:
                    day = each_td.text
                    class_atr = each_td.get_attribute("class")
                    if day == target_day and class_atr != "cw":
                        each_td.click()
                        return
        except NoSuchElementException as e:
            print("Caught Error", e, "\nTerminating Program")

    def find_date(self, day, month, year):
        #the date must be a future date
        curr_month, curr_year = self.find_month()
        while curr_month != month or curr_year != year:
            self.next_month()
            curr_month, curr_year = self.find_month()

        self.find_day(day)
        sleep(2)

class Colleges:
    def __init__(self):
        # save all colleges inside of a list
        self.existing_colleges = list()

        self.available_colleges = list()
        # get all existing colleges
        self.exist()
        self.available()

    def exist(self):
        # insert colleges
        column_body = browser.find_element_by_class_name("graphical_planning_column_body") # finds the first element named inside paranthesis.

        each_p = column_body.find_elements_by_class_name("planned_emps_row")
        for pers in each_p:
            # pers = pers.find_element_by_class_name("planned_emps_row_inner")
            # name = pers.find_element_by_class_name("name")
            name = pers.find_element_by_class_name("dropdown-toggle").text.strip()
            self.existing_colleges.append(name)

    def available(self):
        browser.find_element_by_class_name("add").click()
        sleep(1)
        browser.find_elements_by_class_name("select2-chosen")[8].click()

        drop_menu = browser.find_elements_by_class_name("select2-results")
        for name in drop_menu:
            if name.text and name.text not in self.existing_colleges:
                self.available_colleges.append(name.text.strip())
        sleep(1)
        # put up drop menu
        browser.refresh()
        sleep(1)

    def print_colleges(self):
        print("Existing:")
        for col in self.existing_colleges:
            print(col)
        print("\n")

    def print_avalible_colleges(self):
        print("Available:")
        for col in self.available_colleges:
            print(col)
        print("\n")

    def add_existing_college(self, new_name):
        sleep(1)
        browser.find_element_by_class_name("add").click()
        sleep(1)
        browser.find_elements_by_class_name("select2-chosen")[8].click()
        drop_menu = browser.find_element_by_xpath('//*[@id="select2-drop"]/ul')
        all_drop_menu = drop_menu.find_elements_by_tag_name("li")
        found = False

        for each in all_drop_menu:
            if each.text == new_name:
                each.click()

                time_span = browser.find_elements_by_class_name("inline_time_input_preview")[4]
                time_span.click()
                # time span
                pyautogui.write("0000", interval=0.25)
                pyautogui.write("1000", interval=0.25)

                # break time
                break_time = browser.find_elements_by_class_name("inline_time_input_preview")[8]
                break_time.click()
                pyautogui.write("0500", interval=0.25)
                pyautogui.write("0530", interval=0.25)
                found = True
                break

        if not found:
            print("Cant find", new_name)
            browser.refresh()
            sleep(1)
            return
        print("Added", new_name)
        browser.find_element_by_id("emp_add_modal_add").click()

login()
s = Scheme()
s.graphics_schedual()
s.press_date()
day_stop = "14"
month_stop = "April"
year_stop = "2021"

s.find_date(day_stop, month_stop, year_stop)

c = Colleges()
c.print_avalible_colleges()
college = input("Input College:\n")

while college:
    c.add_existing_college(college)
    college = input("Input College:\n")
# c.print_avalible_colleges()
# c.print_colleges()
print("DONE")