class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.dados = [None] * capacidade

    def push(self, dado):
        if self.pilha_esta_cheia():
            raise Exception("PilhaCheiaErro")
        if not isinstance(dado, (int, str)) and not (isinstance(dado, tuple) and len(dado) == 4):
            raise Exception("TipoErro")
        self.topo += 1
        self.dados[self.topo] = dado

    def pop(self):
        if self.pilha_esta_vazia():
            raise Exception("PilhaVaziaErro")
        dado = self.dados[self.topo]
        self.topo -= 1
        return dado

    def pilha_esta_vazia(self):
        return self.topo == -1

    def pilha_esta_cheia(self):
        return self.topo == self.capacidade - 1

    def swap(self):
        if self.topo > 0:
            self.dados[self.topo], self.dados[self.topo - 1] = self.dados[self.topo - 1], self.dados[self.topo]

    def length(self):
        return self.topo + 1

def torre_de_hanoi(n, origem, destino, intermediaria):
    lista_de_discos = list(range(n, 0, -1))
    A = list(range(n, 0, -1))
    B = []
    C = []
    capacidade_pilha = 2**n - 1
    pilha = Pilha(capacidade_pilha)
    pilha.push((n, origem, destino, intermediaria))
    movimentos = 0
    input("Pronto para iniciar a Torre de Hanoi? Pressione [ENTER] para iniciar")

    print(f'A = {A}')
    print(f'B = {B}')
    print(f'C = {C}')

    while not pilha.pilha_esta_vazia():
        n, origem, destino, intermediaria = pilha.pop()
        if n == 1:
            movimentos += 1
            disco = None

            if origem == 'A':
                disco = A.pop()
            elif origem == 'B':
                disco = B.pop()
            elif origem == 'C':
                disco = C.pop()

            if destino == 'A':
                A.append(disco)
            elif destino == 'B':
                B.append(disco)
            elif destino == 'C':
                C.append(disco)

            print(f'Mova o disco {disco} de {origem} para {destino}')
            print(f'A = {A}')
            print(f'B = {B}')
            print(f'C = {C}')
            input("Pressione [ENTER] para continuar...")

        else:
            pilha.push((n - 1, intermediaria, destino, origem))
            pilha.push((1, origem, destino, intermediaria))
            pilha.push((n - 1, origem, intermediaria, destino))

    print(f'O número de movimentos necessários para completar o jogo foi: {movimentos}')

# Exemplo de uso:
n = 3  # Número de discos
torre_de_hanoi(n, 'A', 'C', 'B')
