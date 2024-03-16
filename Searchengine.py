from elasticsearch import Elasticsearch

# Initialize the Elasticsearch client
es = Elasticsearch()

# Index the data
es.index(index='stock_data', doc_type='_doc', body={
    'name': 'Apple Inc.',
    'ticker': 'AAPL',
    'price': 150.0,
    'industry': 'Technology'
})

# Search for a particular stock
query = {
    "query": {
        "match": {
            "name": "Apple"
        }
    }
}

# Execute the search query
response = es.search(index='stock_data', body=query)

# Print the search results
print(response['hits']['hits'])
