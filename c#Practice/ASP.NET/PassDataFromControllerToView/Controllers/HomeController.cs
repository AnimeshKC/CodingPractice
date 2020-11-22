using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using PassDataFromControllerToView.Models;

namespace PassDataFromControllerToView.Controllers
{
    public class HomeController : Controller
    {
        // GET: Home
        public ActionResult Index()
        {
            ViewBag.User = "Default";
            ViewBag.Preference = "None";
            return View();
        }
        public ActionResult GetEmployee()
        {
            var employees = new List<Employee>() {new Employee()
            {
                EmployeeId = 1,
                EmployeeName = "John Smith"
            },new Employee()
            {
                EmployeeId = 2,
                EmployeeName = "Jane Smith"
            }
        };

            ViewBag.Employees = employees;
            return View();
        }
    }
}