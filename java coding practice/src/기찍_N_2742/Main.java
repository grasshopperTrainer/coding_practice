package ±âÂï_N_2742;


import java.io.*;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		for (int i=1; i<N+1; i++) {
			bw.write(Integer.toString(i));
			bw.newLine();
		}
		bw.flush();
		bw.close();
	}
}