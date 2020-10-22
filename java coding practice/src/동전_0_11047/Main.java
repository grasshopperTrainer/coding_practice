package µ¿Àü_0_11047;

import java.io.*;
import java.util.StringTokenizer;


public class Main {
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		int[] coins = new int[N];
		for (int i=N-1; 0<=i; i--) {
			coins[i] = Integer.parseInt(br.readLine());
		}
		
		int count = 0;
		for (int i=0; i<N; i++) {
			if (K == 0) {
				break;
			}
			if (coins[i] <= K) {
				count += K/coins[i];
				K = K%coins[i];
			}
		}
		System.out.print(count);
	}
}
