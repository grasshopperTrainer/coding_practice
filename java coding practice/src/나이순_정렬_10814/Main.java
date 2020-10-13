package 나이순_정렬_10814;

import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;



public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		ArrayList<User> users = new ArrayList<User>();
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			
			int age = Integer.parseInt(st.nextToken());
			String name = st.nextToken();
			users.add(new User(age, name, i));
		}
		
		Collections.sort(users);
		for (int i=0; i<N; i++) {
			User user = users.get(i);
			bw.write(String.format("%d %s", user.age, user.name));
			bw.newLine();
		}
		
		bw.flush();
		br.close();
		bw.close();
	}
}


class User implements Comparable<User> {
	public int age;
	public String name;
	public int index;
	
	User(int age, String name, int index) {
		this.age = age;
		this.name = name;
		this.index = index;
	}
	
	@Override
	public int compareTo(User another) {
		if (this.age < another.age) {
			return -1;
		} else if (this.age == another.age) {
			if (this.index < another.index) {
				return -1;
			} else {
				return 1;
			}
		} else {
			return 1;
		}
	}
}
