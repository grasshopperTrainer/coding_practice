package ¾ËÆÄºª_Ã£±â_10809;

import java.io.*;
import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.Collectors;



public class Main {

	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		
		String str = sc.next();
		sc.close();
		
		int[] alphas = new int[26];
		Arrays.fill(alphas, -1);
		for (int i=0; i<str.length(); i++) {
			int idx = (int)str.charAt(i) - (int)'a';
			if (alphas[idx] == -1) {
				alphas[idx] = i;
			}
		}
		String answer = Arrays.stream(alphas)
				.mapToObj(Integer::toString)
				.collect(Collectors.joining(" "));
		System.out.print(answer);
	}
}