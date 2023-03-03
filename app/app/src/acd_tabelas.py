from acd_lst.models import *
#from acd_lst.models import T21ListaTabelasDCP, T01TabelaDCP,T02TabelaDCP 

def tipos_de_campos(codigo):
    campos = []
    print("código: " + str(codigo))

    if (codigo == 17 or codigo ==18):
        print("tabelas de juros 0,5% \\e 1%")
    
    elif (codigo == 16):
        print("tabela de juros")
        campos = ['data',
                'cod_indexador',
                'meta_selic',
                'taxa_mensal']
        
    elif (codigo == 19):
        print("tabela SELIC")
        campos = ['data',
                'cod_indexador',
                'indice_correcao']

    elif (codigo == 20):
        # print("Tabela de Série Histórica")
        campos = ['ord',
               'vigencia',
               'moeda',
               'alteracao',
               'legislacao']
               
    
    elif (codigo == 24):
        #print("Tabela da WebGCALC")
        pass
    
    else:
        campos = ['data',
               'cod_indexador',
               'var_per_mensal',
               'num_indice_var_mensal',
               'fator_vigente',
               'indice_correcao']
    
    return campos


def criar_lista_campos(tab, codigo, campo):
    lista = []
    listaS = []    
    print("código: " + str(codigo))

    if (codigo == 17 or codigo ==18):
        # print("tabelas de juros 0,5% \\e 1%")
        pass
    
    elif (codigo == 16):
        # print("tabela de juros poupança")
        for i in range(tab.count()):
            listaS.append(i)
            listaS.append(tab.values()[i][campo[0]]) #t16_data
            listaS.append(tab.values()[i][campo[1]]) #t16_indexador
            percentual = tab.values()[i][campo[2]] #t16_meta_selic            
            listaS.append(percentual * 100) if percentual else listaS.append(0) # se percentual for null or nonetype vai dar erro
            percentual = tab.values()[i][campo[3]] #t16_taxa_mensal
            listaS.append(percentual * 100) if percentual else listaS.append(0) # se percentual for null or nonetype vai dar erro
            lista.append(listaS)
            listaS = []
    
    elif (codigo == 19):
        #  tabela SELIC        
        for i in range(tab.count()):
            listaS.append(i)
            listaS.append(tab.values()[i][campo[0]]) #t19_data
            listaS.append(tab.values()[i][campo[1]]) #t19_indexador
            percentual = tab.values()[i][campo[2]] #t19_indice
            listaS.append(percentual * 100) if percentual else listaS.append(0)
            lista.append(listaS)
            listaS = []

    elif (codigo == 20):
        # Tabela de Série Histórica 
        for i in range(tab.count()):
            listaS.append(i)
            listaS.append(tab.values()[i][campo[0]]) #t20_ord
            listaS.append(tab.values()[i][campo[1]]) #t20_vigencia
            listaS.append(tab.values()[i][campo[2]]) #t20_moeda
            listaS.append(tab.values()[i][campo[3]]) #t20_alteracao
            listaS.append(tab.values()[i][campo[4]]) #t20_legislacao
            lista.append(listaS)
            listaS = []
    
    elif (codigo == 24):
        # Tabela da WebGCALC
        pass

    else:
        percentual = 0       
        
        for i in range(tab.count()):
            listaS.append(i)
            listaS.append(tab.values()[i][campo[0]]) # data
            listaS.append(tab.values()[i][campo[1]]) # cod_indexador
            percentual = tab.values()[i][campo[2]] # var_per_mensal            
            listaS.append(percentual * 100) if percentual else listaS.append(0) # se percentual for null or nonetype vai dar erro# se percentual for null or nonetype vai dar erro
            listaS.append(tab.values()[i][campo[3]]) # num_indice_var_mensal
            listaS.append(tab.values()[i][campo[4]]) # fator_vigente
            listaS.append(tab.values()[i][campo[5]]) # indice_correcao
            lista.append(listaS)
            listaS = []            
    
    return lista


def postar_tabelas_indices(nome_tabela):

    selecao = T21ListaTabelasDCP.objects.get(t21_nome_tabela = nome_tabela)

    num_codigo_tabela = selecao.t21_cod_tabela    

    cod_tab = str(num_codigo_tabela)
    nome_tab = selecao.t21_nome_tabela
    descricao = str(selecao.t21_obs_tabela)
       
    prefixo = 't0'+ cod_tab  if len(cod_tab) < 2 else 't' + cod_tab 
    print("(acd_tabelas.py)")
    print("========== prefixo: " + prefixo)
    print("========== PREFIXO: " + prefixo.upper())

    
    listacampos = tipos_de_campos(num_codigo_tabela)

    campo = [ prefixo + '_' + listacampos[i] for i in range(len(listacampos))]
    tabela = eval(prefixo.upper() + 'TabelaDCP') #T01TabelaDCP    
    tabDCP = tabela.objects.all()
    
    print(campo)

    if tabDCP.count() == 0:
        return {}
    
    #print(tabDCP.count())
    #print(campo)

    listaP = criar_lista_campos(tabDCP, num_codigo_tabela, campo)

    data_atualizacao = listaP[-1][1]
    numero_linhas = len(listaP)
    
    print(f"========== data_atualizacao: {data_atualizacao}")
    print(f'========== tamanho da lista de índices: {numero_linhas}')
    print(f'========== código da tabela: {cod_tab}')
    print(f'========== tabela: {nome_tab}')
    #print(f'========== descrição: {descricao}')

    return {'tabela':nome_tab,
            'lista':listaP,
	    	'data_atualizacao':data_atualizacao,
	    	'tamanho':numero_linhas,
	    	'descricao':descricao,
            'codigo': cod_tab }
    