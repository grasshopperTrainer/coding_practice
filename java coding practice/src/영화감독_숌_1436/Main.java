package ¿µÈ­°¨µ¶_¼ò_1436;

import java.io.*;
import java.util.Scanner;


public class Main {

	public static void main(String[] args) throws IOException{
		
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		sc.close();
		
		int counter = 0;
		int num = 666;
		while (true) {
			int tempNum = num;
			boolean numFound = false;
			while (666 <= tempNum) {
				if (tempNum%1000 == 666) {
					numFound = true;
					break;
				} else {
					tempNum /= 10;
				}
			}
			if (numFound && ++counter == N) {
				break;
			}
			num++;
		}

		System.out.print(num);
	}
}