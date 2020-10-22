package Çà·Ä_Á¦°ö_10830;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main {
	static int DIVIDER = 1000;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		long B = Long.parseLong(st.nextToken());

		int[][] matrix = new int[N][N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				matrix[i][j] = Integer.parseInt(st.nextToken()) % DIVIDER;
			}
		}

		int[][] resultM = calc(matrix, B);
		for (int i = 0; i < N; i++) {
			String row = Arrays.stream(resultM[i])
					.mapToObj(Integer::toString)
					.collect(Collectors.joining(" "));
			System.out.println(row);
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

	static int[][] multMatrix(int[][] A, int[][] B) {
		int N = A.length;
		int[][] result = new int[N][N];
		for (int a = 0; a < N; a++) {
			for (int d = 0; d < N; d++) {
				long val = 0;
				for (int b = 0; b < N; b++) {
					val += A[a][b] * B[b][d];
				}
				result[a][d] = (int)(val%DIVIDER);
			}
		}
		return result;
	}
}

