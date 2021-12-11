# Step 1: order tasks following EDD rule => current sequence

# Step 2: Withing the current sequence, identify the first task that is late, that is, L > 0

# Step 3: Select the said task and its predecessors. This new sequence will be called confrontation sequence and the algorithm will move to the next step. If a late task doesn´t exist, then the algorithm has reached the optimal sequence.

# Step 4: Remove the task with the highest processing time from the confrontation sequence and place it in the removed sequence. The total sequence will be the current sequence + the removed sequence. Repeat from the second step.
tarefa1 = {
    'p': 3,
    'd': 15
}

tarefa2 = {
    'p': 6,
    'd': 25
}

tarefa3 = {
    'p': 4,
    'd': 30
}

def sort_lista_d(lista):
    # assuming we´re in the third item
    lista_d = []
    sorted_lista = []
    for each_item in lista:
        lista_d.append(each_item['d'])
    lista_d.sort() # lista com os d's em ordem crescente
    print(lista_d)

    for each_item in lista_d: # pra cada d nessa lista
        for i in range(0, len(lista)):
            if each_item == lista[i]['d']: # se o d for igual ao da tarefa na lista original
                sorted_lista.append(lista[i]) # adiciona na lista 
    
    return sorted_lista


# jobs[1]['p'] => 3
edd = [tarefa1, tarefa2, tarefa3]
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



# EDD da gambiarra

lista_d=[15, 3, 8, 24, 8, 25, 8, 3]

dic_jd={}

for i in range(0, len(lista_d)):
    dic_jd[i+1]=lista_d[i]

keys_list=list(dic_jd.keys())
values_list=list(dic_jd.values())
lista_d.sort()

seq_atual=[]
for item in lista_d:
     ind=values_list.index(item)
     job=keys_list[ind]
     seq_atual.append(job)
     values_list.remove(item)
     values_list.insert(ind,"pinto")

print(seq_atual)
