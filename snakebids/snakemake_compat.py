# type: ignore

try:
    from snakemake.cli import main
    from snakemake.common import configfile
    from snakemake.common.configfile import load_configfile
except ImportError:
    import snakemake.io as configfile
    from snakemake import main
    from snakemake.io import load_configfile

from snakemake.exceptions import WildcardError
from snakemake.io import expand
from snakemake.script import Snakemake

__all__ = [
    "load_configfile",
    "main",
    "expand",
    "Snakemake",
    "WildcardError",
    "configfile",
]
