from treechart.basics import *
from core.geometry import *
from treechart.classic_shapes import *
from treechart.optimize import *

class ApplyLayout:
    def __init__(self):
        self.placed_nodes = {}  # Already placed nodes and their status

    def resolve_overlaps(self):
        """Check and resolve all box overlaps"""
        resolve_cross_level1_overlaps(self.placed_nodes,DETAIL_SPACING, 0, "horizontal")
        resolve_within_level1_overlaps(self.placed_nodes, 0, DETAIL_BOX_HEIGHT + DETAIL_SPACING, "horizontal")

    def layout_node(self, node, x, y):
        """Recursively layout according to node level"""
        if node.level == 0:
            w, h = MAIN_TOPIC_BOX_WIDTH, MAIN_TOPIC_BOX_HEIGHT
        elif node.level == 1:
            w, h = SUB_TOPIC_BOX_WIDTH, SUB_TOPIC_BOX_HEIGHT
        else:
            w, h = DETAIL_BOX_WIDTH, DETAIL_BOX_HEIGHT

        node.shape = Box(x, y, w, h)
        # Add this node to the placed list and initialize as unshifted
        self.placed_nodes[node.id] = {"node": node}

        if node.level == 0 and node.children:
            center_y = node.shape.center[1]
            current_x = node.shape.right + SPACING  # horizontal direction
            num_children = len(node.children)
            
            total_height = 0
            for i, c in enumerate(node.children):
                total_height += c.required_height

            start_y = center_y - total_height / 2
            current_y = start_y
            for i, c in enumerate(node.children):
                child_x = current_x
                child_y = current_y
                self.layout_node(c, child_x, child_y)
                current_y += c.required_height + SPACING

        elif node.level >= 1 and node.children:
            center_y = node.shape.center[1]
            current_x = node.shape.right + SPACING  # horizontal direction
            num_children = len(node.children)
            
            total_height = (num_children - 1) * DETAIL_SPACING + num_children * DETAIL_BOX_HEIGHT
            start_y = center_y - total_height / 2
             
            current_y = start_y
            for i, c in enumerate(node.children):
                child_x = current_x
                child_y = current_y
                self.layout_node(c, child_x, child_y)
                current_y += DETAIL_BOX_HEIGHT + DETAIL_SPACING

    def apply(self, root):
        """Main layout entry point"""
        rw, rh = MAIN_TOPIC_BOX_WIDTH, MAIN_TOPIC_BOX_HEIGHT
        root_x = LEFT_MARGIN
        root_y = (SLIDE_HEIGHT / 2) - (rh / 2)
        self.layout_node(root, root_x, root_y)

if __name__ == "__main__":
    pass
