/*
 * Soma dos N primeiros naturais — versão monolítica
 *
 * Sem estruturas de controle: só goto, labels e atribuições.
 * Cada label corresponde exatamente a um rótulo da notação formal
 * usada na Máquina de Traços (ver maquina_de_tracos/programas.py).
 *
 *   1: S := 0
 *   2: I := 1
 *   3: se I > N então vá para 7
 *   4: S := S + I
 *   5: I := I + 1
 *   6: vá para 3
 *   7: halt
 */

#include <stdio.h>

int main(void) {
    int N, S, I;

    printf("Informe N: ");
    scanf("%d", &N);

    S = 0;
    I = 1;

    rotulo3:
        if (I > N) goto rotulo7;
    rotulo4:
        S = S + I;                
    rotulo5:
        I = I + 1;                
    rotulo6:
        goto rotulo3;             

    rotulo7:                      
        printf("soma(1..%d) = %d\n", N, S);
        return 0;
}
