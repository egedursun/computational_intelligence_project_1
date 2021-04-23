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
import java.util.Date;
import java.util.Timer;

public class Test {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		//Determine the password to get cracked
		String target = "İşlemselZeka_DL_20";
		
		//String target = "Benim adım Ege Doğan Dursun. Daha uzun bir parolanın ne kadar sürede kırıldığını inceleyelim.";
		//String target = "Asker 98234 Silah Kek 10493 Yemek Çatal Kaşık Bıçak 9e32984 Kedi Köpek Muz 394823984 Kulaklık Teknoloji 888238 ____ Bilgisayar Klavye Mouse Dergi _3894__2839 Gazete Virüs Karantina 2020 1094 ___ 2392983982 12983 _ 32984983289 Teknik Detay Fakir ___ 9329893248 ;;;::: Yoksul Zengin Otomobil";
		
		int targetChromosomeLength = target.length();
		System.out.println("Size of the target password: " + targetChromosomeLength);
		
		//The problem will be solved 10 times.
		int solutionTimes = 10;
		
		//Determine the hyper-parameters that the genetic algorithm will use.
		int populationSize = 100; //optimal: 100 individuals
		int epochAmount = 2500; //optimal : 15000 generations
		int mutationChance = 25; //optimal : 5% chance of mutation
		int crossoverChance = 90; //optimal : 90% chance of crossing-over
		int maxParents = populationSize/2; //optimal : 50% of the population selected as parents
		int graphTurns = epochAmount/(100); //optimal: 100 graph lines 
		
		ArrayList<Double> averageFitnesses = new ArrayList<Double>();
		ArrayList<Integer> fullFitAmounts = new ArrayList<Integer>();
		ArrayList<Double> times = new ArrayList<Double>();
		
		//Generate an initial population.
		ArrayList<Individual> population = Population.createPopulation(populationSize, targetChromosomeLength);
		ArrayList<Individual> finalPopulation = population;
		
		Timer timer = new Timer();
		
		//Solve the question in n number of times.
		for (int i = 0; i<solutionTimes; i++) {
			
			double startTime = System.currentTimeMillis();
			
			//Evolve the population by using the hyper-paremeters.
			finalPopulation = Evolution.evolvePopulation(target, population, epochAmount, maxParents, crossoverChance, 
																					mutationChance, graphTurns);
			
			double elapsedTime = (new Date()).getTime() - startTime;
			times.add(elapsedTime);
			double avgFitness = Fitness.showAverageFitness(finalPopulation);
			System.out.println(finalPopulation.get(0).getFitness());
			int fullFitAmount = Fitness.calculateCorrectMatches(finalPopulation, target);
			averageFitnesses.add(avgFitness);
			fullFitAmounts.add(fullFitAmount);
		}
		
		//List the chromosome data of the final population.
		Population.listPopulationChromosomes(finalPopulation);
		
		//Print the solution data
		System.out.println("SOLUTION INFORMATION: ");
		System.out.println("_____________________");
		for(int i = 0; i<solutionTimes; i++) {
			System.out.println("Turn : " + (i+1));
			System.out.println("Total Epochs : " + epochAmount);
			System.out.println("(%) Final Average Fitness : %" + (int)(averageFitnesses.get(i)/targetChromosomeLength*100));
			System.out.println(" (%) of Population With Perfect Match to The Password : %" + (int)((double)fullFitAmounts.get(i)/populationSize*100));
			System.out.println("Time for completing the turn: " + times.get(i) + " milliseconds.");
			System.out.println("Example Solution from the Population : " + finalPopulation.get(0).getChromosome());
			System.out.println("____________________");
		}
	}
	

}
