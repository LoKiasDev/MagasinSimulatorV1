import json

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name} ({self.position})"

    @staticmethod
    def load_employees_from_json(json_file, shop_name):
        employees = []
        with open(json_file, 'r') as file:
            data = json.load(file)
            if shop_name in data:
                employees_list = data[shop_name]
                for employee_info in employees_list:
                    name = employee_info.get('employee_name', '')
                    position = employee_info.get('employee_position', '')
                    employees.append(Employee(name, position))
        return employees

    @staticmethod
    def save_employees_to_json(employees, shop_name):
        try:
            with open('employe_list.json', 'r') as ef:
                employee_data = json.load(ef)
        except FileNotFoundError:
            employee_data = {}
        employee_data[shop_name] = [
            {
                'employee_name': emp.name,
                'employee_position': emp.position
            }
            for emp in employees
        ]
        with open('employe_list.json', 'w') as ef:
            json.dump(employee_data, ef, indent=4)
    @classmethod
    def add_employee(cls, shop, employee):
        shop.employees.append(employee)
        cls.save_employees_to_json(shop.employees, shop.shop_name)
    @classmethod
    def remove_employee(cls, shop, employee_name):
        shop.employees = [emp for emp in shop.employees if emp.name != employee_name]
        cls.save_employees_to_json(shop.employees, shop.shop_name)
