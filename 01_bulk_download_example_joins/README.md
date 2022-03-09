# Bulk Download Files: Example Joins

The code scripts in this folder walk through the joining of various bulk download files:

| Script             | Description           | 
| ---    			 |---					 |
| country_ipc_selection.R | *Demonstrates using ipc and location to select patents* |
| join_assignee.Rmd  | *Describes joining of assignee, location, and patent tables*|
| join_assignee.html |	*HTML version of join_assignee.Rmd*|
| join_inventor.Rmd  | *Describes joining of inventor, location, and patent tables*|
| join_inventor.html | *HTML version of join_inventor.Rmd*|		 

Note: 

You will need to set your working directory/folder path in the r setup block in the .Rmd scripts above. Here is the line you will need to change:
	
	 knitr::opts_knit$set(root.dir = "TODO: ADD DIRECTORY PATH HERE")