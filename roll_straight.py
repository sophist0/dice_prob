import random
import itertools
import matplotlib.pyplot as plt

class SimParams:
    def __init__(self, trials, seq):
        self.trials = trials
        self.seq = seq
        self.val_stats = ["in_roll", "not_in_roll"]

        # add seq_combo_labels (depend on the seq)
        self.seq_stats = []
        seq_combos = self._get_non_empty_combos()
        self._get_seq_stats(seq_combos)

    def _get_seq_stats(self, seq_combos):
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
                self.seq_stats.append(label)

    def _get_non_empty_combos(self):
        combos = []
        for n in range(0, len(self.seq)+1):
            combos.append(itertools.combinations(self.seq, n))
        return combos

class SimData:
    def __init__(self, sim_params, dice):
        self.trials = sim_params.trials
        self.dice = dice
        self.val_stats = None
        self.seq_stats = None
        self.init_data(seq, sim_params.val_stats, sim_params.seq_stats)

    def init_data(self, seq, val_props, seq_props):
        self.val_stats = {}
        for val in seq:
            self.val_stats[val] = {}
            for stat in val_props:
                self.val_stats[val][stat] = 0

        self.seq_stats = {}
        for label in seq_props:
            self.seq_stats[label] = 0

    def display_results(self):
        # Only works for the sequence 1,2
        print()
        print("########################################################################")
        print()
        print("dice: ", self.dice)
        print()
        print("probability 1 and 2: ", self.seq_stats["1,2_not_"]/self.trials)
        print()
        print("probability not 1 and not 2: ", self.seq_stats["_not_1,2"]/self.trials)
        print()
        print("probability 1: ", self.val_stats[1]["in_roll"]/self.trials)
        print()
        print("probability not 1: ", self.val_stats[1]["not_in_roll"]/self.trials)
        print()
        print("probability 1 and not 2: ", self.seq_stats["1_not_2"]/self.val_stats[2]["not_in_roll"])
        print()

class SimTrial:
    def __init__(self, seq, data):
        self.target_seq = seq
        self.data = data

    def _check_val_in_roll(self, val, roll):
        if (val in roll):
            return True
        return False

    def check_seq_in_roll(self, seq, roll):
        passed = True
        for val in seq:
            if not self._check_val_in_roll(val, roll):
                passed = False
                break
        return passed

    def check_no_val_in_roll(self, seq, roll):
        passed = True
        for val in seq:
            if self._check_val_in_roll(val, roll):
                passed = False
                break
        return passed

    def _check_seq1_in_seq2_out(self, seq1, seq2, roll):
        passed = True
        if not self.check_seq_in_roll(seq1, roll):
            passed = False

        if not self.check_no_val_in_roll(seq2, roll):
            passed = False
        return passed

    def _str_list_2_seq(self, str_list):
        # should be possible with map or lambda function
        nseq = []
        for val in str_list:
            if val != ",":
                nseq.append(int(val))
        return nseq

    def run(self, dice):
        roll = random.choices([1, 2, 3, 4, 5, 6], k=dice)
        for val in self.target_seq:
            if self._check_val_in_roll(val, roll):
                self.data.val_stats[val]["in_roll"] += 1

            if not self._check_val_in_roll(val, roll):
                self.data.val_stats[val]["not_in_roll"] += 1

        for label in self.data.seq_stats.keys():
            slabel = label.split("_")

            # should be possible with map or lambda function
            seq1 = self._str_list_2_seq(slabel[0])
            seq2 = self._str_list_2_seq(slabel[2])

            if self._check_seq1_in_seq2_out(seq1, seq2, roll):
                self.data.seq_stats[label] += 1

class DiceSim:
    def __init__(self, trials, seq, dvec):
        self.dice_vec = dvec
        self.params = SimParams(trials, seq)

    def run_trials_for_n_dice(self, dice):
        data = SimData(self.params, dice)
        trial = SimTrial(seq, data)
        for x in range(self.params.trials):
            trial.run(dice)

        data.display_results()
        return data

    def run_sim(self):
        seq_prob = []
        for dice in self.dice_vec:
            data = self.run_trials_for_n_dice(dice)
            seq_prob.append(data.seq_stats["1,2_not_"]/trials)
        return seq_prob

########################################################################
# Main
########################################################################

# Estimate the probability of rolling a straight
dvec = list(range(1, 11))
trials = 100000
seq = list(range(1, 3))

sim = DiceSim(trials, seq, dvec)
seq_prob = sim.run_sim()

########################################
# plot
########################################
plt.plot(dvec, seq_prob)
plt.xlabel("dice rolled")
plt.ylabel("seq probability")
plt.title("seq: 1,2")
plt.legend(["Simulation Results"])
plt.show()
