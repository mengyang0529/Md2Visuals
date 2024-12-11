from treechart.basics import *
from core.geometry import *
from treechart.classic_shapes import *

class BuildLines:
    def __init__(self):
        self.layout_lines = {}
    
    def update_lines(self, node, pt1, pt2):
        if node.id not in self.layout_lines:
            self.layout_lines[node.id] = []
        self.layout_lines[node.id].append((pt1, pt2))

    def handle_level_0_lines(self, node):
        self.update_lines(node, Point(0,0), Point(0,0))

    def handle_more_level_lines(self, node):
        parent = node.parent
        
        pt1 = Point(parent.shape.center[0], parent.shape.bottom)
        pt2 = Point(parent.shape.center[0], parent.shape.bottom + SPACING/2)
        self.update_lines(node, pt1, pt2)

        pt3 = Point(node.shape.center[0], parent.shape.bottom + SPACING/2)
        pt4 = Point(node.shape.center[0], node.shape.top)
        self.update_lines(node, pt3, pt4)

        pt5 = pt2
        pt6 = pt3
        self.update_lines(node, pt5, pt6)

    def build_node_lines(self, node):
        if node.level == 0:
            self.handle_level_0_lines(node)
        else:
            self.handle_more_level_lines(node)

        for c in node.children:
            self.build_node_lines(c)

    def build(self, root):
        self.build_node_lines(root)
        return self.layout_lines


if __name__ == "__main__":
    pass