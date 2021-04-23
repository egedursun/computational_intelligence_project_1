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

import Evolution
import Population
import time
import matplotlib.pyplot as plt

"""
I will define a game like the following :
    -A logistics company want to distribute N95 face masks to warehouses in each of the 81 city in Turkey to help with COVID-19 infection.
    -They need to find an efficient way to deliver the face masks. 
    -The warehouses need the masks immediately so there is no time to find the "perfect" solution.
    -The company needs to find an "optimal" solution in the given amount of time.
    -
"""

#Define the hyperparameters that will be used in genetic algorithm
pop_size = 100
elite_pop_size = 20
mutation_rate = 0.01
generations = 100
city_amount = 81
max_distance_xy = 2000
graph_pieces = 2

#Maximum time to find solutions (minutes)
total_time = 5
total_turns = 10

time_share = (total_time*60)/total_turns

#Define a common city list (problem) for each turn
city_list = Population.create_cities(city_amount, max_distance_xy)

#Start the genetic algorithm
history = []
for i in range(0, 10):
    
    print("TURN NUMBER : ", (i+1))
    
    start = time.time()
    

    #This code works depending on the time limit and turn amount. It gives each turn an equal time share.
    bestRoute, progress = Evolution.genetic_algorithm(pop_size, 
                                           elite_pop_size, 
                                           mutation_rate, 
                                           generations,
                                           graph_pieces,
                                           city_amount,
                                           max_distance_xy,
                                           city_list,
                                           time_share)
    
    #This code ignores the time limit and trains the genetic algorithm based on the number of generations
    """
    bestRoute, progress = Evolution.genetic_algorithm(pop_size, 
                                           elite_pop_size, 
                                           mutation_rate, 
                                           generations,
                                           graph_pieces,
                                           city_amount,
                                           max_distance_xy,
                                           city_list)
    """


    end = time.time()
    history.append(progress)

    #Print the best route for the final population
    print("Best Route  (x1, y1) -> (x2, y2) -> ... -> (xn, yn) : ")
    print(bestRoute)

    #Print the total number of generations
    print("Total Number of Generations : ", generations)

    #Print the total time of the calculation
    elapsed_time = (end-start)
    print("Total Time Elapsed for Turn : ", int(elapsed_time*1000) , " milliseconds.")
    
    print("______________________________")
    

plt.title("Fitness Level among All Turns")
plt.ylabel('Distance')
plt.xlabel('Generation')
for i in range(0, len(history)):
    plt.plot(history[i])
plt.show()
    
    