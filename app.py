from classe.shops import Shop
from classe.employe import Employee
from classe.produit import Produit

def main():
    while True:
        shops = Shop.load_shops_from_json('shop_list.json', 'employe_list.json', 'produit_list.json')
        
        print("Liste des magasins disponibles :")
        for i, shop in enumerate(shops, start=1):
            print(f"{i}. {shop}")
            print("Rayons disponibles dans ce magasin :")
            for rayon in shop.rayons_list:
                print(f"- {rayon['rayon_nom']} ({rayon['rayon_categorie']})")
            print("Employés dans ce magasin :")
            for employee in shop.employees:
                print(f"- {employee}")
            print("Produit du magasin + quantité")
            for produit in shop.produit:
                print(f"- {produit}")
                
        entreprise_changement = int(input("À quelle entreprise voulez-vous appliquer des changements (En chiffre) : "))
        choice_changement = int(input("Voulez-vous gérer les employés, les produits ou les rayons ? (Entrez 1 pour les employés, 2 pour les produits, 3 pour les rayons) : "))
        
        if choice_changement == 1:
            while True:
                choice_employe = int(input("Voulez-vous en rajouter ou en supprimer ? (Entrez 1 pour rajouter, 2 pour supprimer, 3 pour revenir) : "))
                if choice_employe == 1:
                    new_employee_name = input("Nom de l'employé : ")
                    new_employee_position = input("Position de l'employé : ")
                    new_employee = Employee(new_employee_name, new_employee_position)
                    Employee.add_employee(shops[entreprise_changement - 1], new_employee)
                    print("Changement effectué !")
                    break  
                elif choice_employe == 2:
                    employee_to_remove = input("Nom de l'employé à supprimer : ")
                    Employee.remove_employee(shops[entreprise_changement - 1], employee_to_remove)
                    print("Changement effectué !")
                    break  
                elif choice_employe == 3:
                    break 
        
        elif choice_changement == 2:
            while True:
                choice_produit = int(input("Voulez-vous en rajouter ou en supprimer ? (Entrez 1 pour rajouter, 2 pour supprimer, 3 pour revenir) : "))
                if choice_produit == 1:
                    new_produit_name = input("Le nom du produit : ")
                    new_produit_quantite = input("La quantité du produit: ")
                    new_produit = Produit(new_produit_name, new_produit_quantite)
                    Produit.add_produit(shops[entreprise_changement - 1], new_produit)
                    print("Changement effectué !")
                    break  
                elif choice_produit == 2:
                    produit_to_remove = input("Le nom du produit : ")
                    Produit.remove_produit(shops[entreprise_changement - 1], produit_to_remove)
                    print("Changement effectué !")
                    break  
                elif choice_produit == 3:
                    break  
        
        elif choice_changement == 3:
            while True:
                choice_rayon = int(input("Voulez-vous ajouter ou supprimer un rayon ? (Entrez 1 pour ajouter, 2 pour supprimer, 3 pour revenir) : "))
                if choice_rayon == 1:
                    new_rayon_nom = input("Nom du nouveau rayon : ")
                    new_rayon_categorie = input("Catégorie du nouveau rayon : ")
                    shops[entreprise_changement - 1].add_rayon(new_rayon_nom, new_rayon_categorie)
                    print("Changement effectué !")
                    break  
                elif choice_rayon == 2:
                    rayon_to_remove = input("Nom du rayon à supprimer : ")
                    shops[entreprise_changement - 1].remove_rayon(rayon_to_remove)
                    print("Changement effectué !")
                    break 
                elif choice_rayon == 3:
                    break  
        
        else:
            print("Choix invalide.")

        again = input("Voulez-vous effectuer une autre action ? (oui/non) : ").lower()
        if again != 'oui':
            break  

if __name__ == "__main__":
    main()
