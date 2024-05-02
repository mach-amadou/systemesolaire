response = {
    "bodies": [
        {"semimajorAxis": 0},
        {"semimajorAxis": 0},
        {"semimajorAxis": 0},
        {"semimajorAxis": 0},
        {"semimajorAxis": 0},
        {"semimajorAxis": 90},
        {"semimajorAxis": 706},
        {"semimajorAxis": 1184},
        {"semimajorAxis": 1351},
        {"semimajorAxis": 9000}
    ]
}

# Parcourir la liste des objets dans la réponse
for body in response["bodies"]:
    # Extraire la valeur de la clé "semimajorAxis"
    semimajor_axis = body["semimajorAxis"]
    # Afficher la valeur
    print(semimajor_axis)