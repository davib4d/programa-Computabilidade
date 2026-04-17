.intel_syntax noprefix

.section .data
prompt:  .asciz "Informe N: "
fmt_in:  .asciz "%d"
fmt_out: .asciz "soma(1..%d) = %d\n"

.section .bss
.lcomm N, 4
.lcomm S, 4
.lcomm I, 4

.section .text
.globl main
main:
    push rbp
    mov rbp, rsp
    sub rsp, 16

    # printf("Informe N: ")
    lea rdi, [rip + prompt]
    xor eax, eax
    call printf

    # scanf("%d", &N)
    lea rdi, [rip + fmt_in]
    lea rsi, [rip + N]
    xor eax, eax
    call scanf

    # S = 0; I = 1;
    mov dword ptr [rip + S], 0
    mov dword ptr [rip + I], 1

rotulo3:
    mov eax, dword ptr [rip + I]
    mov ecx, dword ptr [rip + N]
    cmp eax, ecx
    jg rotulo7
rotulo4:
    mov eax, dword ptr [rip + S]
    add eax, dword ptr [rip + I]
    mov dword ptr [rip + S], eax
rotulo5:
    mov eax, dword ptr [rip + I]
    add eax, 1
    mov dword ptr [rip + I], eax
rotulo6:
    jmp rotulo3

rotulo7:
    # printf("soma(1..%d) = %d\n", N, S)
    lea rdi, [rip + fmt_out]
    mov esi, dword ptr [rip + N]
    mov edx, dword ptr [rip + S]
    xor eax, eax
    call printf

    mov eax, 0
    leave
    ret
