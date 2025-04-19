from selenium import webdriver as opcoes
from selenium.webdriver.common.by import By

import pyautogui as espera
import pyautogui as teclado

import pandas as pd

navegador = opcoes.Chrome()
navegador.get("https://www.magazineluiza.com.br")

navegador.find_element(By.ID,"input-search").send_keys("geladeira")

espera.sleep(3)

teclado.press("Enter")

espera.sleep(10)

listadf = []

produtos=navegador.find_elements(By.CLASS_NAME, "ghzctf")

for item in produtos:
    nome = ""
    preco = ""
    url = ""

    if nome == "":
        try:
            nome = item.find_element(By.CLASS_NAME, "dHamKz").text
        except Exception:
            pass

    elif nome == "":
        try:
            nome = item.find_element(By.CLASS_NAME, "sc-doohEh").text
        except Exception:
            pass

    print(nome)

    if preco == "":

        try:
            preco = item.find_element(By.CLASS_NAME, "dpUJi").text
        except Exception:
            pass

    elif preco == "":

        try:
            preco = item.find_element(By.CLASS_NAME, "sc-dcJsrY").text
        except Exception:
            pass

    elif preco == "":

        try:
            precoProduto = item.find_element(By.CLASS_NAME, "cGSMNm").text
        except Exception:
            pass

    elif preco == "":

        try:
            preco = item.find_element(By.CLASS_NAME, "sc-dWZqqJ").text
        except Exception:
            pass

    else:

        preco = "0"

    if url == "":
        try:
            url = item.find_element(By.TAG_NAME, "a").get_attribute("href")
        except Exception:
            pass

#    print(nome, "-", preco)
#    print(url)

    linhas = ([nome, preco, url])

    listadf.append(linhas)

excel = pd.ExcelWriter("DadosGeladeiraMagalu.xlsx", engine='xlsxwriter')
excel.close()

df = pd.DataFrame(listadf, columns=['Descrição', 'Preço', 'Url'])

excel = pd.ExcelWriter("DadosGeladeiraMagalu.xlsx", engine='xlsxwriter')

df.to_excel(excel, sheet_name = 'Dados', index=False)## Não trazer indices
worksheet = excel.sheets['Dados']
worksheet.set_column('A:C', 50)
excel.close()


