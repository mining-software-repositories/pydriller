# Author: Armando Soares Sousa
# e-mail: armando@ufpi.edu.br
# Created on: 02/28/2019

# This is the first attempt to analysis a software project via Mining Software Repository
# The analysis of MSR uses pydriller (https://pydriller.readthedocs.io) as the main tool
# to extract the information about the software repository analized

import datetime
from pydriller import RepositoryMining

# List all Commits from Authors
def listAllCommmitsFromAuthors(repostory):
    for commit in RepositoryMining(repostory).traverse_commits():
        print('hash {} authored by {} e-mail {} on date {}'.format(commit.hash, commit.author.name, commit.author.email, commit.author_date))

# List all Files changed for each Commit
def listAllFilesChangedInCommit(repostory):
    for commit in RepositoryMining(repostory).traverse_commits():
        for modification in commit.modifications:
            print('Author {} modified {} in commit {}'.format(commit.author.name, modification.filename, commit.hash))

# Return all developers that have been saved at least one commit on repository
def listAllDevelopersHaveCommits(repository):
    list_of_developers = []
    for commit in RepositoryMining(repository).traverse_commits():
        author = commit.author.name
        if (author not in list_of_developers):
            list_of_developers.append(author)
    return list_of_developers

# Show the current date time of System
def showDateTime():
    now = datetime.datetime.now()
    return now

def basicAnalysisReportMSR(repository, branch, list_of_developers):
    print("1. The following repository will be analized", repository)
    print("2. The following branch will be analized", branch)
    print("3. The following developers have been worked in the project: ", list_of_developers)
    print("4. The following commits have been saved in the project")
    print('List all commits from authors of ', repository)
    listAllCommmitsFromAuthors(repository)
    print("5. The following files were changed for each commit")
    listAllFilesChangedInCommit(repository)

repostory_promocity = '/Users/armandosoaressousa/git/promocity'
branch = ''
list_of_developers = listAllDevelopersHaveCommits(repostory_promocity)

print("SysRepo Analysis - v: 0.0.1", showDateTime())
basicAnalysisReportMSR(repostory_promocity, branch, list_of_developers)
