# -*- coding: utf-8 -*-
"""Group_main.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15BXjITh9FFvLfSyzeajpVY9AGkllIkvT
"""

import os
import sys
print(os.path.dirname(os.path.dirname( os.path.abspath(__file__) )) )
project_root_path = os.path.dirname(os.path.dirname( os.path.abspath(__file__) ))
sys.path.append(project_root_path)

import my_library.load_input_data as input_loader
import my_library.load_dictionary1 as dictionary1_loader
import my_library.load_dictionary2 as dictionary2_loader
import my_library.count_polarity_statistics as counter
import my_library.predict_polarity as predictor
import my_library.manage_output as output_manager

sentence_arrays = input_loader.load("../data/processed_data.txt")

d1 = dictionary1_loader.load("../data/dictionary1.txt")
d2 = dictionary2_loader.load("../data/dictionary2.txt")

result = []
for i in range(len(sentence_arrays)):
    sentence = sentence_arrays[i]
    count_statistics = counter.count(d1,d2,sentence)
    result.append( predictor.predict(count_statistics) )

output_manager.output(sentence_arrays, result)
