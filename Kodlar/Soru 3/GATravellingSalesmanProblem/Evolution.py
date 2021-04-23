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

import FitnessEvaluation
import MatingPool
import Mutation
import Population
import matplotlib.pyplot as plt
import time


#This function handles the operations for each evolutionary generation
def next_generation(current_gen, elite_pop_size, mutation_rate):
    
    #Rank the population depending on the fitness level
    pop_ranked = FitnessEvaluation.rank_routes(current_gen)
    
    #Select parents by using the ranked population (depending on fitness level)
    selection_results = MatingPool.selection(pop_ranked, elite_pop_size)
    
    #Create a mating pool by using the selection results from the previous line
    matingpool = MatingPool.mating_pool(current_gen, selection_results)
    
    #Breed the parents in the mating pool and create children
    children = MatingPool.breed_population(matingpool, elite_pop_size)
    
    #Mutate the population / or not, depending on the mutation rate
    next_generation = Mutation.mutate_population(children, mutation_rate)
    
    #return the next generation
    return next_generation


#This function is the wrapper function that handles the evolution in multiple generations
def genetic_algorithm(pop_size, elite_size, mutation_rate, generations, graph_pieces, city_amount, max_distance_xy, population=None, time_share=None):
    
    #Create a city list for the 
    if (population == None):
        population = Population.create_cities(city_amount, max_distance_xy)
    
    #Create an initial population
    pop = Population.initial_population(pop_size, population)
    
    progress = []
    progress.append(1 / FitnessEvaluation.rank_routes(pop)[0][1])
    
    #Initial distance before begining the genetic algorithm
    initial_distance = (1 / FitnessEvaluation.rank_routes(pop)[0][1])
    
    #Start the genetic algorithm
    if time_share == None:
        for i in range(0, generations):
            pop = next_generation(pop, elite_size, mutation_rate)
            progress.append(1 / FitnessEvaluation.rank_routes(pop)[0][1])
        
            if i%(int)(generations/100) == 0:
                print("%",(int(i/generations*100)), end =" => ")
            #We show the graph of the fitness level in population for a total number of "graphPieces"
            if i%(generations/graph_pieces) == 0:
                plt.plot(progress)
                plt.title("Fitness Level among Population")
                plt.ylabel('Distance')
                plt.xlabel('Generation')
                plt.pause(0.000001)
        plt.title("Fitness Level among Population")
        plt.ylabel('Distance')
        plt.xlabel('Generation')
        plt.plot(progress)
        plt.show()
    else:
        total_time = 0
        i = 0
        while total_time < time_share:
            start = time.time()
            pop = next_generation(pop, elite_size, mutation_rate)
            progress.append(1 / FitnessEvaluation.rank_routes(pop)[0][1])
        
            if i%(int(time_share/(time_share/(20*time_share))/50)) == 0:
                print("%",(int(total_time/time_share*100)), end =" => ")
            #We show the graph of the fitness level in population for a total number of "graphPieces"
            if i%(int(time_share/(time_share/(20*time_share))/graph_pieces)) == 0:
                plt.plot(progress)
                plt.title("Fitness Level among Population")
                plt.ylabel('Distance')
                plt.xlabel('Generation')
                plt.pause(0.000001)
            
            end = time.time()
            time_elapsed = (end-start)
            total_time = total_time + time_elapsed
            i = i + 1
            
        plt.title("Fitness Level among Population")
        plt.ylabel('Distance')
        plt.xlabel('Generation')
        plt.plot(progress)
        plt.show()
    
    #Show the initial distance and the final solution (best one in population) to the user
    print("Initial Distance: ", initial_distance)
    print("Final Distance: " + str(1 / FitnessEvaluation.rank_routes(pop)[0][1]))
    best_route_index = FitnessEvaluation.rank_routes(pop)[0][0]
    best_route = pop[best_route_index]
    
    #Return the best route
    return best_route, progress