# Boilerplate Python

How to use this boilerplate with github:

1. Clone the repository
2. Create the branch main (git checkout -b main)
3. Create the branch docs (git checkout -b docs)
4. Add branch protection rules inside the repository settings
Rule: main Options: "Require a pull request before merging" "Dismiss stale pull request approvals when new commits are pushed" "Require status checks to pass before merging" "Require branches to be up to date before merging" "Status checks that are required: deploy prerelease test code-style" "Require conversation resolution before merging"
Rule: develop Options: "Require a pull request before merging" "Dismiss stale pull request approvals when new commits are pushed" "Require status checks to pass before merging" "Status checks that are required: test code-style" "Require conversation resolution before merging" "Restrict who can push to matching branches: People, teams, or apps with push access"
Rule: feature-* Options: "Restrict who can push to matching branches: People, teams, or apps with push access" "Allow force pushes: Everyone" "Allow deletions"
Rule: docs Options: None
5. Add protected tags inside the repository settings
Rule: v*
6. If you want to use SonarCloud: make sure to add the mandatory environment variables inside the repository settings SONAR_TOKEN, adjust the sonar-project.properties file and enable it inside the workflows tests.yml and release.yml
7. If you want to use Dependabot: make sure to enable it inside the security menu
8. If you want to use Semantic-Release: make sure to add the mandatory environment variables inside the repository settings RELEASE_TOKEN which is an PAT for pushing to the releases inside github with push and tagging rights
9. Make sure to adjust the General settings inside the repository settings:
"Always suggest updating pull request branches"
"Allow auto-merge"
"Automatically delete head branches"
10. Next adjust the name boilerplate_python and boilerplate-python in all relevant files and filenames
11. Last update this README.md file with the correct information using the README_EXAMPLE.md file
