import pandas as pd
from twilio.rest import Client

#conexao com id da twilio para disparo de sms
account_sid = 'AC2c89e005d30a2d52064b668627f54xxx'
auth_token = '40b81bdcfdd1bc637eec0801d922exxx'
client = Client(account_sid, auth_token)

#Abrindo os arquivos do excel e enviando a mensagem
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] >= 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] >= 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] >= 55000,'Vendas'].values[0]
        print(f'No mês {mes} o vendedor(a) {vendedor} bateu a meta de vendas com o valor de {vendas}')
        message = client.messages.create(
            body=f'No mês de {mes} o vendedor(a) {vendedor} bateu a meta de vendas com o valor de {vendas}',
            from_='+19378588327',
            to='+551197038xxxx'
        )
        print(message.sid)

