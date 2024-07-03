from flask import Flask, jsonify, request
from graphql import GraphQLSchema, GraphQLObjectType, GraphQLField, GraphQLString, execute, parse

app = Flask(__name__)

# Define your GraphQL schema
query_type = GraphQLObjectType(
    name='Query',
    fields={
        'hello': GraphQLField(
            type_=GraphQLString,
            resolve=lambda obj, info: 'Hello world!'
        )
    }
)

schema = GraphQLSchema(query=query_type)

# Define your GraphQL endpoint
@app.route('/graphql', methods=['POST'])
def graphql_request():
    content_type = request.headers.get('Content-Type')
    if content_type != 'application/json':
        return jsonify({'error': 'Content-Type must be application/json'}), 400

    try:
        data = request.get_json()
        query = data.get('query')
        if not query:
            return jsonify({'error': 'Missing query parameter'}), 400

        result = execute(schema, parse(query))
        return jsonify(result.data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
