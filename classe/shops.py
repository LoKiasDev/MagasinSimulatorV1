import json

class Shop:
    def __init__(self, shop_name: str, rayons_list: int):
        self.shop_name = shop_name
        self.rayons_list = rayons_list

    def __str__(self):
        return self.shop_name

    @classmethod
    def load_shops_from_json(cls, json_file):
        shops = []
        with open(json_file, 'r') as file:
            data = json.load(file)
            for shop_data in data.get('shops', []):
                shop_name = shop_data.get('shop_name', 'Default Shop')
                rayons = shop_data.get('rayons', [])
                rayons_list = [
                    {
                        'rayon_nom': rayon.get('rayon_nom', 'Dafault Name Rayon'),
                        'rayon_categorie': rayon.get('rayon_categorie', 'Deault Categorie Rayon')
                    }
                    for rayon in rayons
                ]
                shops.append(cls(shop_name, rayons_list))  
        return shops