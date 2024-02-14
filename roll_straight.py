import random
import itertools
import matplotlib.pyplot as plt

def check_val_in_roll(val, roll):
    if (val in roll):
        return True
    return False


def check_seq_in_roll(seq, roll):
    passed = True
    for val in seq:
        if not check_val_in_roll(val, roll):
            passed = False
            break
    return passed


def check_no_val_in_roll(seq, roll):
    passed = True
    for val in seq:
        if check_val_in_roll(val, roll):
            passed = False
            break
    return passed


def check_seq1_in_seq2_out(seq1, seq2, roll):
    passed = True
    if not check_seq_in_roll(seq1, roll):
        passed = False

    if not check_no_val_in_roll(seq2, roll):
        passed = False
    return passed


def init_data(val_stats, seq_stats, combo_stats):
    data = {}
    for val in seq:
        data[val] = {}
        for stat in val_stats:
            data[val][stat] = 0

    for stat in seq_stats:
        data[stat] = 0

    data["combo_stats"] = {}
    for label in combo_stats:
        data["combo_stats"][label] = 0

    return data

def get_non_empty_combos(seq):
    combos = []
    for n in range(1, len(seq)):
        combos.append(itertools.combinations(seq, n))
    return combos

def str_list_2_seq(str_list):
    # should be possible with map or lambda function
    nseq = []
    for val in str_list:
        if val != ",":
            nseq.append(int(val))
    return nseq

def run_trials_for_n_dice(seq, dice, trials, val_stats, seq_stats, combo_stats):

    data = init_data(val_stats, seq_stats, combo_stats)
    for x in range(trials):

        roll = random.choices([1, 2, 3, 4, 5, 6], k=dice)

        if check_seq_in_roll(seq, roll):
            data["seq_in_roll"] += 1

        if check_no_val_in_roll(seq, roll):
            data["no_val_in_roll"] += 1

        for val in seq:
            if check_val_in_roll(val, roll):
                data[val]["in_roll"] += 1

            if not check_val_in_roll(val, roll):
                data[val]["not_in_roll"] += 1

        for label in data["combo_stats"]:
            slabel = label.split("_")

            # should be possible with map or lambda function
            seq1 = str_list_2_seq(slabel[0])
            seq2 = str_list_2_seq(slabel[2])

            if check_seq1_in_seq2_out(seq1, seq2, roll):
                data["combo_stats"][label] += 1

    print()
    print("########################################################################")
    print()
    print("dice: ", dice)
    print()
    print("probability 1 and 2: ", data["seq_in_roll"]/trials)
    print()
    print("probability not 1 and not 2: ", data["no_val_in_roll"]/trials)
    print()
    print("probability 1: ", data[1]["in_roll"]/trials)
    print()
    print("probability not 1: ", data[1]["not_in_roll"]/trials)
    print()
    print("probability 1 and not 2: ", data["combo_stats"]["1_not_2"]/data[1]["not_in_roll"])
    print()
    return data


# Estimate the probability of rolling a straight
dvec = list(range(1,21))
trials = 100000
seq = list(range(1, 3))

val_stats = ["in_roll", "not_in_roll"]

# these are really combo stats for empty seqs
seq_stats = ["seq_in_roll", "no_val_in_roll"]

# add seq_combo_labels (depend on the seq)
combo_stats = []
seq_combos = get_non_empty_combos(seq)
for n in range(len(seq_combos)):
    print()
    print("n=", n+1)
    n_combos = seq_combos[n]
    for combo in n_combos:
        print(combo)

        in_seq = []
        out_seq = []
        for val in seq:
            if val in combo:
                in_seq.append(str(val))
            else:
                out_seq.append(str(val))
        label = ",".join(in_seq) + "_not_" + ",".join(out_seq)
        combo_stats.append(label)

print()
print("combos")
print(combo_stats)
print()

seq_prob = []
for dice in dvec:
    data = run_trials_for_n_dice(seq, dice, trials, val_stats, seq_stats, combo_stats)
    seq_prob.append(data["seq_in_roll"]/trials)


########################################
# plot
########################################
plt.plot(dvec, seq_prob)
plt.xlabel("dice rolled")
plt.ylabel("seq probability")
plt.title("seq: 1,2")
plt.legend(["Simulation Results"])
plt.show()
