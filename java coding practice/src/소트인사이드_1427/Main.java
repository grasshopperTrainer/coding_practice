package 소트인사이드_1427;

import java.io.*;
import java.util.Arrays;
import java.util.Comparator;
import java.util.stream.Collectors;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		String strInt = Arrays.stream(Integer.toString(N).split(""))
				.sorted(Comparator.reverseOrder())
				.collect(Collectors.joining());
		
		System.out.print(Integer.parseInt(strInt));
	}
}