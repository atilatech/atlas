# Atlas
Atila's Tool for Learning any Subject (starting with crypto).

Atlas is a search engine that allows you to parse a collection of URLs,
index them into a database and make it searchable.

## Installation

`source install.sh`

Put your environment variables into the newly created .env file

`source .env`

`pip install -e .`

## Quickstart


```shell
# 1. Parse and index your content:
python atlas/content_parser.py

# 2. Initialize your content:
python atlas/content_index.py

# 3. Run the API
python api/api.py

# 4. Send a GET request to your api
curl --location --request GET 'http://127.0.0.1:8080/api/search?q=what+is+an+NFT'
# or open your browser to `http://127.0.0.1:8080/api/search?q=<your_search_term>` 
```


## Troubleshooting

`ModuleNotFoundError: No module named 'atlas'`

Set your $PYTHONPATH. See this [SO answer](ModuleNotFoundError: No module named 'atlas')