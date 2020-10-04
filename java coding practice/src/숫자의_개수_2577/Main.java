package 숫자의_개수_2577;

import java.io.*;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int A = Integer.parseInt(br.readLine());
		int B = Integer.parseInt(br.readLine());
		int C = Integer.parseInt(br.readLine());
		
		int[] counter = new int[10];
		int D = A * B * C;
		String s = Integer.toString(D);
		
		for (String c: s.split("")) {
			counter[Integer.parseInt(c)]++;
		}
		
		for (int i: counter) {
			System.out.println(i);
		}
	}
}