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

public class Fitness {

	
	//This function evaluates the fitness level of the population. Max possible fitness level is
	//the maximum character amount of the target string.
	public static ArrayList<Individual> evaluateFitness(ArrayList<Individual> population, String target) {
		
		for (int i = 0; i<population.size(); i++) {
			
			int fitness = 0;
			Individual curIndividual = population.get(i);
			for (int j = 0; j<curIndividual.getChromosomeLength(); j++) {
				if (target.charAt(j) == curIndividual.getChromosome().charAt(j)) {
					fitness = fitness + 1;
				}
			}
			curIndividual.setFitness(fitness);
		}
		return population;
	}
	
	//This function shows the average fitness level of a population based on averaging 
	//how many characters are matching with the target string.
	public static double showAverageFitness(ArrayList<Individual> population) {
		
		double summation = 0;
		for (int i = 0; i<population.size(); i++) {
			summation = summation + population.get(i).getFitness();
		}
		double average = summation/population.size();
		
		return average;
	}
	
	
	//This function returns exactly how many members of the population provides a perfect
	//100% match with the target string to provide insight.
	public static int calculateCorrectMatches(ArrayList<Individual> population, String target) {
		
		int total = 0;
		for(int i = 0; i<population.size(); i++) {
			if(population.get(i).getChromosome().equals(target)) {
				total = total + 1;
			}
		}
		
		return total;
	}
}
