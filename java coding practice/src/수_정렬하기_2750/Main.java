package 수_정렬하기_2750;

import java.io.*;
import java.util.Collections;
import java.util.ArrayList;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		ArrayList<Integer> nums = new ArrayList<Integer>();
		for (int i=0; i<N; i++) {
			nums.add(Integer.parseInt(br.readLine()));
		}
		
		Collections.sort(nums);
		for (int i=0; i<N; i++) {
			bw.write(Integer.toString(nums.get(i)));
			bw.newLine();
		}
		bw.flush();
		bw.close();
		br.close();
	}
}