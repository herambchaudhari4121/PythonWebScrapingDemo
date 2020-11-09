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

Facebook careers Page URL is `'https://www.facebook.com/careers/jobs/'`

Reviewing facebook careers page, I was able to identify the pattern in which the job listing were stored. Following are snippets copied using the Chrome Developer Tools.

```
#search_result > div._8tk7
```

```
#search_result > div._8tk7 > a:nth-child(1)
```

Leading to the following important code snippets

```
links = soup.find('div', {'class': '_8tk7'}).findAll('a')
```

- Using the links, iterate to extract the link text and URL.
- Place it in a dictionary.

```
def get_job_listing(url):
    req = requests.get(url)

    soup = BeautifulSoup(req.text, 'lxml')

    links = soup.find('div', {'class': '_8tk7'}).findAll('a')

    for link in links:
        job_details = dict()
        job_details['name'] = link.text
        job_details['href'] = link['href']
        print(job_details)
```

# To run the webscraper_demo

```
python webscraper_demo.py
```

# Example output of the demo

```
{'name': 'Engineering Manager - Malware Analysis InfrastructureMenlo Park, CASoftware EngineeringEngineering', 'href': '/careers/jobs/1035151026857199/'}
{'name': 'Research Intern, Artificial IntelligenceMontreal, CanadaInternship - PhDArtificial Intelligence', 'href': '/careers/jobs/615554365978704/'}
{'name': 'Full Stack Software Engineering ManagerLondon, United KingdomSoftware EngineeringEngineering', 'href': '/careers/jobs/2610480139072156/'}
{'name': 'Manager, HCM IntegrationsAustin, TX +1 moreInfrastructureIT', 'href': '/careers/jobs/200121818028842/'}
{'name': 'Director, Product Marketing, Workplace London, United KingdomProduct ManagementPartnerships', 'href': '/careers/jobs/295726081470260/'}
{'name': 'Data Engineer, Analytics (Family Ecosystems)Menlo Park, CA +1 moreData & Analytics+1 moreData Engineering', 'href': '/careers/jobs/3223521017874109/'}
{'name': 'Communications Manager, Monetization - LatamSão Paulo, BrazilCommunications & Public PolicyCorporate Communications', 'href': '/careers/jobs/1764302053725468/'}
{'name': 'Research Manager, Business Integrity - Authenticity Menlo Park, CA +1 moreResearchUser Experience', 'href': '/careers/jobs/630632180850801/'}
{'name': 'Manager, Market Operations, Burmese marketDublin, IrelandGlobal OperationsMarket Operations', 'href': '/careers/jobs/1125165764532430/'}
{'name': 'Manager, Software Engineering, CompilersMenlo Park, CAInfrastructureEngineering', 'href': '/careers/jobs/1147169172318394/'}
```

The extraction of minimum and preferred qualification output from a single URL would look like:

```
{ 'minimum': [ '8+ years of experience in organizational design, change '
               'management, leadership and development, or other relevant '
               'fields',
               'Experience developing rewards and incentives and leading '
               'culture change initiatives',
               'Experience working inside fast-moving companies/organizations',
               'Proven experience working collaboratively across a wide '
               'variety of functions to drive effective outcomes',
               'Communication skills and project management experience',
               'Experience with consensus-building',
               'Experience operating independently and execute flawlessly on '
               'both the strategic and operational level',
               'Experience working on a new team with ambiguity and changing '
               'responsibilities',
               'BA/BS Degree'],
  'preferred': [ 'Advanced degree preferred',
                 'Experience or expertise understanding the impacts of '
                 'technology',
                 'Working with technical and product teams',
                 'Experience representing companies externally and internally '
                 'at the executive level',
                 'Experience working in a globally matrixed organization '
                 'preferably in Technology',
                 'Experience working with a broad array of teams to implement '
                 'success metrics',
                 'Experience building a program from inception to '
                 'implementation']}
```

# Room for improvement

- catch connection errors such as MaxRetryErrors, Failure to Connect etc.
