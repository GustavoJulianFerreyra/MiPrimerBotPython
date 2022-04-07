from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert 
from selenium.webdriver.common.keys import Keys
from time import sleep
import autoit
#from selenium.webdriver.chrome.options import Options
#from BotTelegram import comentario
from config import contra,correo,direccionChrome
def main():
    botTelegram()
def botTelegram():
    direccionChrome
    #Futura Interaccion con Telegram 
    publicFacebook()
def publicFacebook():
    try:
      service = Service(direccionChrome)
    except:
      print('No tienes el Driver de Chrome Instalado o la direccion esta incorrecta')
    service.start()
    driver = webdriver.Remote(service.service_url)
    driver.set_window_size(480, 800)
    driver.get('https://m.facebook.com')
    variable = driver.find_element_by_xpath('//*[@id="m_login_email"]')
    variable.send_keys(correo)
    variable.send_keys(Keys.TAB)
    variable= driver.find_element_by_xpath('//*[@id="m_login_password"]')
    variable.send_keys(contra)
    variable.send_keys(Keys.ENTER)
    sleep(15)
    ahoraNo= driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div[3]/div[1]/div/div/a')
    ahoraNo.click()
    sleep(15)
    click_publicar = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[1]/div[3]/div/div/div[1]/div[2]')
    click_publicar.click()
    sleep(5)
    publcacionMessage = driver.find_element_by_xpath('//*[@id="uniqid_1"]')
    publcacionMessage.send_keys('Hola Esto es una prueba de un bot ejecutado en python')
    sleep(10)
    imagenMessage = driver.find_element_by_xpath('//*[@id="structured_composer_form"]/div[6]/div/button[1]/div/div[2]')
    imagenMessage.click()
    sleep(2)
    subirArchivo = driver.find_element_by_class_name('_50o7 touchable _21db')
    subirArchivo.click()
    alerta()
    sleep(10)
    publicar = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div/div/div[5]/div[3]/div/div/button')
    publicar.click()
    alert = Alert(driver) 
    print(alert.text) 
    alert.accept() 
    driver.quit()
if __name__ == '__main__':
    main()
    
def alerta():
  autoit.win_active("Open") 
  autoit.control_send("Open","Edit1",r"address\Python-logo.txt")
  autoit.control_send("Open","Edit1","{ENTER}")
