package 체스판_다시_칠하기_1018;

import java.io.*;
import java.util.StringTokenizer;


public class Main {

	public static void main(String[] args) throws IOException{		
		int size = 8;
		char[] signs = new char[] {'B', 'W'};
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		char[][] board = new char[N][M];
		for (int n=0; n<N; n++) {
			board[n] = br.readLine().toCharArray();
		}
		
		int minCount = 2500;
		for (int n=0; n<N-size+1; n++) {
			for (int m=0; m<M-size+1; m++) {
				for (int k=0; k<2; k++) {
					
					char prevSign = signs[k];
					int tempCount = 0;
					for (int i=n; i<n+size; i++) {
						for (int j=m; j<m+size; j++) {
							if (j==m) {
								if (prevSign != board[i][j]) {
									tempCount++;									
								}
							} else {
								if (board[i][j] == prevSign) {
									tempCount++;									
								}
								prevSign = prevSign == signs[0] ? signs[1] : signs[0];
							}
						}
					}
					
					if (tempCount < minCount) {
						minCount = tempCount;
					}
				}
			}
		}
		
		System.out.print(minCount);
	}
}