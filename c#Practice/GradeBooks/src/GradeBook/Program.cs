using System;

namespace GradeBook
{
    class Program
    {
        static void Main(string[] args)
        {   
            double result = 0;
            double[] grades = new double[4] {14, 16.5, 18, 22};
            foreach(double grade in grades){
                result += grade;
            }
            Console.WriteLine(result);
        }
    }
}
