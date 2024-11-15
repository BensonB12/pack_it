import pytest
from cell import Cell
from rectangle import Rectangle


@pytest.mark.parametrize(
    "bottom_left, top_right",
    [
        # Backwards corners
        (Cell(x=4, y=4), Cell(x=2, y=2)),
        (Cell(x=0, y=2), Cell(x=2, y=2)),
        (Cell(x=2, y=0), Cell(x=2, y=2)),
        # Area is 0
        (Cell(x=2, y=2), Cell(x=2, y=0)),
        (Cell(x=2, y=2), Cell(x=0, y=2)),
    ],
)
def test_invalid_rectangle(bottom_left, top_right):
    with pytest.raises(ValueError, match="Area cannot be less than 1"):
        Rectangle(bottom_left, top_right)
