tarefa1 = {
    'p': 3,
    'd': 15
}

tarefa2 = {
    'p': 6,
    'd': 25
}

tarefa3 = {
    'p': 5,
    'd': 14
}

tarefa4 = {
    'p': 3,
    'd': 7
}

tarefa5 = {
    'p': 7,
    'd': 22
}

tarefa6 = {
    'p': 2,
    'd': 10
}

tarefa7 = {
    'p': 2,
    'd': 12
}

tarefa8 = {
    'p': 4,
    'd': 32
}

tarefa9 = {
    'p': 5,
    'd': 26
}

tarefa10 = {
    'p': 4,
    'd': 18
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


# Aplicar regra EDD na sequência original
edd = [tarefa1, tarefa2, tarefa3, tarefa4, tarefa5, tarefa6, tarefa7, tarefa8, tarefa9, tarefa10]
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

# Verificar os atrasos
# Calcular:
## C
## L = D - C
lista_c = []
lista_l = []

counter_c = 0

for each_item in edd_sorted:
    counter_l = 0
    counter_c += each_item['p']
    lista_c.append(counter_c)
    counter_l = counter_c - each_item['d']
    lista_l.append(counter_l)

print(lista_c)
print(lista_l)

atraso = 0

## Where the loop should begins
lista_confronto = []
lista_removidas = []
lista_atual = []

for i in range(0, len(lista_l)):
    if lista_l[i] <= 0:
        lista_confronto.append(edd_sorted[i])

print(lista_confronto)
lista_ps = []          
for i in range(0, len(lista_confronto)):
    lista_ps.append(lista_confronto[i]['p'])

max_confronto_p = max(lista_ps)
max_confronto_i = lista_ps.index(max_confronto_p)
max_confronto = lista_confronto[max_confronto_i]

lista_removidas.append(max_confronto)
lista_confronto.clear()
lista_atual = edd_sorted
del lista_atual[max_confronto_i]
print(lista_atual + lista_removidas)