import pygame, sys
from pygame.locals import *
import pygame.freetype
import time

class enigmaKeyboard:
    def __init__(self, keys="ABCDEF"):
        self.keys = keys
        self.row1 = keys[:3]
        self.row2 = keys[3:]

    def add_key(self, letter, color, position_x=50, position_y=500):
        self.letter = letter
        self.color = color
        self.position_x = position_x
        self.position_y = position_y

        self.circle = pygame.draw.circle(enigma, self.color, (self.position_x, self.position_y), 20)
        self.text = enigma_font.render_to(enigma, (self.position_x - 8, self.position_y - 8), self.letter, white)

    def add_rows(self):
        self.position_x = 50
        self.position_y = 500
        counter = 100
        for key in self.row1:
            self.circle = pygame.draw.circle(enigma, gray, (self.position_x + counter, self.position_y), 20)
            self.text = enigma_font.render_to(enigma, (self.position_x - 8 + counter, self.position_y - 8), key, white)
            counter += 100
        counter = 100

        for key in self.row2:
            self.circle = pygame.draw.circle(enigma, gray, (self.position_x + counter, self.position_y + 100), 20)
            self.text = enigma_font.render_to(enigma, (self.position_x - 8 + counter, self.position_y - 8 + 100), key, white)
            counter += 100
        counter = 100

wiring = {"A":"C", "B":"D", "C":"F", "D":"A", "E":"E", "F":"B"}
reflector_wiring = {"A":"D", "B":"C", "E":"F"}

class Enigma:
    def __init__(self):
        self.index_finder = ["A", "B", "C", "D", "E", "F", "A", "B", "C", "D", "E", "F", "A", "B", "C",
        "D", "E", "F", "A", "B", "C", "D", "E", "F"] #probably should be better : set shift to 0 when out of index.
        self.shift = 0

    def get_input(self, user_input):
        self.user_input = user_input.upper()
        return self.user_input

    def rotor_move_right(self):
        self.shift += 1
        for i in range(len(self.index_finder)):
            if self.index_finder[i] == self.user_input:
                return self.index_finder[i+self.shift]

    def crypt_letter(self, letter):
        self.wiring = wiring
        return wiring[letter]

    def reflect(self, reflect):
        self.wiring = reflector_wiring
        try:
            return self.wiring[reflect]
        except:
            for i in self.wiring.keys():
                if reflect == self.wiring[i]:
                    return i

    def decrypt_letter(self, letter): #which is basically crypting it again.
        self.wiring = wiring
        reversed_wiring = {value:key for key, value in self.wiring.items()}
        return reversed_wiring[self.wiring[letter]]

test = Enigma()
def do_the_job(letter):
    get_it = letter
    user_input = test.get_input(get_it) # INPUT "A"

    ready_to_crypt = test.rotor_move_right()
    print("Shifted {shift} position.".format(shift=test.shift))

    crypted_letter = test.crypt_letter(ready_to_crypt)
    print("Encrypted from: {shifted} to: {crypted}".format(shifted=ready_to_crypt, crypted=crypted_letter))

    reflected_letter = test.reflect(ready_to_crypt)
    print("Reflected from: {ref_in} to: {ref_out}".format(ref_in =ready_to_crypt, ref_out=reflected_letter))


    lights_panel = test.decrypt_letter(reflected_letter)
    print("==== CRYPTED LETTER: {letter}".format(letter=lights_panel))

    return lights_panel
def display_output(letter_to_display):
    output_font.render_to(enigma, (205, 200), letter_to_display, white)

# ================
# SETTING UP PYGAME
# =================

pygame.init()
# Set up the window dimensions
display_width = 500
display_height = 800

# Setup the colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (169,169,169)
dark_gray = (70,70,70)
orange = (255, 160, 60)

enigma = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Enigma Simulator Lite')
enigma_font = pygame.freetype.Font("Arial Bold.ttf", 24)
output_font = pygame.freetype.Font("Arial Bold.ttf", 140)

run = True
while run:
    pygame.time.delay(200)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    enigma.fill(dark_gray)
    rows = enigmaKeyboard()
    rows.add_rows()

    enigma_font.render_to(enigma, (130, 700), "Press SPACE to reset.", white)
    pygame.display.update()

    #Keyboard PRESSED
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            a = enigmaKeyboard()
            a.add_key("A", orange, 150, 500)
            result = do_the_job("A")
            display_output(result)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_b:
            b = enigmaKeyboard()
            b.add_key("B", orange, 250, 500)
            result = do_the_job("B")
            display_output(result)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_c:
            c = enigmaKeyboard()
            c.add_key("C", orange, 350, 500)
            result = do_the_job("C")
            display_output(result)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d:
            d = enigmaKeyboard()
            d.add_key("D", orange, 150, 600)
            result = do_the_job("D")
            display_output(result)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_e:
            e = enigmaKeyboard()
            e.add_key("E", orange, 250, 600)
            result = do_the_job("E")
            display_output(result)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_f:
            f = enigmaKeyboard()
            f.add_key("F", orange, 350, 600)
            result = do_the_job("F")
            display_output(result)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            test.shift = 0
            print("==== SET SHIFT TO 0 ====")

    pygame.display.update()

pygame.quit()
