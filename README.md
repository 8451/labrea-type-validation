# Labrea Test
Utilities for testing code written with [labrea](https://github.com/8451/labrea)

![](https://img.shields.io/badge/version-0.0.1-blue.svg)
[![lifecycle](https://img.shields.io/badge/lifecycle-stable-green.svg)](https://www.tidyverse.org/lifecycle/#stable)
[![PyPI Downloads](https://img.shields.io/pypi/dm/labrea-test.svg?label=PyPI%20downloads)](https://pypi.org/project/labrea-test/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Coverage](https://raw.githubusercontent.com/8451/labrea-test/meta/coverage/coverage.svg)](https://github.com/8451/labrea-test/tree/meta/coverage)
[![docs](https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat)](https://8451.github.io/labrea-test)

## Installation
Labrea is available for install via pip.

```bash
pip install labrea-test
````

Alternatively, you can install the latest development version from GitHub.

```bash
pip install git+https://github.com/8451/labrea-test@develop
```

## Usage

During testing, you may want to mock a certain dataset (or other `Evaluatable`) to known value.
This can be done using the `labrea_test.Mock` context manager, which ensures that at the end
of the block, any mocking is torn down.

```python
import labrea_test
from labrea import dataset


@dataset
def foo() -> str:
    return "foo"


def test_foo():
    with labrea_test.Mock() as mock:
        mock(foo, "bar")
        assert foo() == "bar"

    assert foo() == "foo"
```

`Mock` can be used to mock any `Evaluatable` object, and can take a plain value or another
`Evaluatable` object as the value to mock to.

```python
@dataset
def bar() -> str:
    return "bar"


def test_foo():
    with labrea_test.Mock() as mock:
        mock(foo, bar)
        assert foo() == "bar"

    assert foo() == "foo"
```

## Contributing
If you would like to contribute to **labrea-test**, please read the
[Contributing Guide](docs/source/contributing.md).

## Changelog
A summary of recent updates to **labrea-test** can be found in the
[Changelog](docs/source/changelog.md).

## Maintainers

| Maintainer                                                | Email                    |
|-----------------------------------------------------------|--------------------------|
| [Austin Warner](https://github.com/austinwarner-8451)     | austin.warner@8451.com   |
| [Michael Stoepel](https://github.com/michaelstoepel-8451) | michael.stoepel@8451.com |

## Links
- Report a bug or request a feature: https://github.com/8451/labrea-test/issues/new/choose
- Documentation: https://8451.github.io/labrea-test
