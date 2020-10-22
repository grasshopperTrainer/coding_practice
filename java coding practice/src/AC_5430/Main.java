package AC_5430;

import java.io.*;
import java.util.Collections;
import java.util.LinkedList;
import java.util.stream.Collectors;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(br.readLine());
		for (int t=0; t<T; t++) {
			String commands = br.readLine().trim();
			int N = Integer.parseInt(br.readLine());
			
			String line = br.readLine().trim();
			LinkedList<Integer> nums = new LinkedList<Integer>();
			if (line.length() != 2) {
				for (String s: line.substring(1, line.length()-1).split(",")) {
					nums.add(Integer.parseInt(s));
				}
			}
			
			boolean noAnswer = false;
			boolean isForward = true;
			for (char command : commands.toCharArray()) {
				if (command =='R') {
					isForward = !isForward;
				} else if (!nums.isEmpty()) {
					if (isForward) {
						nums.pollFirst();
					} else {
						nums.pollLast();
					}
				} else {
					bw.write("error\n");
					noAnswer = true;
					break;
				}
			}
			
			if (!noAnswer) {
				if (!isForward) {
					Collections.reverse(nums);
				}
				String strNums = "[" + nums.stream()
						.map(n -> Integer.toString(n))
						.collect(Collectors.joining(","))
						+ "]\n";
				bw.write(strNums);
			}
		}
		bw.close();
	}
}