### Hexlet tests and linter status:
<a href="https://codeclimate.com/github/MarfaNikitina/python-project-lvl3/maintainability"><img src="https://api.codeclimate.com/v1/badges/d260d37738fc862be73c/maintainability" /></a>
<a href="https://codeclimate.com/github/MarfaNikitina/python-project-lvl3/test_coverage"><img src="https://api.codeclimate.com/v1/badges/d260d37738fc862be73c/test_coverage" /></a>

[![Pytest check](https://github.com/MarfaNikitina/python-project-lvl3/actions/workflows/pytest-check.yml/badge.svg)](https://github.com/MarfaNikitina/python-project-lvl3/actions/workflows/pytest-check.yml)
[![linter check](https://github.com/MarfaNikitina/python-project-lvl3/actions/workflows/linter-check.yml/badge.svg)](https://github.com/MarfaNikitina/python-project-lvl3/actions/workflows/linter-check.yml)
[![Actions Status](https://github.com/MarfaNikitina/python-project-lvl3/workflows/hexlet-check/badge.svg)](https://github.com/MarfaNikitina/python-project-lvl3/actions)


<h1>Рage-loader</h1> - command line utility that downloads a page from the network and puts it in the specified existing directory (by default, in the program launch directory).
<h3>The program displays the full path to the downloaded file:</h3>

[![asciicast](https://asciinema.org/a/XAHVzpqKRHuDtGelgXOKa99aW.svg)](https://asciinema.org/a/XAHVzpqKRHuDtGelgXOKa99aW)

<h4>Also, the utility downloads the necessary resources from the page (images, css, js-files).</h4>

[![asciicast](https://asciinema.org/a/E6L5nrVldNNwRxdtitgpoFghH.svg)](https://asciinema.org/a/E6L5nrVldNNwRxdtitgpoFghH)

<h4>When erroneous arguments are passed to the load function, exceptions are raised and error messages are printed to the console</h4>

<h4>Non-existent writable directory:</h4>

[![asciicast](https://asciinema.org/a/FcDtunP2E25VQcDBnz4Ke2KQt.svg)](https://asciinema.org/a/FcDtunP2E25VQcDBnz4Ke2KQt)

<h4>Defunct web page:</h4>

[![asciicast](https://asciinema.org/a/lr5nf9tgPCnnBhbNOljvR3PKI.svg)](https://asciinema.org/a/lr5nf9tgPCnnBhbNOljvR3PKI)


<h3>Dependencies:</h3>
<ul>
<li>python = "^3.10"</li>
<li>requests = "^2.28.1"</li>
<li>pytest = "^7.1.3"</li>
<li>beautifulsoup4 = "^4.11.1"</li>
<li>progress="^1.6"</li>
</ul>

<h3>Installation</h3>
<ul>
<li>Before installing the package, you need to make sure that you have Python version 3.8 or higher installed: python3 --version.</li>
<li>Also, to work with the project, you need to have Poetry installed. </li>
<li>To work with the package, you need to clone the repository to your computer:<br>
# clone via HTTPS:<br>
>> https://github.com/MarfaNikitina/python-project-lvl3.git<br>
# clone via SSH:<br>
>> git clone git@github.com:MarfaNikitina/python-project-lvl3.git</li>

<li>You need to go to the project directory and install the package:<br><br>
>>> cd python-project-lvl3<br>
>>> poetry build<br>
>>> python3 -m pip install --user dist/*.whl </li>
<li>Use the command: <br>
>>> page-loader --output dir URL<br>
where 'dir' - is the directory where you want to save the downloaded resources<br>
and 'URL' - URL of the page you want to download</li>
</ul>










 

