import json
from classe.employe import Employee
from classe.produit import Produit

class Shop:
    def __init__(self, shop_name, rayons_list, employees, produit):
        self.shop_name = shop_name
        self.rayons_list = rayons_list
        self.employees = employees
        self.produit = produit

    def __str__(self):
        return self.shop_name

    @classmethod
    def load_shops_from_json(cls, shop_list_file, employee_list_file, produit_list_file):
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
                produit = Produit.load_employees_from_json(produit_list_file, shop_name)
                shops.append(cls(shop_name, rayons_list, employees, produit))
        return shops
    
    def add_rayon(self, rayon_nom, rayon_categorie):
        new_rayon = {
            'rayon_nom': rayon_nom,
            'rayon_categorie': rayon_categorie
        }
        self.rayons_list.append(new_rayon)
        self.save_shop_to_json()  

    def remove_rayon(self, rayon_nom):
        self.rayons_list = [rayon for rayon in self.rayons_list if rayon['rayon_nom'] != rayon_nom]
        self.save_shop_to_json() 

    def save_shop_to_json(self):
        shop_data = {
            'shop_name': self.shop_name,
            'rayons': self.rayons_list
        }
        try:
            with open('shop_list.json', 'r') as sf:
                all_shops_data = json.load(sf)
        except FileNotFoundError:
            all_shops_data = {'shops': []}
        shop_found = False
        for shop_info in all_shops_data['shops']:
            if shop_info['shop_name'] == self.shop_name:
                shop_info.update(shop_data)
                shop_found = True
                break
        if not shop_found:
            all_shops_data['shops'].append(shop_data)
        with open('shop_list.json', 'w') as sf:
            json.dump(all_shops_data, sf, indent=4)

    

