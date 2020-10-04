package 최소_최대_10818;

import java.io.*;
import java.util.StringTokenizer;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int minVal = Integer.MAX_VALUE;
		int maxVal = Integer.MIN_VALUE;
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i=0; i<N; i++) {
			int n = Integer.parseInt(st.nextToken());
			minVal = Integer.min(minVal, n);
			maxVal = Integer.max(maxVal, n);
		}
		System.out.print(String.format("%d %d", minVal, maxVal));
	}
}