from data.grid import Grid

def test_create_grid():
    grid = Grid(3, 3)
    assert grid.rows == 3
    assert grid.columns == 3
    assert len(grid.grid) == 3
    assert len(grid.grid[0]) == 3
    assert grid.getCell(0,0).north == None
    assert grid.getCell(0,0).east == grid.getCell(0,1)
    assert grid.getCell(0,0).south == grid.getCell(1,0)
    assert grid.getCell(0,0).west == None
    assert grid.getCell(1,1).north == grid.getCell(0,1)
    assert grid.getCell(1,1).east == grid.getCell(1,2)
    assert grid.getCell(1,1).south == grid.getCell(2,1)
    assert grid.getCell(1,1).west == grid.getCell(1,0)
