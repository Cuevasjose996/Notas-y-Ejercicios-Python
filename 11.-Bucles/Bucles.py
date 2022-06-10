"""dato importante x=0
                x +=1"""

#una iteracion es repetir una vez un conjunto de variables

"""Bucles son estructuras, con un segmento de codigo, que 
se repiten tantas veces como se cumpla una condicion determinada"""

'''Iterador: Un iterador es un contador que poseen los bucles, 
es unportante que los bucles tengan un iterador, de otra forma el bucle sera infinito'''

"""Break: Es una forma de detener un bucle a llegar a una condicion definida"""

"""while <condicion>:
    <instrucciones de codigo>
    <incrementar o decrecer el contador>"""

n=5
while n>0:
    print(n)
    n=n-1
print("despegue!")

"""for<contador>in<nombre de lista>:
    <segmento de codigo>"""

lista=[1,2,3,4,5]
for i in lista:
    print(i)
