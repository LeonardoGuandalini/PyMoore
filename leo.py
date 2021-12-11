tarefa1 = {
    'p': 3,
    'd': 25
}

tarefa2 = {
    'p': 6,
    'd': 15
}

tarefa3 = {
    'p': 4,
    'd': 30
}

tarefa4 = {
    'p': 5,
    'd': 15
}



def sort_lista_d(lista):
    
    lista_d = []
    sorted_lista = []
    for each_item in lista:
        lista_d.append(each_item['d'])
    lista_d.sort()
    print(lista)
    print(lista_d)

    for each_item in lista_d:
        for i in range(0, len(lista)):
            if each_item == lista[i]['d']:
                sorted_lista.append(lista[i])
                lista_d.insert(lista_d.index(each_item), 'macaco')
                lista_d.pop(lista_d.index(each_item))
                
    
        print(sorted_lista)
        print(lista_d)


       
    return sorted_lista



edd = [tarefa1, tarefa2, tarefa3, tarefa4]
edd_sorted = []
for i in range(0, len(edd)):
    if i == 0:
        edd_sorted.append(edd[i])
    elif i == 1:
        if (edd[i]['d'] < edd[i-1]['d']):
            edd_sorted.insert(i-1, edd[i])
        else:
            edd_sorted.append(edd[i])            
    else:
        edd_sorted.append(edd[i])
        
edd_sorted = sort_lista_d(edd_sorted)
print(edd_sorted)