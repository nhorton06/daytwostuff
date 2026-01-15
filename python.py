#%%

#%%

#%%

#%%

# "Path": @nhorton06 ➜ /workspaces/daytwostuff (main)

# The environment should not be included in the environment in the repo itself because it is a 
# local environment specific to the user's machine.

# New "path": (.venv) @nhorton06 ➜ /workspaces/daytwostuff (main)
# The main difference is the (.venv) at the beginning, indcating the active virtual environment

#%%
import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/MMiDS-textbook/MMiDS-textbook.github.io/refs/heads/main/utils/datasets/penguins-measurements.csv')
print(data.head())


# %%

# Extension menu observations: There is an icon showing
# that the extension is installed and active in the codespace. 
# There also is no longer an install button for the extension
# as it is already installed.

# 3 Useful elements of Data Wrangler extension:
# 1. Instant transformations to data (fill, drop, type, etc.)
# 2. Automatic pandas code preview and export
# 3. Launch from many file types (csv, excel, json, etc.)

# Plotly Version: 6.5.1

# Why we use requirements.txt file:
# To specify the exact versions of packages needed, ensure consistency across
# users and environments, and make it easier to install needed dependencies.

# Recipe: 
# 1. Create new github repo or fork existing one to account, create codespace from repo
# 2. Open VSCode locally and connect to codespace
# 3. Create a virtual environment (python -m venv .venv)and activate it (source .venv/bin/activate)
# 4. Install required packages using pip and/or requirements.txt (pip install -r requirements.txt)
# 5. Install Data Wrangler extension in codespace (if not already installed)
# 6. Use git to add any changes (git add .   git commit -m "commit msg"    git push)
# 7. Make sure your .gitignore includes your .venv and any other private files
