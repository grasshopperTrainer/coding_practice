package ATM_11399;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int[] times = new int[N];
		for (int i=0; i<N; i++) {
			times[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(times);
		int total = 0;
		for (int i=0; i<N; i++) {
			total += times[i]*(N-i);
		}
		System.out.print(total);
	}
}
