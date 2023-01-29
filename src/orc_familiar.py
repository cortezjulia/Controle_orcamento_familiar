#PROJETO DE TABELA PARA CONTROLE DE ORÇAMENTO FAMILIAR
#OBJETIVO É EXERCITAR AS TÉCNICAS DE CONSTRUÇÃO DE FUNÇOES E TRABALHO COM LISTAS
import os



op_int=0
j=0
posicao_ref=28
posicao=30
valores=[]
meses=[]
itens=[]
valores_oficiais_habi=['','','','','','','','','','']
valores_oficiais_renda=['','','','','','']
valores_oficiais_saude=['','','','','']
valores_oficiais_impo=['','']
valores_oficiais_auto=['','','','','','','']
valores_oficiais_desppes=['','','','','','','','']
valores_oficiais_depe=['','','','','','','','']
valores_oficiais_lazer=['','','','','','','']
valores_oficiais_inv=['','','']

#LISTA DE VALORES PRÉ-DEFINIDOS DE PARAMETROS PARA USUÁRIO ALTERAR
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

#FUNÇÃO PARA GERAR MENU PRINCIPAL E RECEBER ESCOLHA DO USUARIO 
def menu_ini():
    os.system('cls') 
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
                global op_int
                op_int=int(op)
                break


#RECEBE OS VALORES DE MES, ITEM E VALOR QUE O USUARIO QUER ADICIONAR A TABELA
def recebe_valores(item,valor,mes):
   
    valores.append(valor)
    meses.append(mes)
    itens.append(item)
    for salvo in itens:
        print(salvo)
    for salvo in valores:
        print(salvo)
    for salvo in meses:
        print(salvo)


def imprime_valores():
        
   
        flag_itens=0
        global j
        global op_int
        global posicao
        global posicao_ref
 
        i=0
        while i<len(meses_oficiais) and flag_itens==0:
            if meses_oficiais[i]==meses[j]:
                flag_itens=1
                if i==0:
                    posicao_ref=28
                    posicao=posicao_ref
                else:

                    posicao=posicao_ref+(i*5)    
            i+=1
        #renda
        if op_int==1:
            i=0
            while i<len(renda):
                
                if renda[i]==itens[j]:
                    valores_oficiais_renda.insert(i,valores[j])
            
                i+=1
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
        #imposto
        elif op_int==3:
            i=0
            while i<len(imposto):
           
                if imposto[i]==itens[j]:
                    valores_oficiais_impo.insert(i,valores[j])  
            
                i+=1
        #auto
        elif op_int==4:
            i=0
            while i<len(auto):
            
                if auto[i]==itens[j]:
                    valores_oficiais_auto.insert(i,valores[j])
            
                i+=1
        #desp_pessoais
        elif op_int==5:
            i=0
            while i<len(desp_pessoais):
                
                if desp_pessoais[i]==itens[j]:
                    valores_oficiais_desppes.insert(i,valores[j]) 
                
                i+=1
            
        #dependentes
        elif op_int==6:
            i=0
            while i<len(depententes):
                
                if depententes[i]==itens[j]:
                    valores_oficiais_depe.insert(i,valores[j]) 
            
                i+=1

        #lazer
        elif op_int==7:
            i=0
            while i<len(lazer):
            
                if lazer[i]==itens[j]:
                    valores_oficiais_lazer.insert(i,valores[j]) 
            
                i+=1
        #investimentos
        elif op_int==8:
            i=0
            while i<len(investimentos):
                
                if investimentos[i]==itens[j]:
                    valores_oficiais_inv.insert(i,valores[j])
                
                i+=1
        j+=1
        
        
        print('*******Planilha de Controle de Orçamento Familiar******')
    
        print("                          ",*meses_oficiais, sep = "  ")
        
        k=0
        while k<len(renda):

            posicao_palavra=len(renda[k])
            posicao_final=posicao-posicao_palavra
            item_printar=renda[k]+(posicao_final*' ')
            print(renda[k],item_printar[k],end="\n") 
            
            k+=1          


              
while True:
    menu_ini()
    mes_usuario=input('Insira o mês: ')
    item_usuario=input('Insira o item: ')
    valor_usuario=input('Insira o valor: ')
    recebe_valores(item_usuario,valor_usuario,mes_usuario)
    os.system('cls') 
    imprime_valores()
       




