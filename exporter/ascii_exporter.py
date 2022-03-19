from data.cell import Cell
from data.grid import Grid


class ASCIIExporter():

    @staticmethod
    def export(grid: Grid) -> str:
        output = '+' + ('---+' * grid.columns) + '\n'
        for row in grid.each_row():
            top = '|'
            bottom = '+'
            for cell in row:
                if cell == None:
                    cell = Cell(-1, -1)
                body = '   '
                east_boundary = '|'
                if cell.is_linked(cell.east):
                    east_boundary = ' '
                top = top + body + east_boundary
                south_boundary = '---'
                if cell.is_linked(cell.south):
                    south_boundary = '   '
                corner = '+'
                bottom = bottom + south_boundary + corner
            output = output + top + '\n' + bottom + '\n'
        return output
    
    @staticmethod
    def export_to_file(grid: Grid, filename: str) -> None:
        ascii_str = ASCIIExporter.export(grid)
        with open(filename, 'w') as output_file:
            output_file.write(ascii_str)