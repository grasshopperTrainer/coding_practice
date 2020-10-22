package °ýÈ£_9012;

import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		for (int i = 0; i < N; i++) {
			int checker = 0;
			boolean badBracket = false;
			for (char s: br.readLine().toCharArray()) {
				if (s == '(') {
					checker++;
				} else {
					checker--;
				}
				if (checker < 0) {
					bw.write("NO");
					bw.newLine();
					badBracket = true;
					break;
				}
			}
			if (!badBracket) {
				if (checker == 0) {
					bw.write("YES");
				} else {
					bw.write("NO");
				}
				bw.newLine();
			}
		}
		bw.flush();
		bw.close();
	}
}
