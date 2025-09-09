#Sistema para simulação de emprestimos com juros compostos

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

taxa = 0.035 #3,5%
vlr_final_emprestimo = calcula_emprestimo(vlr_emprestimo, taxa, qtd_meses)
vlr_emprestimo, salario, qtd_meses = receber_valor()
juros = vlr_final_emprestimo - valor_emprestimo

print("============== Resultado da Simulação de Emprestimo =============")
print(f"Valor final a pagar: {cal_emprestimo:.2f}")
print(f"Taxa de juros: R$ {taxa:.2%}")
print(f"Valor salário informado: R$ {vrl_salario:.2f}")
print("Quantidade de meses para pagamento:",qtd_meses)
print(f"Valor de juros: R$ {juros:.2f}")
