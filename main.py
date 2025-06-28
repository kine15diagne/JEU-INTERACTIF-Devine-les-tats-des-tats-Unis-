import pandas
import turtle

from numpy.random import get_state

screen = turtle.Screen()
screen.title("U.S. STATES GAME")  # Ceci définit le titre de la fenêtre
image = "blank_states_img.gif"

screen.addshape(image)  # Cela doit être fait avant de définir la forme de la tortue
turtle.shape(image)

# Fonction pour obtenir les coordonnées du clic de souris
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

# TODO 1 : Positionner chaque État et faire en sorte que la fenêtre ne se ferme pas après un clic
# Cette méthode permet d’obtenir les coordonnées (x, y) en cliquant sur la carte
# Comme nous avons déjà le fichier CSV, cette méthode n’est pas nécessaire ici

states = pandas.read_csv("50_states.csv")
state_list = states["state"].to_list()
print(state_list)

# Vérifier si la réponse est dans la liste des États, et si c’est correct :
# créer une tortue pour écrire le nom de l’État sur la carte
guessed_state = []

while len(guessed_state) <= 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_state)}/50 États trouvés",
        prompt="Écrivez le nom d’un État :"
    ).title()  # Met automatiquement la première lettre en majuscule
    print(answer_state)  # Affiche les États saisis pour suivre les bonnes réponses

    if answer_state is None or answer_state == "Exit":
        # missing_state = []
        # for x in state_list:
        #     if x not in guessed_state:
        #         missing_state.append(x)
        missing_state = [state for state in state_list if state not in guessed_state]
        print(missing_state)
        brush_up = pandas.DataFrame(missing_state)
        brush_up.to_csv("states_to_learn.csv")  # Sauvegarde les États non trouvés
        break

    if answer_state in state_list:
        guessed_state.append(answer_state)
        t = turtle.Turtle()  # Création d’une nouvelle tortue
        t.hideturtle()
        t.penup()
        states_data = states[states.state == answer_state]  # Récupère la ligne correspondant à l’État deviné
        # Comme states_data est une ligne du tableau, on peut accéder à ses coordonnées
        t.goto(states_data.x.item(), states_data.y.item())  # .item() pour extraire la valeur
        t.write(answer_state)  # Écrit le nom de l’État sur la carte

    elif answer_state not in state_list:
        print(f"{answer_state} ne fait pas partie des 50 États,\n Réessaie")
