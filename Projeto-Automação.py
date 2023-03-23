

#!/usr/bin/env python
# coding: utf-8
 

estaticmethod
import pyautogui
import pyperclip
import time
pyautogui.click(x=118, y=741)
time.sleep(5)
pyautogui.PAUSE = 1

# pyautogui.click -> clicar
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> conjunto de tecla
# pyautogui.write -> escrever

""" passo 1 entrar no sistema da empresa (no link do drive)"""
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(5)

"""Passo 2: Navegar no sistema e encontrar a base de vendas (entrar na pasta exportar)"""
pyautogui.click(x=400, y=314, clicks=2)

"""Passo 3: Exportar o relatório (fazer o download)"""
pyautogui.click(x=419, y=481)
pyautogui.click(x=1176, y=195)
pyautogui.click(x=1018, y=606)
time.sleep(5)

"""Vamos agora ler um o arquivo baixado para pegar os indicadores"""

"""Passo 4: Calcular os indicadores (Faturamento e quntidade de produtos)"""
import pandas 
tabela = pandas.read_excel(r"C:\Users\User\Desktop\LiraHastag\Aula 1-Minicurso-Python\Vendas.xlsx")
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()
print(faturamento)
print(quantidade)

"""Passo 5: Enviar um e-mail para a diretoria"""

"""abrir aba e entrar no e-mail"""
pyautogui.hotkey("ctrl", "t") # abre a aba
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(5)

"""Clicar no botão escreve"""
pyautogui.click(x=134, y=216)

"""Destinatáio"""
time.sleep(5)
pyautogui.write("ddscosmeticos@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")

"""assunto"""
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

"""corpo do e-mail""" #enviar o e-mail

texto = f"""
Prezados Senhores, bom dia!

Informo que o faturamento de ontem foi de: R$ {faturamento:,.2f}
A quantidade de produtos vendidos foi de: {quantidade:,}

Att,
Daniel Douglas"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

"""Anexar um arquivo"""
pyautogui.click(x=928, y=705)
pyautogui.hotkey("ctrl", "t")
pyautogui.click(x=532, y=266)
pyautogui.press("enter")
time.sleep(4)

"""Enviar o e-mail com o anexo"""
pyautogui.hotkey("ctrl", "enter")



import time 
time.sleep(5)
print(pyautogui.position())


# 

#!pip install pyautogui
