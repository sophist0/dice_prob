import math
from scipy.special import comb
import matplotlib.pyplot as plt

def compute_m_3():
    max_dice = 20
    min_dice = 3
    dvec = list(range(min_dice, max_dice+1))
    qvec = []

    for n in dvec:
        q = 1 - 3*math.pow(5/6,n) + 3*math.pow(4/6,n) - math.pow(3/6,n)
        qvec.append(q)

    return qvec, dvec

def analytic_sol(seq_end, max_dice):
    min_dice = seq_end
    dvec = list(range(min_dice, max_dice+1))
    qvec = []

    for n in dvec:
        q = 0
        for i in range(seq_end+1):
            frac = (6-i)/6
            c = comb(seq_end, i)
            sign = math.pow(-1, i)
            q += sign * c * math.pow(frac, n)
        qvec.append(q)
    return qvec, dvec
