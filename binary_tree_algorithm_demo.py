from algorithm.binary_tree_algorithm import BinaryTreeAlgorithm
from data.grid import Grid
from exporter.ascii_exporter import ASCIIExporter


grid = Grid(4, 4)
algorithm = BinaryTreeAlgorithm()
algorithm.on(grid)
ASCIIExporter.export_to_file(grid, 'out/binary_tree.txt')