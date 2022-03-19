from argparse import ArgumentError
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
                self.grid[i][j].north = self.getCell(i-1, j)
                self.grid[i][j].east = self.getCell(i, j+1)
                self.grid[i][j].south = self.getCell(i+1, j)
                self.grid[i][j].west = self.getCell(i, j-1)

    def getCell(self, row: int, column: int) -> Union[Cell, None]:
        if row < 0 or row >= self.rows:
            return None
        if column < 0 or column >= self.columns:
            return None
        return self.grid[row][column]