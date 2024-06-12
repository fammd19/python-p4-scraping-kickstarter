from kickstarter_scraper import projects

for project in projects:
    print(project.upper())
    description = projects[project]["description"]
    print(description)
    print("*"*30)