package ≈Î∞Ë«–_2108;

import java.io.*;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int[] numCounts = new int[8001];
		int num;
		
		double ave = 0;
		int center = 0;
		int common = 0;
		int range = 0;
		int min = 4000;
		int max = -4000;
		
		for (int i=0; i<N; i++) {
			num = Integer.parseInt(br.readLine());
			numCounts[num+4000]++;
			ave += num;
			if (num < min) {
				min = num;
			}
			if (max < num) {
				max = num;
			}
		}
		
		ave = ave/N;
		
		int half = N/2;
		int numNum = 0;
		
		int commonCount = 0;
		int commonResetCount = 0;
		for (int i=0; i<8001; i++) {
			// find center
			if (numNum <= half & half < (numNum += numCounts[i])) {
				center = i-4000;
			}
			
			if (numCounts[i] > commonCount) {
				common = i-4000;
				commonCount = numCounts[i];
				commonResetCount = 1;
			} else if (numCounts[i] == commonCount) {
				if (commonResetCount == 1) {
					commonResetCount++;
					common = i-4000;
				}
			}
		}
		
		range = max-min;
		
		System.out.println(Math.round(ave));
		System.out.println(center);
		System.out.println(common);
		System.out.println(range);
	}
}