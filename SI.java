
import java.lang.*;
public class SI {

	/**
	 * @param args
	 */
	
	
	public static void interest()
	{
		double p=1000;
		double r=.10;
		double n=1;
		int count=0;
		System.out.println("P\tR\tN\tAmount");
		while(count<10)
		{
			double amount=p*Math.pow(1+r,n);
			System.out.println(p+"\t"+r+"\t"+n+"\t"+amount);
			p=p+1000;
			r+=.1;
			n+=1;
			count++;
		}
	}
	public static void main(String[] args) {
		
		// TODO Auto-generated method stub
	System.out.println("Table for various values of Principal, ROI and time...");
	interest();
	
	}

}
