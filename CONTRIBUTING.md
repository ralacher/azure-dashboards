Please follow these guidelines to ensure sure your widget is added.

# Files and Folders
1. New widgets should be added as JSON files to the [data](data) directory
2. Widget names should include the name of the primary Azure service, technologies used, and other identifying features, e.g. `app-service-waf-python.json`

# JSON Schema
THe properties in the JSON file are used to render a Markdown file. The image shows where each property is used.
|Property|Required|Comments|
|---|---|---|
|title|true|Title of the Markdown tile|
|subtitle|true|Subtitle of the Markdown tile|
|description|true|Text used to populate the main body of the tile|
|cost|true|Value used to populate the cost shield of the tile|
|time|true|Value used to populate the time to deploy shield of the tile|
|costLink|true|URL to the Azure Pricing Calculator estimate|
|documentationLink|true|URL of the GitHub, Microsoft Documentation, or other documentation for the demo|
|githubLink|true|URL of the GitHub repository for the demo|
