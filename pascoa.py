# EDD da gambiarra

lista_d=[15, 3, 8, 24, 8, 25, 8, 3]
lista_c=[]
dic_jd={}
dic_jc={}

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
