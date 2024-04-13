import json
from classe.employe import Employee

class Shop:
    def __init__(self, shop_name, rayons_list, employees):
        self.shop_name = shop_name
        self.rayons_list = rayons_list
        self.employees = employees
    def __str__(self):
        return self.shop_name
    @classmethod
    def load_shops_from_json(cls, shop_list_file, employee_list_file):
        shops = []
        with open(shop_list_file, 'r') as shop_file:
            shop_data = json.load(shop_file)
            for shop_info in shop_data.get('shops', []):
                shop_name = shop_info.get('shop_name', '')
                rayons = shop_info.get('rayons', [])
                rayons_list = [
                    {
                        'rayon_nom': rayon.get('rayon_nom', ''),
                        'rayon_categorie': rayon.get('rayon_categorie', '')
                    }
                    for rayon in rayons
                ]
                employees = Employee.load_employees_from_json(employee_list_file, shop_name)
                shops.append(cls(shop_name, rayons_list, employees))
        return shops
