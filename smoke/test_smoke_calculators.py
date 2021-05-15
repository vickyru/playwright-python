import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from pages.calculator_page import CalculatorPage


def test_smoke_addition_operator(page, browser):
    calculator_page = CalculatorPage(page)
    calculator_page.navigate()
    calculator_page.fill_first_number("20")
    calculator_page.select_operator("ADDITION")
    calculator_page.fill_second_number("30")
    calculator_page.click_go()
    assert (calculator_page.result() == "50")
    browser.close


def test_smoke_subtraction_operator(page, browser):
    calculator_page = CalculatorPage(page)
    calculator_page.navigate()
    calculator_page.fill_first_number("20")
    calculator_page.select_operator("SUBTRACTION")
    calculator_page.fill_second_number("10")
    calculator_page.click_go()
    assert (calculator_page.result() == "10")
    browser.close


def test_smoke_division_operator(page, browser):
    calculator_page = CalculatorPage(page)
    calculator_page.navigate()
    calculator_page.fill_first_number("20")
    calculator_page.select_operator("DIVISION")
    calculator_page.fill_second_number("10")
    calculator_page.click_go()
    assert (calculator_page.result() == "2")
    browser.close


def test_smoke_multiplication_operator(page, browser):
    calculator_page = CalculatorPage(page)
    calculator_page.navigate()
    calculator_page.fill_first_number("20")
    calculator_page.select_operator("MULTIPLICATION")
    calculator_page.fill_second_number("10")
    calculator_page.click_go()
    assert (calculator_page.result() == "200")
    browser.close


def test_smoke_modulo_operator(page, browser):
    calculator_page = CalculatorPage(page)
    calculator_page.navigate()
    calculator_page.fill_first_number("100")
    calculator_page.select_operator("MODULO")
    calculator_page.fill_second_number("30")
    calculator_page.click_go()
    assert (calculator_page.result() == "10")
    browser.close
