import graphene
from graphene_django import DjangoObjectType
from .models import MyModel


class MyModelType(DjangoObjectType):
    class Meta:
        model = MyModel


class Query(graphene.ObjectType):
    mymodels = graphene.List(MyModelType)

    def resolve_mymodel(self, info):
        return MyModel.objects.all()


schema = graphene.Schema(query=Query)
