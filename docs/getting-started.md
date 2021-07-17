---
title: Getting started
---

# Getting started

The Black Ox is a database migration assistant tool, when migrating databases to a new version, this tool is used to check for compatibility issues that may compromise database functionality as well as the database's performance. If you're familiar with Python, you
can install Black Ox with [`pip`][1], the Python package manager.

## Prerequisites

-   Install [git](https://git-scm.com/)
-   Install [Python](https://www.python.org/)

## Installation

### with pip

Black Ox can be installed with `pip`:

```
pip install black-ox
```

### with git

Black Ox can be directly used from [GitHub][3] by cloning the
repository into a subfolder of your project root which might be useful if you
want to use the very latest version:

1. Clone repository to your local

```
    $ git clone https://github.com/nawinto99/black-ox.git
```

1. Ensure [poetry](https://python-poetry.org/docs/) is installed, if not follow below.

```
    $ cd black-ox
    $ python -m pip install --upgrade pip
    $ pip install poetry
```

1. Install dependencies and start your virtualenv:

```
    $ poetry install
```

[1]: #with-pip-recommended
[3]: https://github.com/nawinto99/black-ox
