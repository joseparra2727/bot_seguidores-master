import selenium  
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

def botig():
    opc = Options()
    opc.add_argument("--start-maximized")
    driver = webdriver.Chrome( options=opc)
    driver.get("https://addmefast.com/")
    ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div/div[4]/form/div[1]/div[1]/input[1]")).click().send_keys("kwargsfunction@gmail.com").perform()
    time.sleep(1.6)
    ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div/div[4]/form/div[1]/div[1]/input[2]")).click().send_keys("Ago123456789#").perform()
    time.sleep(2.5)
    ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div/div[4]/form/div[1]/div[1]/input[3]")).click().perform()
    time.sleep(8)

    #YOUTUBE
    
    driver.execute_script("window.scrollTo(0, window.scrollY + 400)")
    ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div[2]/div[31]/a")).click().perform()
    time.sleep(2)
    ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[3]/center/div[2]/div[1]/div[2]/center/div/div/center[2]/a/div")).click().perform()
    time.sleep(10)


print(botig())