import src.data_generator as data_generator
import src.md_generator_cli as md_generator_cli

file_name = "../docs/source/note_example.md"  # change here if the path not right
plot_dir = "./plots/"             # change the dir if the path not right

try:
    md_file = md_generator.doc_quick_plots(file_name,title = "example note", plot_dir = plot_dir)
    print("markdown files can be found in the docs-source-note_example.markdown.md")
except FileNotFoundError:
    "plots not found, run `make_plot` first"

