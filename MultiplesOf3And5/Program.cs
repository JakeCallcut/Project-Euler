using System;

namespace MultiplesOf3And5
{
    class Program
    {
        static void Main(string[] args)
        {
            //Problem 1, project euler, Multiples of 3 and 5
            int counter = 0;
            int total = 0;

            do
            {
                if (counter % 3 == 0)
                {
                    total = total + counter;
                    counter++;
                }
                else if (counter % 5 == 0)
                {
                    total = total + counter;
                    counter++;
                }
                else
                {
                    counter++;
                }
            } while (counter < 1000);

            Console.WriteLine(total);
        }
    }
}
