import strawberry
from strawberry.fastapi import GraphQLRouter

from app.schema import Mutation, Query

schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)
