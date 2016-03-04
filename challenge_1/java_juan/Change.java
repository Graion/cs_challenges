public class Change {

	public static void main(String[] args) {
		int[] values = {1, 5, 10};
		System.out.println(giveMeChange(values, 28));
	}
	
	public static int giveMeChange(int[] values, int change){
		 int numberOfCoins = 0;

		 if(values.length>0){
			 for(int index = values.length; index>0; index--){
				numberOfCoins += change / values[index-1];
			    change = change % values[index-1];
			 }	 
		 }
		 
		 return numberOfCoins;
	}
}
