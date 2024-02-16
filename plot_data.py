import os
import pickle
import matplotlib.pyplot as plt
from roll_straight import SimData

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
    legend_names.append("seq: " + "".join(char_seq))

plt.xlabel("dice rolled")
plt.ylabel("seq probability")
plt.legend(legend_names)
plt.show()

