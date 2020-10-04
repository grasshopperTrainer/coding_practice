package »ó¼ö_2908;

import java.io.*;
import java.util.Scanner;


public class Main {

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		
		String a = new StringBuffer(sc.next()).reverse().toString();
		String b = new StringBuffer(sc.next()).reverse().toString();
		sc.close();
		
		if ((Integer.parseInt(a)) < (Integer.parseInt(b))) {
			System.out.print(b);
		} else {
			System.out.print(a);
		}
	}
}