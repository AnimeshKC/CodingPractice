using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using leave_managment.Data;

namespace leave_managment.Contracts
{
    interface ILeaveAllocation: IRepositoryBase<LeaveAllocation>
    {
    }
}
