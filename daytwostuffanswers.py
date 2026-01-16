
# %%
import pandas as pd
import seaborn as sns

#%%
df = pd.read_csv("dataset.csv")
df.head(5)

#%%
"""
### Answers

### Open the Codespace in your local VS Code
- Question 5: path --> /workspaces/daytwostuff

### Create a virtual environment
- Question 4: No, you should not include the enviornment 
in your repository. Most enviornments are machine-specific and tend 
to make the repos unnecessarily large. Instead, it is better practice 
to add a requirments.txt file. 

- Question 5: The "path" is the same, "/workspaces/daytwostuff". 
However, the terminal prompt is slightly different, including the "(venv)" 
before the path -- "(venv) /workspaces/daytwostuff $".


### Extension Management
- Question 2: The Data Wrangler extension menu contains extension 
details, features, and changelog. In the details section, it demos the 
data exploration and preparation processes. In this section is also 
provides guidance setting up your enviornment, explains the interface, 
and discusses next steps. 

- Question 3:
    1. CSV files and DataFrames can be previewed in a clean table format without writing any code.
    2. You can filter rows, rename columns, handle missing values, and change data types using the UI.
    3. Every action you take generates Python code, which is useful for reusability, reproducibility, and learning in general.

    
### Package managing
- Question 2: Version: 6.5.1

- Question 5: The `requirements.txt` file ensures consistent 
environments across different machines, making projects easier to set 
up and execute for others. It also specifies package versions, which helps 
limit compatibility issues. Using the `pip install -r requirements.txt` 
command allows dependencies to be installed quickly and conveniently.

### Pip Freeze/(create if needed) the requirements.txt file
- Question 1: Terminal command = `pip freeze > requirements.txt`

"""
