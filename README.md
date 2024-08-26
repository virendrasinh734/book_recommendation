# book_recommendation_engine
## Overview
This project is a hybrid book recommendation engine designed to suggest books based on user preferences and book descriptions. 
Apart from using the conventional collaborative filtering based on user reviews , I incorporated the book descriptions that I scraped from Open Library and apllied natural language processing (NLP) particulary Doc2Vec to deliver hybrid personalized and content-based recommendations.

## Key Features
Collaborative Filtering: Utilizes user-item interactions to recommend books.<br>
NLP with Doc2Vec: Analyzes book descriptions to generate embeddings for content-based recommendations.<br>
Cosine Similarity: Employed to measure similarity in both collaborative filtering and content-based approaches.<br>

## Implementation Details
<li>Collaborative Filtering:
Applied both user-based and item-based approaches using cosine similarity to identify similar users and items based on historical ratings.</li><br>
<li>Data Collection:
Scraped book descriptions from OpenLibrary to enrich the dataset with textual information.</li><br>
<li>NLP and Embeddings:
Processed book descriptions using Doc2Vec to create vector embeddings that capture semantic similarities between books.</li><br>
<li>Recommendation System:
Combined collaborative filtering results with content-based recommendations derived from Doc2Vec embeddings to enhance the recommendation accuracy.</li><br>
Web App:
Used flask in the backend and created a simple website , where user can search (implemented fuzzy search) for a book and get recommendations using this hybridised model.<br>

## Usage:
<li>Clone the repository.</li>
<li>Install the necessary dependencies mentioned in requirements.txt.</li>
<li>Run the app.py.</li>
<li>It will take some time to download the model (essentially the end cosine similarity matrix) (as it is quite large in size I used AWS cloud storage service)</li> 


## Conclusion
This project demonstrates an effective integration of collaborative filtering and NLP techniques to provide robust book recommendations. By leveraging both user interactions and content analysis, the engine offers a comprehensive recommendation solution.
Feel free to customize this template further based on additional features or specific instructions for running the project.
