package µ¦_10866;

import java.io.*;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;

		int N = Integer.parseInt(br.readLine());

		LinkedList<Integer> deque = new LinkedList<Integer>();
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			String inst = st.nextToken();
			if (inst.equals("push_front")) {
				deque.addFirst(Integer.parseInt(st.nextToken()));
			} else if (inst.equals("push_back")) {
				deque.addLast(Integer.parseInt(st.nextToken()));
			} else {
				if ("size empty".contains(inst)) {
					if (inst.equals("size")) {
						bw.write(Integer.toString(deque.size()));
					} else if (inst.equals("empty")) {
						bw.write(deque.isEmpty() ? "1" : "0");
					}
				} else {
					if (deque.isEmpty()) {
						bw.write("-1");
					} else {
						if (inst.equals("pop_front")) {
							bw.write(Integer.toString(deque.pollFirst()));
						} else if (inst.equals("pop_back")) {
							bw.write(Integer.toString(deque.pollLast()));
						} else if (inst.equals("front")) {
							bw.write(Integer.toString(deque.peekFirst()));
						} else if (inst.equals("back")) {
							bw.write(Integer.toString(deque.peekLast()));
						}
					}
				}
				bw.newLine();
			}
		}

		bw.close();
	}
}