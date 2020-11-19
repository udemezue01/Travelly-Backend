import graphene


from .app_schema import Query
from post.mutations import (

	PostCreateMutation,
	PostUpdateMutation,
	PostDeleteMutation,
	PostLikeToggleMutation,

	CommentCreateMutation,
	CommentUpdateMutation,
	CommentDeleteMutation,

	)

from userprofile.mutations import(

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

	comment_create		=  CommentCreateMutation.Field()
	comment_update 		=  CommentUpdateMutation.Field()
	comment_delete		=  CommentDeleteMutation.Field()

	# The Guide Create, Update and Delete Mutation

	




class Query(Query, graphene.ObjectType):

	pass

schema = graphene.Schema(query  = Query, mutation = Mutation)