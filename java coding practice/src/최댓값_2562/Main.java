package ÃÖ´ñ°ª_2562;

import java.io.*;
import java.util.StringTokenizer;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] maxVal = {Integer.MIN_VALUE, -1};
		for (int i=0; i<9; i++) {
			int n = Integer.parseInt(br.readLine());
			System.out.println(String.format("%d %d", n, i));
			if (maxVal[0] < n) {
				maxVal = new int[] {n, i+1};
			}
		}
		System.out.println(Integer.toString(maxVal[0]));
		System.out.println(Integer.toString(maxVal[1]));
	}
}