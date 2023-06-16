import timeit
import numpy as np  #Bibliotheque utilisée pour manipuler les matrices

def plusCourte_Distance(C):
    n = C.shape[0]  # Nombre de sommets dans le graphe
    C_k = np.empty_like(C)  # Initialisation de la matrice des chemins les plus courts

    for k in range(n):
        for i in range(n):
            for j in range(n):
                C_k[i,j] = min(C[i,j], C[i,k] + C[k,j])

        C = np.copy(C_k)  # La matrice C^k-1 devient la matrice C^k

    return C
inf=np.inf
C = np.array([[0, 3, inf, 7],
              [8, 0, 2, inf],
              [5, inf, 0, 1],
              [2, inf, inf, 0]])

C_plusCourte_Distance = plusCourte_Distance(C)

print(C_plusCourte_Distance)

# Mesure du temps d'exécution avec timeit
t = timeit.timeit(lambda: plusCourte_Distance(C), number=1) 
print("Durée d'exécution : %.5f secondes" % t)