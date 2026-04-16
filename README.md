# Programas, Máquinas e Equivalência — AV1 Teoria da Computabilidade

**Disciplina:** Teoria da Computabilidade — Prof. Daniel Leal Souza
**Turma:** CC5NA

## Integrantes

**Davi Maciel Corrêa**
**Gabriel Alencar Albuquerque**
**Alberto Eduardo Acosta**

---

## Função implementada

**Soma dos N primeiros naturais:**

```
soma(N) = 1 + 2 + ... + N
```

| Entrada | Saída |
|---------|-------|
| N = 0   | 0     |
| N = 1   | 1     |
| N = 3   | 6     |
| N = 5   | 15    |
| N = 10  | 55    |

A função foi escolhida por ser simples o bastante para gerar traços legíveis na Máquina de Traços, mas rica o suficiente para evidenciar diferenças estruturais entre os três estilos de programa.

---

## Linguagens utilizadas

| Componente          | Linguagem |
|---------------------|-----------|
| Programa monolítico | C (gcc)   |
| Programa iterativo  | Python 3  |
| Programa recursivo  | Python 3  |
| Máquina de Traços   | Python 3  |

---

## Organização dos arquivos

```
.
├── README.md
├── monolitico/
│   └── soma.c              programa monolítico com goto; labels correspondem
│                           exatamente aos rótulos da notação formal
├── iterativo/
│   └── soma.py             programa iterativo (while explícito)
├── recursivo/
│   └── soma.py             programa recursivo (condição-base + chamada recursiva)
└── maquina_de_tracos/
    ├── maquina.py          engine da Máquina de Traços
    ├── programas.py        definições formais de P_mono e P_alt
    └── analise.py          script principal: gera fitas e analisa equivalência
```

---

## Como compilar e executar

### Pré-requisitos

- **C:** gcc (qualquer versão recente)
- **Python:** 3.8+

### Programa monolítico (C)

```bash
gcc -o monolitico/soma monolitico/soma.c
./monolitico/soma
# >> Informe N: 5
# >> soma(1..5) = 15
```

### Programa iterativo (Python)

```bash
python iterativo/soma.py
# >> Informe N: 5
# >> soma(1..5) = 15
```

### Programa recursivo (Python)

```bash
python recursivo/soma.py
# >> Informe N: 5
# >> soma(1..5) = 15
```

### Máquina de Traços (análise completa)

```bash
# roda a análise com N=3 (padrão)
cd maquina_de_tracos
python analise.py

# ou passa N como argumento
python analise.py 4
```

O script imprime:
1. A notação formal dos dois programas comparados (P_mono e P_alt)
2. A fita de traços de cada um
3. A demonstração de **equivalência forte** (P_mono ≡ P_iter_formal)
4. A demonstração de **não-equivalência** (P_mono ≢ P_alt)

---

## Descrição dos programas

### Monolítico (`monolitico/soma.c`)

Usa apenas `goto` e labels — sem `while`, `for` ou funções. Cada label numerado no código-fonte corresponde a um rótulo da descrição formal usada na Máquina de Traços:

```
1: S := 0         2: I := 1
3: se I > N → 7   4: S := S + I
5: I := I + 1     6: vá para 3    7: halt
```

### Iterativo (`iterativo/soma.py`)

Usa `while` explícito. Quando traduzido para notação monolítica formal, o `while I <= N` vira o par de instruções `(3: se I > N → halt, 6: goto 3)` — produzindo o mesmo programa que P_mono. Isso é a base da equivalência forte demonstrada.

### Recursivo (`recursivo/soma.py`)

Usa chamada recursiva com condição-base `soma(0) = 0`. Estrutura de execução fundamentalmente diferente: em vez de um loop sobre estados de memória compartilhada, empilha chamadas na stack. Por isso, a análise via Máquina de Traços exige normalização para comparação direta com os outros.

---

## Máquina de Traços — visão geral

A Máquina de Traços recebe um programa na notação formal (dicionário de rótulos → instruções) e um estado inicial, e produz a **fita de configurações**:

```
⟨rótulo, memória⟩  ⊢  ⟨rótulo', memória'⟩  ⊢  ...  ⊢  ⟨halt, memória_final⟩
```

**Dois programas são fortemente equivalentes** quando, para toda entrada, as suas fitas são idênticas — mesmos rótulos visitados, mesma sequência de estados de memória.

### Equivalência demonstrada: P_mono ≡ P_iter_formal

A tradução formal do programa iterativo Python gera exatamente os mesmos rótulos e as mesmas transições de memória de P_mono. Fitas identicas → equivalência forte.

### Não-equivalência demonstrada: P_mono ≢ P_alt

P_alt conta de N para 1 (I começa em N, decrementa). Para N = 3, o passo 2 já diverge:

```
P_mono : ⟨3, {N=3, S=0, I=1}⟩   ← I foi inicializado com 1
P_alt  : ⟨3, {N=3, S=0, I=3}⟩   ← I foi inicializado com N=3
```

Os estados de memória nunca voltam a coincidir, mesmo que a saída final (S = 6) seja a mesma. Mesma função computada, traços distintos → **não fortemente equivalentes**.

---

## Uso de Inteligência Artificial
Claude: Apoio à estruturação do README, principalmente apoio na implementação código da Máquina de Traços, ajudou apenas estruturalmente com comentários e identação dos códigos em geral.
Gamma: Uso para apresentação de slides melhor estruturada
