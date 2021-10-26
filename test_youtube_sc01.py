import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Firefox(executable_path="C:\\Users\\Animesh_Mukherjee\\Downloads\\geckodriver-v0.30.0-win32")
driver.get("https://www.youtube.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.NAME, "search_query").click()
driver.find_element(By.NAME, "search_query").send_keys("EPAM Systems Global")
time.sleep(2)
driver.find_element(By.ID, "search-icon-legacy").click()
# driver.find_element(By.CLASS_NAME, "style-scope ytd-channel-name").click()
# elements = driver.find_elements(By.TAG_NAME, "yt-formatted-string")
# elements[0].click()
time.sleep(3)
#driver.find_element(By.XPATH,"//yt-formatted-string[@xpath='1']").click()
driver.find_element(By.XPATH,"(.//*[normalize-space(text()) and normalize-space(.)='Filters'])[1]/following::yt-formatted-string[2]").click()
driver.find_element(By.XPATH, "//div[normalize-space()='Videos']").click()
# time.sleep(3)
# titles = driver.find_elements(By.XPATH, "//*[@id='video-title']")
# titles.__getitem__(0).click()
# driver.find_element(By.XPATH, "(//a[@id='video-title'])[2]").click()
# for title in titles:
#     print(title)



