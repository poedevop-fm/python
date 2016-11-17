#!/usr/bin/python3

import sys

print (sys.version_info)
print(sys.version)

print(sys.platform)
print("Hello dbl quotes")
print('Hello, simple quote')
print("c'est - appostrophe requiert une dbl quote")
print("""les tripples quotes sont
utiles pour les textes
en plusieurs lignes""")

str = "Spam"
print (str)

print("\n afficher les éléments d/'une liste :")

a= ['a','b','c','d','e','f','g','h']
print(a[:4])
print(a[5:7])
print(a[2:4])
print(a[-4:])
print(a[3:-3])


print("\nformattage de chaînes :\n")
i=5
mykey="temps"
fois=20
print('la valeur %2.2f et le mot \'%s\' apparaissent %d fois, ' %(i, mykey, fois))
print("\n le dernier signe % indique que ce qui le suit, s'applique aux valeurs des % précédents")
print("\n: %2.2f et le mot \'%s \n")

print("\nautre méthode de formatage :\n")

print('la valeur {} et le mot \'{}\' apparaissent {} fois'.format(i, mykey, fois))

print("\n les tests conditionnels :\n")
print("\n if :\n")

valeur ="cat"
if valeur == "cat" : # les 2point equivale à then
    print("ok")

print("\n if imbriqués :\n")

valeur ="cat"
if valeur == "cat" : # les 2point equivale à then
    print("ok")
elif valeur == "dog":
    print("dog ok")
else:
    print("inconnu")

print("\n chq valeur de la liste seq, est affecté dans l'ordre, aux variables a,b,c,d :\n")
print("pour : seq = [1,2,3,4] et a,b,c,d=seq, on affiche a\n")

seq = [1,2,3,4]
a,b,c,d=seq
print(a)  #affiche 1

print("\n pour : seq = [1,2,3,4] et a,b,c,d=seq, on affiche c\n")

seq1 = [1,2,3,4]
aa,bb,cc,dd=seq1
print(cc)  #affiche 3

print("\n boucle For :\n")


for letter in "Spam":
    print("Current letter" ,letter)

fruits = ['banane','pomme', 'mangue']
for fruit in fruits:
    if fruit =="banane":
        print(fruit[2])
    print("mon fruit",fruit)

for num in range (1,10):
    print(num)
    print("\n------------")
    if num ==6:
        break


for num in range (1,10):
    print(num)
    if num ==4:
        break

for num in range (1,10):
    print(num)
    if num ==5:
        continue
    if num == 7:
            break

var = 10
while True:
    var-=1
    if(var==6):  #les parenthèse dans if sont optionnelles
        continue
    print(var)
    if(var ==0):
        break

print ("end loop")

print ("\ncode très utilisé en python, on lit d'abord l'après for (x in a) puis on applique l'avant for (x**2)\n")

a = [1,2,3,4,5,6,7,8,9,10]
squares = [x**2 for x in a]
print(squares)

# on a 2 variables temps et distance
temps=6.896
distance=19.7
vitesse=distance/temps
msg="La vitesse est de = {:.2f} metre par seconde"
print(msg.format(vitesse))
print("La vitesse est de : {:.2f} par seconde ".format(vitesse))

# en utilisant la fonction range
# afficher les entiers de 0 à 3
# de 4 à 7

#nombre=[0,1,2,3,4,5,6,7]
for i in range(0,4):
   # if i<=3:
        print(i)
print('\n')

#nombre = [1, 2, 3, 4, 5, 6, 7]
for i in range(4,8):
    # if i > 3:
        print(i)

#nombre = [1, 2, 3, 4, 5, 6, 7]
for i in range(0,10):
    if i > 3:
        print("---",i)
    if i == 7:
        break


# avec une boucle for, afficher les caractères de la chaine suivante
msg="c'est la formation Devops"
for c in msg:
    print(c)

# sur la liste suivante faire les actions suivantes :
liste = [17,38,10,25,72]
#trier et afficher la liste
liste.sort()
print(liste)
# ajouter l'élément 12 et afficher la liste
liste.append(12)
print(liste)
# afficher l'indice de l'élément 17
print(liste.index(17))
# enlever l'élément 38 et afficher la liste
liste.remove(38)
print(liste)
# afficher la sous liste, du 3eme element jusqu'à la fin de la liste
print(liste[2:])
