from random import choice
from data.cell import Cell
from data.grid import Grid


class BinaryTreeAlgorithm():

    def on(self, grid: Grid) -> None:
        for cell in grid.each_cell():
            neighbours: list[Cell] = []
            if cell.north != None:
                neighbours.append(cell.north)
            if cell.east != None:
                neighbours.append(cell.east)
            if len(neighbours) == 0:
                continue
            cell.link(choice(neighbours))