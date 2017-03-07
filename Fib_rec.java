import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;


public class Fib_rec {

	/**
	 * @param args

	 */
	public static int Fib(int n)
	{
		if (n==1)
			return 1;
		if (n==2)
			return 1;
		return Fib(n-1)+Fib(n-2);
	}
	
	public static int Factorial(int n)
	{
		int result;
		if (n==0|n==1)
		{
			return 1;
		}
		else
		{
			result=n*Factorial(n-1);
			
		}
		
		return result;
	}
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter number: ");
		int number=Integer.parseInt(br.readLine());
		
		
		for(int i=1;i<=number;i++)
		{
			int fib=Fib(i);
			System.out.println(fib);
		}
	
		System.out.println("Recursive call to factorial: ");
		int fact=Factorial(number);
		System.out.print(fact);
	}

}
