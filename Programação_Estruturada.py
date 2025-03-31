preco_cafe_pequeno = 2
preco_cafe_medio = 5
preco_cafe_grande = 6

orcamento_usuario = input('Qual é o seu orçamento? ')

try:
   orcamento_usuario = int(orcamento_usuario)
except:
   print('Por favor, insira um número')
   exit()

if orcamento_usuario > 0:
   if orcamento_usuario >= preco_cafe_grande:
       print('Você pode comprar o café grande')
       if orcamento_usuario == preco_cafe_grande:
           print('É completo')
       else:
           print('Seu troco é', orcamento_usuario - preco_cafe_grande)
   elif orcamento_usuario == preco_cafe_medio:
       print('Você pode comprar o café médio')
       print('É completo')
   elif orcamento_usuario >= preco_cafe_pequeno:
       print('Você pode comprar o café pequeno')
       if orcamento_usuario == preco_cafe_pequeno:
           print('É completo')
       else:
           print('Seu troco é', orcamento_usuario - preco_cafe_pequeno)
