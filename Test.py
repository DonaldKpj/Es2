import ABR
import ARN
import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt

# creazione di un array con valori random
def array(n):
    A = []
    for i in range(0, n):
        A.insert(i, int(np.random.rand()*100))
    return A

# creazione di un array con valori orinati
def array_ordinato(n):
    A = []
    for i in range(0, n):
        A.insert(i, i)
    return A

# creazione di un array ordinato al contrario
def array_ordinato_al_contrario(n):
    A = array_ordinato(n)
    A.reverse()
    return A

# creazione dell'albero
def crea_albero(tree, A):
    for x in range(0, len(A)):
        tree.insert(A[x])

# calcolo tempo di inserimento di un pool di dati (A)
def tempo_insert(tree, A):
    start = timer()
    crea_albero(tree, A)
    end = timer()
    return end - start

# calcolo tempo di ricerca di un valore (n)
def tempo_find(tree, n):
    k = int(np.random.rand() * n)
    start = timer()
    tree.find(k)
    end = timer()
    return end - start


# calcolo altezza abero, in maniera ricorsiva
def height(root):
    if root is None:
        return 0
    leftAns = height(root.left)
    rightAns = height(root.right)
    return 1+max(leftAns, rightAns)


def main():
    # matrice inserimento alberi random
    tempiRinsertABR = []
    tempiRinsertARN = []

    # matrice inserimento alberi ordinati
    tempiOinsertABR = []
    tempiOinsertARN = []

    # matrice ricerca alberi random
    temporicABRR = []
    temporicARNR = []

    # matrice ricerca alberi ordinati
    temporicABRO = []
    temporicARNO = []

    # file inserimento random
    e = open('InserimentoRandom.txt', 'w')
    e.write('InserimentoRandom\n')
    e.write('Dimensione ')
    e.write(' ABR ')
    e.write(' ARN ')
    e.write(' AltezzaABR ')
    e.write(' AltezzaARN\n')

    # file ricerca random
    f = open('RicercaRandom.txt', 'w')
    f.write('RicercaRandom\n')
    f.write('Dimensione ')
    f.write(' ABR ')
    f.write(' ARN ')
    f.write(' AltezzaABR ')
    f.write(' AltezzaARN\n')

    # file inserimento ordinato
    g = open('InserimentoOrdinato.txt', 'w')
    g.write('InserimentoOridnato\n')
    g.write('Dimensione ')
    g.write(' ABR ')
    g.write(' ARN ')
    g.write(' AltezzaABR ')
    g.write(' AltezzaARN\n')

    # file ricerca ordinata
    h = open('RicercaOrdinata.txt', 'w')
    h.write('RicercaOrdinata\n')
    h.write('Dimensione ')
    h.write(' ABR ')
    h.write(' ARN ')
    h.write(' AltezzaABR ')
    h.write(' AltezzaARN\n')


    # altezza alberi con input random
    hABRrandom = np.zeros((21, 1))
    hABRrandomMedia =[]
    hARNrandom = np.zeros((21, 1))
    hARNrandomMedia = []

    # altezza alberi con input ordinati
    hABRordinata = np.zeros((21,1))
    hABRordinataMedia = []
    hARNordinata = np.zeros((21,1))
    hARNordinataMedia = []


    timeABRinsertR = np.zeros((21, 1))
    timeARNinsertR = np.zeros((21, 1))
    timeABRinsertO = np.zeros((21, 1))
    timeARNinsertO = np.zeros((21, 1))

    timeABRR = np.zeros((21, 1))
    timeARNR = np.zeros((21, 1))
    timeABRO = np.zeros((21, 1))
    timeARNO = np.zeros((21, 1))


    # calcolo totale della somma dei tempi di calcolo
    # test su 500 prove
    for i in range(1, 500):
        x = 0
        # dimensione degli alberi, da 10 a 2000 con passo 100
        for j in range(10, 2000, 100):
            x += 1

            # sezione test con input random
            tree1 = ABR.ABR()
            tree2 = ARN.ARN()
            A = array(j)
            B = A[:]
            # tempi inserimento in abr e arn randomici
            timeABRinsertR[x] += tempo_insert(tree1, A)
            timeARNinsertR[x] += tempo_insert(tree2, B)
            # tempi ricerca in abr e arn randomici
            timeABRR[x] += tempo_find(tree1, j)
            timeARNR[x] += tempo_find(tree2, j)
            # altezza alberi con input randomici
            hABRrandom[x] += height(tree1.root)
            hARNrandom[x] += height(tree1.root)
            A.clear()
            B.clear()

            # sezione test con input ordinato
            tree1 = ABR.ABR()
            tree2 = ARN.ARN()
            A = array_ordinato(j)
            B = A[:]
            # tempi inserimento in abr e arn ordinati
            timeABRinsertO[x] += tempo_insert(tree1, A)
            timeARNinsertO[x] += tempo_insert(tree2, B)
            # tempi ricerca in abr e arn ordinati
            timeABRO[x] += tempo_find(tree1, j)
            timeARNO[x] += tempo_find(tree2, j)
            # altezza alberi con input ordinati
            hABRordinata[x] += height(tree1.root)
            hARNordinata[x] += height(tree2.root)
            A.clear()
            B.clear()


    # sezione in cui si scrive la media dei dati su txt
    x = 0
    for j in range(10, 2000, 100):
        x += 1

        hABRrandomMedia.insert(x, hABRrandom[x] / i)
        hARNrandomMedia.insert(x, hARNrandom[x] / i)

        tempiRinsertABR.insert(x, timeABRinsertR[x]/i)
        tempiRinsertARN.insert(x, timeARNinsertR[x]/i)

        # scrittura su file InserimentoRandom.txt
        if x % 5:
            e.write(str(j))
            e.write(' & ')
            temp = round((float(timeABRinsertR[x] / i)), 5)
            e.write(str(temp))
            e.write(' & ')
            temp = round((float(timeARNinsertR[x] / i)), 5)
            e.write(str(temp))
            e.write(' & ')
            temp = int(hABRrandom[x] / i)
            e.write(str(temp))
            e.write(' & ')
            temp = int(hARNrandom[x] / i)
            e.write(str(temp))
            e.write(' \\\ \hline\n')


        temporicABRR.insert(x, timeABRR[x]/i)
        temporicARNR.insert(x, timeARNR[x]/i)

        # scrittura su file RicercaRandom.txt
        if x % 5:
            f.write(str(j))
            f.write(' & ')

            temp = str(round((float(timeABRR[x] / i)), 7))
            temp2 = temp
            temp = float(temp2)
            f.write(str(temp))
            f.write(' & ')

            temp = str(round((float(timeARNR[x] / i)), 7))
            temp2 = temp
            temp = float(temp2)
            f.write(str(temp))
            f.write(' & ')

            temp = int(hABRrandom[x] / i)
            f.write(str(temp))
            f.write(' & ')

            temp = int(hARNrandom[x] / i)
            f.write(str(temp))
            f.write(' \\\ \hline\n')


        hABRordinataMedia.insert(x, hABRordinata[x] / i)
        hARNordinataMedia.insert(x, hARNordinata[x] / i)

        tempiOinsertABR.insert(x, timeABRinsertO[x] / i)
        tempiOinsertARN.insert(x, timeARNinsertO[x] / i)

        # scrittura su file InserimentoOrdinato.txt
        if x % 5:
            g.write(str(j))
            g.write(' & ')
            temp = round((float(timeABRinsertO[x] / i)), 5)
            g.write(str(temp))
            g.write(' & ')
            temp = round((float(timeARNinsertO[x] / i)), 5)
            g.write(str(temp))
            g.write(' & ')
            temp = int(hABRordinata[x] / i)
            g.write(str(temp))
            g.write(' & ')
            temp = int(hARNordinata[x] / i)
            g.write(str(temp))
            g.write(' \\\ \hline\n')


        temporicABRO.insert(x, timeABRO[x] / i)
        temporicARNO.insert(x, timeARNO[x] / i)

        #scrittura su file RicercaOrdinata.txt
        if x % 5:
            h.write(str(j))
            h.write(' & ')

            temp = round((float(timeABRO[x] / i)), 7)
            h.write(str(temp))
            h.write(' & ')

            temp = round((float(timeARNO[x] / i)), 7)
            h.write(str(temp))
            h.write(' & ')

            h.write(str(int(hABRordinata[x] / i)))
            h.write(' & ')

            h.write(str(int(hARNordinata[x] / i)))
            h.write(' \\\ \hline\n')


    #plotting

    x = np.arange(10, 2000, 100)
    plt.plot(x, tempiRinsertABR, label="ABR")
    plt.plot(x, tempiRinsertARN, label="ARN")
    plt.legend()
    plt.savefig('ABRrandom.png', bbox_inches='tight')
    plt.close()

    plt.plot(x, temporicABRR, label="ABR")
    plt.plot(x, temporicARNR, label="ARN")
    plt.legend()
    plt.savefig('ABRricR.png', bbox_inches='tight')
    plt.close()

    plt.plot(x, tempiOinsertABR, label="ABR")
    plt.plot(x, tempiOinsertARN, label="ARN")
    plt.legend()
    plt.savefig('ABRordinati.png', bbox_inches='tight')
    plt.close()

    plt.plot(x, temporicABRO, label="ABR")
    plt.plot(x, temporicARNO, label="ARN")
    plt.legend()
    plt.savefig('ABRricO.png', bbox_inches='tight')
    plt.close()

    e.close()
    f.close()
    g.close()
    h.close()


if __name__ == '__main__':
    main()



