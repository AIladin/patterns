import employee
import visitor

if __name__ == "__main__":
    salary_up = visitor.SalaryUpVisitor(0.5)
    salary_down = visitor.SalaryDownVisitor(0.01)

    team = employee.EmployeeCollection()
    team.add_employee(employee.Manager(5000.0))
    team.add_employee(employee.ITSupport(3500.0))
    team.add_employee(employee.SalesPerson(1500.0))

    print("Team salay before:", team.get_salary())
    team.accept(salary_up)
    print("Team salay after:", team.get_salary())

    it_support = employee.ITSupport(10_000.0)
    print("IT support salary before:", it_support.get_salary())
    it_support.accept(salary_down)
    print("IT support salary after:", it_support.get_salary())
