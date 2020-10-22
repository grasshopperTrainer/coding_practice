package 스택_수열_1874;

import java.io.*;
import java.util.ArrayList;
import java.util.Stack;
import java.util.stream.Collectors;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		Stack<Integer> stack = new Stack<Integer>();
		stack.add(0);

		int N = Integer.parseInt(br.readLine());

		int nextNum = 1;
		boolean noSolution = false;
		ArrayList<String> signs = new ArrayList<String>();
		for (int i = 0; i < N; i++) {
			int targetNum = Integer.parseInt(br.readLine());
			while (stack.lastElement() < targetNum) {
				stack.add(nextNum++);
				signs.add("+");
			}
			while (stack.lastElement() > targetNum) {
				stack.pop();
				signs.add("-");
			}

			if (stack.lastElement() == targetNum) {
				stack.pop();
				signs.add("-");
			} else {
				noSolution = true;
				break;
			}

		}
		br.close();

		if (noSolution) {
			System.out.print("NO");
		} else {
			System.out.print(signs.stream().collect(Collectors.joining("\n")));
		}
	}
}