package 크로아티아_알파벳_2941;

import java.io.*;
import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.HashSet;

public class Main {

	public static void main(String[] args) throws IOException {
		String[] sChars = new String[] {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
		HashSet<String> sCharSet = new HashSet<>(Arrays.stream(sChars).collect(Collectors.toSet()));
		
		Scanner sc = new Scanner(System.in);
		String str = sc.next();
		sc.close();
		
		int count = 0;
		int idx = 0;
		while (idx < str.length()) {
			if (idx < str.length()-1 && sCharSet.contains(str.substring(idx, idx+2))) {
				count++;
				idx += 2;
			} else if (idx < str.length()-2 && sCharSet.contains(str.substring(idx, idx+3))) {
				count++;
				idx += 3;
			} else {
				count++;
				idx++;
			}
		}
		
		System.out.print(count);
	}
}