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

public class MatingPool {

	//This method selects parents from the population depending on their fitness level.
	//Basically only parents who have either the average or more than the average fitness level of the generation
	//are selected. There is also a limit on the parents that will be selected. 
	public static ArrayList<Individual> selectParentsByFitness(ArrayList<Individual> population, 
																double averageFitness, 
																int maximumParents) {
		
		ArrayList<Individual> parents = new ArrayList();
		for (int i = 0; i<population.size(); i++) {
			if(population.get(i).getFitness() >= averageFitness){
				if(parents.size() < maximumParents) {
					parents.add(population.get(i));
				}
			}
		}
		
		return parents;
	}
	
	
	//This method creates a children by randomly selected individuals from "available parent pool". Then
	//it applies a crossing over or not depending on the crossover chance.
	public static ArrayList<Individual> produceOffspringsByCrossover(ArrayList<Individual> parents, 
																	int populationSize, 
																	int crossoverChance){
		
		ArrayList<Individual> children = new ArrayList();
		Random r = new Random();
		int chromoLength = parents.get(0).getChromosomeLength();
		
		for(int i = 0; i<populationSize; i++) {
			
			int coDie = r.nextInt(100)+1;
			String parent1 = parents.get(r.nextInt(parents.size())).getChromosome();
			String parent2 = parents.get(r.nextInt(parents.size())).getChromosome();
			String childChromosome;
			
			if (coDie < crossoverChance){
				
				int coIndex = r.nextInt(chromoLength);
				String chromoPiece1 = parent1.substring(0, coIndex);
				String chromoPiece2 = parent2.substring(coIndex);
				
				childChromosome = chromoPiece1 + chromoPiece2;
			
			}
			else {
				
				int fomDie = r.nextInt(2);
				if(fomDie == 0) {
					
					childChromosome = parent1;
				}
				else {
					childChromosome = parent2;
				}
			}
			
			Individual child = new Individual(chromoLength);
			child.setChromosome(childChromosome);
			children.add(child);
			
		}
		
		return children;
		
	}
}
