package Ä«µå2_2164;

import java.io.*;
import java.util.LinkedList;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());

		LinkedList<Integer> deque = new LinkedList<Integer>();
		for (int i=1; i<=N; i++) {
			deque.add(i);
		}
		while (true) {
			if (deque.size() == 1) {
				System.out.print(deque.peek());
				break;
			}
			deque.pop();
			deque.addLast(deque.pop());
		}
	}
}