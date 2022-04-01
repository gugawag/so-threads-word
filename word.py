from threading import Thread
import time

# o texto completo
global texto
texto = ''

# nova parte digitada do texto
global nova_parte
nova_parte = ''

# guarda qual o tamanho anterior do texto para ver se houve alteração
global tamanho_anterior
tamanho_anterior = 0

# usada para saber se deve salvar no arquivo (mudou o texto)
global salvar_dados
salvar_dados = False


# OBS.: para ver os dados no arquivo temporário,
# tem que aguardar um pouco para ver o SO descarregar.

def pega_dados():
    global texto
    global nova_parte
    while True:
        nova_parte = input()
        texto += nova_parte.replace('\n', '')
        time.sleep(0)


def calcula_letras():
    global texto
    global tamanho_anterior
    global salvar_dados
    while True:
        if len(texto) > tamanho_anterior:
            print('Texto: [', texto, ']')
            print('#caracteres:', len(texto), '\n')
            tamanho_anterior = len(texto)
            salvar_dados = True
        time.sleep(0)


def salva_dados():
    global nova_parte
    global salvar_dados
    while True:
        if salvar_dados:
            with open('arq_temp.txt', 'a') as f:
                f.write(nova_parte)
            salvar_dados = False
        time.sleep(0)


print('Digite um texto, dando enter entre pedaços digitados:')
# com threads (paralelismo)
t_escrita = Thread(target=pega_dados)
t_estatica = Thread(target=calcula_letras)
t_salvamento = Thread(target=salva_dados)

t_escrita.start()
t_estatica.start()
t_salvamento.start()

t_escrita.join()
t_estatica.join()
t_salvamento.join()

# sem threads seria sequencial
# pega_dados()
# calcula_letras()
# salva_dados()
