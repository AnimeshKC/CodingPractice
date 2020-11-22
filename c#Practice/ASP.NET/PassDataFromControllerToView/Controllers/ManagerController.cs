using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace PassDataFromControllerToView.Controllers
{
    public class ManagerController : Controller
    {
        // GET: Manager
        public ActionResult Index()
        {
            return Content("Just a Test Return");
        }
        [Route("Manager/PassValue/{value}")]
        public ActionResult PassValue(int value)
        {
            return Content("The Value is " + value);
        }
    }
}