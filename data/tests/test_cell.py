from data.cell import Cell


def test_create_cell():
    cell = Cell(1, 2)
    assert cell.row == 1
    assert cell.column == 2
    assert len(cell.links) == 0
    assert cell.north == None
    assert cell.east == None
    assert cell.south == None
    assert cell.west == None
    assert cell.id != None

def test_cell_link():
    cell1 = Cell(1, 2)
    cell2 = Cell(1, 1)
    assert cell1.id != cell2.id
    assert len(cell1.links) == 0
    assert len(cell2.links) == 0
    cell1.link(cell2)
    assert len(cell1.links) == 1
    assert len(cell2.links) == 1
    assert cell1.links[cell2]
    assert cell2.links[cell1]

def test_cell_unlink():
    cell1 = Cell(1, 2)
    cell2 = Cell(1, 1)
    cell1.link(cell2)
    assert cell1.links[cell2]
    assert cell2.links[cell1]
    cell1.unlink(cell2)
    assert len(cell1.links) == 0
    assert len(cell2.links) == 0
    assert cell2 not in cell1.links
    assert cell1 not in cell2.links

def test_cell_all_links():
    cell1 = Cell(1, 2)
    cell2 = Cell(1, 1)
    cell3 = Cell(1, 3)
    cell1.link(cell2)
    cell1.link(cell3)
    all_cell1_links = cell1.all_links()
    assert len(all_cell1_links) == 2
    assert cell2 in all_cell1_links
    assert cell3 in all_cell1_links

def test_cell_is_linked():
    cell1 = Cell(1, 2)
    cell2 = Cell(1, 1)
    cell1.link(cell2)
    assert cell1.is_linked(cell2)
    assert cell2.is_linked(cell1)
    cell2.unlink(cell1)
    assert not cell1.is_linked(cell2)
    assert not cell2.is_linked(cell1)

def test_cell_neighbours():
    cell = Cell(1, 2)
    cell_north = Cell(0, 2)
    cell_east = Cell(1, 3)
    cell_west = Cell(1, 1)
    cell_south = Cell(2, 2)
    cell.north = cell_north
    cell.east = cell_east
    cell.south = cell_south
    cell.west = cell_west
    cell_neighbours = cell.neighbours()
    assert len(cell_neighbours) == 4
    assert cell_north in cell_neighbours
    assert cell_east in cell_neighbours
    assert cell_south in cell_neighbours
    assert cell_west in cell_neighbours

def test_cell_neighbours_where_not_all_neighbours():
    cell = Cell(1, 2)
    cell_north = Cell(0, 2)
    cell_east = Cell(1, 3)
    cell_west = Cell(1, 1)
    cell.north = cell_north
    cell.east = cell_east
    cell.west = cell_west
    cell_neighbours = cell.neighbours()
    assert len(cell_neighbours) == 3
    assert cell_north in cell_neighbours
    assert cell_east in cell_neighbours
    assert cell_west in cell_neighbours
