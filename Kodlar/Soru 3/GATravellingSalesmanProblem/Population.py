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
from City import City

def create_cities(city_amount, max_distance_xy):
    city_list = []
    for i in range(0,city_amount):
        city_list.append(City(x=int(random.random() * max_distance_xy), y=int(random.random() * max_distance_xy)))
    return city_list

#This method is used to create routes between cities.
def create_route(city_list):
    route = random.sample(city_list, len(city_list))
    return route


#This method is used for creating an initial solution population
def initial_population(pop_size, city_list):
    population = []

    for i in range(0, pop_size):
        population.append(create_route(city_list))
    return population