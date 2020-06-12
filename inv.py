from datetime import date

resumo_ops = list()  # Lista mestra
operacoes = list()

print('=' * 50)
mont_inicial = float(input('Montante inicial: R$'))
soma_saida: float = 0

while True:
    print('=' * 50)
    qtd_papeis = int(input('Informe a quantidade de papeis comprados: '))
    operacoes.append(qtd_papeis)  # Registro 0
    if qtd_papeis == 0:
        break

    v_ent = float(input('Valor de entrada no papel: R$'))
    operacoes.append(v_ent)  # Registro 1

    v_saida = float(input('Valor de saída no saída: R$'))
    operacoes.append(v_saida)  # Registro 2

    tot_ent = v_ent * qtd_papeis
    operacoes.append(tot_ent)  # Registro 3

    tot_saida = v_saida * qtd_papeis
    operacoes.append(tot_saida)  # Registro 4

    resut_saida = tot_saida - tot_ent  # ganho/perda
    soma_saida += resut_saida  # Acumulador de ganhos/perdas
    operacoes.append(resut_saida)  # Registro 5

    resumo_ops.append(operacoes[:])
    operacoes.clear()

mont_final = mont_inicial + soma_saida

# Criando relatório
arquivo = open('Resumo_dia.txt', 'a', encoding='UTF-8')
arquivo.write(f'{"=" * 105}\n')
arquivo.write(f'RESUMO TRANSAÇÕES DIA {date.today()}'.center(105))
arquivo.write(f'\n{"-" * 105}\n')
arquivo.write(f'{"QTD":<7}{"ENTRADA UND":<20}{"SAÍDA UND":<20}{"TOTAL ENTRADA":<20}{"TOTAL SAÍDA":<15}'
              f'{"GANHO/PERDA":>8}\n')
arquivo.write(f'{"-" * 105}\n')
for i, a in enumerate(resumo_ops):
    arquivo.write(f'{a[0]:<6} R${a[1]:<17.2f} R${a[2]:<17.2f} R${a[3]:<17.2f} R${a[4]:<15.2f} R${a[5]:<8.2f}\n')
arquivo.write(f'{"-" * 105}\n')
arquivo.write(f'-> Valor montante inicial: R${mont_inicial:.2f}\n')
arquivo.write(f'-> Montante final: R${mont_final:.2f}\n')
arquivo.write(f'-> Valor ganho R${soma_saida:.2f}\n')
arquivo.close()

print('=' * 105)
print(f'{"Op.":<5}{"QTD":<7}{"ENTRADA UND":<20}{"SAÍDA UND":<20}{"TOTAL ENTRADA":<20}{"TOTAL SAÍDA":<15}'
      f'{"GANHO/PERDA":>8}')  # Formatação de espaçamentos (cabeçalho)
print('=' * 105)

for i, a in enumerate(resumo_ops):
    print(f'{i + 1:<4} {a[0]:<6} R${a[1]:<17.2f} R${a[2]:<17.2f} R${a[3]:<17.2f} R${a[4]:<15.2f} R${a[5]:<8.2f}')

print('=' * 105)
print(f'-> Valor montante inicial: R${mont_inicial:.2f}')
print(f'-> Montante final: R${mont_final:.2f}')
print(f'-> Valor ganho R${soma_saida:.2f}')
