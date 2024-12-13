from timeline.timeline import Timeline
from treechart.treechart import TreeChart
import argparse
import importlib

def main(args):
    module_name = ".".join([args.module, args.module])
    class_dict = {"timeline": "Timeline", "treechart": "TreeChart"}  # Dictionary of available classes
    class_name = class_dict[args.module]
    style_name = args.style  # Get the style name from arguments

    # Dynamically import the module
    try:
        module = importlib.import_module(module_name)  # Import the module
        cls = getattr(module, class_name)  # Get the class from the module   
        style_method = getattr(cls, style_name)  # Get the style method (e.g., Style1)
        instance = style_method(args.input)  # Use style method to instantiate
        instance.save_ppt(args.output)

    except (ImportError, AttributeError) as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate a PowerPoint presentation from a Markdown file.")
    parser.add_argument('--module', '-m', required=True, help="The module containing the class.")
    parser.add_argument('--style', '-s', required=True, help="Style name (e.g., Style1).")
    parser.add_argument('--input', '-i', required=True, help="Input file.")
    parser.add_argument('--output', '-o', required=True, help="Path to save the generated PPTX file.")
    args = parser.parse_args()
    main(args)
