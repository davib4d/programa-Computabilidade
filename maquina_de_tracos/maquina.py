# Máquina de Traços — engine de execução para programas monolíticos formais
#
# Um programa é representado como um dicionário { rotulo: instrucao },
# onde cada instrucao é uma tupla com os campos:
#
#   ('atrib',   var, expr_fn)    — S := expr; próximo rótulo = atual + 1
#   ('se_goto', cond_fn, dest)   — se cond then goto dest; senão atual + 1
#   ('goto',    dest)            — goto dest
#   ('halt',)                    — encerra a computação
#
# A memória é um dicionário { nome_variavel: valor }.
# Variáveis não inicializadas aparecem como INDEF na fita de saída.

INDEF = "_"   # sentinela para variável indefinida

class MaquinaDeTracos:

    def executar(self, programa, estado_inicial, max_passos=2000):
        estado = dict(estado_inicial)
        rotulo = min(programa)
        traco  = [(rotulo, dict(estado))]

        for _ in range(max_passos):
            if rotulo not in programa:
                break

            tipo, *args = programa[rotulo]

            if tipo == 'atrib':
                var, expr = args
                estado[var] = expr(estado)
                rotulo += 1

            elif tipo == 'se_goto':
                cond, dest = args
                rotulo = dest if cond(estado) else rotulo + 1

            elif tipo == 'goto':
                rotulo = args[0]

            elif tipo == 'halt':
                traco.append(('halt', dict(estado)))
                return traco

            traco.append((rotulo, dict(estado)))

        return traco  # saiu por max_passos sem halt — provavelmente diverge

    # ------------------------------------------------------------------

    def formatar_fita(self, traco, ordem_vars=None):
        """
        Retorna a fita de traços no formato ⟨rótulo, {vars}⟩ ⊢ ...
        ordem_vars controla a ordem de exibição das variáveis.
        """
        linhas = []
        for i, (rotulo, estado) in enumerate(traco):
            if ordem_vars:
                pares = [f"{v}={estado.get(v, INDEF)}" for v in ordem_vars]
            else:
                pares = [f"{k}={v}" for k, v in sorted(estado.items())]
            cfg = f"⟨{rotulo}, {{{', '.join(pares)}}}⟩"
            prefixo = "   " if i == 0 else "⊢  "
            linhas.append(f"{prefixo}{cfg}")
        return "\n".join(linhas)

    # ------------------------------------------------------------------

    def comparar(self, traco1, traco2):
        for i, (c1, c2) in enumerate(zip(traco1, traco2)):
            if c1 != c2:
                return False, i
        if len(traco1) != len(traco2):
            return False, min(len(traco1), len(traco2))
        return True, -1
