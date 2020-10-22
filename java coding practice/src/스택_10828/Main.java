package Ω∫≈√_10828;

import java.io.*;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		Stack<Integer> stack = new Stack<Integer>();
		int N = Integer.parseInt(br.readLine());
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			String command = st.nextToken();
			if (command.equals("push")) {
				stack.push(Integer.parseInt(st.nextToken()));
			} else {
				if (command.equals("top")) {
					bw.write(stack.empty() ? "-1" : Integer.toString(stack.lastElement()));
				} else if (command.equals("size")) {
					bw.write(Integer.toString(stack.size()));
				} else if (command.equals("empty")) {
					bw.write(stack.empty() ? "1" : "0");
				} else if (command.equals("pop")) {
					bw.write(stack.empty() ? "-1" : Integer.toString(stack.pop()));
				}
				bw.newLine();
			}
		}

		bw.flush();
		bw.close();
	}
}
