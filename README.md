# pyskel_bc

A skeleton of a Python package with CLI and test suite included. Taken from
[pyskel](https://github.com/mapbox/pyskel) and modified slightly for quickstarting British Columbia python packages as per BC's [guide](https://github.com/bcgov/BC-Policy-Framework-For-GitHub/tree/master/BC-Gov-Org-HowTo).

![pyskel](https://farm4.staticflickr.com/3951/15672691531_3037819613_o_d.png)

## Customization quick start

To use pyskel_bc as the start of a new project, do the following, preferably in
a virtual environment. Clone the repo.

```
    git clone https://github.com/smnorris/pyskel_bc myproject
    cd myproject
```

Replace all occurrences of 'pyskel_bc' with the name of your own project.
(Note: the commands below require bash, find, and sed and are yet tested only on OS X.)

```
    if [ -d pyskel_bc ]; then find . -not -path './.git*' -type f -exec sed -i '' -e 's/pyskel_bc/myproject/g' {} + ; fi
    mv pyskel_bc myproject
```

Then install in locally editable (``-e``) mode and run the tests.

```
    pip install -e .[test]
    py.test
```

Finally, give the command line program a try.

```
    myproject --help
    myproject 4
```

To help prevent uncustomized forks of pyskel_bc from being uploaded to PyPI,
the setup's upload command is configured to dry run. Make sure to remove this
configuration from
[setup.cfg](https://docs.python.org/2/install/index.html#inst-config-syntax)
when you customize pyskel_bc.

A [post on the Mapbox blog](https://www.mapbox.com/blog/pyskel) has more
information about this project.

## See also

Here are a few other tools for initializing Python projects:

- Paste Script's [paster create](http://pythonpaste.org/script/#paster-create) 
- [cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) is
a Cookiecutter template for a Python package. Cookiecutter supports many languages, includes Travis configuration and much more.


## Requirements

## Installation

## Project Status

## Goals/Roadmap

## Getting Help or Reporting an Issue

## How to Contribute

## License

    Copyright 2016 Province of British Columbia

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at 

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
