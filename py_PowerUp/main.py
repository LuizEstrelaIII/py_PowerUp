import pyautogui    #SÓ RODA SE ABRIR PELO PROMPT
import pandas as pd
import time

pyautogui.PAUSE = 0.3

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=785, y=551)
pyautogui.write("estrela.luiz@uol.com.br")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.click(x=940, y=800) #clicar no botão de login
time.sleep(3)

tabela = pd.read_csv("produtos.csv")

#cadastrar produto
for linha in tabela.index:

    pyautogui.click(x= 853, y=394)        


    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(5000)


