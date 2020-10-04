package ³ª¸ÓÁö_10430;

import java.io.*;
import java.util.StringTokenizer;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int a = Integer.parseInt(st.nextToken());
		int b = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());
		
		int[] results = new int[4];
		results[0] = (a+b)%c;
		results[1] = ((a%c) + (b%c))%c;
		results[2] = (a*b)%c;
		results[3] = ((a%c) * (b%c))%c;
		
		for (int i: results) {
			System.out.println(i);
		}
	}

}
