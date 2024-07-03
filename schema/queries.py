from graphql import (
    GraphQLObjectType,
    GraphQLField,
    GraphQLString
)
from schema.types import UserType, PostType

QueryType = GraphQLObjectType(
    name='Query',
    fields={
        'hello': GraphQLField(
            type_=GraphQLString,
            resolve=lambda obj, info: 'Hello world!'
        ),
        'user': GraphQLField(
            type_=UserType,
            resolve=lambda obj, info: {'id': 1, 'name': 'John Doe', 'email': 'john.doe@example.com', 'age': 30}
        ),
        'post': GraphQLField(
            type_=PostType,
            resolve=lambda obj, info: {'id': 1, 'title': 'First Post', 'content': 'This is my first post!', 'author': {'id': 1, 'name': 'John Doe'}}
        )
    }
)
