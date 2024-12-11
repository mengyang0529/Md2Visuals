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
        if not node.children:
            return
        if node.level == 0:
            current_y = node.shape.bottom + SPACING  # vertical direction
            center_x = node.shape.center[0]
            num_children = len(node.children)
            
            total_width = sum(c.required_width + SPACING for c in node.children) - SPACING
            start_x = center_x - total_width/2  
            current_x = start_x
            for i, c in enumerate(node.children):
                child_x = current_x + c.required_width / 2 - SUB_TOPIC_BOX_WIDTH / 2
                child_y = current_y
                self.layout_node(c, child_x, child_y)
                current_x += c.required_width + SPACING 
        else:
            current_y = node.shape.bottom + SPACING  # vertical direction
            center_x = node.shape.center[0]
            num_children = len(node.children)
            
            total_width = (num_children - 1) * DETAIL_SPACING + num_children * DETAIL_BOX_WIDTH
            start_x = center_x - total_width / 2 
             
            current_x = start_x
            for i, c in enumerate(node.children):
                child_x = current_x
                child_y = current_y
                self.layout_node(c, child_x, child_y)
                current_x += DETAIL_BOX_WIDTH + DETAIL_SPACING

    def apply(self, root):
        """Main layout entry point"""
        rw, rh = MAIN_TOPIC_BOX_WIDTH, MAIN_TOPIC_BOX_HEIGHT
        root_x = (SLIDE_WIDTH / 2) - (rw / 2)
        root_y = TOP_MARGIN
        self.layout_node(root, root_x, root_y)

if __name__ == "__main__":
    pass
