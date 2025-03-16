# News API Bias Aggregator 

Using a small database of news sources, this project generates a political bias score for a user-supplied story or topic.
 
## How it works

### Technologies: Python, Django, DRF, NewsAPI, Requests, React, Javascript, CSS, HTML

The project uses a single-page React app to function as the GUI, wherein users can input a topic of their choice. Once the user has done so, a post request is created where it is interpreted by the backend and converted into a URL to query the NewsAPI. The returned JSON is then processed, and saved ready to be retrieved via a Get request, and served to the GUI where it displays a gradient, graphically representing the proportion of representation the story has from the various points along the political spectrum. 

## What was learnt from the project

* Further solidified my understanding of OOP
* Familiarized myself with handling JSON; understanding the file format’s structure and writing custom parsing functions to access nested entries
* Foundation of Django’s serializers and ORM, alongside integrating my bespoke backend code with DRF to create a simple but effective functional API.
* Fundamental React concepts such as props, managing state, callback functions, and understanding the DOM
* How to utilise the FetchAPI to facilitate frontend API requests

## Future Improvements

To create a fuller picture of the complete news coverage of a given topic, a system of semantic analysis could be implemented to gauge the possible political affiliation of uncategorized sources. This could be done via data analysis libraries like Pandas, to measure the frequency of certain vocabulary and how often they occur in Left leaning sources for example.
A pipe between the project and an LLM API could be utilised to create a story summary from the collated sources, giving users a brief overview of the general story coverage.
Redesign UI with the addition of a library such as tailwind to create a more refined and professional looking GUI
Add user functionality as to save past queries, and possibly perform updates on these queries





