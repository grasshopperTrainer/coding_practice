package 알람_시계_2884;

import java.io.*;
import java.util.StringTokenizer;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int h = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		m -= 45;
		if (m < 0) {
			m += 60;
			h -= 1;
		}
		if (h < 0) {
			h += 24;
		}
		
		System.out.print(Integer.toString(h)+" "+Integer.toString(m));
	}
}