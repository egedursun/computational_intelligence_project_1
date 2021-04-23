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

public class Mutation {

	//This method applies or not applies a mutation to the population depending on the probability
	//parameter given as mutationChance.
	public static ArrayList<Individual> mutatePopulation(ArrayList<Individual> children, int mutationChance){
		
		String alphabet = "ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZabcçdefgğhıijklmnoöpqrsştuüvwxyz0123456789_*!+%&/=;,.: ";
		Random r = new Random();
		int chromoLength = children.get(0).getChromosomeLength();
		
		for (int i=0; i<children.size(); i++) {
			
			int mute_die = r.nextInt(100)+1;
			
			if(mute_die < mutationChance) {
				
				int randGeneIndex = r.nextInt(chromoLength);
				String newGene = Character.toString(alphabet.charAt(r.nextInt(alphabet.length())));
				String currentChromosome = children.get(i).getChromosome();
				currentChromosome = currentChromosome.substring(0, randGeneIndex) + newGene + currentChromosome.substring(randGeneIndex+1);
				children.get(i).setChromosome(currentChromosome);
			}
		}
		
		return children;
	}
}
