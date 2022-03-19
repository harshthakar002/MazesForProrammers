from __future__ import annotations
from uuid import uuid4


class Cell():

    def __init__(self, row: int, column: int) -> None:
        self.id = uuid4().int
        self.row = row
        self.column = column
        self.north: Cell = None
        self.east: Cell = None
        self.south: Cell = None
        self.west: Cell = None
        self.links: dict[Cell, bool] = {}

    def __hash__(self) -> int:
        return self.id
    
    def link(self, cell: Cell, bidi: bool = True) -> None:
        self.links[cell] = True
        if bidi:
            cell.link(self, False)
    
    def unlink(self, cell: Cell, bidi: bool = True) -> None:
        del self.links[cell]
        if bidi:
            cell.unlink(self, False)
    
    def all_links(self) -> list[Cell]:
        return self.links.keys()

    def is_linked(self, cell: Cell) -> bool:
        return cell in self.links and self.links[cell]
    
    def neighbours(self) -> list[Cell]:
        adjacent_cells: list[Cell] = []
        if self.north != None:
            adjacent_cells.append(self.north)
        if self.east != None:
            adjacent_cells.append(self.east)
        if self.south != None:
            adjacent_cells.append(self.south)
        if self.west != None:
            adjacent_cells.append(self.west)
        return adjacent_cells
    
    def __eq__(self, cell: Cell | None) -> bool:
        return cell != None and self.id == cell.id and self.row == cell.row and self.column == cell.column