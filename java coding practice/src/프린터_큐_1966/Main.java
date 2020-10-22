package 프린터_큐_1966;

import java.io.*;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(br.readLine());
		for (int i = 0; i < T; i++) {
			LinkedList<Integer> deque = new LinkedList<Integer>();
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			// form ranks and count for each rank
			LinkedList<int[]> ranks = new LinkedList<int[]>();
			HashMap<Integer, Integer> rankMap = new HashMap<Integer, Integer>();
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				int rank = Integer.parseInt(st.nextToken());
				ranks.add(new int[] {rank, j});
				rankMap.put(rank, rankMap.getOrDefault(rank, 0) + 1);
			}
			// sort rank counts to use when checking to print 
			LinkedList<int[]> rankCounts = new LinkedList<int[]>();
			for (int k : rankMap.keySet()) {
				rankCounts.add(new int[] { k, rankMap.get(k) });
			}
			rankCounts.sort(Comparator.comparing(n -> -n[0]));
			
			int printCount = 0;
			while (true) {
				if (ranks.peekFirst()[0] == rankCounts.peekFirst()[0]) {
					printCount++;
					if (--rankCounts.peekFirst()[1] == 0) {
						rankCounts.pollFirst();
					}
					if (ranks.pollFirst()[1] == M) {
						bw.write(Integer.toString(printCount));
						bw.newLine();
						break;
					}
				} else {
					ranks.addLast(ranks.pollFirst());
				}
			}
		}
		bw.close();
	}
}