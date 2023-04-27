from src.verificacpf import formater
from src.timestamp import time_stamp

def grava_arquivo_cpfs_invalidos(lista_invalidos,modulo_utilizado):
	str_lista = ''

	diretorio = '/Users/rangel/Desktop/'
	nome = 'log_cpf_invalidos_'
	extensao = '.txt'
	hora = time_stamp()
	path_completa = diretorio+nome+hora+extensao

	cabecalho = modulo_utilizado + " LISTA DE CPFS INVÁLIDOS: \n\n"
	
	for cpf in lista_invalidos:
		cpf = formater(cpf)
		str_lista = str_lista + cpf +'\n'
	
	arquivo = open(path_completa, "w")
	arquivo.write(cabecalho+str_lista)
	arquivo.close()

	