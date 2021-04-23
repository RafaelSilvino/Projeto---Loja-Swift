"""
Sala: 9A
Gabriel Sales dos Santos
Pedro Henrique Perdim 
Rafael dos Santos Silvino
"""

print("+----------------------------------------+")
print("|               Loja Swift               |")
print("+----------------------------------------+")
print(" ")

print("+----------------------------------------+")
print("|            Tabela de Preço             |")
print("+----------------------------------------+")
print("| Código |Descrição       | Preço por kg |")
print("+----------------------------------------+")
print("|   1    |Picanha         |   R$ 45.00   |")
print("+----------------------------------------+")
print("|   2    |Salmão Selvagem |   R$ 70.00   |")
print("+----------------------------------------+")
print("|   3    |Alcatra         |   R$ 35.00   |")
print("+----------------------------------------+")
print("|   4    |Maminha         |   R$ 40.00   |")
print("+----------------------------------------+")
print(" ")

print("+-------------------------------------------------------------------+")
print("|                          Nota de compra                           |")
print("+-------------------------------------------------------------------+")

confirmacao = True

soma = 0

while confirmacao:

    codigo = int(input("Informe o código do produto: "))

    if codigo == 1:
        quant_1 = float(input('Informe a quantidade em kg: ')) 
        preco_1 = quant_1 * 45

        soma += preco_1

        print(f"|   1    | Picanha                      |   R$ {float(preco_1)}|    R$ {soma}|")
        print(" ")

    elif codigo == 2:
        quant_2 = float(input('Informe a quantidade em kg: ')) 
        preco_2 = quant_2 * 70

        soma += preco_2

        print(f"|   2    | Salmão Selvagem              |   R$ {float(preco_2)}|    R$ {soma}|")
        print(" ")
    
    elif codigo == 3:
        quant_3 = float(input('Informe a quantidade em kg: ')) 
        preco_3 = quant_3 * 35

        soma += preco_3

        print(f"|   3    | Alcatra                      |   R$ {float(preco_3)}|    R$ {soma}|")
        print(" ")
 
    elif codigo == 4:
        quant_4 = float(input('Informe a quantidade em kg: ')) 
        preco_4 = quant_4 * 40

        soma += preco_4

        print(f"|   4    | Maminha                      |   R$ {float(preco_4)}|    R$ {soma}|")
        print(" ")

    elif codigo > 4:
        print("Coloque um código de produto que realmente exista")
        print("")

    elif codigo == 0:
        print("Informe a quantidade em kg: 0")
        print(f"O total da compra foi de R$ {soma}")
        confirmacao = False
