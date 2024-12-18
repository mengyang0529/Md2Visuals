# Md2Visuals:Markdown to PPTX Mind Map Generator

This project leverages the `python-pptx` library to create PowerPoint presentations with mind maps based on input from Markdown-formatted documents. It streamlines the process of converting structured text into visually engaging slides.

## Features

- **Markdown Input**: Use simple Markdown syntax to define the structure of your mind map.
- **Automated PPTX Creation**: Generate PowerPoint presentations programmatically with `python-pptx`.
- **Hierarchical Mind Map**: Convert Markdown headers and lists into a clear, hierarchical mind map.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mengyang0529/md2visuals.git
   cd md2visuals
   ```
   
## Usage

1. Create a Markdown file (e.g., `example.md`) with the desired content structure:
   - [timeline example](doc/timeline.md)
   - [treechart example](doc/treechart.md)

2. Run the script to generate the PowerPoint file:

   ```bash
   python demo.py -m treechart -s Style2 --input example.md --output output.pptx
   ```

3. Open the generated `output.pptx` file in PowerPoint to view your mind map.


## Dependencies

- Python 3.12+
- `python-pptx`

Install additional dependencies using:

```bash
pip install python-pptx
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- [python-pptx Documentation](https://python-pptx.readthedocs.io/)
- Markdown syntax inspiration from [CommonMark](https://commonmark.org/)

---

Feel free to reach out if you encounter any issues or have suggestions for improvements!