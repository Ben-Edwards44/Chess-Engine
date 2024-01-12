import src.graphics.draw as draw
import src.graphics.input as input
import src.graphics.graphics_const as graphics_const

import pygame
from os import listdir


class Piece:
    def __init__(self, name, img_path, x, y):
        self.name = name
        self.img_path = img_path

        self.act_x = x
        self.act_y = y

        self.step_x = graphics_const.SCREEN_WIDTH // 8
        self.step_y = graphics_const.SCREEN_HEIGHT // 8

        self.img_width = self.step_x
        self.img_height = self.step_y

        self.draw_x, self.draw_y = self.get_draw_pos(x, y)

    def get_draw_pos(self, x, y): 
        #x and y are swapped because the array inxs are opposite to cartesian coords
        draw_x = y * self.step_y
        draw_y = x * self.step_x

        return draw_x, draw_y
    
    def overwrite_draw_pos(self, mouse_x, mouse_y):
        #ensure center of image goes to mouse pos
        offset_x = self.step_x // 2
        offset_y = self.step_y // 2

        self.draw_x = mouse_x - offset_x
        self.draw_y = mouse_y - offset_y


def init_graphics():
    global images
    global window

    pygame.init()
    pygame.display.set_caption("Chess Engine")

    window = pygame.display.set_mode((graphics_const.SCREEN_WIDTH, graphics_const.SCREEN_HEIGHT))
    images = get_images()


def get_images():
    images = []
    for i in ["white", "black"]:
        path = f"src/graphics/images/{i}"
        img_names = listdir(path)

        #images in form {name : path} e.g. {"queen" : "Images/White/queen.png"}
        images.append({x[:-4] : f"{path}\\{x}" for x in img_names})

    return images


def get_piece(value, x, y):
    #find colour
    if value > 6:
        is_white = False
        value -= 6
    else:
        is_white = True

    #get image
    name = graphics_const.PIECE_VALUES[value]
    img_dict = images[0] if is_white else images[1]
    img_path = img_dict[name]

    new_piece = Piece(name, img_path, x, y)

    return new_piece


def build_pieces(board):
    #return list of Piece objects with starting position and image path

    piece_list = []
    for x in range(8):
        for y in range(8):
            value = board[x][y]

            if value != 0:
                new_piece = get_piece(value, x, y)
                piece_list.append(new_piece)
            
    return piece_list


def draw_board(board):
    piece_list = build_pieces(board)
    draw.draw_board(window, piece_list)


def dragging_piece(board):
    x, y = pygame.mouse.get_pos()

    board[input.selected_piece.x][input.selected_piece.y] = 0

    selected = get_piece(input.selected_piece.piece_value, input.selected_piece.x, input.selected_piece.y)
    selected.overwrite_draw_pos(x, y)

    piece_list = build_pieces(board)
    piece_list.append(selected)

    draw.draw_board(window, piece_list)

    board[input.selected_piece.x][input.selected_piece.y] = input.selected_piece.piece_value


def graphics_loop(board):
    #loop until the player has made a move

    board_copy = [[i for i in x] for x in board]

    while True:
        window.fill((0, 0, 0))

        player_move = input.get_player_input(board_copy)

        if input.selected_piece == None:
            draw_board(player_move)
        else:
            #player has selected a piece
            dragging_piece(player_move)

        pygame.display.update()

        #has player has made move?
        if player_move != board:
            return player_move