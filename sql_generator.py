from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',
)

#schema = "A GraphQL movie schema would define a Movie type with fields like title(String), releaseDate (Date), posterUrl (String), genre (String or an array of genre types), director(String), actors (an array of Actor objects), and a unique id (Int), allowing users to query for specific movie details and related information based on their needs. "
schema = "A book table with a title field of string type which is the primary key, an author_id field of integer type which is the foreign key to the Author table. The Author table has the name field of String type and the author_id field of integer type which is the primary key for the table"
text = "get a list of all the books written by a particular author named Conan"
messages= [
    {
        "role": "system",
        "content": "You are a SQL query generator.",
    },
    {
        "role": "user",
        "content": "Given the following SQL schema:"
                   + schema +
                   "Please transform the following text into a SQL query:" +
                   text
    },
    {
        "role": "assistant",
        "content": "Generate the SQL query.",
    },
]
# Generate Query
response = client.chat.completions.create(
    model='deepseek-r1:7b',
    messages=messages
)

#Generate the whole message
messages.append(response.choices[0].message)
print(f"Message: {messages}")

#Trim the Query
msg = messages.pop().content
trim_first = msg.index('```sql') + 6
trim_last = msg.index('```', trim_first + 3)

print(f"Query: {msg[trim_first:trim_last:]}")

