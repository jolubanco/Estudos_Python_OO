class Cliente:

    def __init__(self,nome):
        self.__nome = nome

    #metodos que dao acesso ao objeto, para poder alterar
    @property
    def nome(self): #nome igual do atributo
        print('chamando @property nome()')
        return self.__nome.title()

    @nome.setter
    def nome(self,nome):
        print('chamando setter nome()')
        self.__nome = nome