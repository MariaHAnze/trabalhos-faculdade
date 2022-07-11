def dimensoesObjeto(): #definição da função de dimensões do objeto
    while True: #Enquanto os valores digitados para as dimensões do objeto forem numéricos, o programa rodará as condições if. Caso contrário, o programa  será interrompido (except Value Error) até que um número seja digitado.
        try:

            alt = float(input('Digite a altura do objeto em cm: '))
            comp = float(input('Digite o comprimento do objeto em cm: '))
            larg = float(input('Digite a largura do objeto em cm: '))
            vol = alt * comp * larg
            print(f'O volume do objeto é {vol:.2f} cm³.')
            if vol < 1000:
                return 10
            elif 1000 <= vol < 10000:
                return 20
            elif 10000 <= vol< 30000:
                return 30
            elif 30000 <= vol < 100000:
                return 50
            else:
                print('Não aceitamos objetos tão grandes! \nEntre com as dimensões novamente.')
                continue #caso as dimensões não correspondam às condições acima, o programa irá imprimir o texto acima. A função continue será executada, recomeçando a função dimensoesObjeto.
        except ValueError:
            print('Você digitou alguma dimensão com valor não numérico. \nEntre com as dimensões novamente.')
            continue #se não for digitado um valor numérico, o programa irá imprimir a mensagem acima, e a função dimensoesObjeto rodará novamente, até que valores numéricos sejam inseridos.

def rotaObjeto():
    while True:
        try:
            rota = str(input(
                'Selecione a rota: \nRS: de Rio de Janeiro para São Paulo \nSR: de São Paulo para Rio de Janeiro \nBS: de Brasília para São Paulo \nSB: de São Paulo para Brasília \nBR: de Brasília para Rio de Janeiro \nRB: de Rio de Janeiro para Brasília \n>> '))
            if rota == 'RS' or rota == 'SR':
                return 1
            if rota == 'BS' or rota == 'SB':
                return 1.2
            if rota == 'BR' or rota == 'RB':
                return 1.5
            else:
                print('Você digitou uma rota que não existe! \nEntre com uma rota válida novamente.')
                continue
        except ValueError:
            print('Você digitou uma rota que não existe. \nEntre com uma rota válida novamente.')

def pesoObjeto(): #a segunda função criada é referente ao peso do objeto, onde o programa vai testar as condições abaixo
    while True:
        try:
            peso = float(input('Digite o peso do objeto em kg: '))
            if peso <= 0.1:
                return 1
            if 0.1 <= peso < 1:
                return 1.5
            if 1 <= peso < 10:
                return 2
            if 10 <= 10 < 30:
                return 3
            else:
                print('Não aceitamos objetos tão pesados! \nEntre com os valores novamente.')
                continue #novamente, caso o peso do objeto seja diferente das condições acima, o programa ira imprimir a mensaem acima e o programa será executado novamente.
        except ValueError:
            print('Você digitou o peso com um valor não numérico. \nEntre com o peso novamente.')
            continue #se digitarmos uma letra, por exemplo, o input não será reconhecido, e a função pesoObjeto será executada novamente.

print('Bem vindo à companhia de logística Maria Helena Niedermaier Anze, RU: 4088829')

#este é o programa principal, invocando as funções de dimensão, peso e rota do objeto.

dim = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total = dim * peso * rota
print(f'O valor total a pagar será de R${total:.2f}')