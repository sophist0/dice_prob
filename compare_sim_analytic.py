import os
import pickle
import matplotlib.pyplot as plt
from roll_straight import SimData
from analytic_sol import compute_m_1, compute_m_2, compute_m_3, compute_m_4, compute_m_5, compute_m_6

def main():
    data_dir = "data/"
    data_files = os.listdir(data_dir)
    data_files.sort(reverse=True)

    legend_names = []
    dice_vec = list(range(0, 21))
    for file_name in data_files:

        prob_vec = []
        data_file = open(data_dir + file_name, "rb")
        data = pickle.load(data_file)
        seq = file_name.split("_")[3]
        seq_label = seq + "_not_"    

        for dice in dice_vec:
            key = str(dice) + "_dice"
            dice_data = data[key]
            prob_vec.append(dice_data.seq_stats[seq_label] / dice_data.trials)

        print(prob_vec)
        print(seq)
        char_seq = list(map(str, seq))
        plt.plot(dice_vec, prob_vec)
        legend_names.append("sim seq: " + "".join(char_seq))

    # analytic sol
    dvec, qvec = compute_m_1()
    plt.plot(dvec, qvec, "*")

    dvec, qvec = compute_m_2()
    plt.plot(dvec, qvec, "*")

    dvec, qvec = compute_m_3()
    plt.plot(dvec, qvec, "*")

    dvec, qvec = compute_m_4()
    plt.plot(dvec, qvec, "*")

    dvec, qvec = compute_m_5()
    plt.plot(dvec, qvec, "*")

    dvec, qvec = compute_m_6()
    plt.plot(dvec, qvec, "*")

    analytic_legend = ["analyic seq: 1", "analyic seq: 1,2", "analyic seq: 1,2,3", "analyic seq: 1,2,3,4", "analyic seq: 1,2,3,4,5", "analyic seq: 1,2,3,4,5,6"]

    plt.xlabel("dice rolled")
    plt.ylabel("seq probability")
    plt.legend(legend_names + analytic_legend)
    plt.show()

if __name__ == "__main__":
    main()