# MISTRAL APPLICATION README
## Overview
For my application I decided to build a fairly simple chatbot. that takes in a pdf/docx file from the same folder and whether they want just a study guide or both a study guide and some practice questions. I did this by chunking up the documents into a reasonable length for the LLM to easily tokenes it effeciently and then  

## Installation
The main things with installation are obviously vllm, pytorch, pypdf2,python-docx, ipywidgets==7.7.1, transformers and hugging faces hub.  Then log into hugging faces as that is what I used to create the model.  From there you just have to 

## Testing
My main way to test was by running the code and having test text documents as end a very good end to end test.  However I als built unit tests with test imputs to make sure my generation parsing worked and was compatible with the methods I built.
