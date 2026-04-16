# Soma dos N primeiros naturais — versão iterativa
#
# Estrutura explícita de repetição (while), sem recursão.
# Mapeia diretamente para P_mono na notação formal da Máquina de Traços:
# o while é equivalente ao par (se_goto + goto) do programa monolítico.

def soma_iterativa(N):
    S = 0  
    I = 1   
    while I <= N:  
        S = S + I   
        I = I + 1   
                    
    return S        

if __name__ == "__main__":
    N = int(input("Informe N: "))
    print(f"soma(1..{N}) = {soma_iterativa(N)}")
