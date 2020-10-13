package 수_정렬하기_3;

import java.io.*;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		int[] numCounts = new int[10_001];
		for (int i=0; i<N; i++) {
			numCounts[Integer.parseInt(br.readLine())]++;
		}
		
		for (int i=1; i<10_001; i++) {
			String strInt = Integer.toString(i);
			for (int j=0; j<numCounts[i]; j++) {
				bw.write(strInt);
				bw.newLine();
			}
		}
		bw.flush();
		bw.close();
		br.close();
	}
}