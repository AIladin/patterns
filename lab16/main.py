from employee import Employee
from staff_list import StaffList


def main():
    staff = StaffList([Employee(f"Employee {i}") for i in range(10)])
    for member in staff:
        print(member.get_name())


if __name__ == "__main__":
    main()
