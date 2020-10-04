package OXÄûÁî_8958;

import java.io.*;


public class Main {

	public static void main(String[] args) throws IOException{
		char GOOD = 'O';
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(br.readLine());
		for (int i=0; i<T; i++) {
			int sumScore = 0;
			int score = 0;
			for (char c: br.readLine().toCharArray()) {
				if (c == GOOD) {
					score++;
					sumScore += score;
				} else {
					score = 0;
				}
			}
			bw.write(Integer.toString(sumScore));
			bw.newLine();
		}
		bw.flush();
		bw.close();
	}
}