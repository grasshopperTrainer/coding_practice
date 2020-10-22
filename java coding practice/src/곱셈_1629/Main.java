package °ö¼À_1629;

import java.io.*;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int A = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(st.nextToken());
		
		System.out.print(calc(A, B, C));
	}
	
	static int calc(int a, int b, int c) {
		if (b == 1) {
			return a%c;
		}

		long d = calc(a, b/2, c);
		long temp = (d*d)%c;
		if (b%2 == 1) {
			temp = temp*a;
			return (int)(temp%c);
		} else {
			return (int)(temp%c);
		}
	}
}