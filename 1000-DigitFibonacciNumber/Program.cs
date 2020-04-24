using System;

namespace _1000_DigitFibonacciNumber
{
    class Program
    {   
        //Problem 25, Project Euler, 1000-Digit Fibonacci Sequence
        static void Main(string[] args)
        {
            int digits = 10;
            long currnum = 1134903170;
            long prevnum = 701408733;
            long nextnum = 0;
            int index = 45;

            do
            {
                nextnum = prevnum + currnum;
                prevnum = currnum;
                currnum = nextnum;

                digits = Convert.ToString(currnum).Length;
                index++;

            } while (digits < 50);

            Console.WriteLine(prevnum);
            Console.WriteLine(currnum);
            Console.WriteLine(index);
            Console.WriteLine("test");      //alg works but takes a very long amount of time
            Console.ReadKey();

        }
    }
}
