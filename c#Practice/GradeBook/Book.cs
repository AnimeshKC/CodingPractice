using System;
using System.Collections.Generic;

namespace GradeBook
{
    public delegate void GradeAddedDelegate(object sender, EventArgs args);

    public class Book
    {
        private double average;
        private double highestGrade;
        private double lowestGrade;
        private List<double> grades;
        private string name;
        public Book(string name)
        {
            this.name = name;
            average = 0;
            highestGrade = double.MinValue;
            grades = new List<double>() { };
            lowestGrade = double.MaxValue;
        }
        public event GradeAddedDelegate GradeAdded;
        public void AddGrade(double grade) //adds a grade and also updates the average
        {
            if (grade >100 || grade < 0)
            {
                throw new ArgumentException();
            }
            grades.Add(grade);
            average += (grade - average) / grades.Count; //constant time update that reduces chance of overflowing
            UpdateHighest(grade);
            UpdateLowest(grade);
            if(GradeAdded != null)
            {
                GradeAdded(this, new EventArgs());
            }
        }

        private char GetGrade()
        {
            switch (this.average)
            {
                case double d when d >= 90.00:
                    return 'A';
                case double d when d >= 75.00:
                    return 'B';
                case double d when d >= 60.00:
                    return 'C';
                case double d when d >= 50.00:
                    return 'D';
                default:
                    return 'F';
            }
        }

        private void UpdateHighest(double grade)
        {
            if (grade > highestGrade)
            {
                highestGrade = grade;
            }
        }
        private void UpdateLowest(double grade){
            if (grade < lowestGrade){
                lowestGrade = grade;
            }
        }
        public Statistics getStatistics()
        {
            Statistics result = new Statistics();
            result.average = average;
            result.lowest = lowestGrade;
            result.highest = highestGrade;
            result.letterGrade = GetGrade();
            return result;
        }
        public string Name
        {
            get
            {
                return name;
            }
            set
            {
                if (!String.IsNullOrEmpty(value))
                {
                    name = value;
                }
                else
                {
                    Console.WriteLine("Name has not been changed because the value is null or empty");
                }
            }
        }
    }

}