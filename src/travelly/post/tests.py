from django.test import TestCase

# Create your tests here.

import json
from graphene_django.utils.testing import GraphQLTestCase 



class PostTestCase(GraphQLTestCase):

	def test_post_query(self):

		response = self.query(
			'''

			''',
			op_name = Post,


			)
		content  = json.loads(response.content)

		self.assertResponseNoErrors(response)


	def test_single_post_query(self):

		response = self.query(

			'''

			''',

			op_name = Post,
			variables = {id:1}

			)

		content = json.loads(response.content)

		self.assertResponseNoErrors(response)
