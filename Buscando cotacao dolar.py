# Automação feita para entrar no site da Petrobras com Pyautogui

import pyautogui as bot

def cotacao():
    bot.sleep(2)
    bot.PAUSE = 2
    bot.press('win')
    bot.write('Google chrome')
    bot.press('enter')
    bot.click(x=408, y=417)
    bot.click(x=357, y=-717)
    bot.write('www.google.com')
    bot.press('enter')
    bot.click(x=494, y=-481)
    bot.write('cotacao do dolar hoje')
    bot.press('enter')

    bot.alert('Fim do processo')

cotacao()
