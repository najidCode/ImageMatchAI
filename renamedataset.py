import os

def rename_images_in_folder(folder_path):
    # Vérifier si le dossier existe
    if not os.path.exists(folder_path):
        print(f"Le dossier {folder_path} n'existe pas.")
        return

    # Lister tous les fichiers du dossier
    files = os.listdir(folder_path)
    
    # Filtrer les fichiers avec des extensions valides
    valid_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')
    images = [f for f in files if f.lower().endswith(valid_extensions)]
    
    # Renommer les fichiers séquentiellement
    for index, image in enumerate(images, start=1):
        # Nouveau nom pour l'image
        new_name = f"{index}.png"
        old_path = os.path.join(folder_path, image)
        new_path = os.path.join(folder_path, new_name)

        # Renommer le fichier
        os.rename(old_path, new_path)
        print(f"Renommé : {old_path} → {new_path}")
    
    print("Renommage terminé !")

# Exemple d'utilisation
folder_path = "C:\\Users\hp\Downloads\\NAJID_MOHAMED_WEB\\NAJID_MOHAMED_\Dataset\Camera"
rename_images_in_folder(folder_path)
