#!/usr/bin/env python3

def checkmate(board):
    if not isinstance(board, str) or not board.strip():
        print("Error")
        return

    lines = [line for line in board.splitlines() if line]
    n = len(lines)

    if n == 0 or any(len(line) != n for line in lines):
        print("Error")
        return

    kings = []
    for r in range(n):
        for c in range(n):
            if lines[r][c] == 'K':
                kings.append((r, c))

    if len(kings) != 1:
        print("Error")
        return

    kr, kc = kings[0]

    for dc in [-1, 1]:
        pr, pc = kr + 1, kc + dc
        if 0 <= pr < n and 0 <= pc < n:
            if lines[pr][pc] == 'P':
                print("Success")
                return

    straight_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in straight_directions:
        r, c = kr + dr, kc + dc
        while 0 <= r < n and 0 <= c < n:
            piece = lines[r][c]
            if piece in ('R', 'Q'):
                print("Success")
                return
            elif piece in ('P', 'B', 'K'):
                break
            r += dr
            c += dc

    diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in diagonal_directions:
        r, c = kr + dr, kc + dc
        while 0 <= r < n and 0 <= c < n:
            piece = lines[r][c]
            if piece in ('B', 'Q'):
                print("Success")
                return
            elif piece in ('P', 'R', 'K'):
                break
            r += dr
            c += dc

    print("Fail")
    
