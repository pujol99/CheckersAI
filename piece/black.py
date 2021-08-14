from piece.piece import *


class Black(Piece):
    img = BROWN

    def posible_moves(self, bo, rec=False, x=None, y=None, kills=0, no_kill=True, tr=True, tl=True, dr=True, dl=True):
        """
            :param bo: recieves a game state
            :param rec: if a kill has been done we only look other kill movements (not queen)
            :param x, y: initial position
            :param kills: kill counter of current path
            :param no_kill: queen moves with no killing, they are the first ones to look
            :param tr, tl, dr, dl: check certain position or not
            :return: structure -> list of tuples: (end, kill, nkills)
        """
        # LOCAL VARIABLES
        value = self.value
        if value == -1:
            limity = 0
            limitxr = 7
            limitxl = 0
        else:
            limity = 7
            limitxr = 7
            limitxl = 0
        if x == None:
            x, y = self.x, self.y

        # NOT QUEEN
        if not self.queen:
            # (-1, -1) -> no kill
            # RIGHT
            if x < limitxr and y is not limity and not rec:
                if bo[y + value][x + 1] == 0:
                    self.moves.append(((x + 1, y + value), (-1, -1), kills))

            # LEFT
            if x > limitxl and y is not limity and not rec:
                if bo[y + value][x - 1] == 0:
                    self.moves.append(((x - 1, y + value), (-1, -1), kills))

            # RIGHT KILL
            if x < limitxr - 1 and y is not limity - value and y is not limity:
                if bo[y + value][x + 1] == -value and bo[y + value * 2][x + 2] == 0:
                    self.moves.append(((x + 2, y + value * 2), (x + 1, y + value), kills + 1))
                    self.posible_moves(bo, True, x + 2, y + value * 2, kills + 1)

            # LEFT KILL
            if x > limitxl + 1 and y is not limity - value and y is not limity:
                if bo[y + value][x - 1] == -value and bo[y + value * 2][x - 2] == 0:
                    self.moves.append(((x - 2, y + value * 2), (x - 1, y + value), kills + 1))
                    self.posible_moves(bo, True, x - 2, y + value * 2, kills + 1)

        # QUEEN
        else:
            # CHECK FIRST NO KILL MOVEMENTS
            if no_kill:
                # TOP RIGHT
                tx, ty = x, y
                # Check until find border
                while tx < 7 and ty > 0:
                    if bo[ty - 1][tx + 1] == 0:
                        self.moves.append(((tx + 1, ty - 1), (-1, -1), 0))
                    # Stop if find own piece or enemy piece
                    else:
                        break
                    # Next position
                    tx += 1
                    ty -= 1

                # TOP LEFT
                tx, ty = x, y
                # Check until find border
                while tx > 0 and ty > 0:
                    if bo[ty - 1][tx - 1] == 0:
                        self.moves.append(((tx - 1, ty - 1), (-1, -1), 0))
                    # Stop if find own piece or enemy piece
                    else:
                        break
                    # Next position
                    tx -= 1
                    ty -= 1
                # DOWN RIGHT
                tx, ty = x, y
                # Check until find border
                while tx < 7 and ty < 7:
                    if bo[ty + 1][tx + 1] == 0:
                        self.moves.append(((tx + 1, ty + 1), (-1, -1), 0))
                    else:
                        break
                    tx += 1
                    ty += 1
                # DOWN LEFT
                tx, ty = x, y
                while tx > 0 and ty < 7:
                    if bo[ty + 1][tx - 1] == 0:
                        self.moves.append(((tx - 1, ty + 1), (-1, -1), 0))
                    # Stop if find own piece or enemy piece
                    else:
                        break
                    # Next position
                    tx -= 1
                    ty += 1
                self.posible_moves(bo, True, x, y, 0, False, True, True, True, True)
            # Check for queen kill movements
            else:
                # TOP RIGHT KILL
                if self.toprk:
                    tx, ty = x, y
                    kill = 0
                    # While no border
                    while tx < 6 and ty > 1:
                        # If kill found
                        if bo[ty - 1][tx + 1] == -value and bo[ty - 2][tx + 2] == 0:
                            # Set params from kill end
                            ttx, tty = tx + 2, ty - 2
                            kill += 1
                            cont = -1
                            # From this point check right and left until find border
                            while ttx < 8 and tty > -1:
                                # obj is what we found until reach border
                                obj = bo[tty][ttx]
                                # If blank space add move and say which directions we will look now
                                if obj == 0:
                                    # Add move to moves
                                    self.moves.append(((ttx, tty), (ttx + cont, tty - cont), kills + kill))

                                    # New directions available
                                    self.toprk = False
                                    self.downlk = False
                                    self.downrk = True
                                    self.toplk = True

                                    # Make move in a copy board search from this new board and then reset board
                                    bo[tty - cont][ttx + cont] = 0
                                    copy = [row[:] for row in bo]
                                    self.posible_moves(copy, True, ttx, tty, kills + kill, False, False, True, True,
                                                       False)
                                    bo[tty - cont][ttx + cont] = -value

                                    # Remember original available directions
                                    self.toprk = tr
                                    self.downlk = dl
                                    self.downrk = dr
                                    self.toplk = tl

                                    # Update params
                                    cont -= 1
                                    ttx += 1
                                    tty -= 1
                                # If enemy break while and restart kill process
                                elif obj == -value:
                                    tx, ty = ttx - 1, tty + 1
                                    break
                                # If teammate end search
                                else:
                                    tx, ty = -3, -3
                                    break
                            # If after kill there are more blank spaces search right and left in them
                            if obj == 0:
                                tx += 1
                                ty -= 1
                        # If two enemies consec. break
                        elif bo[ty - 1][tx + 1] == -value and bo[ty - 2][tx + 2] == -value:
                            break
                        # If teammate break
                        elif bo[ty - 1][tx + 1] == value:
                            break
                        # If blank space go to the next one
                        else:
                            tx += 1
                            ty -= 1
                # TOP LEFT KILL
                if self.toplk:
                    tx, ty = x, y
                    kill = 0
                    # While no border
                    while tx > 1 and ty > 1:
                        # If kill found
                        if bo[ty - 1][tx - 1] == -value and bo[ty - 2][tx - 2] == 0:
                            # Set params from kill end
                            ttx, tty = tx - 2, ty - 2
                            kill += 1
                            cont = -1
                            # From this point check right and left until find border
                            while ttx > -1 and tty > -1:
                                # obj is what we found until reach border
                                obj = bo[tty][ttx]
                                # If blank space add move and say which directions we will look now
                                if obj == 0:
                                    # Add move to moves
                                    self.moves.append(((ttx, tty), (ttx - cont, tty - cont), kills + kill))

                                    # New directions available
                                    self.toplk = False
                                    self.downrk = False
                                    self.downlk = True
                                    self.toprk = True

                                    # Make move in a copy board search from this new board and then reset board
                                    bo[tty - cont][ttx - cont] = 0
                                    copy = [row[:] for row in bo]
                                    self.posible_moves(copy, True, ttx, tty, kills + kill, False, True, False, False,
                                                       True)
                                    bo[tty - cont][ttx - cont] = -value

                                    # Remember original available directions
                                    self.toprk = tr
                                    self.downlk = dl
                                    self.downrk = dr
                                    self.toplk = tl

                                    # Update params
                                    cont -= 1
                                    ttx -= 1
                                    tty -= 1
                                # If enemy break while and restart kill process
                                elif obj == -value:
                                    tx, ty = ttx + 1, tty + 1
                                    break
                                # If teammate end search
                                else:
                                    tx, ty = -3, -3
                                    break
                            # If after kill there are more blank spaces search right and left in them
                            if obj == 0:
                                tx -= 1
                                ty -= 1
                        # If two enemies consec. break
                        elif bo[ty - 1][tx - 1] == -value and bo[ty - 2][tx - 2] == -value:
                            break
                        # If teammate break
                        elif bo[ty - 1][tx - 1] == value:
                            break
                        # If blank space go to the next one
                        else:
                            tx -= 1
                            ty -= 1
                # DOWN RIGHT KILL
                if self.downrk:
                    tx, ty = x, y
                    kill = 0
                    # While no border
                    while tx < 6 and ty < 6:
                        # If kill found
                        if bo[ty + 1][tx + 1] == -value and bo[ty + 2][tx + 2] == 0:
                            # Set params from kill end
                            ttx, tty = tx + 2, ty + 2
                            kill += 1
                            cont = -1
                            # From this point check right and left until find border
                            while ttx < 8 and tty < 8:
                                # obj is what we found until reach border
                                obj = bo[tty][ttx]
                                # If blank space add move and say which directions we will look now
                                if obj == 0:
                                    # Add move to moves
                                    self.moves.append(((ttx, tty), (ttx + cont, tty + cont), kills + kill))

                                    # New directions available
                                    self.toprk = True
                                    self.downlk = True
                                    self.downrk = False
                                    self.toplk = False

                                    # Make move in a copy board search from this new board and then reset board
                                    bo[tty + cont][ttx + cont] = 0
                                    copy = [row[:] for row in bo]
                                    self.posible_moves(copy, True, ttx, tty, kills + kill, False, True, False, False,
                                                       True)
                                    bo[tty + cont][ttx + cont] = -value

                                    # Remember original available directions
                                    self.toprk = tr
                                    self.downlk = dl
                                    self.downrk = dr
                                    self.toplk = tl

                                    # Update params
                                    cont -= 1
                                    ttx += 1
                                    tty += 1
                                # If enemy break while and restart kill process
                                elif obj == -value:
                                    tx, ty = ttx - 1, tty - 1
                                    break
                                # If teammate end search
                                else:
                                    tx, ty = -3, -3
                                    break
                            # If after kill there are more blank spaces search right and left in them
                            if obj == 0:
                                tx += 1
                                ty += 1
                        # If two enemies consec. break
                        elif bo[ty + 1][tx + 1] == -value and bo[ty + 2][tx + 2] == -value:
                            break
                        # If teammate break
                        elif bo[ty + 1][tx + 1] == value:
                            break
                        # If blank space go to the next one
                        else:
                            tx += 1
                            ty += 1
                # DOWN LEFT KILL
                if self.downlk:
                    tx, ty = x, y
                    kill = 0
                    # While no border
                    while tx > 1 and ty < 6:
                        # If kill found
                        if bo[ty + 1][tx - 1] == -value and bo[ty + 2][tx - 2] == 0:
                            # Set params from kill end
                            ttx, tty = tx - 2, ty + 2
                            kill += 1
                            cont = -1
                            # From this point check right and left until find border
                            while ttx > -1 and tty < 8:
                                # obj is what we found until reach border
                                obj = bo[tty][ttx]
                                # If blank space add move and say which directions we will look now
                                if obj == 0:
                                    # Add move to moves
                                    self.moves.append(((ttx, tty), (ttx - cont, tty + cont), kills + kill))

                                    # New directions available
                                    self.toprk = False
                                    self.downlk = False
                                    self.downrk = True
                                    self.toplk = True

                                    # Make move in a copy board search from this new board and then reset board
                                    bo[tty + cont][ttx - cont] = 0
                                    copy = [row[:] for row in bo]
                                    self.posible_moves(copy, True, ttx, tty, kills + kill, False, False, True, True,
                                                       False)
                                    bo[tty + cont][ttx - cont] = -value

                                    # Remember original available directions
                                    self.toprk = tr
                                    self.downlk = dl
                                    self.downrk = dr
                                    self.toplk = tl

                                    # Update params
                                    cont -= 1
                                    ttx -= 1
                                    tty += 1
                                # If enemy break while and restart kill process
                                elif obj == -value:
                                    tx, ty = ttx + 1, tty - 1
                                    break
                                # If teammate end search
                                else:
                                    tx, ty = -3, -3
                                    break
                            # If after kill there are more blank spaces search right and left in them
                            if obj == 0:
                                tx -= 1
                                ty += 1
                        # If two enemies consec. break
                        elif bo[ty + 1][tx - 1] == -value and bo[ty + 2][tx - 2] == -value:
                            break
                        # If teammate break
                        elif bo[ty + 1][tx - 1] == value:
                            break
                        # If blank space go to the next one
                        else:
                            tx -= 1
                            ty += 1

