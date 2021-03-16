class Conta:

    def __init__(self,numero,titular,saldo,limite): #função construtora
        print('Construindo objeto... {}'.format(self)) #self é o 'endereço' do objeto
        # o comando __ na frente do nome do atributo faz com que ele se torne privado, e só posso ser acessado por métodos
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('Saldo de {} do titular {}'.format(self.__saldo,self.__titular))

    def deposita(self,valor):
        self.__saldo += valor

##############################Método Privado ###################################

    def __pode_sacar(self,valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return (valor_a_sacar <= valor_disponivel_a_sacar)

#esse método foi criado apelas para ser usado dentro da classe e não fora
#não deve aparecer para solicitar no console, sem um aviso pelo menos

##############################Método Privado ###################################

    def saca(self,valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print('Saldo Insuficiente!')

    def transfere(self,valor,destino):
        if(self.__pode_sacar(valor)):
            self.saca(valor)
            destino.deposita(valor)
        else:
            print('Saldo Insuficiente!')

    @property
    def saldo(self):
        return self.__saldo
    # para chamar basta fazer conta.saldo, (nome_objeto.nome_property), ele irá chamar este método em vez de chamar o atributo em si

    @property
    def titular(self): #get retorna, não recebe
        return self.__titular

    #def get_titular(self): #get retorna, não recebe
    #    return self.__titular

    @property #substitui o get no python, fica mais explicito (o nome da property tem que ser igual do atributo, menos o __)
    def limite(self):
        return self.__limite

    @limite.setter #substitui o set no python, fica mais explicito
    def limite(self,limite):
        self.__limite = limite

    #def set_limite(self,limite): #set recebe, não retorna, altera os valores
     #   self.__limite = limite

    @staticmethod #Metodos estátisco, são da classe e não do objeto conta. Para chamar Nome_Classe.metodo(), não passar o self na def
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa' : '104', 'Bradesco' : '237'}
