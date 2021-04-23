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

import random

#Mutate the individual depending on the mutation rate
def mutate(individual, mutation_rate):
    for swapped in range(len(individual)):
        if(random.random() < mutation_rate):
            swap_with = int(random.random() * len(individual))
            
            city1 = individual[swapped]
            city2 = individual[swap_with]
            
            individual[swapped] = city2
            individual[swap_with] = city1
    return individual


#Mutate the population depending on the mutation rate
def mutate_population(population, mutation_rate):
    mutated_population = []
    
    for ind in range(0, len(population)):
        mutated_ind = mutate(population[ind], mutation_rate)
        mutated_population.append(mutated_ind)
    return mutated_population