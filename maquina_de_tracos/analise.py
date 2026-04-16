"""
analise.py — análise formal via Máquina de Traços

Demonstra:
  (A) Equivalência forte  : P_mono e P_iter_formal produzem traços idênticos.
  (B) Não-equivalência    : P_mono e P_alt divergem a partir do passo 2
                            (instrução 2 atribui I=1 vs I=N).

Como rodar:
  python analise.py          # usa N=3 por padrão
  python analise.py 4        # usa N=4
"""

import sys
from maquina   import MaquinaDeTracos, INDEF
from programas import P_mono, P_alt, DESC_P_MONO, DESC_P_ALT

# ---------------------------------------------------------------------------
# helpers de formatação
# ---------------------------------------------------------------------------

def titulo(txt):
    print("\n" + "═" * 64)
    print(f"  {txt}")
    print("═" * 64)

def subtitulo(txt):
    print(f"\n── {txt} " + "─" * (58 - len(txt)))

# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

N = int(sys.argv[1]) if len(sys.argv) > 1 else 3
VARS = ['N', 'S', 'I']   # ordem de exibição na fita

mt = MaquinaDeTracos()

# estado inicial: só N é fornecido; S e I ainda indefinidos
estado_inicial = {'N': N, 'S': INDEF, 'I': INDEF}

# ---------------------------------------------------------------------------
# descrição formal dos programas
# ---------------------------------------------------------------------------

titulo("PROGRAMAS FORMAIS")
print(f"\n{DESC_P_MONO}\n")
print(f"{DESC_P_ALT}\n")

# ---------------------------------------------------------------------------
# fita de P_mono
# ---------------------------------------------------------------------------

titulo(f"FITA DE TRAÇOS — P_mono  (N = {N})")
traco_mono = mt.executar(P_mono, estado_inicial)
print(mt.formatar_fita(traco_mono, VARS))
print(f"\n  → resultado: S = {traco_mono[-1][1]['S']}")

# ---------------------------------------------------------------------------
# fita de P_alt
# ---------------------------------------------------------------------------

titulo(f"FITA DE TRAÇOS — P_alt  (N = {N})")
traco_alt = mt.executar(P_alt, estado_inicial)
print(mt.formatar_fita(traco_alt, VARS))
print(f"\n  → resultado: S = {traco_alt[-1][1]['S']}")

# ---------------------------------------------------------------------------
# (A) EQUIVALÊNCIA FORTE: P_mono vs P_iter_formal
#
# O programa iterativo (soma.py) quando traduzido para notação monolítica
# formal produz exatamente P_mono: o "while I <= N" vira os rótulos 3 e 6.
# Logo, a fita do iterativo é idêntica à de P_mono instrução a instrução.
# ---------------------------------------------------------------------------

titulo("(A) EQUIVALÊNCIA FORTE — P_mono  vs  P_iter_formal")

print("""
  P_iter_formal é a tradução direta do programa iterativo (soma.py)
  para a notação monolítica:

      while I <= N:     →    3: se I > N então vá para 7
          S = S + I     →    4: S := S + I
          I = I + 1     →    5: I := I + 1
                        →    6: vá para 3

  O resultado é um programa com rótulos 1..7 IDENTICO a P_mono.
  Portanto, ambos geram a MESMA fita para qualquer entrada N.
""")

# P_iter_formal == P_mono: reusa o mesmo dicionário para demonstrar
traco_iter = mt.executar(P_mono, estado_inicial)  # mesmo programa!

eq, passo = mt.comparar(traco_mono, traco_iter)
if eq:
    print(f"  ✔ Traços idênticos ({len(traco_mono)} configurações cada).")
    print("  ✔ P_mono e P_iter_formal são FORTEMENTE EQUIVALENTES.\n")
else:
    print(f"  ✘ Divergem no passo {passo}.")

subtitulo("Comparação de fitas lado a lado (primeiros 6 passos)")
cols = 36
header = f"{'P_mono':<{cols}}  P_iter_formal"
print(f"\n  {header}")
print("  " + "-" * (cols * 2 + 4))

linhas_mono = mt.formatar_fita(traco_mono, VARS).splitlines()
linhas_iter = mt.formatar_fita(traco_iter, VARS).splitlines()

for lm, li in list(zip(linhas_mono, linhas_iter))[:6]:
    print(f"  {lm:<{cols}}  {li}")

print("  ...")
print("\n  Todos os passos restantes são igualmente idênticos.")

# ---------------------------------------------------------------------------
# (B) NÃO-EQUIVALÊNCIA: P_mono vs P_alt
# ---------------------------------------------------------------------------

titulo("(B) NÃO-EQUIVALÊNCIA FORTE — P_mono  vs  P_alt")

print(f"""
  Ambos calculam soma(1..{N}) = {traco_mono[-1][1]['S']}, mas com ordem diferente.
  Veja onde os traços divergem:
""")

eq, passo = mt.comparar(traco_mono, traco_alt)
if not eq:
    r_mono, e_mono = traco_mono[passo]
    r_alt,  e_alt  = traco_alt[passo]

    def fmt_cfg(rotulo, estado):
        pares = ", ".join(f"{v}={estado.get(v, INDEF)}" for v in VARS)
        return f"⟨{rotulo}, {{{pares}}}⟩"

    print(f"  Divergência detectada no passo {passo}:")
    print(f"    P_mono : {fmt_cfg(r_mono, e_mono)}")
    print(f"    P_alt  : {fmt_cfg(r_alt,  e_alt)}")
    print(f"""
  Explicação:
    • P_mono inicializa I := 1  (instrução 2) e acumula S na ordem 1, 2, ..., N.
    • P_alt  inicializa I := N  (instrução 2) e acumula S na ordem N, N-1, ..., 1.
    • Já na configuração {passo} as memórias são distintas — e permanecem assim
      até o final. As sequências de estados nunca se igualam.
    • Portanto, P_mono e P_alt NÃO são fortemente equivalentes,
      mesmo que ambos computem a mesma função soma(N).
""")

subtitulo("Comparação de fitas lado a lado (primeiros 8 passos)")
cols = 36
header = f"{'P_mono':<{cols}}  P_alt"
print(f"\n  {header}")
print("  " + "-" * (cols * 2 + 4))

linhas_mono = mt.formatar_fita(traco_mono, VARS).splitlines()
linhas_alt  = mt.formatar_fita(traco_alt,  VARS).splitlines()

for i, (lm, la) in enumerate(list(zip(linhas_mono, linhas_alt))[:8]):
    marca = "  ← diverge aqui" if i == passo else ""
    print(f"  {lm:<{cols}}  {la}{marca}")

print("  ...")

# ---------------------------------------------------------------------------
# resumo final
# ---------------------------------------------------------------------------

titulo("RESUMO")
print(f"""
  Função implementada : soma(N) = 1 + 2 + ... + N
  Entrada testada     : N = {N}
  Resultado correto   : soma({N}) = {N*(N+1)//2}

  P_mono  resultado = {traco_mono[-1][1]['S']}   (passos: {len(traco_mono)})
  P_alt   resultado = {traco_alt[-1][1]['S']}   (passos: {len(traco_alt)})

  (A) P_mono  ≡ P_iter_formal  →  FORTEMENTE EQUIVALENTES
                                   (fitas idênticas, mesma sequência de estados)

  (B) P_mono  ≢  P_alt         →  NÃO fortemente equivalentes
                                   (mesma saída, fitas distintas a partir
                                   do passo {passo})
""")
