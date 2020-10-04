package ³ª¸ÓÁö_3052;

import java.io.*;
import java.util.HashSet;


public class Main {

	public static void main(String[] args) throws IOException{
		int DIVIDER = 42;

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		HashSet set = new HashSet();
		for (int i=0; i<10; i++) {
			set.add(Integer.parseInt(br.readLine())%DIVIDER);
		}
		
		System.out.print(set.size());
	}
}