#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EGE DOĞAN DURSUN - 05170000006
CEM ÇORBACIOĞLU - 05130000242
EGE ÜNİVERSİTESİ
MÜHENDİSLİK FAKÜLTESİ
BİLGİSAYAR MÜHENDİSLİĞİ BÖLÜMÜ
2019-2020 BAHAR DÖNEMİ
İŞLEMSEL ZEKA VE DERİN ÖĞRENME DERSİ  - CIDL2020-P1
PROJE 1 - SORU 3 - ALTERNATİF 3: GENETİK ALGORİTMALARLA TRAVELLING SALESMAN PROBLEMİ ÇÖZÜMÜ
TARİH : 13 NİSAN 2020
"""

import pandas as pd
import random
import numpy as np


#Select individuals from the ranked(sorted) population for creating the mating pool 
def selection(pop_ranked, elite_pop_size):
    selection_results = []
    df = pd.DataFrame(np.array(pop_ranked), columns=["Index","Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()
    
    for i in range(0, elite_pop_size):
        selection_results.append(pop_ranked[i][0])
    for i in range(0, len(pop_ranked) - elite_pop_size):
        pick = 100*random.random()
        for i in range(0, len(pop_ranked)):
            if pick <= df.iat[i,3]:
                selection_results.append(pop_ranked[i][0])
                break
    return selection_results
                
 
#Method for preparing the mating pool               
def mating_pool(population, selection_results):
    matingpool = []
    for i in range(0, len(selection_results)):
        index = selection_results[i]
        matingpool.append(population[index])
    return matingpool


#Breeding the parents
def breed(parent1, parent2):
    child = []
    child_P1 = []
    child_P2 = []
    
    gene_A = int(random.random() * len(parent1))
    gene_B = int(random.random() * len(parent1))
    
    start_gene = min(gene_A, gene_B)
    end_gene = max(gene_A, gene_B)

    for i in range(start_gene, end_gene):
        child_P1.append(parent1[i])
        
    child_P2 = [item for item in parent2 if item not in child_P1]

    child = child_P1 + child_P2
    return child


#Breeding method for the population
def breed_population(matingpool, elite_pop_size):
    children = []
    length = len(matingpool) - elite_pop_size
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0,elite_pop_size):
        children.append(matingpool[i])
    
    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool)-i-1])
        children.append(child)
    return children
    
    