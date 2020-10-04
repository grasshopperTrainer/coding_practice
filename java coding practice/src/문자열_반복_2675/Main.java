package 문자열_반복_2675;

import java.io.*;
import java.util.Collections;
import java.util.StringTokenizer;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(br.readLine());
		for (int i=0; i<T; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int count = Integer.parseInt(st.nextToken());
			String answer = "";
			for (String s: st.nextToken().split("")) {
				answer += String.join("", Collections.nCopies(count, s));
			}
			bw.write(answer);
			bw.newLine();
		}
		bw.flush();
		bw.close();
		br.close();
	}
}