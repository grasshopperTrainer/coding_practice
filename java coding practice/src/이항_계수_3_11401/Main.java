package 이항_계수_3_11401;

import java.io.*;
import java.util.StringTokenizer;

public class Main {
	static int DIVIDER = 1_000_000_007;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int[][] dp = new int[N+1][K+1];
		
		System.out.print(calc(N, K, dp));
	}
	
	static int calc(int n, int k, int[][] dp) {
		if (dp[n][k] != 0) {
			return dp[n][k];
		}
		if (n == k) {
			return 1;
		}
		if (k == 0) {
			return 1;
		}
		int v = (calc(n-1, k-1, dp)+calc(n-1, k, dp))%DIVIDER;
		dp[n][k] = v; 
		return v;
	}
}