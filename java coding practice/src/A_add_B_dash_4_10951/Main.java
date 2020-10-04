package A_add_B_dash_4_10951;

import java.io.*;
import java.util.StringTokenizer;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String line;
		while (true) {
			line = br.readLine();
			if (line == null) {
				break;
			}
			StringTokenizer st = new StringTokenizer(line);			
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			bw.write(Integer.toString(a+b));
			bw.newLine();
		}
		bw.flush();
		bw.close();
	}
}