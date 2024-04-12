from classe.shops import Shop

def main():
    shops = Shop.load_shops_from_json('shop_list.json')
    print("Vous faites une petite randonné mais TOUDINCOU vous voulez faire du shopping")
    print("Magasin dispo : ")
    for i, shop in enumerate(shops, start=1):
        print(f"{i} : {shop}")
    
    choice_shop = input("Dans quelle magasin voulez-vous faire du shopping ? ")
    try:
        index = int(choice_shop) - 1
        if 0 <= index < len(shops):
            selected_shop = shops[index]
            print(f"Vous avez choisi le magasin : {selected_shop}")
            print("Rayons disponibles dans ce magasin :")
            for rayon in selected_shop.rayons_list:
                print(f"- {rayon['rayon_nom']} ({rayon['rayon_categorie']})")
        else:
            print("Vous n'avez pas fait un choix valide. Merci de réessayer.")
    except ValueError:
        print("Veuillez entrer un chiffre valide.")

if __name__ == "__main__":
    main()










