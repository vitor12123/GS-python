import pandas

verificacaoDaVerificacao = True

while verificacaoDaVerificacao :
    verificacao = input("Você esta bem fisicamente ou mentalmente/(s/n): ")
    if verificacao.__len__.trim()  > 1 :
        print("digite apenas s ou n ")
    else:
        verificacaoDaVerificacao = False

nome = input("digite seu nome: ")

def definicaoProblema():
    print("selecione quais dos problemas a seguir mais se encaixa com o seu problema: ")