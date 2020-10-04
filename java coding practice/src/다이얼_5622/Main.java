package ´ÙÀÌ¾ó_5622;

import java.io.*;
import java.util.HashMap;
import java.util.Scanner;


public class Main {

	public static void main(String[] args) throws IOException {
		int[] sizes = new int[] {0, 3, 3, 3, 3, 3, 4, 3, 4};
//		build distance map
		int charInt = (int)'A';
		HashMap<Character, Integer> distMap = new HashMap<>();
		for (int i=0; i<sizes.length; i++) {
			int size = sizes[i];
			for (int j=0; j<size; j++) {
				distMap.put((char)charInt++, i+1+1);
			}
		}		
//		count movement
		Scanner sc = new Scanner(System.in);
		int count = 0;
		for (char c: sc.next().toCharArray()) {
			count += distMap.get(c);
		}
//		print answer
		sc.close();
		System.out.print(count);
	}
}