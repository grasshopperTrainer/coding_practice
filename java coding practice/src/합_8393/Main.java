package гу_8393;

import java.io.*;
import java.util.StringTokenizer;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		
		int summed = 0;
		for (int i=1; i<n+1; i++) {
			summed += i;
		}
		
		System.out.print(summed);
	}
}