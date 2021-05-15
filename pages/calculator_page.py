import sys
import os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../')


class CalculatorPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("/protractor-demo")

    def search(self, text):
        self.page.fill('[aria-label="Enter your search term"]', text)
        self.page.press('[aria-label="Enter your search term"]', "Enter")

    def fill_first_number(self, number):
        self.page.fill("input[ng-model='first']", number)

    def select_operator(self, operator):
        self.page.select_option("select[ng-model='operator']", operator)

    def fill_second_number(self, number):
        self.page.fill("input[ng-model='second']", number)

    def click_go(self):
        self.page.click("text=Go!")

    def result(self):
        selector = "//html/body/div/table/tbody/tr/td[3]"
        self.page.wait_for_selector(selector)
        return self.page.eval_on_selector(selector, "e => e.textContent")
