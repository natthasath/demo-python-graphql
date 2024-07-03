import asyncio
from graphql import GraphQLSchema, GraphQLObjectType, GraphQLField, GraphQLID, GraphQLString, GraphQLInt, GraphQLFloat, GraphQLBoolean, execute, parse, graphql as run_graphql

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

async def main():
    # GraphQL query
    query = '{ hello }'

    # Execute GraphQL query asynchronously
    result = await run_graphql(schema, query)
    
    # Print the result
    print(result.data['hello'])  # Output: Hello world!

# Run the async function
if __name__ == '__main__':
    asyncio.run(main())
