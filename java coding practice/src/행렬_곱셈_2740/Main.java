package Çà·Ä_°ö¼À_2740;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		ArrayList<int[][]> matrices = new ArrayList<int[][]>();
		for (int t=0; t<2; t++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			int[][] matrix = new int[N][M];
			for (int i=0; i<N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j=0; j<M; j++) {
					matrix[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			matrices.add(matrix);
		}
		int A = matrices.get(0).length;
		int B = matrices.get(0)[0].length;
		int D = matrices.get(1)[0].length;
		int[][] resultM = new int[A][D];
		for (int a=0; a<A; a++) {
			for (int d=0; d<D; d++) {
				for (int b=0; b<B; b++) {
					resultM[a][d] += matrices.get(0)[a][b]*matrices.get(1)[b][d];						
				}
			}
		}
		
		for (int i=0; i<A; i++) {
			int[] row = resultM[i];
			System.out.println(Arrays.stream(row)
					.mapToObj(Integer::toString)
					.collect(Collectors.joining(" ")));
		}
	}
}