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

class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness= 0.0
    
    #Method to calculate the distance for the route
    def route_distance(self):
        if self.distance ==0:
            path_distance = 0
            for i in range(0, len(self.route)):
                from_city = self.route[i]
                to_city = None
                
                if i + 1 < len(self.route):
                    to_city = self.route[i + 1]
                else:
                    to_city = self.route[0]
                    
                path_distance = path_distance + from_city.distance(to_city)
            self.distance = path_distance
        return self.distance
    
    #Method to calculate the route fitness depending on the route distance
    def route_fitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.route_distance())
        return self.fitness
    
    