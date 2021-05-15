from playwright.sync_api import sync_playwright
from pages.calculator_page import CalculatorPage
import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

with sync_playwright() as play:
    browser = play.chromium.launch(headless=False, channel="chrome")
    page = browser.new_page()
    calculator_page = CalculatorPage(page)
    calculator_page.navigate()
    assert (page.text_content("h3") == "Super Calculator")
    calculator_page.fill_first_number("10")
    calculator_page.select_operator("MULTIPLICATION")
    calculator_page.fill_second_number("10")
    calculator_page.click_go()
    assert (calculator_page.result() == "100")
    browser.close()
