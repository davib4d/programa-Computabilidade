# Soma dos N primeiros naturais — versão recursiva
#
# Condição-base: soma(0) = 0
# Passo recursivo: soma(N) = N + soma(N-1)
#
# Computa a mesma função que os outros dois programas,
# mas via chamadas recursivas — estrutura de execução bem diferente,
# o que vai ficar claro na análise da Máquina de Traços.

def soma_recursiva(N):
    if N == 0:
        return 0
    return N + soma_recursiva(N - 1)

if __name__ == "__main__":
    N = int(input("Informe N: "))
    print(f"soma(1..{N}) = {soma_recursiva(N)}")
