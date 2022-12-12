def cambiar_palabra (frase, p_out, p_in): 
    lista=frase.split(" ") 
    
    for i in range(len(lista)):
        if p_out in lista[i]:
            lista[i]=p_in
    frase_final=" ".join(lista)
    
    return frase_final

print(cambiar_palabra("la vida es un fastidio maravilloso", "fastidio", "suplicio"))
print(cambiar_palabra("dale a tu cuerpo alegria macarena", "cuerpo", "body"))