from graphene_django.utils.testing import GraphQLTestCase
from .schema import schema
from .models import MyModel
from mixer.backend.django import mixer


class MyModelAPITestCase(GraphQLTestCase):
    GRAPHENE_SCHEMA = schema
    GRAPHQL_URL = '/graphql/'

    def test_query_all_mymodels(self):
        my_model = mixer.blend(MyModel)
        response = self.query(
            '''
            query {
              mymodels {
                id
                name
              }
            }
            '''
        )
        self.assertResponseNoErrors(response)
        content = response.json()['data']
        my_models = content['mymodels']
        self.assertEqual(my_models[0]['name'], my_model.name)
