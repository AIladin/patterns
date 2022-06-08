from manager import Manager
from sales_team import SalesTeam
from salesperson import SalesPerson


def main():
    # Team 1
    sales_team_1 = SalesTeam()

    manager_1 = Manager("Manager 1")
    salesperson_1 = SalesPerson("Salesperson 1", manager_1)
    salesperson_2 = SalesPerson("Salesperson 2", manager_1)

    sales_team_1.add_person(manager_1)
    sales_team_1.add_person(salesperson_1)
    sales_team_1.add_person(salesperson_2)

    # Team 2
    sales_team_2 = SalesTeam()

    manager_2 = Manager("Manager 2")
    salesperson_3 = SalesPerson("Salesperson 3", manager_2)
    salesperson_4 = SalesPerson("Salesperson 4", manager_2)

    sales_team_2.add_person(manager_2)
    sales_team_2.add_person(salesperson_3)
    sales_team_2.add_person(salesperson_4)

    corporation = SalesTeam()  # Union if team 1 and team 2
    corporation.add_person(sales_team_1)
    corporation.add_person(sales_team_2)

    corporation.pay_expenses(10)


if __name__ == "__main__":
    main()
