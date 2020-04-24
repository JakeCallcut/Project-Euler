using System;

namespace _10001stPrime
{
    class Program
    {
        //Problem 7, Project Euler, 10001st Prime
        static void Main(string[] args)
        {
            static bool IsPrime(int x)
            {
                for (long i = 2; i < x; i++)
                {
                    if (x % i == 0)
                    {
                        return false;
                    }
                }
                return true;
            }

            int noofprimes = 0;
            int i = 2;
            int lastprime = 2;
            do
            {
                if (IsPrime(i) == true)
                {
                    noofprimes++;
                    lastprime = i;
                }
                i++;
            } while (noofprimes < 10001);

            Console.WriteLine(lastprime);
            Console.WriteLine(i);
            Console.WriteLine(noofprimes);
            Console.ReadKey();
        }
    }
}
