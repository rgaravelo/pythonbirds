class Pessoa:
    def __init__(self, nome=None, idade=None ):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'

class Homem(Pessoa):
    pass

if __name__ == '__main__':
    p = Pessoa('Renan', 30)
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)