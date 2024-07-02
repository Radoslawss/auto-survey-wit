from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Zmienne
username = "login"
password = "pass"
select_value = "5"  # Wartość do wyboru w polu select
message = "Wszystko super"  # Wiadomość do wstawienia w textarea

# Konfiguracja Selenium i przeglądarki
driver = webdriver.Chrome()  # Upewnij się, że masz zainstalowany chromedriver
wait = WebDriverWait(driver, 10)

# Wejście na stronę logowania
driver.get("https://ubi2.wit.edu.pl/?table=1")

# Kliknięcie przycisku "Rozumiem i akceptuję"
accept_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Rozumiem i akceptuję')]")))
accept_button.click()

# Wprowadzenie danych logowania
wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
wait.until(EC.presence_of_element_located((By.NAME, "passwd"))).send_keys(password)

# Kliknięcie przycisku "Zaloguj"
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@value='Zaloguj']")))
login_button.click()
time.sleep(2)

# Przejście do strony z linkami ankiet
driver.get("https://ubi2.wit.edu.pl/?table=18&W=AN")

# Zbieranie linków ankiet
links = []
items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody.MItemList tr.MItem td.MText a.ion-external-a")))
for item in items:
    links.append(item.get_attribute("href"))

# Przetwarzanie każdej ankiety
for link in links:
    driver.get(link)
    # Przycisk "Wypełniam ankietę"
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Wypełniam ankietę')]"))).click()
    counter = 0;  
    while True:
        if counter<=5:
            print(counter)
            time.sleep(.5)
            select = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@name='odpowiedz']")))
            select.send_keys(select_value)
            
            # Przycisk dalej
            wait.until(EC.element_to_be_clickable((By.ID, "button_dalej_widoczny"))).click()
            counter+=1
        elif counter==6:
            print(counter)
            time.sleep(.5)
            textarea =  wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='odpowiedz']")))
            textarea.send_keys(message)
            # Przycisk dalej
            wait.until(EC.element_to_be_clickable((By.ID, "button_dalej_widoczny"))).click()

            # Obsługa popupu
            alert = wait.until(EC.alert_is_present())
            alert.accept()
            time.sleep(1.5)
            break
            

# Zamknij przeglądarkę
driver.quit()