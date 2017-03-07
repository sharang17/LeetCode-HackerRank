
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.*;
public class Reverse {

	/**
	 * @param args
	 */
	public static int reverse(String input)
	{
	
		int i=input.length()-1;
		int input_string=Integer.parseInt(input);
		int output=0;
		double mult=Math.pow(10,i);
		while(i>=0){
			int temp=(int) (input_string%10);
			
			//System.out.println(output);
			i--;
			input_string=input_string/10;
			output=(int) (output+temp*mult);
			mult=mult/10;
			//output+=temp*mult;
			//i--;
			//mult*=10;
			
		}
		
		return output;
	}
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter Number to Reverse: ");
		String input=br.readLine();
		int output=reverse(input);
		System.out.println(output);
		
	}

}
