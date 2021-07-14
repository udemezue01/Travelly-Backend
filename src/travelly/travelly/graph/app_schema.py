import graphene
from graphene_django.types import DjangoObjectType
from graphql import GraphQLError

'''
App models

'''

from django.contrib.auth import get_user_model
User = get_user_model()


from tour.models import (

		Tour,
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


	def resolve_avatar(self, info):

		return info.context.build_absolute_uri(self.avatar.url)

	def resolve_cover_photo(self, info):

		return info.context.build_absolute_uri(self.cover_photo.url)


		# The Tour Model


class TourType(DjangoObjectType):

	class Meta:

		model = Tour

	featured_image = graphene.String()

	gallery_images = graphene.String()

	def resolve_featured_image(self, info):

		return info.context.build_absolute_uri(self.featured_image.url)

	def gallery_images(self, info):

		return info.context.build_absolute_uri(self.gallery_images)



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

	photo   =  graphene.String()
	video 	=  graphene.String()


	def resolve_photo(self, info):
		return info.context.build_absolute_uri(self.photo)

	def resolve_video(self, info):
		return info.context.build_absolute_uri(self.video)

		# The Comment Model

class CommentType(DjangoObjectType):

	class Meta:

		model = Comment

	photo  		= graphene.String()

	def resolve_photo(self, info):

		return info.context.build_absolute_uri(self.photo)






class Query(object):

	# The User Detail

	me  			= 	graphene.Field(UserType)

	# The Profile Detail

	profile 		= 	graphene.Field(ProfileType)

	# The Guide List and Detail Query

	tours 			=  	graphene.List(TourType)
	tour 			= 	graphene.Field(TourType, id = graphene.Int())

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

	def resolve_tours(self, info, **kwargs):

		user 		=  info.context.user

		if user.is_anonymous:

			raise GraphQLError("You must be authenticated to view this guides")

		else:

			return Tour.objects.all()


	def resolve_tour(self, info, **kwargs):

		user 		= info.context.user
		id 			= kwargs.get('id')

		if user.is_anonymous:

			raise GraphQLError("you must be authenticated to view this guide")

		else:
			return Tour.objects.get(pk = id)


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










