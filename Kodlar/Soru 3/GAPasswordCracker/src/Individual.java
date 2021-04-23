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

import java.util.Random;

public class Individual {

	private static int chromosomeLength;
	private String chromosome;
	private int fitness;
	
	public Individual(int chromosomeLength) {
		
		this.chromosomeLength = chromosomeLength;
		this.chromosome = randomizeChromosome();
		this.fitness = 0;
	}
	
	//This method creates a randomized chromosome for the instantiated individual at creation.
	public static String randomizeChromosome() {
		
		String chromosome = "";
		String alphabet = "ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZabcçdefgğhıijklmnoöpqrsştuüvwxyz0123456789_*!+%&/=;,.: ";
		Random r = new Random();
		for (int i = 0; i<chromosomeLength; i++) {
			String cur_char = Character.toString(alphabet.charAt(r.nextInt(alphabet.length())));
			chromosome = chromosome + cur_char;
		}
		
		return chromosome;
	}

	public static int getChromosomeLength() {
		return chromosomeLength;
	}

	public static void setChromosomeLength(int chromosomeLength) {
		Individual.chromosomeLength = chromosomeLength;
	}

	public String getChromosome() {
		return this.chromosome;
	}

	public void setChromosome(String chromosome) {
		this.chromosome = chromosome;
	}
	
	public int getFitness() {
		return this.fitness;
	}
	
	public void setFitness(int fitness) {
		this.fitness = fitness;
	}
}
