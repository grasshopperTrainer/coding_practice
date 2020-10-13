package 단어_정렬_1181;

import java.io.*;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashSet;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		ArrayList<String> words = new ArrayList<String>();
		for (int i=0; i<N; i++) {
			words.add(br.readLine().trim());
		}
		words.sort(Comparator.comparing(String::length).thenComparing(String::compareTo));
		
		HashSet<String> newWords = new HashSet<String>();
		for (String word: words) {
			if (!newWords.contains(word)) {
				newWords.add(word);
				bw.write(word);
				bw.newLine();
			}
		}
		
		bw.flush();
		br.close();
		bw.close();
	}
}