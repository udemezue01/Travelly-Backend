		# GraphQL Imports

import graphene
from graphql import GraphQLError


		# The Root App Schema

from travelly.graph.app_schema import(

		GuideType,
		ReviewType

	)

		# Models For My App

from .models import(

		Guide,
		Review,

	)




		# Guide Create Mutation


class GuideCreateMutation(graphene.Mutation):

	guide 				=  graphene.Field(GuideType)

	class Arguments:


		pass

	def  mutate(self, info, **kwargs):

		pass
		



		# Guide Update Mutation


class GuideUpdateMutation(graphene.Mutation):

	pass


		# Guide Delete Mutation

class GuideDeleteMutation(graphene.Mutation):


	pass



		# Review Create Mutaion


class ReviewCreateMutation(graphene.Mutation):

	pass


		# Review Update Mutation


class ReviewUpdateMutation(graphene.Mutation):

	pass


		# Review Delete Mutation



class ReviewDeleteMutation(graphene.Mutation):


	pass

	
