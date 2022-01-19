from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('./chromedriver.exe')
driver.get("http://www.python.org")

assert "Python" in driver.title

elem = driver.find_element(By.ID, 'id-search-field')
elem.clear()
elem.send_keys('pycon')
elem.send_keys(Keys.RETURN)

assert 'No results found.' not in driver.page_source

print('Test case passed')

driver.close()
