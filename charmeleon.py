# -*- coding: utf-8 -*-

from difflib import SequenceMatcher
import sys

#Compara duas palavras e retorna o grau de semelhança
def Compara(a, b):
	return SequenceMatcher(None, a, b).ratio()

#Executa o programa com os argumentos
def main(fonte, argumentos = ''):
	#Organiza os argumentos '-spaces', '-limit', '-x' e '-y'
	if '-spaces' in argumentos:
		splitspaces = int(argumentos.split('-spaces ')[1].split(' ')[0].strip())
	else:
		splitspaces = 0

	if '-limit' in argumentos:
		limit = float(argumentos.split('-limit ')[1].split(' ')[0].strip())
	else:
		limit = 0

	if '-x' in argumentos:
		x = int(argumentos.split('-x ')[1].split(' ')[0].strip())
	else:
		x = 20

	if '-y' in argumentos:
		y = int(argumentos.split('-y ')[1].split(' ')[0].strip())
	else:
		y = 20

	#Pede a palavra que será comparada com a fonte
	palavra = input('\nPalavra:\n>> ')
	while palavra.strip() == '': #Se não for digitada nenhuma palavra, repetir
		palavra = input('>> ')
	if palavra == 'exit': exit() #Fecha o programa se a palavra for 'exit'
	print('')

	#Se não tiver codificação na fonte, será utf8
	if not ':' in fonte: fonte += ':utf8'
	#Lê o arquivo e transforma as linhas em lista
	arquivo = open(fonte.split(':')[0], 'r', encoding = fonte.split(':')[1]).read().splitlines()

	#Se for demanda, quebrar os espaços de cada linha do arquivo fonte
	for i, linha in enumerate(arquivo):
		if splitspaces == 0:
			arquivo[i] = " ".join(arquivo[i].split()[0:])
		else:
			arquivo[i] = " ".join(arquivo[i].split()[0:splitspaces])

	#Adiciona as semelhanças se atingirem o limite do argumento
	semelhanças = list()
	for linha in arquivo:
		semelhanças.append((linha, Compara(palavra, linha)*100))

	#Printa os itens de semelhança no formato de porcentagem e com os pixels do argumento
	semelhanças.sort(reverse=True, key = lambda x: float(x[1]))
	formatation = "{0:"+str(x)+"} {1:"+str(y)+"}"
	for item in semelhanças:
		if item[1] > limit: print(formatation.format(item[0], str(item[1])+'%'))

	#Volta ao início: pede uma nova palavra para repetir o processo
	main(fonte, argumentos)


if __name__ == "__main__":
	#Checa os argumentos da linha de comando
	if len(sys.argv) == 1:
		print('Comando: charmeleon.py fonte:codificação -spaces NUM -limit NUM -x NUM -y NUM')
		print('fonte: arquivo com as palavras do domínio')
		print('codificação: codificação do arquivo com as palavras do domínio (padrão: utf8)')
		print('-spaces: número de espaços que serão cortados (padrão: infinito)')
		print('-limit: porcentagem mínima a ser mostrada (padrão: 0)')
		print('-x: pixels reservados para a palavra (padrão: 20)')
		print('-y: pixels reservados para a porcentagem (padrão: 20)')
	#Nenhum argumento, apenas o arquivo fonte
	elif len(sys.argv) == 2:
		main(sys.argv[1])
	#Mais de 2 argumentos
	else:
		main(sys.argv[1], " ".join(sys.argv[2:])) #Transforma todos os argumentos em uma string só