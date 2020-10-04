package À±³â_2753;

import java.io.*;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		if (n%4 == 0 & (n%100 != 0 | n%400 == 0)) {
			System.out.print(1);
		} else {
			System.out.print(0);
		}
	}

}