package 정수_N개의_합_15596;

import java.io.*;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		boolean[] marked = new boolean[10_001];
		for (int i=1; i<10_001; i++) {
			if (!marked[i]) {
				bw.write(Integer.toString(i));
				bw.newLine();
				for (int j=i; j<10_001; j=calc(j)) {
					marked[j] = true;
				}
			}
		}
		
		bw.flush();
		bw.close();
	}
	
	static int calc(int i) {
		int summed = i;
		// sum all numbers
		while (true) {
			summed += i%10;
			if ((i /= 10) == 0) {
				break;
			}
		}
		return summed;
	}
}