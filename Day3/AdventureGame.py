def terceiraFase():
    print()
    resp = input("Você está de frente à três portas. Escolha uma: azul, vermelha ou amarela.")
    if(resp.lower() == "amarela"):
        print("Você encontrou o tesouro, parabéns!")
    elif(resp.lower() == "azul"):
        print("Você foi comido por um demonio. Fim de jogo.")
    elif(resp.lower() == "vermelha"):
        print("Você foi quemado vivo. Fim de jogo.")
    else:
        print("Você foi atacado por um animal selvagem. Fim de jogo.")

def segundaFase():
    print()
    resp = input("Você está de frente à um lago. Você prefere esperar ou nadar ?")
    if(resp.lower() == "esperar"):
        terceiraFase()
    else:
        print("Você foi atacado por um animal selvagem. Fim de jogo.")

print(''' 
  .''.
 (~~~~)
   ||
 __||__
/______\
  |  |' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
  |  |'|o| - - - - - - - - - - - - - - - - - - - - - - - - -||
  |  |'| |                                                  ||
  |  |'| |                      . ' .                       ||
  |  |'| |                  . '       ' .                   ||
  |  |'| |              . '    .-'"'-.    ' .               ||
  |  |'| |          . '      ,"       ".      ' .           ||
  |  |'| |      . '        /:           :\        ' .       ||
  |  |'| |  . '            ;  .          ;            ' .   ||
  |  |'| |    ' .          \: . .       :/          . '     ||
  |  |'| |        ' .        `. . .    ,/       . '         ||
  |  |'| |            ' .      `-.,,.-'     . '             ||
  |  |'| |                ' .           . '                 ||
  |  |'| |                    ' .   . '                     ||
  |  |'| |                        '                         ||
  |  |'|o|-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_||
  |  |'
  |  |'
  |  |'
  |  |'
  '~~'
  Bem vindo ao jogo interativo. Sua missão é encotrar o tesouro.
      ''')

resp = input("Você está de frente à uma encruzilhada. Qual lado você escolhe ir ? Esquerda ou Direita ?")

if(resp.lower() == "esquerda"):
    segundaFase()
else:
    print("Você caiu em um buraco. Fim de jogo.")


