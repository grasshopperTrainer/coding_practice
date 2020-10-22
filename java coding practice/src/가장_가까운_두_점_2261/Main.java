package 가장_가까운_두_점_2261;

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
//		points.forEach(System.out::println);
		
		TreeSet<Point> candidates = new TreeSet<Point>();
		candidates.add(points.get(0));
		candidates.add(points.get(1));
		
		int minSqareDist = Point.dist(points.get(0), points.get(1));
		double minDist = Math.sqrt(minSqareDist)+1;	// +1 offset to avoid float comparison inaccuracy
		int leftmost = 0;
		for (int i=2; i<N; i++) {
			Point currentPoint = points.get(i);
			// remove points that are out of bound
			while (true) {
				if (points.get(leftmost).x < currentPoint.x-minDist) {
					candidates.remove(points.get(leftmost));
					leftmost++;
				} else {
					break;
				}
			}
//			System.out.println(i);
//			System.out.println(candidates.size());
			candidates.add(currentPoint);
			if (candidates.size() != 0) {
				// sub set points that are in bound and search for min dist
				Point high = candidates.lower(new Point(currentPoint.x, currentPoint.y+(int)minDist));
				Point low = candidates.higher(new Point(currentPoint.x, currentPoint.y-(int)minDist));
//				System.out.println(currentPoint);
//				System.out.println(String.format("%s %s", low, high));
//				if (low == null) {
//					low = currentPoint;
//					includeLow = false;
//				}
//				if (high == null) {
//					high = currentPoint;
//					includeHigh = false;
//				}
				for (Point p : candidates.subSet(low, true, high, true)) {
					if (p == currentPoint) {
						continue;
					}
					int squareDist = Point.dist(currentPoint, p);
					double tempDist = Math.sqrt(squareDist)+1;
					if (tempDist < minDist) {
						minSqareDist = squareDist;
						minDist = tempDist;
					}
				}
			}
		}
		System.out.print(minSqareDist);
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