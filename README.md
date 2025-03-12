# Labrea Type Validation
Type validation for [labrea](https://github.com/8451/labrea) using [pydantic](https://docs.pydantic.dev/latest/)

![](https://img.shields.io/badge/version-0.0.1-blue.svg)
[![lifecycle](https://img.shields.io/badge/lifecycle-stable-green.svg)](https://www.tidyverse.org/lifecycle/#stable)
[![PyPI Downloads](https://img.shields.io/pypi/dm/labrea-type-validation.svg?label=PyPI%20downloads)](https://pypi.org/project/labrea-type-validation/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Coverage](https://raw.githubusercontent.com/8451/labrea-type-validation/meta/coverage/coverage.svg)](https://github.com/8451/labrea-type-validation/tree/meta/coverage)
[![docs](https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat)](https://8451.github.io/labrea-type-validation)

## Installation
`labrea-type-validation` is available for install via pip.

```bash
pip install labrea-type-validation
````

Alternatively, you can install the latest development version from GitHub.

```bash
pip install git+https://github.com/8451/labrea-type-validation@develop
```

## Usage

When creating an `Option` with labrea, specify the expected type using either of the following syntaxes:

```python
from labrea import Option

X = Option("X", type=int)
Y = Option[int]("Y")
```

Either literal types or type hints can be used, such as `List[int]` or `Union[str, List[str]]`.

To enable type validation, simply import `labrea_type_validation` and call the `enable` function:

```python
import labrea_type_validation

X({"X": "1"})  # No error

labrea_type_validation.enable()

X({"X": "1"})
# ...
# TypeError: Expected type <class 'int'> but got <class 'str'> ('1')
#
# The above exception was the direct cause of the following exception:
#
# Traceback (most recent call last):
# ...
# labrea.exceptions.EvaluationError: Originating in Option('X') | Error during evaluation
```

Type validation can also be used in a `with` statement as a context manager using `enabled`.

```python
with labrea_type_validation.enabled():
    X({"X": "1"})
# ...
# TypeError: Expected type <class 'int'> but got <class 'str'> ('1')
#
# The above exception was the direct cause of the following exception:
#
# Traceback (most recent call last):
# ...
# labrea.exceptions.EvaluationError: Originating in Option('X') | Error during evaluation
```

Alternatively, the `LABREA_TYPE_VALIDATION_ENABLED` environment variable can be set to `TRUE`.

## Multithreaded Applications

Type validation is based on the `labrea.runtime` module. For this reason, type validation is
enabled for the current thread and any threads spawned from it. If you are using a multithreaded
application, ensure that type validation is enabled in the main thread before spawning any new
threads.

## Contributing
If you would like to contribute to **labrea-type-validation**, please read the
[Contributing Guide](docs/source/contributing.md).

## Changelog
A summary of recent updates to **labrea-type-validation** can be found in the
[Changelog](docs/source/changelog.md).

## Maintainers

| Maintainer                                                | Email                    |
|-----------------------------------------------------------|--------------------------|
| [Austin Warner](https://github.com/austinwarner-8451)     | austin.warner@8451.com   |
| [Michael Stoepel](https://github.com/michaelstoepel-8451) | michael.stoepel@8451.com |

## Links
- Report a bug or request a feature: https://github.com/8451/labrea-type-validation/issues/new/choose
- Documentation: https://8451.github.io/labrea-type-validation
