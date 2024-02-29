import random
import pickle
import itertools

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
            n_combos = seq_combos[n]
            for combo in n_combos:
                in_seq = []
                out_seq = []
                for val in self.seq:
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
    def __init__(self, seq, sim_params, dice):
        self.seq = seq
        self.trials = sim_params.trials
        self.dice = dice
        self.val_stats = None
        self.seq_stats = None
        self.init_data(sim_params.val_stats, sim_params.seq_stats)

    def init_data(self, val_props, seq_props):
        self.val_stats = {}
        for val in self.seq:
            self.val_stats[val] = {}
            for stat in val_props:
                self.val_stats[val][stat] = 0

        self.seq_stats = {}
        for label in seq_props:
            self.seq_stats[label] = 0

    def find_seq_len(self, seq_len):
        seq_len_labels = []
        for stat in self.seq_stats:
            sstat = stat.split("_")
            in_seq = sstat[0].split(",")
            if len(in_seq) == 1 and in_seq[0] == "":
                len_in_seq = 0
            else:
                len_in_seq = len(in_seq)

            if len_in_seq == seq_len:
                seq_len_labels.append(stat)
        return seq_len_labels

    def display_results(self):
        print()
        print("########################################################################")
        print()
        print("dice rolled: ", self.dice)
        print("probability 1: ", self.val_stats[1]["in_roll"]/self.trials)
        print("probability not 1: ", self.val_stats[1]["not_in_roll"]/self.trials)
        seq_in_label = self.find_seq_len(len(self.seq))
        print("probability " + seq_in_label[0] + ": ", self.seq_stats[seq_in_label[0]]/self.trials)
        seq_in_label = self.find_seq_len(0)
        print("probability " + seq_in_label[0] + ": ", self.seq_stats[seq_in_label[0]]/self.trials)
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
        if len(str_list) > 0:
            tmp = str_list.split(",")
            return list(map(int, tmp))
        else:
            return []

    def run(self, dice):
        roll = random.choices([1, 2, 3, 4, 5, 6], k=dice)
        for val in self.target_seq:
            if self._check_val_in_roll(val, roll):
                self.data.val_stats[val]["in_roll"] += 1

            if not self._check_val_in_roll(val, roll):
                self.data.val_stats[val]["not_in_roll"] += 1

        for label in self.data.seq_stats.keys():
            slabel = label.split("_")
            seq1 = self._str_list_2_seq(slabel[0])
            seq2 = self._str_list_2_seq(slabel[2])

            if self._check_seq1_in_seq2_out(seq1, seq2, roll):
                self.data.seq_stats[label] += 1

class DiceSim:
    def __init__(self, trials, seq, dvec):
        self.dice_vec = dvec
        self.seq = seq
        self.params = SimParams(trials, self.seq)
        self.sim_data = {}

    def run_trials_for_n_dice(self, dice):
        data = SimData(self.seq, self.params, dice)
        trial = SimTrial(self.seq, data)
        for x in range(self.params.trials):
            trial.run(dice)

        data.display_results()
        return data

    def _save_sim_data(self, seq_label, max_dice):
        data_dir = "data/"
        data_path = data_dir + "m_dice_" + str(max_dice) + "_" + seq_label[0] + ".p"
        data_file = open(data_path, 'wb')
        pickle.dump(self.sim_data, data_file)
        data_file.close()

    def run_sim(self):
        len_seq = len(self.seq)
        seq_prob = []
        for dice in self.dice_vec:
            data = self.run_trials_for_n_dice(dice)
            seq_len_label = data.find_seq_len(len_seq)
            seq_prob.append(data.seq_stats[seq_len_label[0]]/data.trials)

            sim_label = str(dice) + "_dice"
            self.sim_data[sim_label] = data

        max_dice = self.dice_vec[len(self.dice_vec)-1]
        self._save_sim_data(seq_len_label, max_dice)
        return seq_prob

def main():
    ########################################################################
    # Main
    ########################################################################

    # Estimate the probability of rolling a sequence
    dvec = list(range(0, 21))
    trials = 100000
    seq = list(range(1, 3))
    sim = DiceSim(trials, seq, dvec)
    _ = sim.run_sim()

if __name__ == '__main__':
    main()
