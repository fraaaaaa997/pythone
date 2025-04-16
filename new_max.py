""" scrivere un programma python che acquisisca tutte le righe di un file di testo t.txt il cui nome va richiesto all'utente.
il file si suppone contenere un numero per ogni riga (anche con decimali). 
calcolare la media e indicare il valore massimo comprensivo della riga in cui è stato trovato il file. """

def newmax():
    nome_file = input("Inserisci il nome del file: ")

    try:
        with open(nome_file, 'r') as file:
            righe = file.readlines()

        numeri = []
        max_valore = None

        for i, riga in enumerate(righe, start=1):
            try:
                numero = float(riga.strip())
                numeri.append((i, numero))  
                if max_valore is None or numero > max_valore:
                    max_valore = numero
            except ValueError:
                print(f"Valore non valido alla riga {i}: '{riga.strip()}'")

        if numeri:
            media = sum(n for _, n in numeri) / len(numeri)
            righe_max = [riga for riga, valore in numeri if valore == max_valore]

            print(f"Media dei numeri: {media}")
            print(f"Valore massimo: {max_valore} (trovato alle righe: {', '.join(map(str, righe_max))})")
        else:
            print("Nessun numero valido trovato nel file.")

    except FileNotFoundError:
        print(f"Il file '{nome_file}' non è stato trovato.")

if __name__ == "__main__":
    newmax()
