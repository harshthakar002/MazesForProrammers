from argparse import ArgumentError
from random import randint
from typing import Union
from data.cell import Cell


class Grid():

    def __init__(self, rows: int, columns: int) -> None:
        self.rows = rows
        self.columns = columns
        self.grid: list[list[Cell]] = []
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.columns):
                self.grid[i].append(Cell(i, j))
        for i in range(self.rows):
            for j in range(self.columns):
                self.grid[i][j].north = self.get_cell(i-1, j)
                self.grid[i][j].east = self.get_cell(i, j+1)
                self.grid[i][j].south = self.get_cell(i+1, j)
                self.grid[i][j].west = self.get_cell(i, j-1)

    def get_cell(self, row: int, column: int) -> Union[Cell, None]:
        if row < 0 or row >= self.rows:
            return None
        if column < 0 or column >= self.columns:
            return None
        return self.grid[row][column]
    
    def random_cell(self) -> Cell:
        row = randint(0, self.rows - 1)
        column = randint(0, self.columns - 1)
        return self.get_cell(row, column)
    
    def size(self) -> int:
        return self.rows * self.columns
    
    def each_row(self) -> list[list[Cell]]:
        return self.grid
    
    def each_cell(self) -> list[Cell]:
        cells: list[Cell] = []
        for row in self.grid:
            for cell in row:
                cells.append(cell)
        return cells