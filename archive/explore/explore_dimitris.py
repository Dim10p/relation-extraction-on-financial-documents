import pandas as pd
import numpy as np
from scipy.special import softmax
import os
import warnings

pd.options.display.max_colwidth = 100

warnings.simplefilter('ignore', FutureWarning)

df = pd.read_csv(f"{os.getcwd()}\\data\\output5_clean.csv", sep =';')

df['rel_groups_vector'] = df[[str(el) for el in list(np.arange(0,22))]].agg(np.array, axis=1)

df['rel_groups_vector_softmax'] = df['rel_groups_vector'].apply(softmax)

for i in range(22):
    df[f'softmax_{i}'] = df['rel_groups_vector_softmax'].apply(lambda x: pd.Series(x[i]))

df = df.drop(['Unnamed: 0.1', 'Unnamed: 0'], axis=1)

liste = [4.118063,	-0.6361298,	-0.31008655,	-0.48232475,	-0.5064283,	-0.85803676,	-1.484623,	0.27575624,	-0.652831,	-0.8679416,	-1.1210598,	-1.3328899,	-1.0079081,	1.0568024,	3.424184,	-0.9927346,	-0.5455323,	-1.3844525,	-1.1201564,	1.3946096,	-0.6836917,	-0.82878566]
softmax(liste)


df["max_softmax"] = df['rel_groups_vector_softmax'].apply(lambda x: max(x))

def get_second_largest_and_position(lst):
    if len(lst) < 2:
        raise ValueError("List should have at least two elements.")

    largest = float('-inf')  # Initialize with negative infinity
    second_largest = float('-inf')  # Initialize with negative infinity
    largest_index = -1
    second_largest_index = -1

    for i, num in enumerate(lst):
        if num > largest:
            second_largest = largest
            second_largest_index = largest_index
            largest = num
            largest_index = i
        elif num > second_largest and num != largest:
            second_largest = num
            second_largest_index = i

    if second_largest_index == -1:
        raise ValueError("No second largest element found in the list.")

    return [second_largest, second_largest_index]


# test:
my_list = [5, 9, 2, 7, 3, 8, 1, 6, 4]
get_second_largest_and_position(my_list)

df["max_softmax_second"] = df['rel_groups_vector_softmax'].apply(lambda x: get_second_largest_and_position(x))

def monkey_classifier(pred: int,
                      max_prob: float,
                      second_max: list,
                      minimum_accepted_zero: float,
                      minimum_accepted_next: float,
                      minimum_accepted_ratio: float):

  if (pred == 0) & (max_prob < minimum_accepted_zero) & (second_max[0] > minimum_accepted_next) & (second_max[0] / max_prob > minimum_accepted_ratio):
    return second_max[1]
  else:
    return pred

df["corrected_prediction"] = df.apply(lambda row: monkey_classifier(pred=row["prediction"],
                                                                    max_prob=row["max_softmax"],
                                                                    second_max=row["max_softmax_second"],
                                                                    minimum_accepted_zero=1,
                                                                    minimum_accepted_next=0,
                                                                    minimum_accepted_ratio=0.7),
                                      axis=1)

import matplotlib.pyplot as plt
plt.hist(df[df.prediction==0]["max_softmax_second"].apply(lambda x: x[0]))

df["prediction"].value_counts(normalize=False)

df["corrected_prediction"].value_counts(normalize=False)

test = df[df.prediction!=df.corrected_prediction]

output = df[['corrected_prediction']]

output.to_csv(f"{os.getcwd()}\\data\\submission_16.csv", sep ='\t', header = False, index= False)

#0.9,0.3,0.6 submission 16