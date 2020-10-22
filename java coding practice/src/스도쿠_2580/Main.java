package ½ºµµÄí_2580;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.Collectors;


public class Main {
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		ArrayList<int[]> tocheck = new ArrayList<int[]>();
		int[][] board = new int[9][9];
		boolean[][] rows = new boolean[9][10];
		boolean[][] cols = new boolean[9][10];
		boolean[][] blocks = new boolean[9][10];
		
		for (int x=0; x<9; x++) {
			st = new StringTokenizer(br.readLine());
			for (int y=0; y<9; y++) {
				int val = Integer.parseInt(st.nextToken());
				board[x][y] = val;
				
				if (val == 0) {
					tocheck.add(new int[] {x, y});
				}
				rows[x][val] = true;
				cols[y][val] = true;
				blocks[(x/3)*3+(y/3)][val] = true;
			}
		}
		
		br.close();
		
		dfs(0, tocheck, board, rows, cols, blocks);
		
		for (int i=0; i<9; i++) {
			String row = Arrays.stream(board[i]).mapToObj(Integer::toString).collect(Collectors.joining(" "));
			bw.write(row);
			if (i != 8) {
				bw.newLine();
			}
		}
		bw.flush();
		bw.close();
	}
	
	static boolean dfs(int checking, ArrayList<int[]> tocheck, int[][] board, boolean[][] rows, boolean[][] cols, boolean[][] blocks) {
		if (checking == tocheck.size()) {
			return true;
		} else {
			int x = tocheck.get(checking)[0];
			int y = tocheck.get(checking)[1];
			for (int i=1; i<10; i++) {
				if (!rows[x][i] && !cols[y][i] && !blocks[(x/3)*3+(y/3)][i]) {
					
					rows[x][i] = true;
					cols[y][i] = true;
					blocks[(x/3)*3+(y/3)][i] = true;
					board[x][y] = i;
					if (dfs(checking+1, tocheck, board, rows, cols, blocks)) {
						return true;
					}
					
					rows[x][i] = false;
					cols[y][i] = false;
					blocks[(x/3)*3+(y/3)][i] = false;
				}
			}
		}
		return false;
	}
}
