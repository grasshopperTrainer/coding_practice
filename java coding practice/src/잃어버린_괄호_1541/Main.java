package ÀÒ¾î¹ö¸°_°ýÈ£_1541;

import java.io.*;


public class Main {
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		boolean minusFound = false;
		int summed = 0;
		String num = "";
		
		for (char c: br.readLine().toCharArray()) {
			if (Character.isDigit(c)) {
				num += c;
			} else if (minusFound) {
				summed -= Integer.parseInt(num);
				num = "";
			} else {
				summed += Integer.parseInt(num);
				num = "";
				if (c == '-') {
					minusFound = true;
				}
			}
		}
		
		if (minusFound) {
			summed -= Integer.parseInt(num);
		} else {
			summed += Integer.parseInt(num);
		}
		
		System.out.print(summed);
	}
}
