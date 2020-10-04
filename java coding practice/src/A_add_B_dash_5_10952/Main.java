package A_add_B_dash_5_10952;

import java.io.*;
import java.util.StringTokenizer;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		while (true) {
			String line = br.readLine();
			if (line.equals("0 0")) {
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

