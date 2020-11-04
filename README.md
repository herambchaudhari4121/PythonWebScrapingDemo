# Scraping any URL with Requests and Beautiful Soup

- We will install the packages into a virtual environment
- Virtual Environment can be installed using the following command
- `pip install virtualenv`
- You can use `pip list` to review all installed packages
- Initialize a virtual environment folder called `env`
- `virtualenv env` - This creates a new `env` folder
- `ls -la env` lists content of the env folder
- `source env/bin/activate` Use this command to activate the virtual Environment
- Check using `which python` to see the python used is from the virtual Environment.

# Install requests and beautiful soup packages

- `pip install requests`
- `pip install bs4`
- `pip install lxml`

# Before you begin coding the Scraping jobs

- Study the DOM using chrome developer tools - inspect element.
- Identify the HTML tags which needs to be parsed
- Identify the CSS class which can help narrow the section to parse and collect the necessary information.

# Demo choices and important code snippets

```
links = soup.find('div', {'class': '_8tk7'}).findAll('a')
```

Reviewing facebook careers page, I was able to identify the pattern in which the job listing were stored. Following are snippets copied using the Chrome Developer Tools.

```
#search_result > div._8tk7
```

```
#search_result > div._8tk7 > a:nth-child(1)
```

# To run the webscraper_demo

```
python webscraper_demo.py
```
