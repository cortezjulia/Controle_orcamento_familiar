valores=[]
meses=[]
itens=[]
valores_oficiais_habi=[]
valores_oficiais_renda=[]
valores_oficiais_saude=[]
valores_oficiais_impo=[]
valores_oficiais_auto=[]
valores_oficiais_desppes=[]
valores_oficiais_depe=[]
valores_oficiais_lazer=[]
valores_oficiais_inv=[]
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
    i=0
    while i<len(meses_oficiais) and flag_itens==0:
        if meses_oficiais[i]==meses[i]:
            flag_itens=1
        i+=1
    #renda
    i=0
    while i<len(renda):
        if renda[i]==itens[i]:
            valores_oficiais_renda.append(valores[i])
        i+=1
    #habitação
    i=0
    while i<len(habitacao):
        if habitacao[i]==itens[i]:
            valores_oficiais_habi.append(valores[i])
        i+=1
    #saude
    i=0
    while i<len(saude):
        if saude[i]==itens[i]:
            valores_oficiais_saude.append(valores[i])
        i+=1
    #imposto
    i=0
    while i<len(imposto):
        if imposto[i]==itens[i]:
            valores_oficiais_impo.append(valores[i])  
        i+=1
    #auto
    i=0
    while i<len(auto):
        if auto[i]==itens[i]:
            valores_oficiais_auto.append(valores[i])
        i+=1
    #desp_pessoais
    i=0
    while i<len(desp_pessoais):
        if desp_pessoais[i]==itens[i]:
            valores_oficiais_desppes.append(valores[i]) 
        i+=1
    
    #dependentes
    i=0
    while i<len(depententes):
        if depententes[i]==itens[i]:
            valores_oficiais_depe.append(valores[i]) 
        i+=1

    #lazer
    i=0
    while i<len(lazer):
        if lazer[i]==itens[i]:
            valores_oficiais_lazer.append(valores[i]) 
        i+=1
    #investimentos
    i=0
    while i<len(investimentos):
        if investimentos[i]==itens[i]:
            valores_oficiais_inv.append(valores[i])
        i+=1
    
    print('***Planilha de Controle de Orçamento Familiar***')
    print(*meses_oficiais, sep = " ")
    print(*renda, sep = "\n")





while True:
    mes_usuario=input('Insira o mês: ')
    item_usuario=input('Insira o item: ')
    valor_usuario=input('Insira o valor: ')
    recebe_valores(item_usuario,valor_usuario,mes_usuario)

    imprime_valores()
        




