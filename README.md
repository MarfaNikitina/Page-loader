### Hexlet tests and linter status:
<a href="https://codeclimate.com/github/MarfaNikitina/python-project-lvl3/maintainability"><img src="https://api.codeclimate.com/v1/badges/d260d37738fc862be73c/maintainability" /></a>
<a href="https://codeclimate.com/github/MarfaNikitina/python-project-lvl3/test_coverage"><img src="https://api.codeclimate.com/v1/badges/d260d37738fc862be73c/test_coverage" /></a>

[![Pytest check](https://github.com/MarfaNikitina/python-project-lvl3/actions/workflows/pytest-check.yml/badge.svg)](https://github.com/MarfaNikitina/python-project-lvl3/actions/workflows/pytest-check.yml)
[![linter check](https://github.com/MarfaNikitina/python-project-lvl3/actions/workflows/linter-check.yml/badge.svg)](https://github.com/MarfaNikitina/python-project-lvl3/actions/workflows/linter-check.yml)
[![Actions Status](https://github.com/MarfaNikitina/python-project-lvl3/workflows/hexlet-check/badge.svg)](https://github.com/MarfaNikitina/python-project-lvl3/actions)


<h1>Рage-loader</h1> - command line utility that downloads a page from the network and puts it in the specified existing directory (by default, in the program launch directory).
<h3>The program displays the full path to the downloaded file:</h3>

[![asciicast](https://asciinema.org/a/XAHVzpqKRHuDtGelgXOKa99aW.svg)](https://asciinema.org/a/XAHVzpqKRHuDtGelgXOKa99aW)

<h3>Also, the utility downloads the necessary resources from the page (images, css, js-files).</h3>

[![asciicast](https://asciinema.org/a/E6L5nrVldNNwRxdtitgpoFghH.svg)](https://asciinema.org/a/E6L5nrVldNNwRxdtitgpoFghH)

<h3>When erroneous arguments are passed to the load function, exceptions are raised and error messages are printed to the console</h3>

<h3>Non-existent writable directory:</h3>

[![asciicast](https://asciinema.org/a/FcDtunP2E25VQcDBnz4Ke2KQt.svg)](https://asciinema.org/a/FcDtunP2E25VQcDBnz4Ke2KQt)

<h3>Defunct web page:</h3>

[![asciicast](https://asciinema.org/a/lr5nf9tgPCnnBhbNOljvR3PKI.svg)](https://asciinema.org/a/lr5nf9tgPCnnBhbNOljvR3PKI)


<h4>Dependencies:</h4>
<ul>
<li>python = "^3.10"</li>
<li>requests = "^2.28.1"</li>
<li>pytest = "^7.1.3"</li>
<li>beautifulsoup4 = "^4.11.1"</li>
<li>progress="^1.6"</li>
</ul>

<h4>Installation</h4>
<ul>
<ol>Before installing the package, you need to make sure that you have Python version 3.8 or higher installed: python3 --version.</ol>
<ol>Also, to work with the project, you need to have Poetry installed. </ol>
<ol>To work with the package, you need to clone the repository to your computer:
# clone via HTTPS:
>> https://github.com/MarfaNikitina/python-project-lvl3.git
# clone via SSH:
>> git clone git@github.com:MarfaNikitina/python-project-lvl3.git</ol>

<ol>You need to go to the project directory and install the package:
>>> cd python-project-lvl3
>>> poetry build
>>> python3 -m pip install --user dist/*.whl </ol>
<ol>Use the command: 
>>> page-loader --output dir URL
where 'dir' - is the directory where you want to save the downloaded resources
and 'URL' - URL of the page you want to download</ol>
</ul>










 

