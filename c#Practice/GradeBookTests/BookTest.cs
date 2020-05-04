using System;
using Xunit;
using GradeBook;

namespace GradeBookTests
{
    public class BookTests
    {
        [Fact]
        public void gradesObtained()
        {
            Book book = new Book("");
            book.AddGrade(89.1);
            Statistics result = book.getStatistics();
            Assert.Equal('B', result.letterGrade);
            
        }
        [Fact]
        public void Test1()
        {
            Book book = new Book("");
            book.AddGrade(89.1);
            book.AddGrade(90.5);
            book.AddGrade(77.3);

            Statistics result = book.getStatistics();

            Assert.Equal(85.6, result.average, 1);
            Assert.Equal(90.5, result.highest, 1);
            Assert.Equal(77.3, result.lowest, 1);


        }
    }
}
