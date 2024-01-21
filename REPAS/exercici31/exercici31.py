def calcular_factura_IVA(quantitat,iva):
    
    valors_valids = [4,10,21]
    if quantitat not in valors_valids:
        quantitat_amb_iva = quantitat*(1.21)
        iva = 21
    else:
        quantitat_amb_iva = quantitat*((100+iva)/100)
        
    print(f'Valor sense IVA: {quantitat}')
    print(f'IVA: {iva}')
    print(f'Valor amb IVA: {quantitat_amb_iva}')