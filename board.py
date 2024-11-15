from rectangle import Rectangle


class board:
    def __init__(self, size: int):
        self.width = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]

    def add_rectangle(self, rectangle: Rectangle):
        if self._rectangle_is_out_of_board(rectangle):
            raise ValueError("Rectangle has to fit in the board")
        # Check to see if the rectangle overlaps any '1's
        # Update the board

    def _rectangle_is_out_of_board(self, rectangle: Rectangle) -> bool:
        if (
            rectangle.bottom_left_corner.x < 0
            or rectangle.bottom_left_corner.y < 0
            or rectangle.top_right_corner.x >= self.width
            or rectangle.top_right_corner.y >= self.width
        ):
            return True
        return False