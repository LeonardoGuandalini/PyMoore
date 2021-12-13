# EDD da gambiarra


lista_d=[15, 25, 14, 7, 22, 10, 12, 32, 26, 18]
lista_p=[3, 6, 5, 3, 7, 2, 2, 4, 5, 4]
dic_jd={}
dic_jp={}

for i in range(0, len(lista_d)):
    dic_jd[i+1]=lista_d[i]

for i in range(0, len(lista_d)):
    dic_jp[i+1]=lista_p[i]

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

lista_p=[]
for item in seq_atual:
    lista_p.append(dic_jp[item])

def calcula_C(lista_p, lista_d):
    lista_c=[]
    aux=0
    for p in lista_p:
        aux+=p
        lista_c.append(aux)
    return lista_c

def calcula_L(lista_c, lista_d):
    lista_L=[]
    for i in range(len(lista_c)):
        lista_L.append(max([0, lista_c[i]-lista_d[i]]))
    return lista_L

lista_c=calcula_C(lista_p, lista_d)
lista_L=calcula_L(lista_c, lista_d)

print(seq_atual)
print(lista_c)
print(lista_L)

removidas=[]
flag=True

while flag==True:

    seq_confronto=[]
    for i in range(0, len(lista_L)):
        if lista_L[i]==0:
            seq_confronto.append(i+1)
        else:
            seq_confronto.append(i+1)
            break

    p_confronto=[]
    for job in seq_confronto:
        p_confronto.append(dic_jp[job])

    job_index=p_confronto.index(max(p_confronto))
    job=seq_confronto[job_index]
    print('remove' + str(job))
    removidas.append(job)
    seq_atual.remove(job)
    lista_d.pop(job_index)
    lista_p.pop(job_index)

    lista_c=calcula_C(lista_p, lista_d)
    lista_L=calcula_L(lista_c, lista_d)

