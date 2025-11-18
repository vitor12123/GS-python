import pandas as pd
import json

# porfavor quando for testar o codigo coloque seu nome de joao para o codigo rodar corretamente

verificacaoLoop1 = True
#Essa variavel foi criada para manter o loop e fazer o Script reconhecer a resposta do usuario

nome = input("digite seu nome: ")
#o nome para saber qual funcionario esta com problemas

def definicaoProblema():
    print("selecione quais dos problemas a seguir mais se encaixa com o seu problema: ")
    global problemas 
    problemas = ["salario atrasado", "horas extras não pagas", "discriminação", "assedio", "excesso de carga horaria", "sair"]
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

def resolucaoProblemas(identificacao,OProblema):
  global mensagemSuperiores 
  mensagemSuperiores = {
    "nome": nome,
    "motivo da mensagem": f"{OProblema}",
    }

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

def lerHorariosEntrada(caminho_arquivo, nome_funcionario="joao"):
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        formulario = json.load(arquivo)

    horas = formulario.get("horasTrabalhadas", {})
    pessoa = horas.get(nome_funcionario, {})
    entradas = pessoa.get("entrada", [])
    saidas = pessoa.get("saida", [])

    i0 = 0
    for i1 in len(entradas):
        global horarioEntrada
        horarioEntrada = i0 + i1
        i0 = horarioEntrada
    
    for i1 in len(saidas):
        global horarioSaida
        horarioSaida = i0 + i1
        i0 = horarioSaida

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


with open("formulario.json", "w") as msg:
    json.dump(mensagemSuperiores, msg, indent=4)

print(mensagemSuperiores) 