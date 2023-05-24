

### PROGRAMA PARA ABRIR UMA JANELA NA QUAL O USUÁRIO TERA A OPÇÃO DE ESCOLHER ENTRE,
# EXCEL, WORD OU NOTEPAD PARA ABRIR AUTOMATICAMENTE.

import pyautogui as bot

opcao = bot.confirm('Clique no botão desejado',
                    buttons=['Excel', 'Word', 'Notepad'])

# ABRINDO O EXCEL
if opcao == "Excel":
    print('Você escolheu a opção Excel')
    bot.PAUSE = 2
    bot.press('win')
    bot.write('Excel')
    bot.press('enter')
    bot.write('Voce abriu o Excel')


# ABRINDO O WORD
elif opcao == "Word":
    print('Você escolheu a opção Word')
    bot.PAUSE = 2
    bot.press('win')
    bot.write('Word')
    bot.sleep(2)
    bot.press('enter')
    bot.sleep(2)
    bot.click(x=270, y=213)
    bot.write('Voce escolheu a opcao Word ')


#ABRINDO O NOTEPAD
else:
    print('Você escolheu a opção Notepad')
    bot.sleep(2)
    bot.hotkey('win', 'r')
    bot.write('Notepad')
    bot.sleep(2)
    bot.press('enter')
    bot.write('Voce escolheu a opcao  Notepad')


#ACHANDO A POSIÇÃO NA TELA
#bot.sleep(4)
#print(bot.position())
