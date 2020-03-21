[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](http://www.gnu.org/licenses/lgpl-3.0)
[![Build Status](https://travis-ci.org/GRAAL-Research/poutyne-callbacks.svg?branch=master)](https://travis-ci.org/GRAAL-Research/poutyne-callbacks)

## Here is Poutyne-callbacks.

[Poutyne](https://poutyne.org/) is a Keras-like framework for [PyTorch](https://pytorch.org/) and handles much of the boilerplating code needed to train neural networks. One of the key element of Poutyne is the used of callback in the training or testing loop.
Instead of always rewriting logic in our training loop, Poutyne is using many logging callback to handle some of the unfriendly coding step to train a neural networks. But, one can need other kind of callback, suck a handler for MLFlow logging or pushing update notification to yourself or a team. 
This package include usefull callback for Poutyne.

Read the documentation at XX.

Poutyne-callbacks  is compatible with  the __latest version of PyTorch__ ,  __Python >= 3.5__ and __Poutyne__.

### Cite
```
@misc{poutyne-callbacks,
    author = {Beauchemin, David},
    title  = {{Poutyne-callbacks: A callbacks utilities for Poutyne}},
    year   = {2020},
    note   = {\url{https://graal-research.github.io/poutyne-callbacks/}}
}
```


------------------

## Installation

Before installing Poutyne-callbacks, you must have the latest version of [PyTorch](https://pytorch.org/) in your environment and the latest version of [Poutyne](https://poutyne.org/).

- **Install the stable version of Poutyne-callbacks:**

```sh
pip install poutyne-callback
```

- **Install the latest development version of Poutyne-callbacks:**

```sh
pip install -U git+https://github.com/GRAAL-Research/poutyne-callbacks.git@dev
```


------------------

## Examples
> new example with new callbacks

------------------

## Contributing to Poutyne-callbacks

We welcome user input, whether it is regarding bugs found in the library or feature propositions ! Make sure to have a look at our [contributing guidelines](https://github.com/GRAAL-Research/poutyne-callbacks/blob/master/CONTRIBUTING.md) for more details on this matter.

------------------

## License

Poutyne-callbacks is LGPLv3 licensed, as found in the [LICENSE file](https://github.com/GRAAL-Research/poutyne-callbacks/blob/master/LICENSE).

------------------
