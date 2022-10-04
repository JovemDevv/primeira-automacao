import pandas
import pyautogui
import pyperclip
import time

tabela = pandas.read_excel(r"C:\Users\vasco\Downloads\Vendas - Dez.xlsx") 
# o r= é uma raw string, ou seja, não tem caractere especial na string.
print(tabela) #no jupyter usa display(tabela) ai apresenta uma tabela mais elaborada

faturamento = tabela['Valor Final'].sum()
print(faturamento)
quantidade = tabela['Quantidade'].sum()
print(quantidade)

#enviar por e-mail
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://mail.google.com/mail/u/0/#inbox')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(5)

pyautogui.click(x=136, y=190)
time.sleep(3)

pyautogui.write('pythonimpressionador@gmail.com')
pyautogui.press('tab') # pular para o assunto
pyperclip.copy('Relatório de vendas')
pyautogui.hotkey('ctrl', 'v')


pyautogui.press('tab') # para pular pro corpo do e-mail

texto = f'''
Prezados,

Segue o relatório de vendas,
Faturamento: R${faturamento:,.2f}
Quantidade de produtos vendidos: {quantidade:,}

Quaquer suvida estou à disposição.
Att.,
Ana
'''

#Formatação
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
#pyautogui.write(texto) - não aceita caracteres BR

pyautogui.hotkey('ctrl', 'enter') # quase todos os sistemas de e-mail, apertando ctrl+enter, ele envia o e-mail