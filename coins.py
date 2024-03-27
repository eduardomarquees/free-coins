import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuração do WebDriver
servico = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=servico)
url = 'https://br.onlinesoccermanager.com/Login'
driver.maximize_window()
driver.get(url)


def lobby1(driver,xpath):
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
    home = driver.find_element(By.XPATH,xpath)
    home.click()
    time.sleep(5)

def lobby(driver, xpath):
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
    elemento = driver.find_element(By.XPATH, xpath)
    elemento.click()
    time.sleep(15)

def escolher_escudo(driver, xpath):
    selecionar = driver.find_element(By.XPATH,xpath)
    selecionar.click()
    time.sleep(15)

def clicar_moeda_chefe(driver,xpath):
    #WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
    moeda_chefe = driver.find_element(By.XPATH,xpath)
    moeda_chefe.click()
    time.sleep(15)
def clicar_anuncio(driver, xpath):
    anuncio = driver.find_element(By.XPATH,xpath)
    anuncio.click()
    time.sleep(40)

def check_ok(driver, xpath):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        check = driver.find_element(By.XPATH, xpath)
        check.click()
        return True
    except:
        pass

def verificar(driver, xpath):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        elemento = driver.find_element(By.XPATH, xpath)
        elemento.click()
    except:
        print("Elemento não encontrado ou não clicável.")

# Exemplo de uso:
lobby1(driver,'//*[@id="desktop-menu-navbar"]/li[1]/a/div[2]')
lobby(driver, '//*[@id="body-content"]/div[2]/div[1]/div/div[4]/div/div[2]')
escolher_escudo(driver,"//*[@id='desktop-menu-navbar']/li[5]/a/div[1]")
clicar_moeda_chefe(driver, '// *[ @ id = "desktop-menu-navbar"] / li[5] / ul / li[4] / a')
for _ in range(9):
    clicar_anuncio(driver,'//*[@id="body-content"]/div[2]/div[2]/div/div[1]/div')
    verificar(driver, '// *[ @ id = "desktop-menu-navbar"] / li[5] / ul / li[4] / a')
    if check_ok(driver, '//*[@id="modal-dialog-alert"]/div[4]/div/div/div/div[3]/div/div'):
        break;
    else:
        pass