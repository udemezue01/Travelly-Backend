import graphene


from .app_schema import Query



# class Mutation(graphene.ObjectType):

# 	pass




class Query(Query, graphene.ObjectType):

	pass

schema = graphene.Schema(query  = Query,)