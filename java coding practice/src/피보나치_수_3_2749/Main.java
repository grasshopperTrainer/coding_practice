package 피보나치_수_3_2749;

import java.io.*;

public class Main {
	static int DIVIDER = 1_000_000;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		long N = Long.parseLong(br.readLine());
		int[][] matrix = new int[][] { { 1, 1 }, { 1, 0 } };	
		if (N == 1 || N == 2) {
			System.out.print(1);
		} else {
			int[][] m = calc(matrix, N-2);
			int r = multMatrix(m, new int[][] {{1}, {1}})[0][0];
			System.out.print(r);			
		}
	}
	
	static int[][] calc(int[][] M, long B) {
		if (B == 1) {
			return M;
		}
		int[][] tempM = calc(M, B / 2);
		tempM = multMatrix(tempM, tempM);
		if (B % 2 == 1) {
			return multMatrix(tempM, M);
		} else {
			return tempM;
		}
	}

	static int[][] multMatrix(int[][] M1, int[][] M2) {
		int A = M1.length;
		int B = M1[0].length;
		int D = M2[0].length;
		
		int[][] result = new int[A][D];
		for (int a = 0; a < A; a++) {
			for (int d = 0; d < D; d++) {
				long val = 0;
				for (int b = 0; b < B; b++) {
					val += (long)M1[a][b] * M2[b][d];
				}
				result[a][d] = (int)(val%DIVIDER);
			}
		}
		return result;
	}
}
