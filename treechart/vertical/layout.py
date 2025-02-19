from treechart.basics import *
from core.geometry import *
from treechart.classic_shapes import *
from treechart.vertical.measure import MeasureLayout
from treechart.vertical.apply import ApplyLayout
from treechart.vertical.lines import BuildLines

class Layout():
    def __init__(self):
        pass

    def collect_layout_boxes(self, node, layout_boxes):
        layout_boxes[node.id] = node.shape
        for child in node.children:
            self.collect_layout_boxes(child, layout_boxes)

    def create_layout(self, root_node):
        measure = MeasureLayout()
        root_node = measure.measure(root_node)

        layout = ApplyLayout()
        layout.apply(root_node)

        layout_boxes = {}
        self.collect_layout_boxes(root_node, layout_boxes)

        lines_builder = BuildLines()
        layout_lines = lines_builder.build(root_node)

        return layout_boxes, layout_lines

if __name__ == "__main__":
    pass
