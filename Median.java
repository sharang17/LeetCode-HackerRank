import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Vector;
import java.util.Collections;


public class Median {

	/**
	 * @param args
	 */
	public static double median_arrays(List<Integer> num1,List<Integer> num2)
	{
		int size=num1.size()+num2.size();
		int i=0;
		int j=0;
		//double median;
		List nums_sorted=new ArrayList();
		while(i<num1.size()&& j<num2.size())
		{
			if(num1.get(i)<num2.get(j)){
				nums_sorted.add(num1.get(i));
				i++;
			}
			else
			{
				nums_sorted.add(num2.get(j));
				j++;
			}
		}
		if(i==num1.size())
		{
			for(int k=j;k<num2.size();k++)
			{
				nums_sorted.add(num2.get(k));
			}
		}
		else
		{
			for(int k=i;k<num1.size();k++)
			{
				nums_sorted.add(num1.get(k));
			}
		}
		//System.out.println(nums_sorted);
		if(size%2==0)
		{
			double median=Double.parseDouble(nums_sorted.get(size/2).toString())+Double.parseDouble(nums_sorted.get((size/2)+1).toString());
			return median/2;
		}
		else
		{
			double median=Double.parseDouble(nums_sorted.get(size/2).toString());
			return median;
		}
		
	}
	public static boolean check_sorted(List<Integer> num,int array_number)
	{
		for(int i=0;i<=num.size()-2;i++)
		{
			if(num.get(i)<num.get(i+1))
			{
				continue;
			}
			else
			{
				System.out.println("Array "+array_number+ " is not sorted, moving to sort");
				return false;
			}
		}
		return true;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Random rand = new Random();
		List num1 =new ArrayList();
		List num2 =new ArrayList();
		for(int i=1;i<=10;i++)
		{
			num1.add(i);
			num2.add(i+10);
		}
		boolean check1=check_sorted(num1,1);
		if(check1==false)
		{
			Collections.sort(num1);
			
		}
		boolean check2=check_sorted(num2,2);
		if(check2==false)
		{
			Collections.sort(num2);
		}
		
		double median=median_arrays(num1,num2);
		System.out.println("Median of the two sorted arrays is: "+median);
		
		
		
	}

}
