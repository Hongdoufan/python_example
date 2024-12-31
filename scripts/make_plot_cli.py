
#%%
import src.cli_std as cli_std
import src.md_generator_cli as md_generator_cli

var = "mlotst"
mon = "01"  # specific month
cmap_cli='Blues'
clim_cli=(0,400)
cmap_std='OrRd'
clim_std=(0,200)
md_file_name = "../docs/source/note_cli.md"  # change here if the path not right
md_title = "cli"

#%%
plot_dir = "../docs/source/plots/"  # change here if path is not right
plot_dir_m = "./plots/"  

cli_std.cli_std_2d(var, mon, cmap_cli, clim_cli, cmap_std, clim_std, plot_dir)
#%%
md_title = "cli"
md_file = md_generator_cli.doc_quick_plots(md_file_name, md_title, plot_dir_m, var, mon)

print("markdown files can be found in the docs-source-note_example.markdown.md")

#%%

