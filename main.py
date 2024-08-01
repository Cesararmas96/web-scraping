from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.common.by import By
from selenium import webdriver
from question import question
# Para Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configuración para Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

class InstagramBot:

    # Constants for UI elements
    xpath_username = "//input[@name='username']"
    xpath_password = "//input[@name='password']"
    xpath_login_button = "//*[@id='form']/div[3]/button"
    xpath_bot_select = "/html/body/div/div[1]/div/div/main/ul/div/a"
   
   

    def __init__(self, username, password):
        self.username = username
        self.password = password

        # Inicializa el navegador
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(10)  # espera implícita de 10 segundos

    def login(self):
        self.driver.get('https://navai.trocdigital.net/auth')
        time.sleep(3)

        self.driver.find_element(
            By.XPATH, self.xpath_username).send_keys(self.username)
        self.driver.find_element(
            By.XPATH, self.xpath_password).send_keys(self.password)
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.xpath_login_button).click()

        time.sleep(5)
        self.driver.find_element(By.XPATH, self.xpath_bot_select).click()

       
    def comentar(self):
        selected_question = random.choice(question)
        time.sleep(3)
        # Hacer clic en el campo de entrada
        input_field = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/form/div/div[1]/div/input')
        input_field.click()

        # Enviar la pregunta seleccionada
        input_field.send_keys(selected_question)
        time.sleep(3)

        # Hacer clic en el botón de envío
        submit_button = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/form/div/div[2]/button')
        submit_button.click()
        time.sleep(10)  # Espera para observar el resultado

user = "carmas@trocglobal.com"
password = "Welc@me01!"

print('Amounts of comments to generate:')
cantComents = int(input())

ig_bot = InstagramBot(user, password)
ig_bot.login()
time.sleep(4)

# Descomenta estas líneas si necesitas realizar más comentarios
for i in range(cantComents):
    print('Amounts of Comments: ' + str(i + 1))
    ig_bot.comentar()
    time.sleep(10)
print('Finished Comments')
msvcrt.getch()
