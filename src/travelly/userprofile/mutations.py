		# GraphQL Imports

import graphene
from graphql import GraphQLError


		# The Root App Schema

from travelly.graph.app_schema import(

		ProfileType,


	)

		# Models For My App

from .models import(

		Profile,

	)



		# Profile Create Mutation



class ProfileCreateMutation(graphene.Mutation):

	profile 			= 	graphene.Field(ProfileType)

	class Arguments:

		avatar 			= 	graphene.String()
		cover_photo 	= 	graphene.String()
		username		= 	graphene.String()
		bio 			= 	graphene.String()
		location		= 	graphene.String()



	def mutate(self, info, avatar, cover_photo, username, bio, location):

		user 			=  	info.context.user

		# TODO: To validate a username to check for duplicate

		if user.is_anonymous:

			raise GraphQLError("You Must Be Logged In To Create A Profile")

		else:

			profile_obj 			= 	Profile.objects.create(

					user 			= user,
					avatar			= avatar,
					cover_photo		= cover_photo,
					username	 	= username,
					bio 			= bio,
					location		= location

				)
			profile_obj.save()

		return ProfileCreateMutation(profile = profile_obj)



class ProfileUpdateMutation(graphene.Mutation):

	profile 			= 	graphene.Field(ProfileType)

	class Arguments:

		profile_id 		= graphene.Int()
		avatar			= graphene.String()
		cover_photo 	= graphene.String()
		username		= graphene.String()
		bio 			= graphene.String()
		location 		= graphene.String()



	def mutate(self, info, profile_id, avatar, cover_photo, username, bio, location):

		user 			= info.context.user

		# TODO: To validate username and check for duplicate
		if user.is_anonymous:
			raise GraphQLError("You Must Be Logged In To Edit Profile")

		else:

			profile_obj				= Profile.objects.get(pk = profile_id)
			profile_obj.avatar		= avatar,
			profile_obj.cover_photo	= cover_photo,
			profile_obj.username	= username,
			profile_obj.bio 		= bio,
			profile_obj.location	= location

			profile_obj.save()

		return ProfileUpdateMutation(profile = profile_obj)