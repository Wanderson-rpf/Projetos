from datetime import date


def linha(valor=50):
    print('=' * valor)


def leiaDinheiro(msg):
    """
    -> Função para substituir o "." por ","
    na separação dos centavos e validar o valor informado.
    :param msg: Entrada do usuário
    :return: Retorna o valor do tipo float
    """
    valido = False
    while not valido:
        valor = str(input(msg)).replace(',', '.')
        if valor.isalpha() or valor.strip() == '':
            print('Valor incorreto, tente novamente.')
        else:
            valido = True
            return float(valor)


def leiaInt(msg):
    """
    -> Função para validação de valor inteiro.
    :param msg: Entrada do valor pelo usuário.
    :return: Retorna o valor inteiro caso não ocorra erro.
    """
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, SyntaxError):
            print('Valor incorreto, tente novamente.')
        except Exception:
            print('Ocorreu um erro inesperado.')
        else:
            return valor


def criaArquivo(nome):
    """
    -> Função para criar aquivo com resumo das operações realizadas,
    com espaçamentos no cabeçalho e nas informações, incrementa o arquivo
    a cada registro, não excluindo registro anteriores.
    :param nome: Definido na função, deve conter a extenção (exemplo: teste.txt)
    :return: Cria o relatório
    """
    global arquivo
    try:
        arquivo = open(nome, 'a', encoding='UTF-8')
    except Exception:
        print('Ocorreu um erro na criação do aquivo.')
    else:
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
    finally:
        arquivo.close()


def resumoOperacao():
    linha(105)
    print(f'{"Op.":<5}{"QTD":<7}{"ENTRADA UND":<20}{"SAÍDA UND":<20}{"TOTAL ENTRADA":<20}{"TOTAL SAÍDA":<15}'
          f'{"GANHO/PERDA":>8}')
    linha(105)
    for i, a in enumerate(resumo_ops):
        print(f'{i + 1:<4} {a[0]:<6} R${a[1]:<17.2f} R${a[2]:<17.2f} R${a[3]:<17.2f} R${a[4]:<15.2f} R${a[5]:<8.2f}')
    linha(105)
    print(f'-> Valor montante inicial: R${mont_inicial:.2f}')
    print(f'-> Montante final: R${mont_final:.2f}')
    print(f'-> Valor ganho R${soma_saida:.2f}')


resumo_ops = list()  # Lista com todas as transações
operacoes = list()  # lista de transações individuais
soma_saida: float = 0  # Contador
mont_inicial = leiaDinheiro('Montante inicial: R$')

while True:
    linha()
    qtd_papeis = leiaInt('Informe a quantidade de papeis comprados ou "0" para sair: ')
    operacoes.append(qtd_papeis)  # Registro 0
    if qtd_papeis == 0:
        break

    v_ent = leiaDinheiro('Valor de entrada no papel: R$')
    operacoes.append(v_ent)  # Registro 1
    v_saida = leiaDinheiro('Valor de saída no saída: R$')
    operacoes.append(v_saida)  # Registro 2
    tot_ent = v_ent * qtd_papeis
    operacoes.append(tot_ent)  # Registro 3
    tot_saida = v_saida * qtd_papeis
    operacoes.append(tot_saida)  # Registro 4
    resut_saida = tot_saida - tot_ent  # ganho/perda
    soma_saida += resut_saida
    operacoes.append(resut_saida)  # Registro 5
    resumo_ops.append(operacoes[:])
    operacoes.clear()
mont_final = mont_inicial + soma_saida

criaArquivo('Resumo dia.txt')
resumoOperacao()
