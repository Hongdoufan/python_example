def cli_std_2d(var, mon, cmap_cli, clim_cli, cmap_std, clim_std, plot_dir):
    import numpy as np
    import matplotlib.pyplot as plt
    from netCDF4 import Dataset
    import sys
    import pyicon as pyic
    import xarray as xr
    import glob

    # Base directory containing all datasets
    base_dir = "/work/bm1313/b383127/epoc-icon-2024.10/experiments/epoc2_010/work/"

    # Glob pattern to match only specific month datasets
    file_pattern = f"{base_dir}run_*"+mon+"01T000000-*/epoc2_010_oce_2d_1mth_mean_*.nc"

    # Find all matching files
    file_paths = glob.glob(file_pattern)

    # Open multiple datasets and extract only the 'mlotst' variable
    ds = xr.open_mfdataset(file_paths, combine='by_coords')[[var]]

    cli = np.mean(ds[var], axis=0)
    cli.pyic.plot(cmap=cmap_cli, clim=clim_cli, lon_reg=(-90, 10), lat_reg=(30, 80))
    plt.savefig(plot_dir + var + "_" + mon + "_cli.png")
    print("plots saved")

    std = np.std(ds[var], axis=0)
    std.pyic.plot(cmap=cmap_std, clim=clim_std, lon_reg=(-90, 10), lat_reg=(30, 80))
    plt.savefig(plot_dir + var + "_" + mon + "_std.png")
    print("plots saved")
    return 

