import pygame
import connect4
import sys
import math


def main():
    def start_game():
        font = pygame.font.SysFont("monospace", 75)
        label = font.render("Start Game", 1, black)
        button_rect = label.get_rect(center=(width / 2, height / 2))
        pygame.draw.rect(screen, yellow, button_rect, border_radius=10)
        screen.blit(label, button_rect)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        return

    def draw_board(board):
        for c in range(connect4.column_count):
            for r in range(connect4.row_count):
                pygame.draw.rect(screen, blue, (c * squaresize, r * squaresize + squaresize, squaresize, squaresize))
                pygame.draw.circle(screen, black, (
                    int(c * squaresize + squaresize / 2), int(r * squaresize + squaresize + squaresize / 2)), radius)

        for c in range(connect4.column_count):
            for r in range(connect4.row_count):
                if board[r][c] == 1:
                    pygame.draw.circle(screen, red, (
                        int(c * squaresize + squaresize / 2), height - int(r * squaresize + squaresize / 2)), radius)
                elif board[r][c] == 2:
                    pygame.draw.circle(screen, yellow, (
                        int(c * squaresize + squaresize / 2), height - int(r * squaresize + squaresize / 2)), radius)

        pygame.display.update()

    red = (186, 66, 58)
    blue = (95, 130, 194)
    black = (0, 0, 0)
    yellow = (207, 190, 107)

    board = connect4.create_board()
    game_over = False
    turn = 0

    pygame.init()

    squaresize = 100

    width = connect4.column_count * squaresize
    height = (connect4.row_count + 1) * squaresize

    size = (width, height)
    radius = int(squaresize / 2 - 5)

    screen = pygame.display.set_mode(size)

    start_game()

    draw_board(board)
    pygame.display.set_caption('Connect 4!')
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)

    # Window loop
    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, black, (0, 0, width, squaresize))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, red, (posx, int(squaresize / 2)), radius)
                else:
                    pygame.draw.circle(screen, yellow, (posx, int(squaresize / 2)), radius)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, black, (0, 0, width, squaresize))
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx / squaresize))

                    if connect4.is_valid_location(board, col):
                        row = connect4.get_next_open_row(board, col)
                        connect4.drop_piece(board, row, col, 1)

                        if connect4.check_for_win(board, 1):
                            label = myfont.render('Player 1 wins!', 1, red)
                            screen.blit(label, (40, 10))
                            game_over = True

                else:
                    posx = event.pos[0]
                    col = int(math.floor(posx / squaresize))

                    if connect4.is_valid_location(board, col):
                        row = connect4.get_next_open_row(board, col)
                        connect4.drop_piece(board, row, col, 2)

                        if connect4.check_for_win(board, 2):
                            label = myfont.render('Player 2 wins!', 1, yellow)
                            screen.blit(label, (40, 10))
                            game_over = True

                draw_board(board)

                turn += 1
                turn = turn % 2

                if game_over:
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                # Reset game state
                                pygame.draw.rect(screen, black, (0, 0, width, squaresize))
                                start_game()
                                board = connect4.create_board()
                                game_over = False
                                turn = 0
                                draw_board(board)
                                pygame.display.update()
                                break
                        else:
                            continue
                        break
                    pygame.time.wait(3000)


if __name__ == '__main__':
    main()

