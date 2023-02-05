[use]: https://github.com/Andre601/mkdocs-template/generate

[MkDocs]: https://www.mkdocs.org/

[squidfunk]: https://github.com/squidfunk
[MkDocs Material Theme]: https://github.com/squidfunk/mkdocs-material

[facelessuser]: https://github.com/facelessuser
[PyMdown Extensions]: https://github.com/facelessuser/pymdown-extensions/

[Netlify]: https://netlify.com

[mkdocs.yml]: https://github.com/Andre601/mkdocs-template/blob/master/mkdocs.yml
[docs folder]: https://github.com/Andre601/mkdocs-template/blob/master/docs
[workflow]: https://github.com/Andre601/mkdocs-template/blob/master/.github/workflows/deploy.yml

[LICENSE]: https://github.com/Andre601/mkdocs-template/blob/master/LICENSE

[gh-pages]: https://docs.github.com/en/free-pro-team@latest/github/working-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

# MkDocs Material Template
This is a template repository for anyone that wants to use the MkDocs Material Theme.

## Getting Started
To get started, first clone this template by clicking on the Green button labeled [`Use this template`][use].  
On the new screen, give your repository a name and make sure to check `Include all branches`. This will make sure that the `gh-pages` branch is included, or otherwhise publishing the docs to GitHub Pages could cause errors (See [Troubleshooting](#troubleshooting)).

> **Note**  
> GitHub changed how you define from where it takes the pages to build. You are now able to define both a branch and a specific folder from where GitHub would take the files to then deploy them on GitHub Pages.  
> You can read more about this [here][gh-pages].

### Creating pages
To create new pages, just add new markdown files to the [docs folder] of the repository and edit them.  
MkDocs will then turn those into static HTML pages once you [build](#build-pages) or [deploy](#deploy-to-github) the pages.

The template also has some pre-made settings for your convenience to help you with creating documentation much easier.  
In the [mkdocs.yml] will you find many settings that you can alter. Please check the comments and the links they have for more info.

It also contains some extensions that might be useful including:

- Admonition
- CodeHilite
- ToC
- [PyMdown Extensions]

You're free to add, edit or remove any extension at your own discretion, but keep in mind that some expansions might cause compatibility issues with others or require to be downloaded first.  
For that, alter the `requirements.txt` if you also deploy pages using GitHub Actions or [Netlify](#netlify)

## Build Pages
To build pages (locally) can you use the `mkdocs build` command in your prefered command prompt.  
Note that for the successful execution of this command you have to...

- ...be in the folder that contains the `mkdocs.yml`
- ...have Python 3.7 installed
- ...have MkDocs and all required dependencies such as Material for MkDocs installed.  
Note that Material for MkDocs automatically downloads MkDocs and also certain extensions such as the [PyMdown Extensions].

MkDocs would now build the HTML in the defined configuration folder for you to use.

## Deploy to GitHub
If you want to publish the pages on GitHub Pages can you use the [premade workflow][workflow] for this.  
This workflow will setup Python, download Material for MkDocs and all its dependencies and deploy the pages to the `gh-pages` branch to then be viewable under `<username>.github.io/<repository>` (unless you defined a specific CNAME through a CNAME file in the [docs folder]).

Note that in order for this to work will you need to have a `gh-pages` branch already made.

## Netlify
Netlify is an amazing service to build and deploy pages. This template comes with a `runtime.txt` which is used by Netlify to determine the Python version used (They use an old version of Python... Don't ask why).

For more information, please check out their website.

## Dependabot
The repository contains a `dependabot.yml` file inside the `.github` folder which allows automatic updates through GitHub's Dependabot.  
It is configured to target both Python dependencies (inside the `requirements.txt`) and GitHub Actions dependencies, to make sure bot are updated accordingly.

Note that it is configured by default to add the `Type: Update (Dependency)` label and also the `Target: Python (pip)` label for Python and `Target: GitHub Actions` label for GitHub Actions Dependencies.  
Those labels don't exist by default so you have to either create them, or alter the ones in the dependabot.yml (You can also just remove the `labels` sections).

## Troubleshooting
> **The deploy action gives me an error when deploying. What is the issue?**

There can be many issues but the most common ones are that you either don't have a `gh-pages` branch set or that the `requirements.txt` file is missing or its content is invalid.

> **Can I alter the overall style of the pages?**

Yes. Material for MkDocs supports Theme extensions, meaning you can override specific parts of a theme by providing the particular file in a folder and defining this folder as the `custom_dir` one in the [mkdocs.yml].  
This template ships with a `theme` folder that can be used for that and you can just uncomment the aforementioned line in the YAML file.


## Credits
A big thank you goes to the following people/groups:

- [MkDocs] for providing the software, to generate documentation.
- [squidfunk] for the [MkDocs Material Theme].
- [facelessuser] for the [PyMdown Extensions].

## License
This template is served under the MIT license.  
Read the [LICENSE] file for more info.

# Python Project Template

This project follows the Python Standards declared in [PEP 621](https://peps.python.org/pep-0621/).
This uses a pyproject.yaml to configuration the project. In this example, [flit](https://pypi.org/project/flit/) is used to simplify the build process, and publish to pypi.

## Project Organization

- .devcontainer - This directory contains required files for creating a [Codespace](https://github.com/features/codespaces).
- .github
  - workflows - Contains GitHub Actions used for building, testing and publishing.
    - publish-test.yml - Publish wheels to [https://test.pypi.org/](https://test.pypi.org/)
    - publish.yml - Publish wheels to [https://pypi.org/](https://pypi.org/)
    - pull-request.yml - Build and Test pull requests before commiting to main.
    - template-sync.yml - Update GitHub Repo with enhancments to base template
- docs - collect documents (default format .md)
- src - place new source code here
  - python_package - sample package (this can be deleted when creating a new repository)
- tests - contains Python based test cases to validate src code
- .pre-commit-config.yaml - Contains various pre-check fixes for Python
- .templateversionrc - used to track template version usage.
- MANIFEST.in - Declares additional files to include in Python whl
- pyproject.toml - Python Project Declaration
- ws.code-workspace - Recommended configurations for [Visual Studio Code](https://code.visualstudio.com/)

## pyproject.toml

The following sections are defined in the configuration toml.

- build-system
- project
  - optional-dependencies
  - urls
- tool
  - bandit
  - coverage
    - run
    - report
  - pyright
  - pytest
  - tox
  - pylint
    - MESSAGES CONTROL
    - REPORTS
    - REFACTORING
    - BASIC
    - FORMAT
    - LOGGING
    - MISCELLANEOUS
    - SIMILARITIES
    - SPELLING
    - STRING
    - TYPECHECK
    - VARIABLES
    - CLASSES
    - DESIGN
    - IMPORTS
    - EXCEPTIONS

### build-system
TODO: add info on flit configuration

### project
This section defines the project metadata, which may have been previously contained in a setup.py file.

#### optional-dependencies
This are otpimal dependancey groups that can be installed via 'pip install .[tests]'.
One group is included for dependancies required for testing. A second group is included for PySpark based dependancies.

### tool
This section defines the configurations for additional tools used to format, lint, type-check, and analysis Python code.

#### bandit
Performs Security Static Analysis checks on code base.

#### black
Auto-formats code

#### coverage
Configures code coverage reports generatated during testing.

#### pyright
Performs static type checking on Python.

#### pytest
Configures various test markers used during testing.

#### pylint
Performs Linting and Static Analysis. Any modifictions made by the auto-formater (black) are always considered correct.

## Publish to PyPi from GitHub
In order to publish to PyPi, a repostirory secret must be created, "PYPI_PASSWORD". In order to publish to the Test PyPi, a second secret must be added, "TEST_PYPI_PASSWORD". 


## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.

