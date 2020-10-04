package 단어_공부_1157;

import java.io.*;
import java.util.HashMap;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		
		String str = sc.next();
		sc.close();
//		count
		HashMap<Character, Integer> counter = new HashMap<>();
		for (char c : str.toCharArray()) {
			char lower = Character.toLowerCase(c);
			counter.putIfAbsent(lower, 0);
			counter.compute(lower, (Character key, Integer value) -> ++value);
		}

//		evaluate most common
		char theChar = 'a';
		int count = 0;
		for (char c : counter.keySet()) {
			if (count < counter.get(c)) {
				count = counter.get(c);
				theChar = Character.toUpperCase(c);
			} else if (count == counter.get(c)) {
				count = counter.get(c);
				theChar = '?';
			}
		}
		System.out.print(theChar);
	}
}