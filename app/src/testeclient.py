from zeep import Client
import json
#------------------------------------------
#------------Servidor Web Correios --------

client = Client(wsdl='http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx?WSDL')

ret1 = client.service.ListaServicos()
ret2 = client.service.CalcPrazo("41432","70362010","70292070")

#dict_ret1 = json.loads(ret1)
#dict_ret2 = json.loads(ret2)

#print (dict_ret1)
#print (dict_ret2)

#print (retorno2['cServico'][0])

#resultado = retorno2['cServico'][0]
#listaResultado = resultado
#print (ret1)

print (ret1['cServicosCalculo'][0])
y =len(ret1['cServicosCalculo'][0])

w = len(ret1['cServicosCalculo'])
lista = ret1['cServicosCalculo']



for item in lista:
	print (item.codigo)

print(dir(lista)) 
#print (y, w)
#fita = ''
#for i in range(w):
#	x = ret1['cServicosCalculo'][i]
#	print (x.codigo,x.descricao,x.calcula_preco,x.calcula_prazo,x.erro,x.msgErro)

	

#x = ret1['cServicosCalculo'][0]
#print (x['codigo'])
#for k in x:
#	print (k,x[k])


#for k,v in dict1:
#	print (k,v)

"""
lista = {}
resultado = retorno2['cServico'][0]
lista = resultado
print (lista)


#print ('RETORNO1')
#print (retorno1['cServicosCalculo'])

#resultado2 = retorno1['cServicosCalculo']

#print ('RETORNO1[0]')
#print (retorno1['cServicosCalculo'][0])

#novalista = retorno1['cServicosCalculo']
#print ('NOVALISTA')
#print (novalista)

#print('TAMANHO')
#print (len(retorno1['cServicosCalculo']))

#maximo = len(retorno1['cServicosCalculo']
"""
