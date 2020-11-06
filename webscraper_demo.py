import requests
from bs4 import BeautifulSoup
import re

# TODO Potential room for improvmenet would be to save the base URL of
# the company and append the careers relative URL if that is the trend across
# organizations.

def get_jobs():
    return get_job_listing('https://www.facebook.com/careers/jobs/')

def get_job_listing(url):
    req = requests.get(url)

    soup = BeautifulSoup(req.text, 'lxml')

    links = soup.find('div', {'class': '_8tk7'}).findAll('a')
    print(len(links))

    for link in links:
        job_details = dict()
        job_details['name'] = link.text
        job_details['href'] = link['href']
        print(job_details)

    return job_details


# For the POC emo purposes, I am hardcoding the home base URL
def make_full_facebook_job_url(url):
    return 'https://www.facebook.com/' + url;

def extract_qualification(url):
    req = requests.get(make_full_facebook_job_url(url))

    soup = BeautifulSoup(req.text, 'lxml')

    qualification = dict()
    qualification['minimum'] = []
    qualification['preferred'] = []
    extract_qualification_details(soup, '_1n-_ _6hy- _8lf-', qualification, 'minimum', 'Minimum Qualifications')
    extract_qualification_details(soup, '_1n-_ _6hy- _8lf-', qualification, 'preferred', 'Preferred Qualifications')
    print(qualification)

    return qualification

def extract_qualification_details(soup, css_class, qualification, qualification_type, qual_type_description):
    # Reviewing the DOM - one can isolate the DIV with the text "Minimum Qualifications"
    # Then traversing the DOM two level up to isolate the LI tag and scraping the text within
    # LI tag
    min_qual_list = soup.find(text=re.compile(qual_type_description)).parent.parent.findAll('div', {'class' : css_class})

    for min_qual in min_qual_list:
        qualification[qualification_type].append(min_qual.text)


#get_jobs()
extract_qualification('/careers/jobs/2537073536607922/')
