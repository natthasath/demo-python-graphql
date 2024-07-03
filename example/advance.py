import asyncio
from graphql import GraphQLSchema, GraphQLObjectType, GraphQLField, GraphQLID, GraphQLString, GraphQLInt, GraphQLFloat, GraphQLBoolean, execute, parse, graphql as run_graphql

# Define types for more complex schema
user_type = GraphQLObjectType(
    name='User',
    fields={
        'id': GraphQLField(GraphQLInt),
        'name': GraphQLField(GraphQLString),
        'email': GraphQLField(GraphQLString),
        'age': GraphQLField(GraphQLInt)
    }
)

post_type = GraphQLObjectType(
    name='Post',
    fields={
        'id': GraphQLField(GraphQLInt),
        'title': GraphQLField(GraphQLString),
        'content': GraphQLField(GraphQLString),
        'author': GraphQLField(user_type)  # Nested object type
    }
)

# Define your GraphQL schema
query_type = GraphQLObjectType(
    name='Query',
    fields={
        'hello': GraphQLField(
            type_=GraphQLString,
            resolve=lambda obj, info: 'Hello world!'
        ),
        'user': GraphQLField(
            type_=user_type,
            resolve=lambda obj, info: {'id': 1, 'name': 'John Doe', 'email': 'john.doe@example.com', 'age': 30}
        ),
        'post': GraphQLField(
            type_=post_type,
            resolve=lambda obj, info: {'id': 1, 'title': 'First Post', 'content': 'This is my first post!', 'author': {'id': 1, 'name': 'John Doe'}}
        )
    }
)

schema = GraphQLSchema(query=query_type)

async def main():
    # GraphQL query
    query = '''
        {
            hello
            user {
                id
                name
                email
                age
            }
            post {
                id
                title
                content
                author {
                    id
                    name
                }
            }
        }
    '''

    # Execute GraphQL query asynchronously
    result = await run_graphql(schema, query)
    
    # Print the result
    print(result.data)

# Run the async function
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
