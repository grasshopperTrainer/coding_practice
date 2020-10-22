package 가장_가까운_두_점_2261_2;

import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		
		// points sorted by x coordinate
		ArrayList<Point> points = new ArrayList<Point>();
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			points.add(new Point(x, y));
		}
		Collections.sort(points, Comparator.comparing(n -> n.x));
		
		
	}
}

class Point implements Comparable<Point> {
	
	int x;
	int y;
	
	Point(int x, int y) {
		this.x = x;
		this.y = y;
	}

	@Override
	public int compareTo(Point another) {
		if (this.y < another.y) {
			return -1;
		} else if (this.y > another.y) {
			return 1;
		} else {
			if (this.x < another.x) {
				return -1;
			} else if (this.x > another.x) {
				return 1;
			} else {
				return 0;
			}
		}
	}
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return String.format("<Point %d %d>", this.x, this.y);
	}
	
	public static int dist(Point point, Point point2) {
		return (int)Math.pow(point.x-point2.x, 2) + (int)Math.pow(point.y-point2.y, 2);
	}
}