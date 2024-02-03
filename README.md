# pycounts_cxy24
[![codecov](https://codecov.io/gh/cindyzhangxy/pycounts_cxy24/graph/badge.svg?token=BUZJMMYMR8)][![Python 3.12.0](https://img.shields.io/badge/python-3.12.0-blue.svg)][![Documentation Status](https://readthedocs.org/projects/pycounts-cxy24/badge/?version=latest)][![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active-green.svg)(https://www.repostatus.org/#active)] [![License: MIT](https://img.shields.io/badge/License-MIT-teal.svg)![version](https://img.shields.io/github/v/release/cindyzhangxy/pycount_cxy24)]

Calculate word counts in a text file

## Installation

```bash
$ pip install pycounts_cxy24
```

`pycounts` can be used to count words in a text file and plot results
as follows:

```python
from pycounts.pycounts import count_words
from pycounts.plotting import plot_words
import matplotlib.pyplot as plt

file_path = "test.txt"  # path to your file
counts = count_words(file_path)
fig = plot_words(counts, n=10)
plt.show()
```

## Usage

`pycounts` can be used to count words in a text file and plot results
as follows:

```python
from pycounts.pycounts import count_words
from pycounts.plotting import plot_words
import matplotlib.pyplot as plt

file_path = "test.txt"  # path to your file
counts = count_words(file_path)
fig = plot_words(counts, n=10)
plt.show()
```

## Contributing

Interested in contributing? Check out the contributing guidelines. 
Please note that this project is released with a Code of Conduct. 
By contributing to this project, you agree to abide by its terms.

## License

`pycounts` was created by Tomas Beuzen. It is licensed under the terms
of the MIT license.

## Credits

`pycounts` was created with 
[`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and 
the `py-pkgs-cookiecutter` 
[template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
