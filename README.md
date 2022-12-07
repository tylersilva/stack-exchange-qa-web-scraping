# Stack Exchange Q&A Tool

### Video Demo:  https://youtu.be/5wK-p2dD56U
### Description: Web search tool that allows for user queries against multiple Stack Exchange sites. This tool will take the user input and pull the top rated answer from the user selected Stack Exchange site, with appropriate formatting.
<br />

## What is this project?
This tool enables the ability to search for answers to technical questions and returns a top rated result from a selection of Stack Exchange websites, directly within a users terminal. Users have the option to select a relevant Stack Exchange site that aligns with their query, followed by a query that is technical in nature (eg. How to add in Python). If no Stack Exchange site is selected, or the user chooses to ask their question directly in the terminal, the program will default its search to Stack Overflow.
<br />
<br />

## How does it work?
In order to retrieve the information requested by the user this program uses BeatifulSoup4 to perform web scraping. The HTML page formatting is similar across all Stack Exchange sites so users have the option to select which Stack Exchange site they would like to run their queries against, followed by the technical query. Once input, the program performs a Google search isolated to the specified Stack Exchange site and user query. It then pulls the top link provided by Google and captures the "Top Answer" from the respective Stack Exchange site into a variable. This information is then sent back to the users Terminal and displayed formatted using Pyfiglet
<br />
<br />
Note: If no "Top Answer" is available the program will choose the first available answer from the Stack Exchange site page. Additionally, it will throw an error if no answer is available.
<br />
<br />

## What do each of the project files contain and do?
### Modules:
- beautifulsoup4
- pyfiglet
- sys
- urllib3
- requests

<br />

## Why make this?
It is common that a developer or engineer will turn to Google and ultimately Stack Overflow to troubleshoot or seek answers to common programming related questions. I wanted to learn more about web scraping, but also wanted to create something that may benefit myself and fellow developers in the pursuit of programming knowledge. This tool allows for simple technical Q&A functional directly within the terminal which saves time and helps with maintaining focus.