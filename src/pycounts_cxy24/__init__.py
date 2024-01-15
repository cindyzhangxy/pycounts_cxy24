# read version from installed package
from importlib.metadata import version
__version__ = version("pycounts_cxy24")

# populate package namespace
from pycounts_cxy24.pycounts_cxy24 import count_words
from pycounts_cxy24.plotting import plot_words