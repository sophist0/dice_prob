import math
import matplotlib.pyplot as plt

def compute_m_1():
    max_dice = 20
    min_dice = 1
    dvec = list(range(min_dice, max_dice+1))
    qvec = []

    for n in dvec:
        q = 1 - math.pow(5/6,n)
        qvec.append(q)

    return dvec, qvec

def compute_m_2():
    max_dice = 20
    min_dice = 2
    dvec = list(range(min_dice, max_dice+1))
    qvec = []

    for n in dvec:
        q = 1 - 2*math.pow(5/6,n) + math.pow(4/6,n)
        qvec.append(q)

    return dvec, qvec

def compute_m_3():
    max_dice = 20
    min_dice = 3
    dvec = list(range(min_dice, max_dice+1))
    qvec = []

    for n in dvec:
        q = 1 - 3*math.pow(5/6,n) + 3*math.pow(4/6,n) - math.pow(3/6,n)
        qvec.append(q)

    return dvec, qvec

def compute_m_4():
    max_dice = 20
    min_dice = 4
    dvec = list(range(min_dice, max_dice+1))
    qvec = []

    for n in dvec:
        q = 1 - 4*math.pow(5/6,n) + 6*math.pow(4/6,n) - 4*math.pow(3/6,n) + math.pow(2/6,n)
        qvec.append(q)

    return dvec, qvec

def compute_m_5():
    max_dice = 20
    min_dice = 5
    dvec = list(range(min_dice, max_dice+1))
    qvec = []

    for n in dvec:
        q = 1 - 5*math.pow(5/6,n) + 10*math.pow(4/6,n) - 10*math.pow(3/6,n) + 5*math.pow(2/6,n) + math.pow(1/6,n)
        qvec.append(q)

    return dvec, qvec

def compute_m_6():
    max_dice = 20
    min_dice = 6
    dvec = list(range(min_dice, max_dice+1))
    qvec = []

    for n in dvec:
        q = 1 - 6*math.pow(5/6,n) + 15*math.pow(4/6,n) - 20*math.pow(3/6,n) + 15*math.pow(2/6,n) + 6*math.pow(1/6,n)
        qvec.append(q)

    return dvec, qvec

def plot_results(dvec, qvec):
    plt.plot(dvec, qvec)
    plt.xlabel("dice rolled")
    plt.ylabel("seq probability")
    plt.title("seq: 1,2")
    plt.legend(["Analytic Results"])
    plt.show()

if __name__ == "__main__":
    dvec, qvec = compute_m_2()
    plot_results(dvec, qvec)
