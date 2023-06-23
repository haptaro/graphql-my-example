import graphene
from graphene_django import DjangoObjectType
from .models import MyModel


class MyModelType(DjangoObjectType):
    class Meta:
        model = MyModel
        fields = ("id", "name")


class Query(graphene.ObjectType):
    mymodels = graphene.List(MyModelType)

    def resolve_mymodels(self, info):
        return MyModel.objects.all()


schema = graphene.Schema(query=Query)
