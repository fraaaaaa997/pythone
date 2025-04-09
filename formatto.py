#inizializzare una lista con i reciproci dei primi 10 interi. stampare i float risultanti in modo da visualizzare 8 decimali

numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

reciproci = [1 / n for n in numeri]

for n in reciproci:
    print(f"{n:.8f}")
    