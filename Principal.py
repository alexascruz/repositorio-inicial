#Sistema para simulação de emprestimos com juros compostos

#Variáveis globais
taxa = 0.035 #3,5%
percentual_consignavel = 0.35 #35%

def receber_valor():
    vlr_emprestimo = float(input ("Qual o valor de emprestimo pretendido? "))
    salario = float(input ("Digite o seu salário mensal: "))
    qtd_meses = int(input ("Em quantos meses pretende pagar? "))
    return vlr_emprestimo, salario, qtd_meses

#Cálculo do valor final do emprestimo (M = P x (1+i)^t)
#M = Montante final (capital inicial + juros)
#P = Capital inicial (valor emprestado)
#i = Taxa de juros (ao período)
#t = Tempo (número de períodos)
#x = fator de multiplicação
#ˆ = fator exponencial

def calcula_emprestimo(vlr_emprestimo, taxa, qtd_meses):
    calculo_emprestimo = vlr_emprestimo * (1+taxa) ** qtd_meses
    return calculo_emprestimo

def calcula_parcela(vlr_final_emprestimo, qtd_meses):
    calculo_parcela = vlr_final_emprestimo / qtd_meses
    return calculo_parcela

vlr_emprestimo, salario, qtd_meses = receber_valor()
vlr_final_emprestimo = calcula_emprestimo(vlr_emprestimo, taxa, qtd_meses)
juros = vlr_final_emprestimo - vlr_emprestimo
vlr_parcela = calcula_parcela(juros, qtd_meses)

print("============== Resultado da Simulação de Emprestimo =============")
print(f"Valor final a pagar: {vlr_final_emprestimo:.2f}")
print(f"Taxa de juros aplicada: R$ {taxa:.2%}")
print(f"Valor salário informado: R$ {salario:.2f}")
print("Quantidade de meses para pagamento:",qtd_meses)
print(f"Valor de juros: R$ {juros:.2f}")
print(f"Valor da parcela: R$ {vlr_parcela:.2f}")
print("")
