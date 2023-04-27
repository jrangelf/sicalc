from copy import deepcopy
from src.verificacpf import formater
from acd_lst.models import Rubricas, CargoEmprego,OrgaoSiape

def formataDadosServidor (envelope):
	
	dict_dados_servidor = {}
	
	iu = envelope['identificacaoUnica']
	nome = envelope['nome']
	cpf = envelope['CPF']
	
	dict_dados_servidor['iu'] = iu
	dict_dados_servidor['cpf']= cpf
	dict_dados_servidor['nome'] = nome
	
	return dict_dados_servidor

  
def formataDataDeObito (envelope):
	
	str_envelope = str(envelope)

	if len(str_envelope) > 10:
		ano = str_envelope[0:4]
		mes = str_envelope[5:7]
		dia = str_envelope[8:10]
		datadeobito = dia + '/' + mes + "/" + ano

	return datadeobito


def formataFichaFinanceira(envelope):

	def remove_repetidos(l0):
		l = []
		for i in l0:
			if i not in l:
				l.append(i)
				l.sort()
		return l

	def posicao_sufixo_meses(anomes):
		pos = int(str(anomes)[4:6]) - 1
		return pos

	def insere_pagamentos(lista1, lista2):
		l1 = deepcopy(lista1)
		l2 = deepcopy(lista2)

		for n in range(len(l1)):

			ano1 = l1[n][0]
			org1 = l1[n][1]
			rub1 = l1[n][2]
			nom1 = l1[n][3]
			ren1 = l1[n][4]
			seq1 = l1[n][5]

			for m in range(len(l2)):

				ano2 = l2[m][0]
				org2 = l2[m][1]
				rub2 = l2[m][2]
				nom2 = l2[m][3]
				ren2 = l2[m][4]
				seq2 = l2[m][5]
				dat2 = l2[m][6]
				vlr2 = l2[m][7]

				if ano1 == ano2 and org1 == org2 and rub1 == rub2 and ren1 == ren2 and seq1 == seq2:
					pos = posicao_sufixo_meses(dat2)
					l1[n][6][pos] = vlr2

		return l1

	def consolidar_registros(registros):

		reg_aux = deepcopy(registros)

		# cria uma lista sem a data e o valor pago
		lista_aux = []
		for i in range(len(reg_aux)):
			aux = reg_aux[i]
			del aux[7]
			del aux[6]
			lista_aux.append(aux)

		# ordena a lista criada
		lista_ord = []
		lista_ord = remove_repetidos(lista_aux)

		# insere na lista ordenada e sem repetições
		# o sufixo com os meses
		for i in range(len(lista_ord)):
			lista_ord[i].append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

		x1 = [] + lista_ord
		x2 = deepcopy(registros)

		lista_final = []
		lista_final = insere_pagamentos(x1, x2)

		return lista_final
	

	ficha = envelope	
	quantidade_fichas = len(ficha)		
	#print ("Quantidade de fichas:", quantidade_fichas)

	registros, cadastros = [], []
		
	#rubricas_db = Rubricas.objects.all()
	#for j in rubricas_db:
	#	print(j)
		
	#rub = Rubricas.objects.get(codigorubrica='13')
	#print ("Rubrica:", rub.nomerubrica)
	#print("quantidade_fichas:" + str(quantidade_fichas))
	
	if quantidade_fichas > 0:
			
		for i in range(quantidade_fichas):
				
			servidor = ficha[i]['nome']
			cpf = ficha[i]['CPF']
			ano = ficha[i]['ano']
			iu = ficha[i]['identificacaoUnica']
			
			#print ("Ficha Financeira de: ", ano, '\n')
			#print ("Servidor: ",iu, ' - ', servidor, '\n', )

			quantidade_vinculos = len(ficha[i]['vinculos']['vinculo'])
			#print ("Quantidade de vínculos na ficha:", i, " :", quantidade_vinculos)		
			
			#print('(1) ========================')
			#print(ficha[i])

			for j in range(quantidade_vinculos):			
				
				codigo_orgao = ficha[i]['vinculos']['vinculo'][j]['codOrgao']
				matricula = ficha[i]['vinculos']['vinculo'][j]['matricula']
				codigo_grupo_cargo = ficha[i]['vinculos']['vinculo'][j]['codGrupoCargo']
				codigo_cargo = ficha[i]['vinculos']['vinculo'][j]['codCargo']
				classe = ficha[i]['vinculos']['vinculo'][j]['classe']
				padrao = ficha[i]['vinculos']['vinculo'][j]['padrao']
				sigla_regime = ficha[i]['vinculos']['vinculo'][j]['siglaRegimeJuridico']
				
				quantidade_itens=len(ficha[i]['vinculos']['vinculo'][j]['fichaFinanceira']['itemFichaFinanceira'])
				
				#print("CodCargo:",codigo_cargo,"    CodGrupoCargo:",codigo_grupo_cargo)
				#print("(2) =============================")
				#print(ficha[i]['vinculos']['vinculo'][j])
				nomecargo = ''
				nomeorgao = OrgaoSiape.objects.get(codigo=str(codigo_orgao))
				if codigo_cargo != 0 and codigo_grupo_cargo != 0:				
					nomecargo = CargoEmprego.objects.get(codcargo=codigo_cargo, codgrupocargo=codigo_grupo_cargo)
				
				cad = {'ano':ano,'orgao':codigo_orgao,'matricula':matricula,'codgcargo':codigo_grupo_cargo,'codcargo':codigo_cargo,'classe':classe,'padrao':padrao,'sigla':sigla_regime,'nomeorgao':nomeorgao,'nomecargo':nomecargo}
				cadastros.append(cad)

				for k in range(quantidade_itens):
					
					rubrica = ficha[i]['vinculos']['vinculo'][j]['fichaFinanceira']['itemFichaFinanceira'][k]['codigo']
					rendimento = ficha[i]['vinculos']['vinculo'][j]['fichaFinanceira']['itemFichaFinanceira'][k]['rendimento']
					sequencia = ficha[i]['vinculos']['vinculo'][j]['fichaFinanceira']['itemFichaFinanceira'][k]['sequencia']
					datapgto = ficha[i]['vinculos']['vinculo'][j]['fichaFinanceira']['itemFichaFinanceira'][k]['dataPagamento']
					valor = ficha[i]['vinculos']['vinculo'][j]['fichaFinanceira']['itemFichaFinanceira'][k]['valor']
					
					nomerubrica = Rubricas.objects.get(codigorubrica=str(rubrica))
					

					reg = [ano,codigo_orgao, rubrica, str(nomerubrica), rendimento,sequencia,datapgto,float(valor)]
					registros.append(reg)
					
		print ("Servidor: ",iu, ' - ', servidor, '\n', )
		dados_cadastro = {'iu':iu,'nome':servidor,'registros':cadastros}
	else:
		dados_cadastro = {'iu':'','nome':'','registros':''}
		
	#print ("Cadastros:----------------------------------")
	#for i in cadastros:
	#	print (i)
	#print("Dados cadastro:--------------------------------")
	#for i in dados_cadastro.items():
	#	print (i)
	
	#print("=============================================")
	#print ()
	#print("=============================================")

	registros_meses_consolidados =[]
	registros_meses_consolidados = consolidar_registros(registros)

	dicionario = {'cadastro':dados_cadastro,'lancamentos':registros_meses_consolidados}
	
	return dicionario
	


	
			

