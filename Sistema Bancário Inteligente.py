count = count2 = count3 =  saldo = s = s1 = v = v1 = 0
r3 = si = ''
while True:
    print('''======= Banco do Brasil =======
[ 1 ] Criar Conta
[ 2 ] Depositar
[ 3 ] Sacar
[ 4 ] Extrato
[ 5 ] Sair''')
    r = int(input('Digite a opção: '))
    if r == 1 and si:
        print('Já tem uma conta \033[;32mEXISTENTE\033[m')
        continue
    if r == 1:
        print('===== Criando Conta =====')
        nome = str(input('Digite seu 1° nome: '))
        idade = int(input('Digite sua idade: '))
        sexo = str(input('Digite seu sexo: ')).upper().strip()
        r3 = str(input('Voce quer continuar? [S/N] ')).upper().strip()
        si = r3 == 'S'
        if idade < 12:
            print('A conta só pode ser criada se o sujeito for \033[;31mACIMA\033[m de 12 anos')
            continue
        if sexo not in 'FM':
            print('Dados Inválidos... tente novamente')
            continue
        if si:
            print('Obrigado por criar sua conta')
        elif r3 == 'N':
            print('OK, tenha um bom dia')
            continue
    elif r == 2 and si:
        depo = float(input('Digite o valor depositado: R$'))
        if depo <= 0:
            print('Dados Inválidos... tente novamente')
            continue
        else:
            print('Você depositou R${:.2f}'.format(depo))
            count2 += 1
            s += depo
        saldo += depo
    elif r == 3 and si:
        print('=' * 30)
        print('{:^30}'.format(f'Você {saldo} Na conta do Banco'))
        print('=' * 30)
        saque = float(input('Digite o valor sacado: R$'))
        if saque <= 0:
            print('Dados Inválidos... tente novamente')
            continue
        elif saque > saldo:
            print('Dados Inválidos... tente novamente')
            continue
        elif saque < saldo:
            r2 = str(input('Você realmente deseja sacar? [S/N] ')).upper().strip()
            if count3 == 3:
                print('Você atingiu limite de 3 saques... volte depois de um tempo')
                continue
            elif r2 == 'S':
                print('Ok, Você sacou R${:.2f}'.format(saque))
                saldo -= saque
                count3 += 1
                s1 += saque
            elif r2 == 'N':
                print('OK, tenha um bom dia')
                continue
            else:
                print('Dados Inválidos... tente novamente')
                continue
    elif r == 4 and si:
        if count2 == 1:
            v = 'Vez'
        elif count2 > 1:
            v = 'Vezes'
        if count3 == 1:
            v1 = 'Vez'
        elif count3 > 1:
            v1 = 'Vezes'
        print('-' * 30)
        print('{:^30}'.format('Extrato Bancário'))
        print(f'Nome: {nome}')
        print(f'Idade: {idade}')
        print(f'Gênero: {sexo}')
        print(f'Saldo: {saldo}')
        print(f'Você depositou {count2} {v} e o total depositado é {s}')
        print(f'Você saquou {count3} {v1} e o total sacado é {s1}')
        print('-' * 30)
    elif r == 5:
        break
    else:
        print('Dados Inválidos... tente novamente')
    count += 1
print('Saindo do Banco... Volte Sempre')
