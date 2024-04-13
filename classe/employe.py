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
            else:
                pass
        return employees