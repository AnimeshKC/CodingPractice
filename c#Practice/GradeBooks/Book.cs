using System;
using System.Collections.Generic;
using System.Linq;

namespace GradeBooks
{
    class Book
    {
        double average;
        double highestGrade;
        List<double> grades;
        string name;
        public Book(string name)
        {
            this.name = name;
            this.average = 0;
            this.highestGrade = double.MinValue;
            this.grades = new List<double>() { };

        }
        public void addGrade(double grade) //adds a grade and also updates the average
        {
            grades.Add(grade);
            average += (grade - average)/ grades.Count; //constant time update that reduces chance of overflowing
            updateHighest(grade);
        }
        private void updateHighest(double grade)
        {
            if (grade > highestGrade)
            {
                highestGrade = grade;
            }
        }
        public void statistics()
        {
            Console.WriteLine($"In this gradebook, {name}, \n The average grade is {average} \n  The highest grade is {highestGrade}");
        }
    }

}