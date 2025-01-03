
#%%
import src.cli_std as cli_std
import src.md_generator_cli as md_generator_cli

var = "mlotst"
mon = "03"  # specific month
cmap_cli='Blues'
clim_cli=(0,800)
cmap_std='OrRd'
clim_std=(0,400)
md_file_name = "../docs/source/" + var + "_cli.md"  # change here if the path not right
md_title = "EPOC-ICON"

#%%
plot_dir = "../docs/source/plots/"  # change here if path is not right
plot_dir_m = "./plots/"  

cli_std.cli_std_2d(var, mon, cmap_cli, clim_cli, cmap_std, clim_std, plot_dir)
#%%

md_file = md_generator_cli.doc_quick_plots(md_file_name, md_title, plot_dir_m, var, mon)

print("markdown files can be found in the docs-source-.markdown.md")

#%%

