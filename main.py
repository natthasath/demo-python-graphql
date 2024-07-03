import asyncio
from graphql import graphql
from schema.schema import schema

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
    result = await graphql(schema, query)
    print(result.data)

    # GraphQL mutation
    mutation = '''
        mutation {
            createUser(name: "Jane Doe", email: "jane.doe@example.com", age: 25) {
                id
                name
                email
                age
            }
        }
    '''

    # Execute GraphQL mutation asynchronously
    result = await graphql(schema, mutation)
    print(result.data)

if __name__ == '__main__':
    asyncio.run(main())
