import threading
import time

global texto
texto = ''

global tamanho_anterior
tamanho_anterior = 0

global nova_parte
nova_parte = ''


def pega_dados():
    global texto
    global tamanho_anterior
    global nova_parte
    while True:
        nova_parte = input()
        texto += nova_parte.replace('\n', '')
        time.sleep(0)


def salva_dados():
    global texto
    global nova_parte
    while True:
        if len(texto) > tamanho_anterior:
            with open('../dados.txt', 'a') as f:
                f.write(nova_parte)
        time.sleep(0)


def calcula_letras():
    global texto
    global tamanho_anterior
    while True:
        if len(texto) > tamanho_anterior:
            print('Texto: [', texto, ']')
            print('caracteres:', len(texto), '\n')
            tamanho_anterior = len(texto)
        time.sleep(0)


# === Versão com Threads ===
t1 = threading.Thread(target=pega_dados)
t2 = threading.Thread(target=calcula_letras)
t3 = threading.Thread(target=salva_dados)

t1.start()
t2.start()
t3.start()

# === Versão sem threads ===
# pega_dados()
# salva_dados()
# calcula_letras()
