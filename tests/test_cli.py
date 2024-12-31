import src.cli_std as cli_std
import src.md_generator_cli as md_generator_cli

def test_func():
    x,y = cli_std.cli_std_2d()
    
print("plots saved")


def t_func():
    x,y = md_generator_cli.doc_quick_plots()

print("plots")