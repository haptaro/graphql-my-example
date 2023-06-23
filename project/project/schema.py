import graphene
import one.schema
import ingredients.schema


class Query(one.schema.Query, ingredients.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
