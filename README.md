# FUNCIÓ QUE LLEGEIX L'ARXIU PASSAT COM A PARÀMETRE 
# readfile()
Transforma els espais del fitxer en posicions de nombres de 2 en 2 de la llista 'variables'.\
Després, trasllada les variables de punts a la llista 'points'.\
I finalment, prepara el return perquè retorni el nombre de punts, l'alçada, cost alpha, cost beta i la llista dels punts.


# FUNCIÓ QUE PRINTA "impossible" I SURT DEL PROGRAMA 
# impossible()
def impossible():\
    print("impossible")\
    exit()


# FUNCIÓ QUE COMPROVA UN POSSIBLE PONT O AQÜEDUCTE NO VÀLID 
# wrong_cases()
Si un radi de l'arc fos major que l'alçada requerida, seria impossible generar un arc vàlid.\
Si un punt per sobre del centre de l'arc estigues fora del seu radi, voldrà dir que el pont xocaria contra el terreny considerant-ho no vàlid.


# FUNCIÓ QUE CALCULA EL COST MITJANÇANT LA FORMULA PROPOSADA
# cost()
def cost(height, x):\
    return alpha * height + beta * x


# FUNCIÓ PRINCIPAL QUE COMPROVA TOT L'ANTERIOR DE FORMA RECURSIVA FINS QUE ARRIBA A L'ULTIM PUNT
# recursive()
Es calcula la distància en l'eix X entre els dos punts.\
Es calcula el radi sent aquest la meitat de la distància X.\
Es calcula el centre de l'arc:
- La X serà la meitat de la distància X dels dos punts, és a dir, radi més l'X del primer punt.
- La Y serà l'alçada requerida menys el radi.

Es comprova que el punt sigui vàlid.\
Quan només quedin dos punts es sumarà al total els dos pilars + la seva distància al quadrat.\
En cada "iteració" recursiva, es suma l'alçada del primer pilar i la distancia amb el següent.\
En cada "iteració" recursiva, es passa la llista sense el punt ja tractat i el cost acumulat.
