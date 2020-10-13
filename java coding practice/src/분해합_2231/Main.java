package ºÐÇØÇÕ_2231;

import java.io.*;
import java.util.Scanner;


public class Main {

	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		
		int N = Integer.parseInt(sc.next());
		sc.close();
		
		for (int i=0; i<=N; i++) {
			if (calc(i) == N) {
				System.out.println(i);
				break;
			} else if (i == N) {
				System.out.println(0);
			}
		}
	}
	
	static int calc(int n) {
		int temp = n;
		int remainder = n;
		while (remainder != 0) {
			temp += remainder%10;
			remainder /= 10;
		}
		return temp;
	}
}