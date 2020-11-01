		# GraphQL Imports

import graphene
from graphql import GraphQLError


		# The Root App Schema

from travelly.graph.app_schema import(

		PostType,
		CommentType

	)

		# Models For My App

from .models import(

		Post,
		Comment,

	)


		# Post Create Mutation
		
 class PostCreateMutation(graphene.Mutation):

 	post 				= graphene.Field(PostType)

 	class Arguments:

 		user_id 		= graphene.Int()
 		text 			= graphene.String()
 		photo 			= graphene.String()
 		video 			= graphene.String()
 		location		= graphene.String()
 		created_at 		= graphene.DateTime()

 	def mutate(self, info, user_id, text, photo, video, location, created_at):

 		user_id 				=  info.context.user.id

 		if user_id.is_anonymous:

 			raise GraphQLError("You Must Be Logged In To Create Post")

 		else:
 			post_obj  	 		= Post.objects.create(

 					user 		= user_id,
 					text 		= text,
 					photo 		= photo,
 					video 		= video,
 					location	= location,
 					created_at	= created_at

 				)

 			post_obj.save()

 		return PostCreateMutation(post = post_obj)


		# Post update Mutation

class PostUpdateMutation(graphene.Mutation):

	post 				=  graphene.Field(PostType)

	class Arguments:

		post_id			= graphene.Int()
		text 			= graphene.String()
 		photo 			= graphene.String()
 		video 			= graphene.String()
 		location		= graphene.String()

 	def mutate(self, info, post_id, text, photo, video, location):

 		user  			= info.context.user

 		if user.is_anonymous:
 			raise GraphQLError("You Must be Logged In To Edit Post")

 		else:
 			post_obj = Post.objects.get(pk = post_id)
 			post_obj.user 		= user
 			post_obj.text 		= text
 			post_obj.photo 		= photo
 			post_obj.video		= video
 			post_obj.location 	= location

 			post_obj.save() 

 		return PostUpdateMutation(post = post_obj)


		# Post Delete Mutation


class PostDeleteMutation(graphene.Mutation):

	post  		=  graphene.Field(PostType)


	class Arguments:

		post_id = graphene.Field()


	def mutate(self, info, post_id):

		user 		= info.context.user_id

		if user.is_anonymous:
			raise GraphQLError("You Must Be Logged In To Delete Post")

		else:
			post_obj = Post.objects.get(pk = post_id)

			post_obj.delete()

		return None




		# Post Like Toggle Mutation.

class PostLikeToggleMutation(graphene.Mutation):

	post 				= graphene.Field(PostType)

	class Arguments:

		post_id 		= graphene.Int()

	def mutate(self, info, post_id):
		user 			= info.context.user

		post_obj 		= Post.Objects.filter(id = post_id).first()

		if user.is_anonymous:

			raise GraphQLError("You Must be Logged In To Like This Post")

		if user in post_obj.likes.all():

			post_obj.likes.remove(user)
		else:
			post_obj.likes.add(user)

		return PostLikeToggleMutation (post = post_obj)

		# Comment Create Mutation

class CommentCreateMutation(graphene.Mutation):

	comment 			=  graphene.Field(CommentType)

	class Arguments:

		target_id 			= graphene.Int()
		text 				= graphene.String()
		photo 				= graphene.String()
		created_at			= graphene.DateTime()


	def mutate(self, info, target, text, photo, created_at):

		user  				=  	info.context.user
		target_obj 			= 	Post.objects.filter(pk  = target).first()
		if user.is_anonymous:
			raise GraphQLError("You Must Be Logged In To Create Comments")	

		else:

			comment_obj = Comment.objects.create(

					user 		= user,
					target 		= target_obj,
					text 		= text,
					photo 		= photo,
					created_at 	= created_at	

				)

			comment_obj.save()

		return CommentCreateMutation(comment = comment_obj)




		# Comment Update Mutation


		# Comment Delete Mutation



