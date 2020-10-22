package 히스토그램에서_가장_큰_직사각형_6549;

import java.io.*;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;

		String line;
		while (!(line = br.readLine()).equals("0")) {
			st = new StringTokenizer(line);

			int N = Integer.parseInt(st.nextToken());
			int[] vals = new int[N];
			for (int i = 0; i < N; i++) {
				vals[i] = Integer.parseInt(st.nextToken());
			}
			bw.write(Long.toString(calc(0, N, vals)));
			bw.newLine();
		}

		bw.close();
	}

	static long calc(int s, int e, int[] vals) {
		if (s + 1 == e) {
			return vals[s];
		}
		int m = (s + e) / 2;
		// max not crossing middle
		long leftArea = calc(s, m, vals);
		long rightArea = calc(m, e, vals);
		long maxArea = Math.max(leftArea, rightArea);
		// max crossing middle
		long middleArea = 0;
		long height = Math.min(vals[m - 1], vals[m]);
		int l = m - 1;
		int r = m;
		while (true) {
			while (s <= l && height <= vals[l]) {
				l--;
			}
			while (r < e && height <= vals[r]) {
				r++;
			}
			middleArea = Math.max(middleArea, (r - l - 1) * height);
			height = Math.max(s <= l ? vals[l] : 0, r < e ? vals[r] : 0);
			if (l < s && e <= r) {
				break;
			}
		}
		return Math.max(maxArea, middleArea);
	}
}
