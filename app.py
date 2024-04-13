from classe.shops import Shop

def main():
    shops = Shop.load_shops_from_json('shop_list.json', 'employe_list.json')
    
    print("Liste des magasins disponibles :")
    for i, shop in enumerate(shops, start=1):
        print(f"{i}. {shop}")
        print("Rayons disponibles dans ce magasin :")
        for rayon in shop.rayons_list:
            print(f"- {rayon['rayon_nom']} ({rayon['rayon_categorie']})")
        print("Employés dans ce magasin :")
        for employee in shop.employees:
            print(f"- {employee}")

if __name__ == "__main__":
    main()