from graphql import (
    GraphQLObjectType,
    GraphQLField,
    GraphQLString,
    GraphQLInt,
    GraphQLNonNull,
    GraphQLArgument
)
from schema.types import UserType
from resolvers.mutation_resolvers import create_user

MutationType = GraphQLObjectType(
    name='Mutation',
    fields={
        'createUser': GraphQLField(
            type_=UserType,
            args={
                'name': GraphQLArgument(GraphQLNonNull(GraphQLString)),
                'email': GraphQLArgument(GraphQLNonNull(GraphQLString)),
                'age': GraphQLArgument(GraphQLNonNull(GraphQLInt))
            },
            resolve=create_user
        )
    }
)
