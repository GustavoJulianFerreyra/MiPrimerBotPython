from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert 
from selenium.webdriver.common.keys import Keys
from time import sleep
#from selenium.webdriver.chrome.options import Options
#from BotTelegram import comentario
from config import contra,correo,direccionChrome
def main():
    print("Ya estoy al aire")
    try:
      service = Service(direccionChrome)
    except:
      print('No tienes el Driver de Chrome Instalado o la direccion esta incorrecta')
    service.start()
    driver = webdriver.Remote(service.service_url)
    driver.get('https://m.facebook.com')
    variable = driver.find_element_by_xpath('//*[@id="m_login_email"]')
    variable.send_keys(correo)
    variable.send_keys(Keys.TAB)
    variable= driver.find_element_by_xpath('//*[@id="m_login_password"]')
    variable.send_keys(contra)
    variable.send_keys(Keys.ENTER)
    sleep(20)
    ahoraNo= driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div[3]/div[1]/div/div/a')
    ahoraNo.click()
    sleep(20)
    click_publicar = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[1]/div[3]/div/div/div[1]/div[2]')
    click_publicar.click()
    sleep(5)
    ahorano = driver.find_element_by_xpath('//*[@id="uniqid_1"]')
    ahorano.send_keys('Hola Esto es una prueba de un bot ejecutado en python')
    publicar = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div/div/div[5]/div[3]/div/div/button')
    publicar.click()
    alert = Alert(driver) 
    print(alert.text) 
    alert.accept() 
    driver.quit()
if __name__ == '__main__':
    main()