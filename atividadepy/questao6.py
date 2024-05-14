lista_convidados=['neymar','chico moedas','orochi','arthur aguiar','cabelinho']
for convite in lista_convidados:
 print('Estou lhe convidando para jantar',convite)
nome_removido='cabelinho'   
if nome_removido in lista_convidados:
 lista_convidados.remove(nome_removido)

print(f'O {nome_removido}','não pode comparecer')

lista_convidados2=['neymar','chico moedas','orochi','arthur aguiar','mbappe']
for convite2 in lista_convidados2:
 print('venha para aqui em casa comer um cuscuz,',convite2)
