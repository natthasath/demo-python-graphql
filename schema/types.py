from graphql import (
    GraphQLObjectType,
    GraphQLField,
    GraphQLString,
    GraphQLInt
)

UserType = GraphQLObjectType(
    name='User',
    fields={
        'id': GraphQLField(GraphQLInt),
        'name': GraphQLField(GraphQLString),
        'email': GraphQLField(GraphQLString),
        'age': GraphQLField(GraphQLInt)
    }
)

PostType = GraphQLObjectType(
    name='Post',
    fields={
        'id': GraphQLField(GraphQLInt),
        'title': GraphQLField(GraphQLString),
        'content': GraphQLField(GraphQLString),
        'author': GraphQLField(UserType)  # Nested object type
    }
)
