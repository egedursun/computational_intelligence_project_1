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

#Defining the person object for the project
class Person():
    
    def __init__(self, pass_time):
        self.pass_time = pass_time