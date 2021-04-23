#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
EGE DOĞAN DURSUN - 05170000006
CEM ÇORBACIOĞLU - 05130000242
EGE ÜNİVERSİTESİ
MÜHENDİSLİK FAKÜLTESİ
BİLGİSAYAR MÜHENDİSLİĞİ BÖLÜMÜ
2019 - 2020 BAHAR DÖNEMİ 
İŞLEMSEL ZEKA VE DERİN ÖĞRENME DERSİ
PROJE 1 : SORU 2 : ALTERNATİF 2 : BRIDGE AND TORCH PROBLEMİ ÇÖZÜMÜ
YÖNTEM : A* SEARCH & BRUTE FORCE ALGORITHM
TARİH: 20 NİSAN 2020


NOTE:
    While developing our program we have first approached our problem with A* Search to optimize the passing time. 
    But the problem is, even though optimization algorithms are good for minimizing the passing time for the bridge to a lower cost ,
    they have "failed" to lower the cost under the threshold of the torch time limit. So, in order to achieve success and reducing the
    cost under the maximum burn time of the torch, we have applied brute force method.
    
    The lowest amount of time we have reached with the A* Search is : 32 minutes (The maximum time the torch has is 30 minutes. So it does not solve the problem.)
    
    What was the method the A* used to reduce the cost
    
    (A)(B)(C)(D)(E) ---bridge--- ( )( )( )( )( )( )
    A is the one with the minimum cost (1 minutes), B is the one with the second minimum cost (3 minutes). They pass the bridge together in "3" minutes. Total elapsed time is 3 minutes.
    ( )( )(C)(D)(E) ---bridge--- ( )( )( )( )(A)(B)
    A is the one with the minimum cost (1 minutes) on the right side of the bridge. It turns back with the torch in "1" minute. Total elapsed time is 4 minutes.
    ( )(A)(C)(D)(E) ---bridge--- ( )( )( )( )( )(B)
    A is the one with the minimum cost (1 minutes), C is the one with the second minimum cost (6 minutes). They pass the bridge together in "6" minutes. Total elapsed time is 10 minutes.
    ( )( )( )(D)(E) ---bridge--- ( )( )( )(A)(C)(B)
    A is the one with the minimum cost (1 minute) on the right side of the bridge. It turns back with the torch in "1" minute. Total elapsed time is 11 minutes.
    ( )( )(A)(D)(E) ---bridge--- ( )( )( )( )(C)(B)
    A is the one with the minimum cost (1 minute), D is the one with the second minimum cost (8 minutes.) They pass the bridge together in "8" minutes. Total elapsed time is 19 minutes.
    ( )( )( )( )(E) ---bridge--- ( )( )(A)(D)(C)(B)
    A is the one with the minimum cost (1 minute) on the right side of the bridge. It turns back with the torch in "1" minute. Total elapsed time is 20 minutes.
    ( )( )( )(A)(E) ---bridge--- ( )( )( )(D)(C)(B)
    A is the one with the minimum cost (1 minute), E is the one with the second minimum cost (12 minutes). They pass the bridge together in "12" minutes. Total elapsed time is 32 minutes.
    ( )( )( )( )( ) ---bridge--- (A)(E)(D)(C)(B)
    The bridge is passed by everyone in a total of 32 minutes. But the torch only lasts for 30 minutes. So A* search algorithm failed to find a solution.
    
    If you want to try it, the method that solves the problem with A* is in the ASharp_Solver class. The testing line is in the test page and commented out.
    
"""


#Importing the necessary libraries and modules
from Person import Person
from Torch import Torch
from Bridge import Bridge
from ASharp_Solver import solve_bridge_and_torch, solve_bridge_and_torch_asharp
import time as t

#Solution tours will be 25 times
total_sol_num = 25


#Defining people for the first type of problem
people_1 = {
        "A" : Person(pass_time=1),
        "B" : Person(pass_time=2),
        "C" : Person(pass_time=5),
        "D" : Person(pass_time=8),
}

#Defining people for the second type of problem
people_2 = {
        "A" : Person(1),
        "B" : Person(3),
        "C" : Person(6),
        "D" : Person(8),
        "E" : Person(12),
        }

#Defining the torches for the problem
torch_1 = Torch(burn_time=15)

torch_2 = Torch(burn_time=30)


#Defining the Bridges we will use for the problem
bridge_1 = Bridge(people=people_1)

bridge_2 = Bridge(people=people_2)


#This is commented out because it belongs to the question 1, which is another version of the problem, we solved the one on the video
#that was mentioned on the homework file.
"""
result_1, _ = solve_bridge_and_torch(bridge=bridge_1, torch=torch_1, n_epochs=1000)
print("Question 1 : Is there a result? : ", ("YES" if result_1 else "NO"))
"""


#Solving the problem with A* algorithm
solve_bridge_and_torch_asharp(bridge_2, torch_2)


#Solving the question N number of times
times = []
epoch_to_solution = []
for i in range(0, total_sol_num):
    start = t.time()
    result_2, tour_count = solve_bridge_and_torch(bridge=bridge_2, torch=torch_2, n_epochs=5000)
    end = t.time()
    tot_time = end-start
    print("Question 2 : Is there a result? : ", ("YES" if result_2 else "NO"))
    times.append(tot_time)
    epoch_to_solution.append(tour_count)
    

#Show the times until finding the solution for each tour.
for i in range(0, len(times)):
    print("For Solution Number ", (i+1), " -> Time until finding the solution : ", times[i], " seconds.")
   
print("\n")

#Show the average time until finding the solution
avg_time = sum(times) / len(times)
print("AVERAGE TIME TO FIND THE SOLUTION: ", avg_time, " seconds.")
print("\n\n")


#Show the epochs until finding the solution for each tour.
for i in range(0, len(epoch_to_solution)):
    print("For Solution Number ", (i+1), " -> Number of epochs to find the solution : ", epoch_to_solution[i])
   
print("\n")
    
#Show the average epoch amount until finding the solution
avg_epoch = sum(epoch_to_solution) / len(epoch_to_solution)
print("AVERAGE EPOCH AMOUNT TO FIND THE SOLUTION: ", avg_epoch)
    
