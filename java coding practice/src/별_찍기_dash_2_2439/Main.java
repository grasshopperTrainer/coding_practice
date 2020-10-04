package º°_Âï±â_dash_2_2439;

import java.io.*;
import java.util.Collections;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		for (int i=1; i<N+1; i++) {
			String stars = String.join("", Collections.nCopies(i, "*"));
			bw.write(String.format("%"+Integer.toString(N)+"s", stars));
			bw.newLine();
		}
		bw.flush();
		bw.close();	
	}
}
