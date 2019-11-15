#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 10:53:21 2019

@author: matthiasboeker
"""
#Create Cosine Similarity Matrix 


from sklearn.metrics.pairwise import cosine_similarity

div = 10 
cos_corr_mat = np.zeros((int(cc.shape[1]/div),int(cc.shape[1]/div)))
for i in range(0, int(cc.shape[1]/div)):
    for j in range(0, int(cc.shape[1]/div)):
        cos_corr_mat[j,i] = cosine_similarity(cc.iloc[:,i].values.reshape(-1, 1),cc.iloc[:,j].values.reshape(-1, 1))