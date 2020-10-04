package 그룹_단어_체커_1316;

import java.io.*;
import java.util.Scanner;
import java.util.HashSet;


public class Main {

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		int count = T;
		for (int i=0; i<T; i++) {
			HashSet<Character> visitedChar = new HashSet<>();		
			String str = sc.next();
			int idx = 0;
			while (idx < str.length()) {
				if (visitedChar.contains(str.charAt(idx))) {
					count--;
					break;
				} else {
					char theChar = str.charAt(idx);
					visitedChar.add(theChar);
					while (++idx < str.length()) {
						if (str.charAt(idx) != theChar) {
							break;
						}
					}					
				}
			}
			
		}
		sc.close();
		System.out.print(count);
	}
}