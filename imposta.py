
imposta_lorda = float(input("Inserisci l'imposta lorda: "))

aliquota = [0.77, 0.65, 0.57]


if 0 < imposta_lorda < 28000:
    imposta_netta = imposta_lorda * aliquota[0]
elif 28000 <= imposta_lorda < 50000:
    imposta_netta = imposta_lorda * aliquota[1]
elif imposta_lorda >= 50000:
    imposta_netta = imposta_lorda * aliquota[2]
else:
    imposta_netta = 0 
    print("Errore: valore non valido.")


print(f"Imposta netta: {imposta_netta:.2f}")
