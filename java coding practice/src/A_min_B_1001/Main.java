package A_min_B_1001;

import java.io.*;
import java.util.StringTokenizer;
import java.util.Arrays;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line = br.readLine();
		StringTokenizer st = new StringTokenizer(line);
		int[] nums = new int[2];
		for(int i=0; i<2; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}
		System.out.println(nums[0]-nums[1]);
	}

}
