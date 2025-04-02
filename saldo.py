"""  scrivere una funzione che calcoli il saldo di un conto bancario 
dopo che siano trascorsi una dato numero di anni a partire da un dato 
saldo iniziale e con un dato tasso di interesse annuo,
accredtando gli interessi annualmente. Se il numero di anni non viene
passato, si contando i primi 20 anni"""




""" def saldo(saldo_iniziale, tasso_interesse, numero_di_anni = None):
    if numero_di_anni is None:
        numero_di_anni = 20
    saldo_finale = saldo_iniziale * ((1 + tasso_interesse) ** numero_di_anni)
    return saldo_finale
  
print(saldo(1000, 0.05, 15))
 """

def saldo(saldo_iniziale, tasso_interesse, numero_di_anni=None):
    if numero_di_anni is None:
        numero_di_anni = 20  
    else:
        numero_di_anni = numero_di_anni 
    
    saldo_finale = saldo_iniziale * ((1 + tasso_interesse) ** numero_di_anni)
    return saldo_finale


print(saldo(10000, 0.05, 10)) 
print(saldo(10000, 0.05))   