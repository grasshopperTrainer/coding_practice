package 사분면_고르기_14681;

import java.io.*;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int x = Integer.parseInt(br.readLine());
		int y = Integer.parseInt(br.readLine());
		
		if (0 <= x) {
			if (0 <= y) {
				System.out.print(1);							
			} else {
				System.out.print(4);
			}
		} else {
			if (0 <= y) {
				System.out.print(2);
			} else {
				System.out.print(3);
			}
		}
	}

}