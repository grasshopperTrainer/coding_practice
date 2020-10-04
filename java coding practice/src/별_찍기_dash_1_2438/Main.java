package º°_Âï±â_dash_1_2438;

import java.io.*;
import java.util.Collections;



public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		for (int i=1; i<N+1; i++) {
			bw.write(String.join("", Collections.nCopies(i, "*")));
			bw.newLine();
		}
		bw.flush();
		bw.close();	
	}
}
