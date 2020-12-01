
import time
import webbrowser
import pyautogui as pag
import schedule

time.time()

# Cada matéria deve ter seu código inserido, caso tenha matérias extras siga o padrão: aulaUm = "xxx-xxx-xxx"

mat = "xxx-xxxx-xxx"
fis = "xxx-xxxx-xxx"
qui = "xxx-xxxx-xxx"
bio = "xxx-xxxx-xxx"
por = "xxx-xxxx-xxx"
red = "xxx-xxxx-xxx"
ing = "xxx-xxxx-xxx"
lit = "xxx-xxxx-xxx"
fil = "xxx-xxxx-xxx"
soc = "xxx-xxxx-xxx"
his = "xxx-xxxx-xxx"
geo = "xxx-xxxx-xxx"


# Função principal, o código da aula especifica entra na parte do link.
# IMPORTANTE: a parte do link authuser=0 deve ter o numero trocado para logar com a conta desejada 
# esse numero varia de acordo com a conta logada, você pode verificar olhando o link no seu navegador

def link(dclass):
    
    webbrowser.open('https://meet.google.com/' + dclass + '?authuser=0')
    
    time.sleep(10)
    for i in range(5):
        time.sleep(2)
        pag.press('tab')

    time.sleep(2)
    pag.press('enter')

#fechar aba

def fechar():
    pag.hotkey('command', 'w')
    time.sleep(5)

# Abaixo segue a lista com as aulas, isso seria seu horário. Altere-o 

segunda = [mat, mat, mat, mat, mat, mat, mat, mat]
terca = [fis, fis, fis, fis, fis, fis, fis]
quarta = [his, his, his ,his, his, his]
quinta = [qui, qui, qui, por, por, por]
sexta = [geo, geo, geo, geo, geo, geo]


# esse é a execução das aulas. time.sleep indica o tempo entre entrar e fechar a aula em segundos. O padrão é 2700 segundos (45 minutos) voce pode mudar a seu gosto.
# 1200 sendo o tempo do intervalo, linha extra. pode ser removido.


def abrirAula(lis):
    link(lis[0])
    time.sleep(2700)
    fechar()
    link(lis[1])
    time.sleep(2700)
    fechar()
    link(lis[2])
    time.sleep(2700)
    fechar()
    time.sleep(1200)
    link(lis[3])
    time.sleep(2700)
    fechar()
    link(lis[4])
    time.sleep(2700)
    fechar()
    link(lis[5])
    time.sleep(2700)
    fechar()
    link(lis[6])
    time.sleep(2700)
    fechar()

abrirAula(segunda)

