package ЦђБе_1546;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		// parse and find max score
		double[] scores = new double[N];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i=0; i<N; i++) {
			scores[i] = Double.parseDouble(st.nextToken());
		}
		double maxScore = Arrays.stream(scores).max().getAsDouble();
		// calculate average score
		double aveScore = 0;
		for (int i=0; i<N; i++) {
			aveScore += (scores[i]/maxScore)*100;
		}
		aveScore /= scores.length;
		
		System.out.print(aveScore);
	}
}