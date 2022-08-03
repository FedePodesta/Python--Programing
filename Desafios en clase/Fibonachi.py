# ~ #crear serie de fibonacci de n numeros, con lista por comprension
n = 17
semilla = [0,1]
l_fib = [semilla.append(semilla [-1] + semilla [-2]) for i in range (n-2)]
print (semilla)