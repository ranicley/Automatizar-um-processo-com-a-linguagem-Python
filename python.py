import yfinance

ticker = input ('Digite o código da ação: ')
dados = yfinance.Ticker(Ticker)


dados.history()


tabela = dados.history("")
tabela


fechamento = tabela.Close
fechamento

fechamento.plot()


maxima = fechamento.max()
minima = fechamento.min()
atual = fechamento[-1]
print(maxima)
print(minima)
print(atual)


import pyautogui
import pyperclip



destinatario = "seuemail@gmail.com"
assunto = "Análise diária"
mensagem = f"""
Bom dia,
Segue abaixo as análises da ação {yfinance.Ticker} dos últimos seis meses:
Cotação máxima: R${round(maxima,2)}
Cotação mínima: R${round(minima,2)}
Cotação atual: R${round(atual,2)}
Atenciosamente,
Seu nome.
"""

print(destinatario)
print(assunto)
print(mensagem)

pyautogui.PAUSE = 3

pyautogui.hotkey("ctrl", "t")

pyperclip.copy("www.gmail.com")

pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

pyautogui.click(x=2034, y=210)

pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab")

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

pyautogui.click(x=3107, y=975)

pyautogui.hotkey("ctrl", "f4")
print('E-mail enviado com sucesso!')

import time
time.sleep(5)
pyautogui.position()
