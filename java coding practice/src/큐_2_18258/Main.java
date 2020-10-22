package ť_2_18258;

import java.io.*;
import java.util.LinkedList;
import java.util.StringTokenizer;


public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		LinkedList<Integer> que = new LinkedList<Integer>();
		
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			String inst = st.nextToken();
			if (inst.equals("push")) {
				que.add(Integer.parseInt(st.nextToken()));
			} else {
				if (inst.equals("pop")) {
				bw.write(que.isEmpty() ? "-1" : Integer.toString(que.poll()));
				} else if (inst.equals("size")) {
					bw.write(Integer.toString(que.size()));
				} else if (inst.equals("empty")) {
					bw.write(que.isEmpty() ? "1" : "0");
				} else if (inst.equals("front")) {
					bw.write(que.isEmpty() ? "-1" : Integer.toString(que.element()));
				} else if (inst.equals("back")) {
					bw.write(que.isEmpty() ? "-1" : Integer.toString(que.getLast()));
				}
			bw.newLine();
			}
		}
		bw.close();

	}
}