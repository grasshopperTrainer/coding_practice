package ±ÕÇüÀâÈù_¼¼»ó_4949;

import java.io.*;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		String line;
		while (!(line = br.readLine()).equals(".")) {
			Stack<Character> stack = new Stack<Character>();
			boolean badBracket = false;
			for (char c : line.toCharArray()) {
				if ("()[]".contains(Character.toString(c))) {
					if ("([".contains(Character.toString(c))) {
						stack.add(c);
					} else if (c == ')' && !stack.empty() && stack.lastElement() == '(') {
						stack.pop();
					} else if (c == ']' && !stack.empty() && stack.lastElement() == '[') {
						stack.pop();
					} else {
						bw.write("no");
						bw.newLine();
						badBracket = true;
						break;
					}
				}
			}
			if (!badBracket) {
				if (stack.size() == 0) {
					bw.write("yes");
				} else {
					bw.write("no");
				}
				bw.newLine();
			}
		}
		bw.flush();
		bw.close();
	}
}
