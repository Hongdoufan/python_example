from mdutils.mdutils import MdUtils

#%%
def doc_quick_plots(file_name, title, plot_dir, var, mon):
    """
    function to generate the markdown file
    **Parameter**
        *file_name* the name of the markdown file you are gonna make.
        *title* the title in the markdown file.
        *plot_dir* the directory for the images that gonna include in the note.
    """
    md_file = MdUtils(file_name, title="")  # qick plots
    md_file.new_header(level = 1, title = title)

    # overview
    md_file.new_header(level=2, title="Introduction")
    md_file.new_paragraph("Climatology and Standard Deviation of " + var + " in month " + mon + " are shown below.")

    md_file.new_header(level = 2, title = var + "_month" + mon + "_climitalogy")
    md_file.new_line(
        md_file.new_inline_image(
            text="red",
            path=plot_dir  + var + "_" + mon +  "_cli.png",
        )
    )

    md_file.new_header(level = 2, title = var + "_month" + mon + "_Standard Deviation")
    md_file.new_line(
        md_file.new_inline_image(
            text="green",
            path=plot_dir  + var + "_" + mon +  "_std.png",
        )
    )

    md_file.create_md_file()
# %%
