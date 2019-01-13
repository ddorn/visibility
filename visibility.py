import _visibility


def point_to_cpp(x, y):
    return _visibility.vec2(x, y)

def segment_to_cpp(a, b):
    if not isinstance(a, _visibility.vec2):
        a = point_to_cpp(*a)
    if not isinstance(b, _visibility.vec2):
        b = point_to_cpp(*b)

    return _visibility.segment(a, b)

def segment_list_to_cpp(list_):
    return [segment_to_cpp(*s) if not isinstance(s, _visibility.segment) else s for s in list_]


def visible_polygon(point_of_view, segments):
    if not isinstance(point_of_view, _visibility.vec2):
        point_of_view = point_to_cpp(*point_of_view)
    segments = segment_list_to_cpp(segments)
    poly = _visibility.visible_polygon(point_of_view, segments)

    return [(p.x, p.y) for p in poly]


class VisibiltyCalculator:
    """This class is intened to calculate the visibility polygon from different points, but with the same obstacles"""

    def __init__(self, obstacles):
        self.obstacles = segment_list_to_cpp(obstacles)

    def visible_polygon(self, view_point):
        """
        Get the polygon visible from view_point

        :view_point: a (x, y) tuple
        :return: a list of (x, y) tuples in order to draw the polygon.
        """
        pos = _visibility.vec2(*view_point)
        return _visibility.visible_polygon(pos, self.obstacles)
