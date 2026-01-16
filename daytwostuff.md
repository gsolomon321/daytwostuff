---
title: Day Two Stuff
---

## Today we are going to work through getting all our environments setup and do some quick tasks. 
## You will record your answers in the .py file, which will need to be pushed to your repo. You'll submit
## the repo link. 

### Clone the Repo
1. Go to Github and find the DayTwoStuff repo
2. Clone it to your GitHub Account
3. Create a new Codespace from the repo

### Open the Codespace in your local VS Code
1. Open VS Code on your local machine
2. Use the Codespaces extension to open your new Codespace in VS Code
3. Familiarize yourself with the layout of the project
4. Open a new .py file and add the section breaks to create a interactive .py file
    hint: you made need to reload juypter extension and/or add the ipykernel package
5. What is your terminal display "path"? (type/paste as text into the .py file) 

### Create a virtual environment
1. open a bash terminal 
2. type the command for creating a virtual environment
3. make sure the environment is activated
4. Should you include the environment in your repo or not?  
    - **Q4 Answer:** No, you should not include the enviornment in your repository. Most enviornments are machine-specific and tend to make the repos unnecessarily large. Instead, it is better practice to add a requirments.txt file. 
5. Now what is your terminal display "path"? Is it different? 
    - **Q5 Answer:** The "path" is the same, "/workspaces/daytwostuff". However, the terminal prompt is slightly different, including the "(venv)" before the path -- "(venv) /workspaces/daytwostuff $".

### Load/(create if needed) the requirements.txt file
1. use the correct terminal commands to load the requirements file into your virtual environment

### Viewing Data
1. In your current .py file load in a dataset.
2. Find a extension that will allow you to see the data in a data viewer (Data Wrangler)
3. Load the extension and view the data

### Extension Management
1. You've possibilly added a new extension, hopefully it was Data Wrangler, if not search and add it
2. Find the extension in the extension menu. What do you notice about the extension menu? 
    - **Q2 Answer:** The Data Wrangler extension menu contains extension details, features, and changelog. In the details section, it demos the data exploration and preparation processes. In this section is also provides guidance setting up your enviornment, explains the interface, and discusses next steps. 
3. Review the capabilities, what are three useful elements of Data Wrangler
    **Q3 Answers:**
    1. CSV files and DataFrames can be previewed in a clean table format without writing any code.
    2. You can filter rows, rename columns, handle missing values, and change data types using the UI.
    3. Every action you take generates Python code, which is useful for reusability, reproducibility, and learning in general.

### Package managing
1. Install plotly in the terminal
2. Note the version **(version: 6.5.1)**
3. Add plotly to your requirements file using terminal commands
4. Then update the requirements document
5. Why do we use a requirements.txt file?
    **Q5 Answer:**
    - The `requirements.txt` file ensures consistent environments across different machines, making projects easier to set up and execute for others. It also specifies package versions, which helps limit compatibility issues. Using the `pip install -r requirements.txt` command allows dependencies to be installed quickly and conveniently.

### Pip Freeze/(create if needed) the requirements.txt file
1. use the correct terminal commands to update your requirements.txt file: **terminal command** = `pip freeze > requirements.txt`

### Github 
1. You've made several changes to your environment, including adding a python file, dataset and updates to the requirements file
2. Commit and push these changes to your repo

### Recipe
1. Write yourself a step by step recipe for creating a new working project environment
    You don't need to include "loading data"
2. Create a new working project environment using these steps. 

### Submit to canvas
1. Submit your github links (this repo and your new project) to canvas
2. Include your answers to the questions above in the python script, in the first repo.

## If you finish early - take a look at "Sample script.py" The end result should be a map in the browser 
## showing the location of 2000 squirrels in central part. Try to draw, by hand, a flow diagram that includes 
## all the software necessary to make this simple script work. 