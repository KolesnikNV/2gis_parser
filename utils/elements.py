from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


async def get_element_text(driver: WebDriver, path: str) -> str:
    try:
        return driver.find_element(By.CSS_SELECTOR, path).text
    except NoSuchElementException:
        return ""


async def make_scroll(driver, path):
    return driver.execute_script(path)


async def get_elements_text(driver: WebDriver, path: str) -> set:
    phone_set = set()
    try:
        result = driver.find_elements(By.CSS_SELECTOR, path)
        for element in result:
            phone_set.add(element.text)
        return phone_set
    except NoSuchElementException:
        return phone_set


sss = [
    "/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/a",
    "/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[1]/a",
    "/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div/div[1]/a",
    "/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[4]/div/div[1]/a",
    "/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[5]/div/div[1]/a",
    "/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[6]/div/div[1]/a",
    "/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[7]/div/div[1]/a",
    "/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[8]/div/div[1]/a",
    "/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[9]/div/div[1]/a",
    "/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[10]/div/div[1]/a",
    "/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[11]/div/div[1]/a",
    "/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[12]/div/div[1]/a",
]


async def get_elements_href(driver, path):
    link_list = []
    try:
        for link in sss:
            link_list.append(driver.find_element(By.XPATH, link).get_dom_attribute("href"))
        return link_list
    except NoSuchElementException:
        return ""


async def get_element_href(driver, path):
    try:
        return driver.find_element(By.CSS_SELECTOR, path).get_dom_attribute("href")
    except NoSuchElementException:
        return ""


async def get_element_label(driver, path):
    try:
        return driver.find_element(By.CSS_SELECTOR, path).get_attribute("aria-label")
    except NoSuchElementException:
        return ""


async def move_to_element(driver: WebDriver, element) -> None:
    try:
        webdriver.ActionChains(driver).move_to_element(element).perform()
    except StaleElementReferenceException:
        pass


async def element_click(driver, path: str) -> bool:
    try:
        driver.find_element(By.XPATH, path).click()
        return True
    except:
        return False


async def get_find_element(driver, path: str):
    return driver.find_element(By.CSS_SELECTOR, path)
