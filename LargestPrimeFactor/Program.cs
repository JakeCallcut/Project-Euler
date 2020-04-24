using System;

namespace LargestPrimeFactor
{
    class Program
    {   
        //Problem 3, Project Euler, Largest Prime Factor
        const long number = 600851475143;
        static public bool IsPrime(long x)
        {
            for (long i = 2; i < x; i++)
            {
                if(x % i == 0)
                {
                    return false;
                }
            }
            return true;
        }

        static void Main(string[] args)
        {
            //number == 600851475143
            long HPF = 1;

            for (long i = number; i > 2; i--)
            {
                if (number % i == 0)
                {
                    if (Program.IsPrime(i) == true)
                    {
                        if (i > HPF)
                        {
                            HPF = i;
                        }
                    }
                }
            }
            Console.WriteLine(HPF);
            Console.ReadKey();
        }
    }
}
