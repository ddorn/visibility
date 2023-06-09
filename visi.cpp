#include "visibility.hpp"
#include <stdio.h>

using namespace geometry;

std::vector<vec2> visible_polygon (vec2 xy, segmentList segments)
{
    auto poly = visibility_polygon(xy, segments.begin(), segments.end());

	return poly;
}
