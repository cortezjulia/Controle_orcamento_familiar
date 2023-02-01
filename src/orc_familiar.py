#PROJETO DE TABELA PARA CONTROLE DE ORÇAMENTO FAMILIAR
#OBJETIVO É EXERCITAR AS TÉCNICAS DE CONSTRUÇÃO DE FUNÇOES E TRABALHO COM LISTAS
import os

j=0
op_int=0
valores=[]
meses=[]
itens=[]
lista_posicoes=[]
valores_oficiais_habi=['','','','','','','','','','']
valores_oficiais_renda=['','','','','','']
valores_oficiais_saude=['','','','','']
valores_oficiais_impo=['','']
valores_oficiais_auto=['','','','','','','']
valores_oficiais_desppes=['','','','','','','','']
valores_oficiais_depe=['','','','','','','','']
valores_oficiais_lazer=['','','','','','','']
valores_oficiais_inv=['','','']

#LISTA DE ITENS FIXOS DE GASTOS
meses_oficiais=['JAN','FEV','MAR','ABR','MAR','ABR','MAI','JUN','JUL','AGO','SET','OUT','NOV','DEZ']
renda=['Salários','13º Salário','Férias','Renda extra','Alugueis','Juros de Investimento']
habitacao=['Prestação de compra','Aluguel','Água','IPTU','Luz','Telefone','TV por assinatura','Supermercado','Empregada','Reformas']
saude=['Plano de saúde','Médico','Dentista','Medicamentos','Seguro de vida']
imposto=['IRFF','INSS']
auto=['Prestação','Seguro','Combustível','Lavagens','IPVA','Mecânico','Multas']
desp_pessoais=['Higiene pessoal','Cosméticos','Cabelereiro','Vestuário','Lavanderia','Academia','Unhas','Cursos']
depententes=['Escola/Faculdade','Cursos Extras','Material escolar','Esportes/Uniformes','Mesada','Passeios/Férias','Vestuário','Saúde']
lazer=['Restaurantes','Restaurantes','Livraria','Streamings','Passagens','Hotéis','Passeios']
investimentos=['Previdência','Investimentos carro','Aplicações']

renda_printar=[]

#FUNÇÃO PARA GERAR MENU PRINCIPAL E RECEBER ESCOLHA DO USUARIO 
def menu_ini():
    global op_int
    print('*******Planilha de Controle de Orçamento Familiar******')
    
    print("                          ",*meses_oficiais, sep = "  ")
    
    print('',sep='\n')
    print('RENDA FAMILIAR --> DIGITE 1')
    print('',sep='\n')
    print(*renda,sep = "\n")
    print('',sep='\n')
    print('HABITAÇÃO --> DIGITE 2')
    print('',sep='\n')
    print(*habitacao, sep = "\n")
    print('',sep='\n')
    print('SAÚDE --> DIGITE 3')
    print('',sep='\n')
    print(*saude, sep = "\n")
    print('',sep='\n')
    print('IMPOSTOS --> DIGITE 4')
    print('',sep='\n')
    print(*imposto, sep = "\n")
    print('',sep='\n')
    print('AUTOMÓVEL --> DIGITE 5')
    print('',sep='\n')
    print(*auto, sep = "\n")
    print('',sep='\n')
    print('DESPESAS PESSOAIS --> DIGITE 6')
    print('',sep='\n')
    print(*desp_pessoais, sep = "\n")
    print('',sep='\n')
    print('DEPENDENTES --> DIGITE 7')
    print('',sep='\n')
    print(*depententes, sep = "\n")
    print('',sep='\n')
    print('LAZER --> DIGITE 8')
    print('',sep='\n')
    print(*lazer, sep = "\n")
    print('',sep='\n')
    print('INVESTIMENTOS --> DIGITE 9')
    print('',sep='\n')
    print(*investimentos, sep = "\n")
    while True:
        op=input('Insira o número correspondente ao tipo de gasto que quer inserir: ')
        #VERIFICA SE HÁ APENAS NUMEROS
        if op.isdigit()==False:
            continue
        #VERIFICA SE VALOR ESTÁ NA FAIXA PERMITIDA
        else:
            if int(op)<1 or int(op)>9:
                continue
            else:
                op_int=int(op)
                break
    
    #RECEBE OS VALORES DE MES, ITEM E VALOR QUE O USUARIO QUER ADICIONAR A TABELA
def recebe_valores(item,valor,mes):
   
    valores.append(valor)
    meses.append(mes)
    itens.append(item)




def salva_valores():
    global j
    global op_int
    #renda
    if op_int==1:
        i=0
        while i<len(renda):
                
            if renda[i]==itens[j]:
                valores_oficiais_renda.insert(i,valores[j])
            
            i+=1
        return 1
    #habitação
    #i=0
    #while i<len(habitacao):
        #   if habitacao[i]==itens[j]:
        #      valores_oficiais_habi.insert(i,valores[i])
            
        #  i+=1
    #saude
    elif op_int==2:
        i=0
        while i<len(saude):
            
            if saude[i]==itens[j]:
                valores_oficiais_saude.insert(i,valores[j])
                
            i+=1
        return 2

    #imposto
    elif op_int==3:
        i=0
        while i<len(imposto):
           
            if imposto[i]==itens[j]:
                valores_oficiais_impo.insert(i,valores[j])  
            
            i+=1
        return 3
    #auto
    elif op_int==4:
        i=0
        while i<len(auto):
            
            if auto[i]==itens[j]:
                valores_oficiais_auto.insert(i,valores[j])
            
            i+=1
        return 4

    #desp_pessoais
    elif op_int==5:
        i=0
        while i<len(desp_pessoais):
                
            if desp_pessoais[i]==itens[j]:
                valores_oficiais_desppes.insert(i,valores[j]) 
                
            i+=1
        return 5
            
    #dependentes
    elif op_int==6:
        i=0
        while i<len(depententes):
                
            if depententes[i]==itens[j]:
                valores_oficiais_depe.insert(i,valores[j]) 
            
            i+=1
        return 6

    #lazer
    elif op_int==7:
        i=0
        while i<len(lazer):
            
            if lazer[i]==itens[j]:
                valores_oficiais_lazer.insert(i,valores[j]) 
            
            i+=1
        return 7
    #investimentos
    elif op_int==8:
        i=0
        while i<len(investimentos):
                
            if investimentos[i]==itens[j]:
                valores_oficiais_inv.insert(i,valores[j])
                
            i+=1
        return 8
    j+=1
 

def impressao(op_escolhida):
        os.system('cls')
        global posicao
        global posicao_ref
        global m
        
        print('*******Planilha de Controle de Orçamento Familiar******')
        
        print("                          ",*meses_oficiais, sep = "  ")

        if op_escolhida==1:
            lista_item=renda
            lista_valor=valores_oficiais_renda
        if op_escolhida==2: 
            lista_item=saude 
            lista_valor=valores_oficiais_saude 
        if op_escolhida==3:
            lista_item=imposto
            lista_valor=valores_oficiais_impo
        if op_escolhida==4:
            lista_item=auto 
            lista_valor=valores_oficiais_auto
        if op_escolhida==5: 
            lista_item=desp_pessoais
            lista_valor=valores_oficiais_desppes   
        if op_escolhida==6:
            lista_item=depententes 
            lista_valor=valores_oficiais_depe 
        if op_escolhida==7: 
            lista_item=lazer 
            lista_valor=valores_oficiais_lazer
        if op_escolhida==8:
            lista_item=investimentos
            lista_valor=valores_oficiais_inv   
         

        m=0
        posicao_ref=22
        while m<len(lista_item):
            i=0

            if len(meses)>m:
           
                while i<len(meses_oficiais):
                    
                    if meses_oficiais[i]==meses[m]:
                        achou_mes=i
                        break
                    i+=1
            
                if achou_mes==0:
                    
                    posicao=posicao_ref
                else:
                    posicao=posicao_ref+(achou_mes*5)

                posicao_palavra=len(lista_item[m])
                posicao=posicao-posicao_palavra
                
                posicao_final=lista_item[m]+(posicao*' ')
                lista_posicoes.append(posicao_final)
            
            else:
                posicao_final=lista_item[m]+(posicao_ref*' ')
                lista_posicoes.append(posicao_final)
           
            m+=1
        i=0
        while i<len(lista_posicoes):
            print(lista_posicoes[i],lista_valor[i],end='\n')
            i+=1

        

                        
        
        
                   


              
while True:
    
    menu_ini()
    mes_usuario=input('Insira o mês: ')
    item_usuario=input('Insira o item: ')
    valor_usuario=input('Insira o valor: ')
    recebe_valores(item_usuario,valor_usuario,mes_usuario)
    recebe_item=salva_valores()
    impressao(recebe_item)
    

       




