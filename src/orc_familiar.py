valores_f1=[]
meses_f1=[]
itens_f1=[]

def f1_itens(item,valor,mes):
   
    valores_f1.append(valor)
    meses_f1.append(mes)
    itens_f1.append(item)
    for salvo in itens_f1:
        print(salvo)
    for salvo in valores_f1:
        print(salvo)
    for salvo in meses_f1:
        print(salvo)


meses_oficiais=['JAN','FEV','MAR','ABR','MAR','ABR','MAI','JUN','JUL','AGO','SET','OUT','NOV','DEZ']
itens_oficiais=['Salários','13º Salário','Férias','Renda extra','Alugueis','Juros de Investimento',\
'Outros','Prestação de compra','Aluguel','Água','IPTU','Luz','Telefone','TV por assinatura',\
'Supermercado','Empregada','Reformas','Plano de saúde','Médico','Dentista','Medicamentos','Seguro de vida',\
]


while True:
    mes_usuario=input('Insira o mês: ')
    item_usuario=input('Insira o item: ')
    valor_usuario=input('Insira o valor: ')
    f1_itens(item_usuario,valor_usuario,mes_usuario)
        




