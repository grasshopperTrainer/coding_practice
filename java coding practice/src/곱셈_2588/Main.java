package °ö¼À_2588;

import java.io.*;
import java.util.StringTokenizer;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int a = Integer.parseInt(br.readLine());
		int b = Integer.parseInt(br.readLine());
		
//		System.out.println(a);
//		System.out.println(b);
		
		int[] results = new int[4];
		results[0] = a*(b%10);
		results[1] = a*((b/10)%10);
		results[2] = a*(b/100);
		results[3] = a*b;
		
		for(int i: results) {
			System.out.println(i);
		}
	}

}
