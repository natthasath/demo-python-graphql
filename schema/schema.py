from graphql import GraphQLSchema
from schema.queries import QueryType
from schema.mutations import MutationType

schema = GraphQLSchema(query=QueryType, mutation=MutationType)
