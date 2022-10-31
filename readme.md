# AttackWeb .01 (Pre-Alpha)

## Overview
AttackWeb is a Flask application designed to ingest a risk matrix from an Excel template and output an attack graph and accompanying probabilities. This first release contains basic functionality; the next release will improve the user interface.

## Installation
This application is available from GitHub at https://github.com/rob-essex/AttackWeb. The file structure should be copied to your local Python environment (preferably a virtual environment).

## Dependencies
AttackWeb is designed for Python 3.7+ and requires the following libraries to properly function.
- json
- os
- tempfile
- collections
- jsonpickle
- networkx
- IPython.display
- jinja2
- pyvis
- Flask
- pandas

## Operation
Using this program requires users to first prepare the risk matrix for analysis, run the application, then access the results.
### Step 1: Prepare the Risk Matrix Excel File
In the project directory, navigate to the excel folder. AttackWeb will analyse the target.xlsx file, so users may either edit or replace the target.xlsx file with the desired information. Threats – factors that may cause adverse action – are listed in Column A. Risks – the adverse actions – are listed in Row 1. Find the desired Threat in Column A, and input the desired probability of occurrence in the columns corresponding to the risks in Row 1.
NOTE: the information in the target.xlsx file must follow the original format. Specifically, the threat matrix must have exactly the same index items in Row 1 and column A, to include spelling, capitalisation, and punctuation.
### Step 2: Run the Application
Once the dependencies have been installed, open a command line in the project folder and type the following command to launch the application.
> python -m flask run 

The command line will confirm that the Flask application is running.

**NOTE: different operating systems may require different commands to launch Flask applications. Additional system instructions are available at https://flask.palletsprojects.com/en/2.2.x/cli/.** 

### Step 3: Access the Results
Open a browser and navigate to 127.0.0.1:5000. The attack graph visualisation will be at the top of the page, with probabilities between threats and risks listed below.

### Step 4: Close the Application and/or Change Risk Matrix
To close the application, return to the command line above and press “CTRL + C.” To change the values in the Risk Matrix located in targets.xlsx, or to replace the file, first close the application and then follow the instructions in Steps 1-3.

## References, Resources, and Inspiration
The Pyvis module drives the instantiation of a graph network with NetworkX, and also leverages the VisJS Java package to create graphics. Since the Pyvis Network library in release 0.3.0 was not compatible with Python 3, the library has been adjusted for compatibility and included as a local library in pyvisfix_network.py. After additional testing, these adjustments will be shared with the Pyvis team for consideration in future releases. 
Pyvis documentation is available at https://pyvis.readthedocs.io/en/latest/index.html, and the GitHub repository can be found at https://github.com/WestHealth/pyvis/.

NetworkX Network objects serve as the heart of AttackWeb’s graph structure. NetworkX has very thorough documentation and a thriving community available at https://networkx.org/, with a GitHub repository at https://github.com/networkx.

Khuyen Tran wrote an excellent tutorial for Pyvis implementation using Pandas. This shaped the ingest function applied in AttackWeb: https://towardsdatascience.com/pyvis-visualize-interactive-network-graphs-in-python-77e059791f01.

Corey Schafer’s Flask tutorial series is a comprehensive guide to Flask development, from basic functionality to sophisticated and secure applications: https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH.
