package ∫Ì∑¢¿Ë_2798;

import java.io.*;
import java.util.StringTokenizer;
import java.util.Arrays;


public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		int selectionLimit = 3;
		
		int[] nums = new int[N];
		for (int i=0; i<N; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(nums);
		System.out.print(findBest(nums, 0, 0, 0, M, selectionLimit));
	}
	
	static int findBest(int[] nums, int idx, int summed, int numSelected,  int limit, int selectionLimit) {
		if (limit < summed) {
			return 0;
		}
		if (numSelected == selectionLimit) {
			return summed;
		}
		if (idx == nums.length) {
			return 0;
		}
		int bestVal = 0;
		int thisSelected = findBest(nums, idx+1, summed+nums[idx], numSelected+1, limit, selectionLimit);
		bestVal = bestVal < thisSelected ? thisSelected : bestVal;
		int thisNotSelected = findBest(nums, idx+1, summed, numSelected, limit, selectionLimit);
		bestVal = bestVal < thisNotSelected ? thisNotSelected : bestVal;
		return bestVal;
	}
}