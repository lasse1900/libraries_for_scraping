# Job search project

Needed python modules:

"pip install selenium"

Webdriver-manager used "pip install webdriver-manager"

Other installed packages: regex,
html2text,
schedule, python_docx, requests, matplotlib

# New module addition - basic things
Current style on website is that module name and site name are same. same name is used all ower code. Touched files are following.
- config.ini There are first general settings and after those website dependent. If something breaks in for data search in existing modules, then good place is to start on checking module settings and regular expressions at there.
- config.py Settings contains two levels. Config for general settings for all modules and internal class _Website that contains site dependencies.
- main.py Configuration limits to two site lists that should be alike. Use capital letter in module name.
- job.py This module loads the info for found jobs. Current sites behave well with links and selenium is not (yet) needed. Data is searched with regex:s defined in config.ini. Some tuning is made and used module name is same as given in module (lowercase currently).
- new module.py Modules have returned it's name as lower case. Same case is used in job.py.


# SQL query examples
In debug phase there will be extra lines. Example row deletions.

DELETE FROM jobs WHERE title = ''

DELETE FROM jobs WHERE fetch_time = '2022-10-01'

Note that after changes made with "DB Browser for SQLite", 
database will be locked. Locking will be released when "Write Changes" 
button is clicked or database closed in application.

[Learn more about creating GitLab projects.](https://docs.gitlab.com/ee/gitlab-basics/create-project.html)
