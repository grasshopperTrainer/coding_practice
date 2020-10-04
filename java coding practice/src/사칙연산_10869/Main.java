package 사칙연산_10869;

import java.io.*;
import java.util.StringTokenizer;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int a = Integer.parseInt(st.nextToken());
		int b = Integer.parseInt(st.nextToken());
		
		int[] results = new int[5];
		results[0] = a+b;
		results[1] = a-b;
		results[2] = a*b;
		results[3] = a/b;
		results[4] = a%b;
		
		for (int i: results) {
			System.out.println(i);
		}
	}

}
