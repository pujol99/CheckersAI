def game_loop(screen, human_turn, inv, depth_max):
    # LOGIC DOORS
    running = True
    human_turn_copy = human_turn
    first_clik = False
    select_time = False
    hint_time = False
    # SELECTION LISTS
    kill_sel = []
    orign_sel = []
    end_sel = []
    last_sel = []
    # CREATE LOCAL COPIES OF BOARD
    board = make_copy(BOARD)
    prev_board = [make_copy(BOARD)]
    # LOCAL VARIABLES
    xC, yC = 0, 0
    txC, tyC = 0, 0

    if human_turn:
        moves = calculate_moves(HUMAN, board)
    # LOOP
    while running:
        # PROCESS EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                keep_playing = False
            if event.type == pygame.MOUSEBUTTONUP:
                xC, yC = pygame.mouse.get_pos()
                txC, tyC = xC, yC
        # UPDATE VALUES AND CONDITIONS
        if human_turn:
            # Check if PREV button was hitten
            if txC > 100 and txC < 150 and tyC > 450 and tyC < 500 and len(prev_board) > 1:
                hint_time = False
                select_time = True
                # Board is last saved version of itself and reload moves
                board = make_copy(prev_board.pop())

                moves = calculate_moves(HUMAN, board)
                # Reset variables
                xC, yC = 0, 0
                txC, tyC = 0, 0
                # Clear previous selections
                clear_selections([kill_sel, end_sel, orign_sel, last_sel])

            # Check if HINT button was hitten
            if txC > 225 and txC < 275 and tyC > 450 and tyC < 500:
                hint_time = True
                select_time = True
                # Get best move for this board copy
                copy = make_copy(board)
                move = minimax(copy, depth_max, -infinity, +infinity, HUMAN)
                ix, iy, x, y, to_kill, score = move
                # Reset variables
                xC, yC = 0, 0
                txC, tyC = 0, 0
                # Clear everything to show only best origin and end move
                clear_selections([kill_sel, end_sel, orign_sel, last_sel])
                orign_sel.append((ix, iy))
                end_sel.append((x, y))

            # Check if AGAIN button was hitten
            if txC > 350 and txC < 400 and tyC > 450 and tyC < 500:
                hint_time = False
                select_time = True
                human_turn = human_turn_copy
                # Board is last saved version of itself and reload moves
                board = make_copy(BOARD)
                prev_board = [make_copy(BOARD)]

                moves = calculate_moves(HUMAN, board)
                # Reset variables
                xC, yC = 0, 0
                txC, tyC = 0, 0
                # Clear previous selections
                clear_selections([kill_sel, end_sel, orign_sel, last_sel])

            # Check if BOARD PIECE was hitten
            if xC > 50 and xC < 450 and yC > 50 and yC < 450:
                hint_time = False
                select_time = True
                # Get index of the click
                i, j = get_index_click(xC, yC)
                # Check if OWN PIECE was hitten
                if board[j][i].value is HUMAN:
                    clear_selections([kill_sel, end_sel, orign_sel, last_sel])
                    ix, iy = 0, 0
                    for move in moves:
                        orig, kills, fin = move
                        if (i, j) == orig:
                            ix, iy = i, j
                            if (ix, iy) not in orign_sel:
                                orign_sel.append((ix, iy))
                            for kill in kills:
                                if kill not in kill_sel:
                                    kill_sel.append(kill)
                            if fin not in end_sel:
                                end_sel.append(fin)
                            first_clik = True
                            select_time = True
                # Check if BLANK PIECE was hitten and origin is decided
                elif board[j][i].value == 0 and first_clik:
                    for move in moves:
                        orig, kills, fin = move
                        if ((ix, iy), (i, j)) == (orig, fin):
                            prev_board.append(make_copy(board))
                            make_move(board, ix, iy, i, j, kills, HUMAN)
                            prev = 1
                            human_turn = False
                            # Check if game is over
                            if game_over(board):
                                running = False
                            xC, yC = 0, 0
                    first_clik = False
                    select_time = False
                    clear_selections([kill_sel, end_sel, orign_sel])
                # Check if ANY PIECE was hitten
                else:
                    # Reset origin decision and select posible moves
                    first_clik = False
                    if not hint_time:
                        for move in moves:
                            if move[0] not in orign_sel:
                                orign_sel.append(move[0])
            else:
                select_time = True
                # Reset origin decision and select posible moves
                first_clik = False
                if not hint_time:
                    for move in moves:
                        if move[0] not in orign_sel:
                            orign_sel.append(move[0])
        # Computer turn
        else:
            # Check if game is over
            if game_over(board):
                running = False
            else:
                # Calculate the best move for this state and make move
                copy = make_copy(board)
                move = minimax(copy, depth_max, -infinity, +infinity, COMP)
                ix, iy, x, y, to_kill, score = move
                make_move(board, ix, iy, x, y, to_kill, COMP)
                last_sel.append((ix, iy))
                # Reset moves for human
                moves = calculate_moves(HUMAN, board)
                human_turn = True
                # Check if game is over
                if game_over(board):
                    running = False
                time.sleep(0.5)

        # DRAW
        screen.fill(DARK_BLUE)
        screen.blit(BOARD_IMG, (50, 50))
        if select_time:
            select_pieces(screen, orign_sel, board, SELECTED_ORIGN)
            select_pieces(screen, end_sel, board, SELECTED_END)
            select_pieces(screen, last_sel, board, LAST)
            select_pieces(screen, kill_sel, board, SELECTED_KILL)
        if not human_turn:
            text(screen, 20, 'Thinking...', DARK_BLUE, WHITE, 250, 25)
        draw_pieces(screen, inv, board)
        screen.blit(PREV, (100, 450))
        screen.blit(HINT, (225, 450))
        screen.blit(AGAIN, (350, 450))
        pygame.display.flip()