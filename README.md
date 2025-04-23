# Python Template

## 🔧 How to use this template with GitHub

1. **Create a new repository using this template.**  
   Click on **"Use this template"** → **"Create a new repository"** in the top-right corner.


2. **Generate a Personal Access Token (PAT)**

   You will need this token to set branch protection rules and to set up Semantic Releases via GitHub Actions.

   #### 🔑 How to create the token:
   1. Go to [https://github.com/settings/tokens](https://github.com/settings/tokens)
   2. Click **"Generate new token (classic)"**
   3. Provide a name, e.g., `boilerplate-setup`
   4. Set the **expiration date** 
   5. Enable the following permissions:
     - `repo` (full control of private repositories)
     - `admin:repo_hook` (required to set branch protection rules)admin:org
     - `admin:org` -> `read:org`  (required to set branch protection rules)

   6. Click **"Generate token"**
   7. Copy the token immediately, as it will only be shown once!

   #### 🔐 Save the token as a Secret:
   1. Go to your new repository on **Settings** → **Secrets and variables** → **Actions**
   2. Click **"New repository secret"**
   3. Name: `GH_TOKEN`
   4. Value: (paste the copied token here)
   5. Save it by clicking **"Add secret"**

3. **Initial Setup**  
   You can configure your repository **either manually** or **automatically via GitHub Actions**.

   3.1 **Via Actions**
    1. Go to **Actions** → **Setup – Create main branch** → **Run workflow**  
       This will create the `main` branch from `develop`.
    2. Go to **Actions** → **Setup – Branch Protections** → **Run workflow**  
       This will configure all branch protection rules and protected tags.

   3.2 **Manually**
    1. **Create the `main` branch** from `develop`:
       ```bash
       git checkout develop
       git checkout -b main
       git push origin main
       ```  
    2. **Set up branch protection rules** in **Settings → Branch protection rules**:
        - **`main` branch**
            - Require a pull request before merging
            - Dismiss stale pull request approvals when new commits are pushed
            - Require status checks to pass before merging (`deploy`, `prerelease`, `test`, `code-style`)
            - Require branches to be up to date before merging
            - Require conversation resolution before merging
        - **`develop` branch**
            - Require a pull request before merging
            - Dismiss stale pull request approvals when new commits are pushed
            - Require status checks to pass before merging (`test`, `code-style`)
            - Require conversation resolution before merging
            - Restrict who can push: **people, teams, or apps with push access**
        - **`feature-*` branches**
            - Restrict who can push: **people, teams, or apps with push access**
            - Allow force pushes
            - Allow deletions

4. **Add Protected Tags Inside Repository Settings**
  - Rule: `v*` (for version tags)

5. **Enable Dependabot** (if needed)
  - Enable Dependabot in the **Security** tab of your repository.

6. **Set up Semantic Release** (optional)
  - Add the required environment variables in the repository settings:
    - `GH_TOKEN` (a PAT for pushing releases with push and tagging rights)
  - Ensure the appropriate configuration in the workflow files.

7. **Adjust General Repository Settings**
  - Ensure the following options are enabled in **Settings** → **General**:
    - "Always suggest updating pull request branches"
    - "Allow auto-merge"
    - "Automatically delete head branches"

8. **Rename Boilerplate Files**
  - Change instances of `boilerplate_python` and `boilerplate-python` in all relevant files and filenames.

9. **Update README**
  - Update this README file with the correct information, using the `README_EXAMPLE.md` file as a guide.



