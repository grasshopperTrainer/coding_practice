package ÇÑ¼ö_1065;

import java.io.*;
import java.util.Scanner;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		
		int sumCount = N > 9 ? 9 : N;	
		for (int start=1; start<10; start++) {
			for (int gap=-9; gap<=9; gap++) {
				sumCount += count(start, gap, N);				
			}
		}
		System.out.print(Integer.toString(sumCount));
	}
	
	static int count(int num, int gap, int limit) {
		int counter = 0;
		
		int temp = num;
		while (true) {
			int right = temp%10+gap;
			int left = temp*10;
			if (right < 0 || 9 < right || limit < (temp = left+right)) {
				break;
			} else {
				counter++;
			}
		}
		return counter;
	}
}