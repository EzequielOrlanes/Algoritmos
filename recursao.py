def fatorial(x):
    if x == 1:
        return 1
    else:
        return x * fatorial(x - 1)


num = int(input("Insira o número do qual deseja saber o fatorial:"))
print(fatorial(num))

# Como esse código cria uma piha de chamadas de função:
# quarta fatorial (1) ---> primeira a retornar
# terceira fatorial (2) ---> segunda a retornar
# segunda fatorial (3) ---> terceira a retornar
# primeira fatorial(4) ---> quarta e ultima função a retornar.
# Exemplo: 4 * (3 * ( 2 *1 )) = 24
