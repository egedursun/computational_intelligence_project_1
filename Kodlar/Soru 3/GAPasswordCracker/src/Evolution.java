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
import java.util.Random;

import javafx.scene.chart.XYChart;

public class Evolution {

	
	//Class and function that handles the evolution of the population. 
	public static ArrayList<Individual> evolvePopulation(String target, ArrayList<Individual> population, int epochAmount, int maxParents, 
														int crossoverChance, int mutationChance, int eachTurn) {
		
		int populationSize = population.size();
		int chromoLength = population.get(0).getChromosomeLength();
		Random r = new Random();
		ArrayList<Double> averageFitnessHistory = new ArrayList();
		ArrayList<Double> fullFitHistory = new ArrayList();
		
		for(int i = 0; i<epochAmount; i++) {
			
			System.out.println("==============================");
			System.out.println("EPOCH NO: "+ (i+1));
			population = Fitness.evaluateFitness(population, target);
			
			double epochAverage = Fitness.showAverageFitness(population);
			System.out.println("Average Fitness of Population : (" +epochAverage+ " out of "+chromoLength+") . Fitness Percentage : %"+((int)(epochAverage/chromoLength*100)));
			averageFitnessHistory.add(epochAverage);
			
			//todo : calculate correct matches.
			int correctMatches = Fitness.calculateCorrectMatches(population, target);
			System.out.println("Number of total matches in the Population : (" + correctMatches + " out of "+populationSize+ ") . Ratio : %"+(int)((double)correctMatches/populationSize*100));
			fullFitHistory.add((double)correctMatches);
			
			ArrayList<Individual> parents = MatingPool.selectParentsByFitness(population, epochAverage, maxParents);
			System.out.println("Number of parents selected for mating : (" + parents.size() + " out of " + populationSize + ") .");
			
			ArrayList<Individual> children = MatingPool.produceOffspringsByCrossover(parents, populationSize, crossoverChance);
			System.out.println("Number of children produced : " + children.size());
			
			children = Mutation.mutatePopulation(children, mutationChance);
			
			population = children;
			
			Individual exampleChild = population.get(r.nextInt(population.size()));
			System.out.println("A Random Indiviudal Chromosome from Popoulation : ");
			System.out.println(exampleChild.getChromosome());
			
			System.out.println("===============================");
			System.out.println();
			
		}
		
		population = Fitness.evaluateFitness(population, target);
		
		showPopulationData(averageFitnessHistory, epochAmount, chromoLength, eachTurn);
		showFullFitPopulationData(fullFitHistory, epochAmount, populationSize, eachTurn);
		
		showVariationalPopulationGraph(averageFitnessHistory, epochAmount, chromoLength);
		showVariationalFullFitGraph(fullFitHistory, epochAmount, populationSize);
		
		return population;
		
	}
	
	
	//This method shows a basic graphical representation of the evolution history of the full fit population on the console.
	//Full fit population members are the members who are perfectly fit with the target string among the population
	public static void showFullFitPopulationData(ArrayList<Double> history, int epochAmount, int populationSize, int eachTurn) {
		
		double[] yData = new double[history.size()];
		double[] xData = new double[epochAmount];
		
		for (int i = 0; i<history.size(); i++) {
			yData[i] = history.get(i);
		}
		
		for(int j = 0; j<epochAmount; j++) {
			
			xData[j] = j;
		}
		
		System.out.println();
		System.out.println("================================");
		System.out.println("GENERATING FULLY MATCHING INDIVIDUALS' EVOLUTION GRAPH FOR THE POPULATION: ");
		System.out.println();
		
		for (int k =0; k<xData.length; k++) {
			
			if(k%eachTurn == 0) {
				
				int height = (int)(yData[k]/populationSize*100);
				
				System.out.print("["+ k +"] => ");
				for(int l =0; l<height; l++) {
					System.out.print("*");
				}
				for(int m =0; m<(100-height); m++) {
					System.out.print("-");
				}
				System.out.println();
			}
		}
	}
	
	
	//This method shows a variational graphical representation of the full fit members in the population.
	//The difference with the evolution graph is basically this graph only consists of steps in which
	//there has been a positive genetic drift amoung the population.
	public static void showVariationalFullFitGraph(ArrayList<Double> history, int epochAmount, int populationSize) {
		
		double[] yData = new double[history.size()];
		double[] xData = new double[epochAmount];
		
		for(int i = 0; i<history.size(); i++) {
			yData[i] = history.get(i);
		}
		
		for(int j= 0; j<epochAmount; j++) {
			xData[j] = j;
		}
		
		System.out.println();
		System.out.println("================================");
		System.out.println("GENERATING FULLY MATCHING INDIVIDUALS' VARIATIONAL GRAPH FOR THE POPULATION: :");
		System.out.println();
		
		double maxHeight = 0;
		for(int k=0; k<xData.length; k++) {
			
			int height = (int)(yData[k]/populationSize*100);
			
			if(height > maxHeight) {
				
				maxHeight = height; 
				System.out.print("["+ k +"] => ");
				for(int l =0; l<height; l++) {
					System.out.print("*");
				}
				for(int m =0; m<(100-height); m++) {
					System.out.print("-");
				}
				System.out.println();
				
			}
		}	
	}
	
	//This graph shows a basic graphical representation of the population and their average fitness levels on the console.
	public static void showPopulationData(ArrayList<Double> history, int epochAmount, int chromoLength, int eachTurn) {
		
		double[] yData = new double[history.size()];
		double[] xData = new double[epochAmount];
		
		for(int i = 0; i<history.size(); i++) {
			yData[i] = history.get(i);
		}
		
		for(int j= 0; j<epochAmount; j++) {
			xData[j] = j;
		}
		
		System.out.println();
		System.out.println("================================");
		System.out.println("GENERATING EVOLUTIONARY GRAPH FOR THE POPULATION: ");
		System.out.println();
		
		for(int k=0; k<xData.length; k++) {
			
			if(k%eachTurn == 0) {
				
				double currentFitness = yData[k];
				
				int height = (int)(currentFitness/chromoLength*100);
				
				System.out.print("["+ k +"] => ");
				for(int l =0; l<height; l++) {
					System.out.print("*");
				}
				for(int m =0; m<(100-height); m++) {
					System.out.print("-");
				}
				System.out.println();
			}
		}
	}
	
	
	//This graph shows the population and fitness too but variational graph consists only of steps which
	//there has been a positive genetic drift among the population
	public static void showVariationalPopulationGraph(ArrayList<Double> history, int epochAmount, int chromoLength) {
		
		double[] yData = new double[history.size()];
		double[] xData = new double[epochAmount];
		
		for(int i = 0; i<history.size(); i++) {
			yData[i] = history.get(i);
		}
		
		for(int j= 0; j<epochAmount; j++) {
			xData[j] = j;
		}
		
		System.out.println();
		System.out.println("================================");
		System.out.println("GENERATING VARIATIONAL GRAPH FOR THE POPULATION :");
		System.out.println();
		
		double maxHeight = 0;
		for(int k=0; k<xData.length; k++) {
				
			double currentFitness = yData[k];
			
			int height = (int)(currentFitness/chromoLength*100);
			
			if(height > maxHeight) {
				
				maxHeight = height;
				System.out.print("["+ k +"] => ");
				for(int l =0; l<height; l++) {
					System.out.print("*");
				}
				for(int m =0; m<(100-height); m++) {
					System.out.print("-");
				}
				System.out.println();
				
			}	
		}	
	}
}
