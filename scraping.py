import requests
from bs4 import BeautifulSoup

# Extraction of the Python "fake jobs" page's HTML code
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# Parsing the job list
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id = "ResultsContainer")

# Filtering results to Python developer jobs
python_job = results.find_all("h2", string=lambda text: "python" in text.lower())
python_job_elements = [h2_element.parent.parent.parent for h2_element in python_job]

# Printing the list of Python developer jobs' title, company, location and apply link
for job in python_job_elements:
    title = job.find("h2", class_="title")
    company = job.find("h3", class_="company")
    location = job.find("p", class_="location") 
    link_url = job.find_all("a")[1]["href"]
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print(f"Apply here: {link_url}\n")
    print()
