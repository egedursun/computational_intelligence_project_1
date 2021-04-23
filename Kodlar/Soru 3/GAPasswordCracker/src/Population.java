/*
 * EGE DOĞAN DURSUN - 05170000006
 * CEM ÇORBACIOĞLU - 05130000242
 * EGE ÜNİVERSİTESİ
 * MÜHENDİSLİK FAKÜLTESİ
 * BİLGİSAYAR MÜHENDİSLİĞİ BÖLÜMÜ
 * 2019-2020 BAHAR DÖNEMİ
 * İŞLEMSEL ZEKA VE DERİN ÖĞRENME DERSİ - CIDL2020-P1
 * SORU 3 - GENETİK ALGORİTMAYLA ŞİFRE ÇÖZME
 * TARİH : 12 NİSAN 2020
 * 
 */

import java.util.ArrayList;

public class Population {

	//This method creates a population with the selected properties such as populationSize and chromosomeLength
	public static ArrayList<Individual> createPopulation(int populationSize, int chromosomeLength) {
		
		ArrayList<Individual> population = new ArrayList();
		for (int i = 0; i<populationSize; i++) {
			
			Individual newIndividual = new Individual(chromosomeLength);
			population.add(newIndividual);
		}
		
		return population;
	}
	
	//This method shows the chromosome ingredients of each member in a population
	public static void listPopulationChromosomes(ArrayList<Individual> population) {
		
		System.out.println();
		System.out.println("=========================");
		System.out.println("CHROMOSOME INFORMATION OF THE POPULATION: ");
		for(int i =0; i<population.size(); i++) {
			
			System.out.println("Individual Number [" + i +"] => "+ population.get(i).getChromosome());
		}
		System.out.println();
	}
}
