import os
import pickle
import matplotlib.pyplot as plt
from sim_seq_roll import SimData
from analytic_sol import analytic_sol, compute_m_3

def plot_sim_data(dice_vec):
    data_dir = "data/"
    data_files = os.listdir(data_dir)
    data_files.sort(reverse=True)

    legend_names = []
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
    return legend_names

def show_plot(dice_vec, legend_names):

    plt.xticks(dice_vec, dice_vec)
    plt.xlabel("dice rolled")
    plt.ylabel("seq probability")
    plt.legend(legend_names)
    plt.show()

def main():
    max_dice = 20

    # Plot simulation data only
    dice_vec = list(range(0, max_dice+1))
    sim_legend = plot_sim_data(dice_vec)
    show_plot(dice_vec, sim_legend)

    # Plot simulation and analytical data m=3
    sim_legend = plot_sim_data(dice_vec)
    qvec, dvec = compute_m_3()
    plt.plot(dvec, qvec, "*")
    analytic_legend = ["analyic seq: 1,2,3"]
    show_plot(dice_vec, sim_legend + analytic_legend)

    # Plot simulation and analytical data
    sim_legend = plot_sim_data(dice_vec)
    analytic_legend = []
    seq_end = 1
    qvec, dvec = analytic_sol(seq_end, max_dice)
    plt.plot(dvec, qvec, "*")
    analytic_legend.append("analyic seq: 1")

    seq_end = 2
    qvec, dvec = analytic_sol(seq_end, max_dice)
    plt.plot(dvec, qvec, "*")
    analytic_legend.append("analyic seq: 1,2")

    seq_end = 3
    qvec, dvec = analytic_sol(seq_end, max_dice)
    plt.plot(dvec, qvec, "*")
    analytic_legend.append("analyic seq: 1,2,3")

    seq_end = 4
    qvec, dvec = analytic_sol(seq_end, max_dice)
    plt.plot(dvec, qvec, "*")
    analytic_legend.append("analyic seq: 1,2,3,4")

    seq_end = 5
    qvec, dvec = analytic_sol(seq_end, max_dice)
    plt.plot(dvec, qvec, "*")
    analytic_legend.append("analyic seq: 1,2,3,4,5")

    seq_end = 6
    qvec, dvec = analytic_sol(seq_end, max_dice)
    plt.plot(dvec, qvec, "*")
    analytic_legend.append("analyic seq: 1,2,3,4,5,6")

    show_plot(dice_vec, sim_legend + analytic_legend)

if __name__ == "__main__":
    main()
