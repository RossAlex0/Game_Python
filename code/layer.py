import pytmx
import time  # Pour simuler le passage du temps (boucle de jeu)

# Fonction pour détecter le calque d'objet en fonction de la position du personnage
def detect_layer(tmx_data, player_x, player_y):
    for layer in tmx_data.layers:
        if isinstance(layer, pytmx.TiledObjectGroup):
            for obj in layer:
                if obj.x <= player_x <= obj.x + obj.width and obj.y <= player_y <= obj.y + obj.height:
                    return layer.name
    return None

# Chargement de la carte
tmx_data = pytmx.TiledMap('../assets/map/map_0.tmx')

# Position initiale du personnage
player_x, player_y = 100, 150

# Dernier calque détecté (pour éviter de répéter les messages)
last_layer = None

# Simulation d'une boucle de jeu
while True:
    # Ici, le mouvement du personnage serait capté par vos entrées utilisateur
    # Simulons un déplacement en augmentant la position du personnage :
    player_x += 5  # Exemple : le personnage se déplace de 5 unités sur l'axe x
    player_y += 2  # Exemple : le personnage se déplace de 2 unités sur l'axe y

    # Appel de la fonction pour détecter le calque à chaque déplacement
    current_layer = detect_layer(tmx_data, player_x, player_y)

    # Si le calque a changé, on affiche le nouveau calque
    if current_layer != last_layer:
        if current_layer:
            print(f"Le personnage est maintenant sur le calque : {current_layer}")
        else:
            print("Le personnage n'est sur aucun calque d'objet.")
        last_layer = current_layer

    # Pause pour ralentir la boucle (facultatif, pour simulation)
    time.sleep(1)