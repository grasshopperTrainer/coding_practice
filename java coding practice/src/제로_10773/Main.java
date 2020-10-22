package Á¦·Î_10773;

import java.io.*;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		Stack<Integer> stack = new Stack<Integer>();
		int summed = 0;
		int N = Integer.parseInt(br.readLine());
		for (int i = 0; i < N; i++) {
			int num = Integer.parseInt(br.readLine());
			if (num == 0) {
				summed -= stack.pop();
			} else {
				stack.add(num);
				summed += num;
			}
		}
		System.out.print(summed);
	}
}
