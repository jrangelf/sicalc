from zeep import Client

client = Client(wsdl='http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx?WSDL')


def lista_servico():
	servico = client.service.ListaServicos()
	
	lista = servico['cServicosCalculo']
	
	return lista

def calcula_prazo(codigo, cep_origem, cep_destino):

	# "41432","70362010","70292070"
	lista = {}
	prazo = client.service.CalcPrazo(codigo,cep_origem,cep_destino)
	
	resultado = prazo['cServico'][0]
	#lista = resultado

	return resultado


def funcao1():

	return 'texto de retorno da funcao1'

def funcao2(valor):
	valor = valor * 3746
	return valor

def imprime_lista(lista):
	#for i in range(1,26):
	#	lista.append(i)
	return lista

