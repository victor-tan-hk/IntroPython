
#Accessing global variables from __init.py__
from game import name_of_game
print (name_of_game)

#Accessing the module in the top-level package
import game.main_menu

game.main_menu.show_menu()

#Accessing the module in the subpackage
from game.sound.play import  make_cool_sounds

make_cool_sounds()

