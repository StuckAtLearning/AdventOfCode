STRAIGHT_DIRECTION_OPERATION_LOOKUP = {'n': (0, 1), 's': (0, -1), 'w': (-1, 0), 'e': (1, 0)}
DIAGONAL_DIRECTION_OPERATION_LOOKUP = STRAIGHT_DIRECTION_OPERATION_LOOKUP \
    .update({'nw': (-1, 1), 'ne': (1, 1), 'sw': (-1, -1), 'se': (1, -1)})


class GridHandler:
    def __init__(self, parsed_grid: dict[str, set[tuple[int, int]]], outer_frame_thickness: int = 0):
        self.grid = parsed_grid
        self.boundary_thickness = outer_frame_thickness
        self.coord_look_up = self.convert_grid_to_coord_look_up()

    def __str__(self) -> str:
        output = '\n'.join([
            ''.join(
                next(marker for marker, coords in self.grid.items() if (x, y) in coords)
                for x in range(self.get_left_boundary(), self.get_right_boundary() + 1)
            ) for y in range(self.get_top_boundary(), self.get_bottom_boundary() + 1)
        ])

        return output

    def get_left_boundary(self) -> int:
        min_x = min(x for x, _ in self.grid.values()) + self.boundary_thickness
        return min_x

    def get_right_boundary(self) -> int:
        max_x = max(x for x, _ in self.grid.values()) - self.boundary_thickness
        return max_x

    def get_top_boundary(self) -> int:
        min_y = min(y for _, y in self.grid.values()) + self.boundary_thickness
        return min_y

    def get_bottom_boundary(self) -> int:
        max_y = max(y for _, y in self.grid.values()) - self.boundary_thickness
        return max_y

    def get_height(self) -> int:
        return self.get_bottom_boundary() - self.get_top_boundary()

    def get_width(self) -> int:
        return self.get_right_boundary() - self.get_left_boundary()

    @staticmethod
    def move_coord(current_coord: tuple[int, int], step: tuple[int, int]) -> tuple[int, int]:
        return current_coord[0] + step[0], current_coord[1] + step[1]

    # def get_markers(self) -> set[str]:
    #     return set(self.grid.keys())

    def convert_grid_to_coord_look_up(self) -> dict[tuple[int, int], str]:
        coord_look_up = dict()
        for marker, coords in self.grid.items():
            for coord in coords:
                coord_look_up[coord] = marker
        return coord_look_up

    # def convert_coord_look_up_to_grid(self) -> dict[str, set[tuple[int, int]]]:
    #     grid = {marker: set() for marker in self.get_markers()}
    #     for coord, marker in self.coord_look_up.items():
    #         grid[marker].add(coord)
    #     return grid

    def within_boundary(self, current_coord: tuple[int, int]) -> bool:
        return (self.get_left_boundary() <= current_coord[0] <= self.get_right_boundary()) \
               and (self.get_top_boundary() <= current_coord[1] <= self.get_bottom_boundary())

    def get_neighbours(self, current_coord: tuple[int, int], diagonal: bool = False) -> dict[str, tuple[int, int]]:
        neighbours = dict()
        direction_operation = DIAGONAL_DIRECTION_OPERATION_LOOKUP if diagonal else STRAIGHT_DIRECTION_OPERATION_LOOKUP
        for direction, operation in direction_operation:
            neighbour = self.move_coord(current_coord, operation)
            if self.within_boundary(neighbour):
                neighbours[direction] = neighbour
        return neighbours

    def get_neighbours_marker(self, current_coord: tuple[int, int], diagonal: bool = False) -> \
            dict[str, tuple[tuple[int, int], str]]:
        neighbours_marker = dict()
        swapped_grid = self.convert_grid_to_coord_look_up()
        neighbours = self.get_neighbours(current_coord, diagonal)
        for direction, coord in neighbours:
            marker = swapped_grid[coord]
            neighbours_marker[direction] = (coord, marker)
        return neighbours_marker

    def get_surrounding_grid(self, direction: str, height: int, width: int):
        return None
