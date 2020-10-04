package A_add_B_dash_8_11022;

import java.io.*;
import java.util.StringTokenizer;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(br.readLine());
		for (int i=0; i<T; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			bw.write(String.format("Case #%d: %d + %d = %d", i+1, a, b, calc(a, b)));
			bw.newLine();
		}
		bw.flush();
		bw.close();
		
	}
	static int calc(int a, int b) {
		return a + b;
	}
}

