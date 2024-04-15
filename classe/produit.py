import json

class Produit:
    def __init__(self, produit_name, produit_quantite: int):
        self.produit_name = produit_name
        self.produit_quantite = produit_quantite

    def __str__(self):
        return f"{self.produit_name} ({self.produit_quantite})"

    @staticmethod
    def load_employees_from_json(json_file, shop_name):
        produits = []
        with open(json_file, 'r') as file:
            data = json.load(file)
            if shop_name in data:
                produit_list = data[shop_name]
                for produit_info in produit_list:
                    produit_name = produit_info.get('produit_name', '')
                    produit_quantite = produit_info.get('produit_quantity', '')
                    produits.append(Produit(produit_name, produit_quantite))
            else:
                pass
        return produits

    @staticmethod
    def save_produit_to_json(produits, shop_name):
        try:
            with open('produit_list.json', 'r') as ef:
                produit_data = json.load(ef)
        except FileNotFoundError:
            produit_data = {}
        
        produit_data[shop_name] = [
            {
                'produit_name': produit.produit_name,  
                'produit_quantity': produit.produit_quantite  
            }
            for produit in produits
        ]
        
        with open('produit_list.json', 'w') as ef:
            json.dump(produit_data, ef, indent=4)

    @classmethod
    def add_produit(cls, shop, produit):
        shop.produit.append(produit)
        cls.save_produit_to_json(shop.produit, shop.shop_name)

    @classmethod
    def remove_produit(cls, shop, produit_name):
        shop.produit = [p for p in shop.produit if p.produit_name != produit_name]
        cls.save_produit_to_json(shop.produit, shop.shop_name)