# Definições formais dos programas na notação da Máquina de Traços
#
# Função implementada: soma(N) = 1 + 2 + ... + N
#
# P_mono — conta de 1 até N (para cima)
#   Espelho exato do programa monolítico em C e do iterativo em Python.
#   Quando o programa iterativo é traduzido para notação formal,
#   o while (I <= N) vira o par de rótulos 3 e 6 abaixo.
#
# P_alt — conta de N até 1 (para baixo)
#   Computa a mesma função de P_mono, mas tem traços distintos.
#   Serve para demonstrar NÃO-equivalência forte.

# ---------------------------------------------------------------------------
# P_mono  (mesmo traço do monolítico C e do iterativo Python)
# ---------------------------------------------------------------------------

P_mono = {
    1: ('atrib',   'S', lambda s:  0),
    2: ('atrib',   'I', lambda s:  1),
    3: ('se_goto', lambda s: s['I'] > s['N'],   7),
    4: ('atrib',   'S', lambda s:  s['S'] + s['I']),
    5: ('atrib',   'I', lambda s:  s['I'] + 1),
    6: ('goto',    3),
    7: ('halt',),
}

DESC_P_MONO = """\
P_mono — soma contando de 1 até N (para cima)
  1: S := 0
  2: I := 1
  3: se I > N então vá para 7
  4: S := S + I
  5: I := I + 1
  6: vá para 3
  7: halt"""

# ---------------------------------------------------------------------------
# P_alt  (conta ao contrário — mesmo resultado, traço diferente)
# ---------------------------------------------------------------------------

P_alt = {
    1: ('atrib',   'S', lambda s:  0),
    2: ('atrib',   'I', lambda s:  s['N']),
    3: ('se_goto', lambda s: s['I'] == 0,        7),
    4: ('atrib',   'S', lambda s:  s['S'] + s['I']),
    5: ('atrib',   'I', lambda s:  s['I'] - 1),
    6: ('goto',    3),
    7: ('halt',),
}

DESC_P_ALT = """\
P_alt — soma contando de N até 1 (para baixo)
  1: S := 0
  2: I := N
  3: se I = 0 então vá para 7
  4: S := S + I
  5: I := I - 1
  6: vá para 3
  7: halt"""
