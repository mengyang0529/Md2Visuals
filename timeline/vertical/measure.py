from timeline.basics import *
from core.geometry import *

class MeasureLayout:
    def measure_node(self, node):
        # Determine basic size
        if node.level == 0:
            w, h = MAIN_TOPIC_BOX_WIDTH, MAIN_TOPIC_BOX_HEIGHT
        elif node.level == 1:
            w, h = SUB_TOPIC_BOX_WIDTH, SUB_TOPIC_BOX_HEIGHT
        else:
            w, h = DETAIL_BOX_WIDTH, DETAIL_BOX_HEIGHT
            
        node.required_width = w
        node.required_height = h
        
        if node.level == 0:
            if node.children:
                for i, c in enumerate(node.children):
                    c.is_direction = (i % 2 == 0)  # Even indexed child nodes are above, odd indexed are below
        elif node.level == 1:
            if node.children:
                for c in node.children:
                    c.is_direction = node.is_direction  # Child nodes inherit parent's is_direction attribute
        else:
            if node.children:
                for c in node.children:
                    c.is_direction = node.is_direction  # Child nodes inherit parent's is_direction attribute

        for c in node.children:
            c.parent = node
            self.measure_node(c)

    def measure(self, root):
        self.measure_node(root)
