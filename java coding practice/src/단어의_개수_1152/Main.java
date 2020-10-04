package 단어의_개수_1152;

import java.io.*;
import java.util.Scanner;


public class Main {

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		
		int count = 0;
		while (sc.hasNext()) {
			sc.next();
			count++;
		}
		sc.close();
		System.out.print(count);
	}
}