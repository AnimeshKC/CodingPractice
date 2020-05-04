using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace GradeBook
{
    class Program
    {
        static void Main(string[] args)
        {
            Book zenBook = new Book("Zen");
            zenBook.GradeAdded += OnGradeAdded;
            Console.WriteLine("Enter grades or q if finished entering grades");
            while (true){
                Console.WriteLine("Enter a grade: ");
                string input = Console.ReadLine();
                if (input.ToLower() == "q") break;
                try
                {
                    double numberGrade = double.Parse(input);
                    zenBook.AddGrade(numberGrade);
                }
                catch (ArgumentException ex)
                {
                    Console.WriteLine(ex.Message);
                }
                catch (FormatException ex)
                {
                    Console.WriteLine(ex.Message);
                }


            }
            Statistics result;
            result = zenBook.getStatistics();
            Console.WriteLine($"For book owned by {zenBook.Name}, The highest grade is {result.highest}\n" +
                $"The lowest grade is {result.lowest}\n" +
                $"The average grade is {result.average}\n" +
                $"The average letter grade is {result.letterGrade}");
            zenBook.Name = "NewName";
            Console.WriteLine($"New name is: {zenBook.Name}");
            zenBook.Name = "";
            Console.WriteLine($"New name is: {zenBook.Name}");
        }
        static void OnGradeAdded(object sender, EventArgs e)
        {
            Console.WriteLine("A grade was added");
        }
    }
}
