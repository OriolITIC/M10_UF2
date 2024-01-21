def calcular_total_amb_descompte_i_iva(llista_compra,iva):

    total = 0

    for producte, (preu, descompte) in enumerate(llista_compra.items(), start=1):
        preu_amb_descompte = preu - (preu * descompte / 100)
        total += preu_amb_descompte
        print(f"Producte {producte}: Preu amb descompte: {preu_amb_descompte:.2f} €")

    total_amb_iva = total + (total * iva / 100)

    print(f"\nTotal amb descompte i IVA: {total_amb_iva:.2f} €")


