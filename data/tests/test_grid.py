from data.grid import Grid

def test_create_grid():
    grid = Grid(3, 3)
    assert grid.rows == 3
    assert grid.columns == 3
    assert len(grid.grid) == 3
    assert len(grid.grid[0]) == 3
    assert grid.get_cell(0,0).north == None
    assert grid.get_cell(0,0).east == grid.get_cell(0,1)
    assert grid.get_cell(0,0).south == grid.get_cell(1,0)
    assert grid.get_cell(0,0).west == None
    assert grid.get_cell(1,1).north == grid.get_cell(0,1)
    assert grid.get_cell(1,1).east == grid.get_cell(1,2)
    assert grid.get_cell(1,1).south == grid.get_cell(2,1)
    assert grid.get_cell(1,1).west == grid.get_cell(1,0)

def test_grid_random_cell():
    grid = Grid(5, 5)
    assert grid.random_cell() != None

def test_grid_size():
    grid = Grid(5, 5)
    assert grid.size() == 25
    grid = Grid(3, 7)
    assert grid.size() == 21

def test_each_cell():
    grid = Grid(3, 3)
    cells = grid.each_cell()
    assert len(cells) == 9
    for i in range(3):
        for j in range(3):
            assert grid.get_cell(i, j) in cells
