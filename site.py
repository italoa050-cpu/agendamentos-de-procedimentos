nome = input('Qual o seu nome? ')
email = input('Digite seu e-mail: ')
senha = input('Digite sua senha: ')

print('\nCadastro realizado com sucesso!')
print(f'Bem vindo ao sistema de agendamentos Kaidesigns, {nome}!\n')

print('Escolha seu procedimento:')
print('1 - Sobrancelha (R$100)')
print('2 - Design + Henna (R$150)')
print('3 - Brow Lamination (R$200)')

opcao = int(input('Digite o número do procedimento: '))

if opcao == 1:
    valor_procedimento = 100
elif opcao == 2:
    valor_procedimento = 150
elif opcao == 3:
    valor_procedimento = 200
else:
    print('Procedimento inválido')
    exit()

print(f'O valor do procedimento é R$ {valor_procedimento}')

valor_sinal = float(input('Digite o valor do sinal para confirmar o agendamento: '))

valor_restante = valor_procedimento - valor_sinal

if valor_sinal > 0:
    print('\n✅ Procedimento agendado com sucesso!')
    print(f'Sinal pago: R$ {valor_sinal}')
    print(f'Falta pagar no dia: R$ {valor_restante:.2f}')
else:
    print('❌ Agendamento não confirmado. Sinal não pago.')