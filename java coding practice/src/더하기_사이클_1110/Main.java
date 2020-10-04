package 더하기_사이클_1110;

import java.io.*;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		int newN = N;
		int count = 0;
		while (true) {
			count++;
			newN = (newN%10)*10 + (newN/10 + newN%10)%10;
			if (newN == N) {
				System.out.print(count);
				break;
			}
		}
	}
}