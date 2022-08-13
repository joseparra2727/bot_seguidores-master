import time
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver


def bot_likes():

    try:

        opc = Options()
        opc.add_argument("--start-maximized")
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=opc
        )

        driver.get("https://likestool.com/site/login/")

        # BUSCAR EL INPUT VA A PONER EL NOMBRE DE USUARIO Y VA DAR CLICK
        ActionChains(driver.find_element(By.ID, "input-2")).move_to_element(
            driver.find_element(By.ID, "input-1")).click().send_keys("agogosito").perform()

        ActionChains(driver).move_to_element(
            driver.find_element(By.ID, "input-2")).click().send_keys("123456789").perform()

        # DAR CLICK EN ENTRAR

        ActionChains(driver).move_to_element(driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/form/div[4]/input')).click().perform()

        # CUANDO EL ENTRA QUE ESPERE MIENTRAS ENTRA
        time.sleep(20)

        ActionChains(driver).move_to_element(driver.find_element(
            By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/ul/li[2]/a/span")).click().perform()

        time.sleep(1)

        # YOUTUBE LISTA

        ActionChains(driver).move_to_element(driver.find_element(
            By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/ul/li[2]/ul/li[1]/a")).click().perform()
        time.sleep(3)

        contador = 0
        while True:

            contador += 1
            print("DANDO CLIC EN UN VIDEO".format(contador))

            ActionChains(driver).move_to_element(driver.find_element(
                By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/a')).click().perform()

            time.sleep(70)

            driver.refresh()

    except:
        return 0


print(bot_likes())
