#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1 Librería MATH: Python tiene un conjunto relativamente pequeño de operaciones y funciones matemáticas predeterminadas.
#Para agregar más funciones se utilizan las librerias, en este caso la libreria MATH proporciona acceso a 
#las funciones matemáticas definidas en el estándar de C, como lo son las funciones trigonométricas el seno, coseno y 
#tangente, la exponencial y su inversa el logaritmo , y las constantes relacionadas.


# In[59]:


#2

Num1=float(input('Por favor ingrese la base:'))
Num2=float(input('Por favor ingrese el exponente:'))

Resultado=pow(Num1, Num2)

print (Resultado)


# In[82]:


#3


a, b = 0,1
while a <= 100:
    print(a)
    (a,b) = (b,a+b)
    


# In[132]:


#4

altura_arbol = 20


for i in range(1, altura_arbol + 1):
    espacio = ' ' * (altura_arbol - i)
    simbolo = '*' * (2 * i - 1)
    print(espacio + simbolo)


# In[21]:


#5

Palabra=input('Por favor ingrese una palabra:')

contador_a=0
contador_e=0
contador_i=0
contador_o=0
contador_u=0

for i in Palabra:
    
    if i =='a':
        contador_a=contador_a+1
    
    elif i =='e':
        contador_e=contador_e+1
    
    elif i =='i':
        contador_i=contador_i+1
    
    elif i =='o':
        contador_o=contador_o+1
    
    elif i =='u':
        contador_u=contador_u+1

print('La vocal a se repite:', contador_a)
print('La vocal e se repite:', contador_e)
print('La vocal i se repite:', contador_i)
print('La vocal o se repite:', contador_o)
print('La vocal u se repite:', contador_u)


# In[5]:


#6 Append: append es un método que tiene toda lista de Python el cual permite agregar un elemento al final de la lista.
#Acepta cualquier tipo de valor como elemento a agregar: número, cadena, lista, diccionario, objeto, etc.

#Ejemplo Append:

Colores_arcoiris= list (['rojo', 'naranja', 'amarillo', 'verde', 'añil', 'azul'])

Colores_arcoiris.append('violeta')

print(Colores_arcoiris)


#Extend: el método extend() permite agregar todos los elementos de un iterable(lista, tupla, cadena, etc) al final 
#de una lista, lo que permite unir 2 listas.

#Ejemplo Extend:

Receta_ingredientes_liquidos= list (['leche', 'escencia vainilla', 'jugo de naranja', 'claras de huevo'])

Receta_ingredientes_secos= list (['azucar', 'harina', 'polvo de hornear', 'bicarbonato'])

Receta_ingredientes_liquidos.extend(Receta_ingredientes_secos)

print(Receta_ingredientes_liquidos)


#Remove: En Python, el método remove() se utiliza para eliminar el primer elemento de una lista que coincida con el 
#valor proporcionado como argumento.

#Ejemplo Remove:

Frutas= list (['banana', 'papaya', 'melon', 'sandia', 'pera', 'manzana'])

Frutas.remove('manzana')

print (Frutas)

