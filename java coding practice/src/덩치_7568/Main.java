package µ¢Ä¡_7568;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.Collectors;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		// prepare input
		int[][] people = new int[T][2];
		for (int i=0; i<T; i++) {
			st = new StringTokenizer(br.readLine());
			people[i][0] = Integer.parseInt(st.nextToken());
			people[i][1] = Integer.parseInt(st.nextToken());
		}
		// count
		int[] rank = new int[T];
		for (int i=0; i<T; i++) {
			for (int j=0; j<T; j++) {
				if (i == j) continue;
				if (people[i][0] < people[j][0] && people[i][1] < people[j][1]) {
					rank[i]++;
				}
			}
		}
		String answer = Arrays.stream(rank)
				.map(n -> ++n)
				.mapToObj(Integer::toString)
				.collect(Collectors.joining(" "));
		System.out.print(answer);
	}
}