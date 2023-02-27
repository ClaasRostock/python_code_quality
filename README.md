# python_code_quality
python_code_quality is an example package containing demo code for the
Python Code Quality talk.

## Development Setup

1. Install Python 3.9 or higher, i.e. [Python 3.9](https://www.python.org/downloads/release/python-3912/) or [Python 3.10](https://www.python.org/downloads/release/python-3104/)

2. Update pip and setuptools:

    ~~~sh
    $ python -m pip install --upgrade pip setuptools
    ~~~

3. git clone the python_code_quality repository into your local development directory:

    ~~~sh
    git clone https://github.com/ClaasRostock/python_code_quality path/to/your/dev/python_code_quality
    ~~~

4. In the python_code_quality root folder:

    Create a Python virtual environment:
    ~~~sh
    $ python -m venv .venv
    ~~~
    Activate the virtual environment: <br>
    ..on Windows:
    ~~~sh
    > .venv\Scripts\activate.bat
    ~~~
    ..on Linux:
    ~~~sh
    $ source .venv/bin/activate
    ~~~
    Update pip and setuptools:
    ~~~sh
    $ python -m pip install --upgrade pip setuptools
    ~~~
    Install python_code_quality's dependencies:
    ~~~sh
    $ pip install -r requirements-dev.txt
    ~~~

## Meta

Copyright (c) 2023 [Claas Rostock](https://github.com/ClaasRostock)

Claas Rostock – [@LinkedIn](https://www.linkedin.com/in/claasrostock/?locale=en_US) – claas.rostock@dnv.com

Distributed under the MIT license. See [LICENSE](LICENSE.md) for more information.

[https://github.com/ClaasRostock/python_code_quality](https://github.com/ClaasRostock/python_code_quality)

## Contributing

1. Fork it (<https://github.com/ClaasRostock/python_code_quality/fork>)
2. Create your branch (`git checkout -b myBranchName`)
3. Commit your changes (`git commit -am 'place your commit message here'`)
4. Push to the branch (`git push origin myBranchName`)
5. Create a new Pull Request

For your contribution, please make sure you follow the [STYLEGUIDE](STYLEGUIDE.md) before creating the Pull Request.

<!-- Markdown link & img dfn's -->
[python_code_quality_docs]: https://github.com/ClaasRostock/python_code_quality/README.html
