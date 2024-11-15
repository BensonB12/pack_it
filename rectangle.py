from cell import Cell


class Rectangle:
    def __init__(self, bottom_left_corner: Cell, top_right_corner: Cell):
        self._validate_corners(bottom_left_corner, top_right_corner)
        self.bottom_left_corner = bottom_left_corner
        self.top_right_corner = top_right_corner

    @staticmethod
    def _validate_corners(bl: Cell, tr: Cell):
        if bl.x >= tr.x or bl.y >= tr.y:
            raise ValueError("Area cannot be less than 1")

    def get_area(self) -> int:
        return (self.top_right_corner.x - self.bottom_left_corner.x) * (
            self.top_right_corner.y - self.bottom_left_corner.y
        )
