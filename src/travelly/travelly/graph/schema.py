import graphene


from .app_schema import Query
from post.mutation import (

	PostCreateMutation,
	PostUpdateMutation,
	PostDeleteMutation,
	PostLikeToggleMutation

	)

from userprofile.mutation import(

	ProfileCreateMutation,
	ProfileUpdateMutation

	)



class Mutation(graphene.ObjectType):

	# The Profile Create, Update and Delete Mutation

	profile_create		= 	ProfileCreateMutation.Field()
	profile_update		= 	ProfileUpdateMutation.Field()

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