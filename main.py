from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time, random, string
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size));
mot = 'arandgroqirhe', "aahejzkoptzj", "bszs", "nsizntzhxizarnfu", "yeeafzzz", "uixcdwaxzar" # liste immonde pour générer des password
i = 0
driver = webdriver.Chrome()
actions = ActionChains(driver)

while (i < random.randrange(5, 20)) :
    username = mot[random.randrange(len(mot))] + id_generator(random.randrange(4,8)) # Quand j'ai eu besoin de ce script je n'avais pas besoin de password plus compliqué, mais libre à vous de modifier ça à votre guise
    print(username)
    password = id_generator(4) + id_generator(10)
    driver.get('url') # Mettre ici le lien de la page register du site
    driver.find_element("name", "username").send_keys(username)
    driver.find_element("name", "password").send_keys(password)
    driver.find_element("name", "repeatPassword").send_keys(password)
    with open("log.txt", "a") as f:
        f.write( username + " : " +  password + "\n")
    time.sleep(random.randrange(15, 30))
    submit_btn = driver.find_element("xpath", 'xpath du bouton') # Ici coller le xpath du bouton d'enregistrement
    actions.move_to_element(submit_btn).perform()
    time.sleep(random.randrange(7, 50)) # Un timer " random "
    submit_btn.click()
    time.sleep(random.randrange(9, 30)) # Un autre timer " random "
    driver.quit()
    i = i + 1
