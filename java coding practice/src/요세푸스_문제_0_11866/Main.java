package 요세푸스_문제_0_11866;

import java.io.*;
import java.util.LinkedList;
import java.util.StringTokenizer;
import java.util.stream.Collectors;


public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		LinkedList<Integer> que = new LinkedList<Integer>();
		for (int i=1; i<=N; i++) {
			que.add(i);
		}
		
		LinkedList<Integer> answer = new LinkedList<Integer>();
		while (!que.isEmpty()) {
			for (int i=0; i<K-1; i++) {
				que.addLast(que.poll());
			}
			answer.add(que.poll());
		}
		String strAnswer = answer.stream()
				.map(n -> Integer.toString(n))
				.collect(Collectors.joining(", "));
		System.out.print(String.format("<%s>", strAnswer));
	}
}