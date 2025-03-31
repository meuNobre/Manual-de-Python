class Cafe:
        # Construtor
        def __init__(self, nome, preco):
                self.nome = nome
                self.preco = float(preco)
        def verificar_orcamento(self, orcamento):
                # Verifica se o orcamento é válido
                if not isinstance(orcamento, (int, float)):
                        print('Digite um número inteiro ou decimal')
                        exit()
                if orcamento < 0: 
                    print('Desculpe, você não tem dinheiro') 
                    exit() 
        def calcular_troco(self, orcamento):
                return orcamento - self.preco
        
        def vender(self, orcamento):
                self.verificar_orcamento(orcamento)
                if orcamento >= self.preco:
                        print(f'Você pode comprar o café {self.nome}')
                        if orcamento == self.preco:
                                print('É completo')
                        else:
                                print(f'Aqui está seu troco {self.calcular_troco(orcamento)}$')

                        exit('Obrigado pela sua transação')

cafe_pequeno = Cafe('Pequeno', 2)
cafe_medio = Cafe('Médio', 5)
cafe_grande = Cafe('Grande', 6)

try:
   orcamento_usuario = float(input('Qual é o seu orçamento? '))
except ValueError:
   exit('Por favor, insira um número')
  
for cafe in [cafe_grande, cafe_medio, cafe_pequeno]:
   cafe.vender(orcamento_usuario)
