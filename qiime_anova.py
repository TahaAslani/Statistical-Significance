# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 20:56:56 2019

@author: Taha
"""

import pandas as pd
import numpy as np
from scipy import stats

BIOM =  pd.read_excel('table.from_biom.tsv.xlsx')
META =  pd.read_table('sample-metadata.tsv', sep='\t')

LABELS = META.iloc[:,3]
IDS = META.iloc[:,0]
LABELSLIST = list(set(LABELS[1:]))
LOGICAL = np.full((LABELS.shape[0],len(LABELSLIST)), False, dtype=bool)
IDset = []

for ii in range(len(LABELSLIST)):
    
    MyLable = LABELSLIST[ii]
    LOGICAL[:,ii] = LABELS == MyLable
    IDset.append(IDS[LOGICAL[:,ii]])
    
DATA = [[]] * len(IDset)
ChosenRow = 5
for jj in range(1,BIOM.shape[1]):
    for SetCounter in range(len(LABELSLIST)):
        
        if BIOM.iloc[0,jj] in list(IDset[SetCounter]):
            DATA[SetCounter] = DATA[SetCounter] + [BIOM.iloc[ChosenRow,jj]]

stats.ttest_ind(DATA[2],DATA[3], axis=0, equal_var=False)[1]
stats.f_oneway(DATA[0],DATA[1],DATA[2],DATA[3])[1]