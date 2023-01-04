import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC763005e7f4c4a567a2a289da03e0e6fa"
# Your Auth Token from twilio.com/console
auth_token = "4cef59c0e5c05b0ace62b278fedc5b0c"
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. O {vendedor} vendeu {vendas}]')
        message = client.messages.create(
            to="+5514997600175",
            from_="+19853068925",
            body=f'No mês {mes} alguém bateu a meta. O {vendedor} vendeu {vendas}]')

        print(message.sid)













# Para cada arquivo:

#Verificar se algum valor na coluna Vendas daquele arquivo é > que 55k

#If maior que 55k Envia SMS com o Nome, Mês e Vendas.
