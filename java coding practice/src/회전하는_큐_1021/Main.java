package 회전하는_큐_1021;

import java.io.*;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		int[] targets = new int[M];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < M; i++) {
			targets[i] = Integer.parseInt(st.nextToken());
		}

		LinkedList<Integer> deque = new LinkedList<Integer>();
		for (int i = 1; i <= N; i++) {
			deque.add(i);
		}

		int totalCount = 0;
		for (int target : targets) {
			int forwardCount = 0;
			int backwardCount = 0;
			while (true) {
				if (deque.get(forwardCount) == target) {
					backwardCount = deque.size()-forwardCount;
					break;
				} else {
					forwardCount++;
				}
			}
			
			if (forwardCount <= backwardCount) {
				totalCount += forwardCount;
				for (int i=0; i<forwardCount; i++) {
					deque.addLast(deque.pollFirst());
				}
			} else {
				totalCount += backwardCount;
				for (int i=0; i<backwardCount; i++) {
					deque.addFirst(deque.pollLast());
				}
			}
			deque.pollFirst();
		}
		
		System.out.print(totalCount);
	}
}