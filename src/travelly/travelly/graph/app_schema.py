import graphene
from graphene_django.types import DjangoObjectType
from graphql import GraphQLError

'''
App models

'''

from django.contrib.auth import get_user_model
User = get_user_model()


from guide.models import (

		Guide,
		Review,
		Booking

	)

from post.models import (


	Post,
	Comment,

	)

from userprofile.models import(

	Profile

	)



		# The User Model


class UserType(DjangoObjectType):

	class Meta:
		model = User






		# The Profile Model

class ProfileType(DjangoObjectType):

	class Meta:

		model = Profile

	avatar 	 		= graphene.String()
	cover_photo 	= graphene.String()




		# The Guide Model


class GuideType(DjangoObjectType):

	class Meta:

		model = Guide

		# The Review Model


class ReviewType(DjangoObjectType):

	class Meta:

		model = Review

		# The Booking Model


class BookingType(DjangoObjectType):

	class Meta:
		model = Booking

		# The Post Model

class PostType(DjangoObjectType):

	class Meta:

		model = Post

		# The Comment Model

class CommentType(DjangoObjectType):

	class Meta:

		model = Comment






class Query(object):

	# The User Detail

	me  			= 	graphene.Field(UserType)

	# The Profile Detail

	profile 		= 	graphene.Field(ProfileType)

	# The Guide List and Detail Query

	guides 			=  	graphene.List(GuideType)
	guide 			= 	graphene.Field(GuideType, id = graphene.Int())

	# The Review List and Detail Query

	reviews			= 	graphene.List(ReviewType)
	review 			= 	graphene.Field(ReviewType, id = graphene.Int())

	# The Booking List and Detail Query


	Bookings 		= 	graphene.List(BookingType)
	Booking 		= 	graphene.Field(BookingType, id = graphene.Int())

	# The Post List and Detail Query 

	posts 			= 	graphene.List(PostType)
	post 			= 	graphene.Field(PostType, id = graphene.Int())


	# The Comment List and Detail Query


	comments 		= 	graphene.List(CommentType)
	comment 		= 	graphene.Field(CommentType, id = graphene.Int())

	# The Authentication resolve Method




	# The User Detail Resolve Method


	def resolve_me(self, info, **kwargs):

		user 	=  info.context.user
		if user.is_anonymous:
			raise GraphQLError("You Must be authenticated to access this User")

		else:

			return user

	# The Profile Detail Resolve method

	def resolve_profile(self, info, **kwargs):

		user 	 = info.context.user

		if user.is_anonymous:

			raise GraphQLError('You must be authenticated to view this profile')

		else:

			return user.profile

	# The Guide List and Detail Resolve  Method

	def resolve_guides(self, info, **kwargs):

		user 		=  info.context.user

		if user.is_anonymous:

			raise GraphQLError("You must be authenticated to view this guides")

		else:

			return Guide.objects.all()


	def resolve_guide(self, info, **kwargs):

		user 		= info.context.user
		id 			= kwargs.get('id')

		if user.is_anonymous:

			raise GraphQLError("you must be authenticated to view this guide")

		else:
			return Guide.objects.get(pk = id)


	# The Post List and Detail Resolve Method


	def resolve_posts(self, info, **kwargs):

		user 		=  info.context.user

		if user.is_anonymous:

			raise GraphQLError("You must be authenticated to view this posts")

		else:
			return Post.objects.filter(user= user)

	def resolve_post(self, info, **kwargs):

		user 		= info.context.user
		id 			= kwargs.get('id')
		if user.is_anonymous:
			raise GraphQLError("You must be authenticated to view this post")

		else:
			return Post.objects.get(pk = id)

	# The Comments List and Detail Resolve Method


	def resolve_comments(self, info, **kwargs):

		user 		=   info.context.user
		pass


	def resolve_comment(self, info, **kwargs):

		pass










