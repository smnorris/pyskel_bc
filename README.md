# pyskel_bc

A skeleton of a Python package with CLI and test suite included. Taken from
[pyskel](https://github.com/mapbox/pyskel) and modified slightly for quickstarting British Columbia python packages as per BC's [guide](https://github.com/bcgov/BC-Policy-Framework-For-GitHub/tree/master/BC-Gov-Org-HowTo).


## Customization quick start

To use pyskel_bc as the start of a new project, do the following, **preferably in a virtual environment**.  

Clone the repo:

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

Install in locally editable (``-e``) mode and run the tests:

```
    pip install -e .[test]
    py.test
```

Give the command line program a try:

```
    myproject --help
    myproject 4
```

Test with [tox](https://tox.readthedocs.io/en/latest/) if you are supporting multiple versions of Python:

```
    tox
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


## Development and testing on BC GTS

1. Open a windows command prompt and ensure that ArcGIS Python and scripts are inlcuded in the PATH. If a 64bit ArcGIS Python is available, use it:  

    ```
    set PATH="E:\sw_nt\Python27\ArcGISx6410.3";"E:\sw_nt\Python27\ArcGISx6410.3\Scripts";%PATH%
    ```

2. Ensure [pip](https://pypi.python.org/pypi/pip) is available, [install](https://pip.pypa.io/en/stable/installing/) if it is not (to your workspace, not the system Python).

3. Create and enable a [virtualenv](https://virtualenv.pypa.io/en/stable) for testing/development so we don't have to worry about conflicting with system installed python packages:

    ```
    pip install virtualenv   # (if necessary)  
    mkdir myproject_env
    virtualenv myproject_env
    myproject_env\Scripts\activate
    ```

4. If ArcGIS/arcpy is required by the module, ensure we can reach the arcpy module from the virtualenv (based on this [USGS guide](https://my.usgs.gov/confluence/display/cdi/Calling+arcpy+from+an+external+virtual+Python+environment)) by creating a file `Lib\site-packages\ArcGIS.pth` within the virtual environment folder. Include these lines (or similar, check for required 32 bit paths by starting ArcMap and typing `import sys; print sys.path` into the python window):
    ```
    # ArcGIS.pth
    # Path to ArcGIS arcpy modules
    # Place in folder ...\<path to your virtual environment>\lib\site-packages\
            
    E:\\sw_nt\\Python27\\ArcGISx6410.3
    E:\\sw_nt\\Python27\\ArcGISx6410.3\\Lib
    E:\\sw_nt\\Python27\\ArcGISx6410.3\\DLLs
    E:\\sw_nt\\Python27\\ArcGISx6410.3\\Lib\\lib-tk
    E:\\sw_nt\\Python27\\ArcGISx6410.3\\lib\\site-packages
    E:\\sw_nt\\Python27\\ArcGISx6410.3\\lib\\site-packages\\win32
    E:\\sw_nt\\Python27\\ArcGISx6410.3\\lib\\site-packages\\win32\\lib
    E:\\sw_nt\\Python27\\ArcGISx6410.3\\lib\\site-packages\\Pythonwin
    E:\\sw_nt\\ArcGIS\\Desktop10.3\\bin64
    E:\\sw_nt\\ArcGIS\\Desktop10.3\\ArcPy
    E:\\sw_nt\\ArcGIS\\Desktop10.3\\ArcToolBox\\Scripts

    ```

5. Clone the repository: `git clone https://github.com/smnorris/pyskel_bc.git` 

6. Back at the windows command prompt:
    ```
    cd myproject
    pip install -e .[test]
    ```

7. If required, activate the virtualenv within an ArcGIS session by issuing this command from the ArcGIS python window ([as per this question on StackOverflow](https://gis.stackexchange.com/questions/7333/running-arcgis-10-0-under-virtualenv)):
    ```
    execfile(r'<path_to_env>\Scripts\activate_this.py', {'__file__': r'<path_to_env>\Scripts\activate_this.py'})
    import myproject
    ```


## License

    Copyright 2018 Province of British Columbia

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at 

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
