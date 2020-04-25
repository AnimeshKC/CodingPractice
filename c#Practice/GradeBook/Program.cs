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

            foreach (double grade in new List<double> { 76, 82, 58, 44 })
            {
                zenBook.addGrade(grade);
            }
            zenBook.statistics();
            zenBook.addGrade(89);
            zenBook.statistics();
        }
    }
}
