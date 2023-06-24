# !pip install accelerate -U
# !pip install transformers
# !pip install datasets

from src.utils.data_utils import convert_to_list

import os
import pandas as pd
import numpy as np

# set environtmental variable CUDA_LAUNCH_BLOCKING equal to 1 (forces the CPU to be synchronized with the GPU during CUDA operations):
os.environ['CUDA_LAUNCH_BLOCKING'] = "1"

train = pd.read_json("data\\public\\train_refind_official.json")
dev = pd.read_json("data\\public\\dev_refind_official.json")
test = pd.read_json("data\\public\\test_refind_official.json")


private = pd.read_json("data\\private\\private_dataset.json")



# Apply conversion function to the column
train['spacy_ner'] = train["spacy_ner"].apply(convert_to_list)
dev['spacy_ner'] = dev["spacy_ner"].apply(convert_to_list)
test['spacy_ner'] = test["spacy_ner"].apply(convert_to_list)
private['spacy_ner'] = private["spacy_ner"].apply(convert_to_list)


type(private['spacy_ner'][3])


private['spacy_ner']

token_list = ['aGvHD', 'Phase', '1', 'Trial', 'In', 'March', '2021', ',', 'results', 'were', 'published', 'from', 'an', 'Investigator', 'Sponsored', 'Phase', '1', 'study', 'conducted', 'by', 'Joseph', 'Pidala', ',', 'MD', ',', 'PhD', '(', 'Moffitt', 'Cancer', 'Center', ')', ',', 'and', 'Brian', 'C.', 'Betts', ',', 'MD', '(', 'Masonic', 'Cancer', 'Center', 'at', 'the', 'University', 'of', 'Minnesota', ')', ',', 'evaluating', 'pacritinib', ',', 'an', 'investigational', 'oral', 'kinase', 'inhibitor', 'with', 'specificity', 'for', 'JAK2', ',', 'for', 'the', 'prevention', 'of', 'acute', 'graft', '-', 'versus', '-', 'host', 'disease', '(', 'aGvHD', ')', '.']
e1_start = 33
e2_start = 13
ner_list= ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'TITLE', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'PERSON', 'PERSON', 'PERSON', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']

def create_input(token_list, e1_start, e2_start, ner_list):
  output_text = ""
  for i in range(0, len(token_list)):
    if i == e1_start:
      text = str(ner_list[i]) + " "+ str(token_list[i])
      #text =  " "+ str(token_list[i])
    elif i == e2_start:
      text = str(ner_list[i]) + " "+ str(token_list[i])
      #text =  " "+ str(token_list[i])
    else:
      text = token_list[i]
    output_text= output_text + " " + text
  return output_text

test_cleaning = create_input(token_list, e1_start, e2_start, ner_list)
print(test_cleaning)


mapping = { "no_relation": 0,
            "org:date:formed_on" : 1,
            "org:gpe:operations_in" : 2,
            "pers:org:member_of" : 3,
            "pers:org:employee_of" : 4,
            "pers:gov_agy:member_of" : 5,
            "org:org:acquired_by" : 6,
            "org:money:loss_of" : 7,
            "org:gpe:headquartered_in" : 8,
            "pers:univ:employee_of" : 9,
            "org:date:acquired_on" : 10,
            "pers:univ:attended" : 11,
            "org:gpe:formed_in" : 12,
            "org:money:profit_of" : 13,
            "org:money:cost_of" : 14,
            "org:org:subsidiary_of" : 15,
            "org:org:shares_of" : 16,
            "pers:org:founder_of" : 17,
            "pers:title:title" : 18,
            "org:money:revenue_of" : 19,
            "org:org:agreement_with" : 20,
            "pers:univ:member_of":21}

from tqdm import tqdm
tqdm.pandas(desc="create clean input TRAIN")
train["text"] = train.progress_apply(lambda row: create_input(token_list =row["token"], e1_start=row["e1_start"], e2_start = row["e2_start"], ner_list = row["spacy_ner"] ), axis=1)
train["label"] = train["relation"].map(mapping)
train = train[train['label'].notna()]
train.label = train.label.astype(int)

tqdm.pandas(desc="create clean input VAL")
dev["text"] = dev.progress_apply(lambda row: create_input(token_list =row["token"], e1_start=row["e1_start"], e2_start = row["e2_start"], ner_list = row["spacy_ner"] ), axis=1)
dev["label"] = dev["relation"].map(mapping)
dev = dev[dev['label'].notna()]
dev.label = dev.label.astype(int)


tqdm.pandas(desc="create clean input TEST")
test["text"] = test.progress_apply(lambda row: create_input(token_list =row["token"], e1_start=row["e1_start"], e2_start = row["e2_start"], ner_list = row["spacy_ner"] ), axis=1)
test["label"] = test["relation"].map(mapping)
test = test[test['label'].notna()]
test.label = test.label.astype(int)

tqdm.pandas(desc="create clean input PRIVATE-TEST")
private_test["text"] = private_test.progress_apply(lambda row: create_input(token_list =row["token"], e1_start=row["e1_start"], e2_start = row["e2_start"], ner_list = row["spacy_ner"] ), axis=1)
private_test["label"] = 0
private_test = private_test[private_test['label'].notna()]
private_test.label = private_test.label.astype(int)

private_test["text"][0]

import pandas as pd
from datasets import Dataset

def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

train = train.filter(["text","relation","rel_group","label"])
dev = dev.filter(["text","relation","rel_group","label"])
test = test.filter(["text","relation","rel_group","label"])

df = train.append(dev).append(test)