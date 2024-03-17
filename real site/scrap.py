from bs4 import BeautifulSoup
import requests
import time
import json
data = [ ]

#function to scrap jobs
def job_details():
    # Link to the website we want to scrap our data from
    job_post_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation=').text

    # Invoking BeautifulSoup
    soup = BeautifulSoup(job_post_text, 'lxml')

    # Find all jobs on the website
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

        # Get details about jobs
    for job in jobs:
        # specify date job was posted
        date_ptsd = job.find('span', class_='sim-posted').span.text

        if 'few' in date_ptsd:
            job_title = job.find('header', class_='clearfix').h2.text.replace(' ', ' ')
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', ' ')
            skill_req = job.find('span', class_='srp-skills').text.replace(' ', '')
            link_tag = job.find('a')
            link = link_tag.get('href')

            full_detail = {
                'Job Title': job_title.strip(),
                'Company Name': company_name.strip(),
                'Skills Required': skill_req.strip(),
                'Link to Apply': link.strip(),  
                }
            data.append(full_detail) 

    # Convert data to JSON with proper indentation and newlines
    json_data = json.dumps(data, indent=4)

    # Print the JSON data
    print(json_data)




if __name__ == '__main__': 
    while True:
        job_details()
        # Execute the program every 10 minutes
        time_wait = 10
        print(f'Please wait for {time_wait} minutes...')
        time.sleep(time_wait * 60)