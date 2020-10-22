package N_Queen_9663;

import java.io.*;
import java.util.Scanner;


public class Main {

	public static void main(String[] args) throws IOException{
		int N = new Scanner(System.in).nextInt();
		boolean[] a = new boolean[3];
		System.out.print(dfs(N, 0, new boolean[2*N-1], new boolean[2*N-1], new boolean[N]));
	}
	
	static int dfs(int size, int x, boolean[] dia1, boolean[] dia2, boolean[] col) {
		if (x == size) {
			return 1;
		}
		int count = 0;
		for (int y=0; y<size; y++) {
			if (!dia1[x+y] && !dia2[(size-1)+(x-y)] && !col[y]) {
				
				dia1[x+y] = true;
				dia2[(size-1)+(x-y)] = true;
				col[y] = true;
				
				count += dfs(size, x+1, dia1, dia2, col);
				
				dia1[x+y] = false;
				dia2[(size-1)+(x-y)] = false;
				col[y] = false;
			}
		}
		return count;
	}
}
