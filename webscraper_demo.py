import requests
from bs4 import BeautifulSoup

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

get_job_listing('https://www.facebook.com/careers/jobs/')
