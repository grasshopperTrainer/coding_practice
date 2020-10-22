package 회의실배정_1931;

import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;


public class Main {
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int N = Integer.parseInt(br.readLine());
		
		ArrayList<int[]> meatings = new ArrayList<int[]>();
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			int[] meating = new int[] {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
			meatings.add(meating);
		}
		Collections.sort(meatings, (a, b) -> {
			if (a[1] < b[1]) {
				return -1;
			} else if (a[1] > b[1]) {
				return 1;
			} else {
				if (a[0] < b[0]) {
					return -1;
				} else if (a[0] == b[0]) {
					return 0;
				} else {
					return 1;
				}
			}
		});
		int ending = meatings.get(0)[1];
		int count = 1;
		for (int i=1; i<N; i++) {
			if (ending <= meatings.get(i)[0]) {
				ending = meatings.get(i)[1];
				count++;
			}
		}
		System.out.println(count);
	}
}
