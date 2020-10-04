package 시험_성적_9498;

import java.io.*;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		if (90 <= n) {
			System.out.print('A');
		} else if (80 <= n) {
			System.out.print('B');
		} else if (70 <= n) {
			System.out.print('C');
		} else if (60 <= n) {
			System.out.print('D');
		} else {
			System.out.print('F');
		}
	}

}
