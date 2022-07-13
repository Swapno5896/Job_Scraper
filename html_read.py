from bs4 import BeautifulSoup
import requests
import time
def scrap(Skill,location,workExp,unFamilarSkill):
    have_job = []
    link = f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={Skill}&txtLocation={location}&cboWorkExp1={workExp}"
    html_text = requests.get(link).text  # send reequest
    # print(html_text) # hear we can see the html text

    # make instance of beautiful supe
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    # filtering job besed on skill i do't have
    # print('Please give skill that you do not know')
    # unfamiliar_skill = input('>')
    # we have all the firts page job
    for job in jobs:
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text  # find company name from jobs
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')  # replace wide space with small space
            more_info = job.header.h2.a['href']
            colledted_job = {}
            colledted_job['Company_Name'] = company_name[3:len(company_name) - 12]
            colledted_job['Require Skill'] = skills[4:len(skills) - 4]
            colledted_job['More_Info'] = more_info
            have_job.append(colledted_job)
    print(have_job)
    # if unfamiliar_skill not in skills:
    #     with open(f'posts/{Skill}.txt', 'a') as f:
    #         f.write(f'Company name : {company_name.strip()}\n')
    #         f.write(f'Skills name : {skills.strip()}\n')
    #         f.write((f'More link is : {more_info}\n'))
    #         f.write('\n')
    #     print(f'file saved : {Skill}')

    return have_job
