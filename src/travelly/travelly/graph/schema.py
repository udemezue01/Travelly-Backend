import graphene


from .app_schema import Query
from post.mutation import (

	PostCreateMutation,
	PostUpdateMutation,
	PostDeleteMutation,
	PostLikeToggleMutation

	)



class Mutation(graphene.ObjectType):

	# The Post Create, Update and Delete Mutation

	post_create 		= 	PostCreateMutation.Field()
	post_update			=  	PostUpdateMutation.Field()
	Post_delete 		= 	PostDeleteMutation.Field()

	# The Post Like Mutation

	post_like			=  	PostLikeToggleMutation.Field()

	# The comment Create, Update and Delete Mutation




class Query(Query, graphene.ObjectType):

	pass

schema = graphene.Schema(query  = Query, mutation = Mutation)