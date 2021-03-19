
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#driver = webdriver.Firefox

driver=webdriver.Chrome()
#wait = WebDriverWait(driver, 20)

#driver.implicitly_wait(20) # seconds

#myDynamicElement = driver.find_element_by_id("myDynamicElement")

driver.get('http://www.python.org')

driver.find_element_by_link_text("Documentation").click()
driver.find_element_by_link_text("Docs").click()
driver.find_element_by_link_text("index").click()
driver.find_element_by_link_text("Python").click()
driver.find_element_by_link_text("Documentation").click()
driver.find_element_by_link_text("FAQ").click()
driver.find_element_by_link_text("Python").click()
driver.find_element_by_name("System Administration:").send_keys("Ansible")