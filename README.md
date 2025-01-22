# SQL Query Generator from Simple Text Prompts
A simple SQL Query Generator leveraging the deepseek-r1:7b LLM model.

# To Initialize the LLM model in local:

> ollama run deepseek_r1

#Sample Input
> get a list of all the books written by a particular author named Conan

#Output
> SELECT b.title FROM book AS b
> JOIN Author AS a ON b.author_id = a.author_id
> WHERE a.name = 'Conan';
