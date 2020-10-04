package 숫자의_합_11720;

import java.io.*;
import java.util.Scanner;


public class Main {

	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int summed = 0;
		for (String s: sc.next().split("")) {
			summed += Integer.parseInt(s);
		}
		System.out.print(summed);
	}
}