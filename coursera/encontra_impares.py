def encontra_impares(lista, impares = []):
    if lista[0] %2 == 1:
        impares.append(lista[0])
    if len(lista) == 1:
        return impares
    else:
        return encontra_impares(lista[1:], impares)
