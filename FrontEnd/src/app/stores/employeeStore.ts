import { makeAutoObservable, runInAction } from "mobx";
import agent from "../api/agent";
import { Employee } from "../models/employee";
import { format } from "date-fns";
import { convertDate } from "../common/utils/common";

export default class EmployeeStore {
  employeeRegistry = new Map<number, Employee>();
  selectedEmployee: Employee | undefined = undefined;
  editMode = false;
  loading = false;
  loadingInitial = false;

  constructor() {
    makeAutoObservable(this);
  }

  /* returns the employees sort by date of join */
  get employeesByDate() {
    return Array.from(this.employeeRegistry.values()).sort(
      (a, b) => a.empDOJ!.getTime() - b.empDOJ!.getTime()
    );
  }

  /* returns employee list grouped by dote of join */
  get groupedEmployee() {
    return Object.entries(
      this.employeesByDate.reduce((employees, employee) => {
        const date = format(employee.empDOJ!, "dd MMM yyyy");
        employees[date] = employees[date]
          ? [...employees[date], employee]
          : [employee];
        return employees;
      }, {} as { [key: string]: Employee[] })
    );
  }

  /* returns list of all the employees detail */
  loadEmployees = async () => {
    this.setLoadingInitial(true);
    try {
      const employees = await agent.Employees.list();
      employees.forEach((employee) => {
        this.setEmployee(employee);
      });
      this.setLoadingInitial(false);
    } catch (error) {
      console.log(error);
      this.setLoadingInitial(false);
    }
  };

  /* returns employee details by employee id */
  loademployee = async (id: number) => {
    let employee = this.getEmployee(id);
    if (employee) {
      runInAction(() => {
        this.selectedEmployee = employee;
      });
      return employee;
    } else {
      this.setLoadingInitial(true);
      try {
        employee = await agent.Employees.details(id);
        this.setEmployee(employee);
        runInAction(() => {
          this.selectedEmployee = employee;
        });
        this.setLoadingInitial(false);
        return employee;
      } catch (error) {
        console.log(error);
        this.setLoadingInitial(false);
      }
    }
  };

  private setEmployee = (employee: Employee) => {
    employee.empDOJ = new Date(employee.empDOJ!);
    this.employeeRegistry.set(employee.empID, employee);
  };

  private getEmployee = (id: number) => {
    return this.employeeRegistry.get(id);
  };

  setLoadingInitial = (state: boolean) => {
    this.loadingInitial = state;
  };

  setLoading = (state: boolean) => {
    this.loading = state;
  };

  /* creates new employee */
  createEmployee = async (employee: Employee) => {
    this.setLoading(true);
    try {
      let emp: any = JSON.parse(JSON.stringify(employee));
      emp.empDOJ = convertDate(emp.empDOJ);
      await agent.Employees.create(emp).then((data: any) => {
        employee = { ...employee, empID: data.empID };
      });
      runInAction(() => {
        this.employeeRegistry.set(employee.empID, employee);
        this.selectedEmployee = employee;
        this.editMode = false;
      });
      this.setLoading(false);
    } catch (error) {
      console.log(error);
      this.setLoading(false);
    }
  };

  /* updates employee */
  updateEmployee = async (employee: Employee) => {
    this.setLoading(true);
    try {
      let emp: any = JSON.parse(JSON.stringify(employee));
      emp.empDOJ = convertDate(emp.empDOJ);
      await agent.Employees.update(emp);
      runInAction(() => {
        this.employeeRegistry.set(employee.empID, employee);
        this.selectedEmployee = employee;
        this.editMode = false;
      });
      this.setLoading(false);
    } catch (error) {
      console.log(error);
      this.setLoading(false);
    }
  };

  /* deletes employee by employee id */
  deleteemployee = async (id: number) => {
    this.setLoading(true);
    try {
      await agent.Employees.delete(id);
      runInAction(() => {
        this.employeeRegistry.delete(id);
      });
      this.setLoading(false);
    } catch (error) {
      console.log(error);
      this.setLoading(false);
    }
  };
}
