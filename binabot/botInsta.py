from selenium import webdriver
import keyboard
import time

navegador = webdriver.Firefox()
navegador.get("https://www.instagram.com/direct/inbox/")
time.sleep(30)
# navegador.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()  # nao salvar
# time.sleep(2)
# navegador.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()  # agora nao
time.sleep(2)
navegador.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button').click()
time.sleep(2)
navegador.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').click()
for char in "gmacias_correa":
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.1)
time.sleep(2)

navegador.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div').click()
navegador.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/div/button/div').click()
time.sleep(2)
navegador.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').click()
time.sleep(2)
for char in "aaaaaaaaaaaaaaaaaaaaaaaaaa":
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.1)
navegador.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()