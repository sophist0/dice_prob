import math
import matplotlib.pyplot as plt

def compute_m_2():
    max_dice = 20
    min_dice = 2
    dvec = list(range(min_dice, max_dice+1))
    qvec = []

    for n in dvec:
        q = 1 - 2*math.pow(5/6,n) + math.pow(2/3,n)
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
