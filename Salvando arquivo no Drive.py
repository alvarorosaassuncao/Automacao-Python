# SALVANDO ARQUIVO NO GOOGLE DRIVE

#IMPORTANDO AS BIBLIOTECAS
import pyautogui as bot
import time

#DEFININDO MENSAGEM DE ALERTA E TEMPO DE PAUSA DAS LINHAS DE COMANDO
bot.alert('Atenção!! O codigo vai começar a rodar, não use o PC')
bot.PAUSE = 2

#ABRINDO O GOOLE CHROME
bot.press('win')
bot.write('Chrome')
bot.press('enter')

#CLICANDO NA BARRA DE ENDEREÇO E DIGITANDO O URL
bot.click(x=416, y=440)
bot.click(x=257, y=53)
bot.write('https://drive.google.com/drive/my-drive')
bot.press('enter')

#ESCOLHENDO A PASTA DESEJADA
bot.click(x=369, y=585)
bot.press('enter')

#VOLTANDO PARA AREA DE TRABALHO E ARRASTANDO O DOCUMENTO
bot.hotkey('win', 'd')
bot.moveTo(x=34, y=50)
bot.mouseDown()
bot.moveTo(487, y=361)

#ABRINDO A PASTA DO DRIVE
bot.hotkey('alt','tab')

#SOLTANDO O DOCUMENTO PARA SALVAR
bot.mouseUp()
time.sleep(2)

#EXIBINDO MENSAGEM DE ALERTA DE FINALIZACAO DA AUTOMACAO
bot.alert('Ocodigo acabou de rodar! Pode usar seu computador')

