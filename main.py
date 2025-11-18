import pandas as pd
import json

# porfavor quando for testar o codigo coloque seu nome de "joao" para o codigo rodar corretamente

#Essa variavel foi criada para manter o loop e fazer o Script reconhecer a resposta do usuario
verificacaoLoop1 = True

#o nome para saber qual funcionario esta com problemas
nome = input("digite seu nome: ")

# essa função é a que verifica se o funcionario realmente tem trabalhado excessivamente onde o parametro verifica qual funcionario esta reclamando
def lerHorariosEntrada(nome_funcionario ="joao"):
# puxa informações do json da empresa
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

# essas variaveis pega as informações necessarias para a verificação
    horas = dados.get("horasTrabalhadas", {})
    pessoa = horas.get(nome_funcionario, {})
    entradas = pessoa.get("entrada", [])
    saidas = pessoa.get("saida", [])

#soma todas o horario de entrada e saida, para não ter duvidas eu botei os horarios como o inteiro representando as horas e o decimal representando os minutos
    somaEntrada = sum(entradas)
    somaSaida = sum(saidas)

# faz a media dos ultimos 15 dias
    mediaHorasTrabalhadasDia = (somaSaida - somaEntrada) /15

# verificação para ver se a media dos ultimos 15 dias bate com o horario combinado, 9 horas por dia
    if mediaHorasTrabalhadasDia <= 9 :
       print("Não podemos diminuir sua carga horaria, já que você vem trabalhado menos que o tempo de trabalho minimo da empresa, mas tente intervalos entre 5 a 10 minutos 2 vezes por dia.")
       mensagemSuperiores["problema solucionado"] = "ele tem problemas com excesso de carga horaria mas ja trabalha no tempo minimo."
    elif mediaHorasTrabalhadasDia >= 9 : 
       print("Sintimos muito pelo estresse, iremos diminuir sua carga horaria")
       mensagemSuperiores["excesso de carga horaria de funcionario"] = f"diminua a carga horaria de {nome}"

#essa função verifica qual é o problema do funcionario 
def definicaoProblema():
    print("selecione quais dos problemas a seguir mais se encaixa com o seu problema: ")
# a variavel problemas são todos os problemas registrados pela empresa ficticia, caso necessario da para adicionar mais
    global problemas 
    problemas = ["salario atrasado", "horas extras não pagas", "discriminação", "assedio", "excesso de carga horaria", "sair"]
# parte de mostrar quais são os problemas registrados ate então.
    for i in range(len(problemas)):
        print(f"problema numero {i+1}: {problemas[i]}")
    try:
        problema = int(input("qual foi o numero do problema? "))
    except ValueError:
        print("digite apenas numeros")
    if problema <= 5:
      resolucaoProblemas(problema,problemas[problema - 1])
    else: 
      print(f"ok {nome}, ate logo!")

# essa é a função que manda para os superiores resolverem o problema, e ver quais medidas serão tomadas
def resolucaoProblemas(identificacao,OProblema):
  global mensagemSuperiores 
  mensagemSuperiores = {
    "nome": nome,
    "motivo da mensagem": f"{OProblema}",
    }

# verificando qual é o tipo de mensagem que deve chegar aos superiores.
  if identificacao == 1:
    mensagemSuperiores["Pix salario atrasado"] = input("digite o seu pix: ")
  elif identificacao == 2:
    mensagemSuperiores["Pix hora extra"] = input("digite o seu pix: ")
  elif identificacao == 3:
    mensagemSuperiores["quem"] = input("digite o nome de quem te discriminou: ")
    mensagemSuperiores["descricao"] = input("descreva como foi a situação: ")
  elif identificacao == 4: 
    mensagemSuperiores["quem"] = input("digite o nome da pessoa que te assediou:")
    mensagemSuperiores["descricao"] = input("descreva como foi a situação: ")
  elif identificacao == 5:
    lerHorariosEntrada()

# verificação para ver se a pessoa esta bem ou apenas entrou nessa area por engano
while verificacaoLoop1 :
    verificacaoSaude = input(f"Olá {nome}, esta bem fisicamente ou mentalmente / (s/n): ").strip()
    if len(verificacaoSaude) > 1:
        print("digite apenas s ou n ")
    else:
        verificacaoLoop1 = False
        if verificacaoSaude.lower() == "s":
          print(f"Perfeito {nome} ate logo!")
          break
        elif verificacaoSaude.lower() == "n":
          print("eu sinto, preencha o formulario para te ajudarmos!")
          definicaoProblema()

# manda a mensagem selecionada para os superiores, dentro da condicional para nao dar erro.s
if verificacaoSaude.lower() == "n":
  with open("formulario.json", "w") as msg:
      json.dump(mensagemSuperiores, msg, indent=4)

# para ver qual mensagem foi emitida.
  print(mensagemSuperiores) 
