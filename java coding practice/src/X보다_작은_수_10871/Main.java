package X보다_작은_수_10871;

import java.io.*;
import java.util.StringTokenizer;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int X = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<N; i++) {
			int n = Integer.parseInt(st.nextToken());
			if (n < X) {
				bw.write(Integer.toString(n));
				bw.write(" ");
			}
		}
		bw.flush();
		bw.close();	
	}
}
