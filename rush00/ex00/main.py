#!/usr/bin/env python3
from checkmate import checkmate

def main():
    board = """\
nnQnn
nnnnn
nnnnn
nnnnn
nnKnn\
"""
    checkmate(board)

if __name__ == "__main__":
    main()
