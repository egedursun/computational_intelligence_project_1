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


#Import the necessary libraries
import random as r
import copy as cp


#A basic method to graphically represent the bridge to the user for each tour
def visualize_bridge(start_edge, end_edge):
    
    length = len(start_edge) + len(end_edge)

    print("[START-EDGE]   ", end=" ")
    for name, person in start_edge.items():
        print("(",name,")" , end=" ")   
    for i in range(0, length-len(start_edge)):
        print("(   )", end=" ")   
    print(" /============BRIDGE============/ ", end=" ")
    for i in range(0, length-len(end_edge)):
        print("(   )", end=" ")
    for name, person in end_edge.items():
        print("(",name,")", end=" ")
    print("   [END-EDGE]")
    

#A basic method to give the user a brief explanation of the problem.
def show_problem_definition(bridge, torch):
    print("BRIDGE AND TORCH PROBLEM DEFINITION")
    print("'N' PEOPLE come to a river in the night. There is a narrow BRIDGE, but it can only hold '2' PEOPLE at a time.")
    print("They have 1 torch and, because it's night, the TORCH has to be used when crossing the BRIDGE.")
    print("Each PERSON can pass the BRIDGE in 'X' minutes. When '2' PEOPLE cross the BRIDGE together, they must move at the 'SLOWER PERSONS' pace.") 
    print("The question is, can they all get across the BRIDGE if the TORCH lasts only 'Y' minutes?")
    print("_____________________________________")
    print("Total PEOPLE Amount : ", len(bridge.people))
    print("Burn Time of the TORCH : ", torch.burn_time)
    print("PEOPLE Information : ")
    for name, person in bridge.people.items():
        print("PERSON ", name, " can pass the bridge in ", person.pass_time , " minutes. ")
    print("_____________________________________")
    

#The wrapper function that runs the algorithm until a viable solution is found
#or the maximum epoch amount has been reached. It also counts the number of epochs until solution.
def solve_bridge_and_torch(bridge, torch, n_epochs):
    
    show_problem_definition(bridge, torch)
    
    satisfied = False
    tour_count = 0
    epoch = 0
    while satisfied == False and epoch < n_epochs:
        tour_count += 1
        epoch += 1
        print("Total Solution Searches : ", tour_count)
        satisfied = determine_routes(bridge, torch)
    
    return satisfied, tour_count


#The method that determines the routes for the people and runs the basic simulations for passing the bridge and coming back. 
def determine_routes(bridge, torch):
    
    start_edge_people = cp.copy(bridge.people)
    end_edge_people = {}
    
    visualize_bridge(start_edge_people, end_edge_people)
    
    burn_time = torch.burn_time
    elapsed_time = 0
    
    break_flag = False
    satisfied = True
    while break_flag == False:
        
        if elapsed_time > burn_time:
            print("Failed! Total Elapsed Time : ", elapsed_time)
            satisfied = False
            break_flag = True
            break
        elif (len(end_edge_people) == len(bridge.people)):
            print("Solution has been found! Total Elapsed Time: ", elapsed_time)
            satisfied = True
            break_flag = True
            break
        else:
            
            leader = None
            passer = None
            while leader == passer:
                
                """
                SELECT NEW CANDIDATES DEPENDING ON A* ALGORITHM
                """
                leader = r.choice(list(start_edge_people.items()))
                
                passer = r.choice(list(start_edge_people.items()))
                
            leader_pass_time = leader[1].pass_time
            
            if passer != None:
                passer_pass_time = passer[1].pass_time
            else:
                passer_pass_time = 0
                            
            spent_time = max(leader_pass_time, passer_pass_time)
            elapsed_time = elapsed_time + spent_time
            
            end_edge_people[passer[0]] = passer[1]
            start_edge_people.pop(passer[0])
            
            end_edge_people[leader[0]] = leader[1]
            start_edge_people.pop(leader[0])
            
            visualize_bridge(start_edge_people, end_edge_people)
            
            if len(start_edge_people) > 0:
                
                """
                SELECT THE RETURNER CANDIDATE DEPENDING ON A* ALGORITHM
                """
                returner = r.choice(list(end_edge_people.items()))
                returner_pass_time = returner[1].pass_time
                
                spent_time = returner_pass_time
                elapsed_time = elapsed_time + spent_time
                
                start_edge_people[returner[0]] = returner[1]
                end_edge_people.pop(returner[0])
                
                visualize_bridge(start_edge_people, end_edge_people)
                
            else:
                continue         
       
    print("___________")
    return satisfied
            

#The wrapper function that shows problem definition and calls the method that solves the problem using A* search algorithm        
def solve_bridge_and_torch_asharp(bridge, torch):
    
    show_problem_definition(bridge, torch)
    
    determine_route_asharp(bridge, torch)
    

#The basic method to get the person with the smallest cost from the group
def get_min_pass_time(people):
    min_name, min_person = r.choice(list(people.items()))
    for name, person in people.items():
        if person.pass_time <= min_person.pass_time:
            min_person = person
            min_name = name
    return min_name, min_person


#The method that determines the routes for the people using A* Algorithm
def determine_route_asharp(bridge, torch):
    
    start_edge_people = cp.copy(bridge.people)
    end_edge_people = {}
    
    elapsed_time = 0
    visualize_bridge(start_edge_people, end_edge_people)
    print("Total Elapsed Time : ", elapsed_time)
    
    while len(start_edge_people) != 0:
        name_passer_1, passer_1 = get_min_pass_time(start_edge_people)
        start_edge_people.pop(name_passer_1)
        name_passer_2, passer_2 = get_min_pass_time(start_edge_people)
        start_edge_people.pop(name_passer_2)
        
        passer_1_time = passer_1.pass_time
        passer_2_time = passer_2.pass_time
        
        pass_time = max(passer_1_time, passer_2_time)
        elapsed_time = elapsed_time + pass_time
        
        end_edge_people[name_passer_1] = passer_1
        end_edge_people[name_passer_2] = passer_2
        
        visualize_bridge(start_edge_people, end_edge_people)
        print("Total Elapsed Time : ", elapsed_time)
        
        if len(start_edge_people) != 0:
            returner_name, returner = get_min_pass_time(end_edge_people)
            end_edge_people.pop(returner_name)
            start_edge_people[returner_name] = returner
            
            returner_time = returner.pass_time
            elapsed_time = elapsed_time + returner_time
            
            visualize_bridge(start_edge_people, end_edge_people)
            print("Total Elapsed Time : ", elapsed_time)
        
        
    
    
    
    