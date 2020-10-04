package 평균은_넘겠지_4344;

import java.io.*;

import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.DoubleStream;


public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(br.readLine());
		for (int i = 0; i < T; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			double[] scores = DoubleStream
					.generate(() -> Double.parseDouble(st.nextToken()))
					.limit(N)
					.toArray();
			double aveScore = Arrays
					.stream(scores)
					.average()
					.getAsDouble();
			double numAbove = (double) Arrays
					.stream(scores)
					.filter(v -> aveScore < v)
					.count();
			double per = numAbove / N * 100;
			
			bw.write(String.format("%.3f%%", per));
			bw.newLine();
		}
		bw.flush();
		bw.close();

	}
}