package 좌표_정렬하기_2_11651;

import java.io.*;
import java.util.StringTokenizer;
import java.util.Arrays;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		StringTokenizer st;
		int N = Integer.parseInt(br.readLine());
		
		int[][] coords = new int[N][2];
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			coords[i][0] = Integer.parseInt(st.nextToken());
			coords[i][1] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(coords, (i1, i2) -> {
			if (i1[1] == i2[1]) {
				return Integer.compare(i1[0], i2[0]);
			} else {
				return Integer.compare(i1[1], i2[1]);
			}
		});
		for (int i=0; i<N; i++) {
			bw.write(String.format("%d %d", coords[i][0], coords[i][1]));
			bw.newLine();
		}
		bw.flush();
		bw.close();
	}
}