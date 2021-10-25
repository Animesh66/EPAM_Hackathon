from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.nyse.com/")
driver.maximize_window()
driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
#driver.find_element(By.ID, "page-search").send_keys("EPAM")
driver.find_element(By.ID, "page-search").send_keys("EPAM" + Keys.ENTER)
