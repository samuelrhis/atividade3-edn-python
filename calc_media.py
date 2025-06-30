# Entrada das quatro notas
n1, n2, n3, n4 = map(float, input().split())

# Cálculo da média ponderada
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10

# Mostra a média com uma casa decimal
print(f"Media: {media:.1f}")

# Verifica a situação do aluno
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    media_final = (media + nota_exame) / 2
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media_final:.1f}")
