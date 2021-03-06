#How to design a REST API - STEPS

	#Create Object Model
	#Create URIs
	#Create Representations
	#Assign HTTP Methods
	#Logging
	#Security
	#Discovery




#EXPANSION OF STEPS

	#Create Object Model

		#identify which objects will be resources
		#identify which objects will be subresources
		#assign a unique identifier to each resource and sub resource???


	#Create URIs

		#assign a unique identifier to each resource and sub resource???



	#Create Representations

		#Collection Resource - Players
		#Single Resource - Player
		#Collection Resource - Matches Played
		#Single Resource - Matches Played
		#Collection Resource - Matches Played Under Single Player
		#Single Resource - Matches Played Under Single Player


	#Assign HTTP Methods - GET, POST, PUT, DELETE

		#Browse all devices or configurations [Primary Collection]
		#Browse all devices or configurations [Secondary Collection]
		#Browse single device or configuration [Primary Collection]
		#Browse single device or configuration [Secondary Collection]
		#Create a device or configuration
		#Update a device or configuration
		#Remove a device or configuration
		#Applying or Removing a configuration from a device





#IMPLEMENTATION OF STEPS

	#CREATE OBJECT MODEL

		# collection resources

			# arsenal first team, id = 1
			# arsenal academy, id = 2
			# arsenal coaching staff, id = 3


		# singleton resources

			# petr cech, id 11
			# danny welbeck, id 12
			# unai emery, id 31
			# juan carlos carcedo, id 32


		# sub collection resources

			# matches played
			# days at work




	#CREATE URIs

	# scheme/domain/resource

		# http://api.arsenal.com/player-management/firstteam-players - collection resource
		# http://api.arsenal.com/player-management/academy-players - collection resource
		# http://api.arsenal.com/staff-management/coaching-staff - collection resource

		# http://api.arsenal.com/player-management/firstteam-players/{player-id} - singleton resource
		# http://api.arsenal.com/staff-management/coaching-staff/{staff-id} - singleton resource

		# http://api.arsenal.com/player-management/firstteam-players/{player-id}/matches-played - sub collection resource
		# http://api.arsenal.com/staff-management/coaching-staff/{staff-id}/days-at-work - sub collection resource

		# question: a singleton resource can have a sub collection resource, but can a collection resource have a sub collection resource?

		# http://api.arsenal.com/player-management/firstteam-players/{player-id}/matches-played/{match-id} - singleton resource in sub collection resource
		# http://api.arsenal.com/staff-management/coaching-staff/{staff-id}/days-at-work/{date-id} - singleton resource in sub collection resource





		# http://api.arsenal.com/player-management/firstteam-players/11 - singleton resource - petr cech
		# http://api.arsenal.com/player-management/firstteam-players/12 - singleton resource - danny welbeck


		# http://api.arsenal.com/player-management/coaching-staff/31 - singleton resource - unai emery
		# http://api.arsenal.com/player-management/coaching-staff/32 - singleton resource - juan carlos carcedo




'''
	#CREATE REPRESENTATIONS

		#THE BELOW IS WRITTEN IN XML


		#TEMPLATE FOR REPRESENTATIONS

			#COLLECTION RESOURCE

				<collection-resource size="">
					<link rel="self" href="/collection-resource"/>


					<singleton-resource id="id">
						<link rel="self" href="/collection-resource/id"/>
					</singleton-resource>


				</collection-resource>


			#SUB-COLLECTION RESOURCE UNDER SINGLETON RESOURCE

				<sub-collection-resource size="">
					<link rel="self" href="/collection-resource/id/sub-collection-resource"/>


					<sub-singleton-resource id="id">
						<link rel="self" href="/collection-resource/id/sub-collection-resource/id"/>
						<link rel="detail" href="/sub-collection-resource/id"/>
					</sub-singleton-resource>


				</sub-collection-resources>





		#REPRESENTATION FOR COLLECTION RESOURCE - FIRST TEAM PLAYERS

			<firstteam-players size="26">
			    <link rel="self" href="/firstteam-players"/>
			 

			    <firstteam-player id="11">
			    	<link rel="self" href="/firstteam-players/11"/>
			    	...
			    </firstteam-player>

			    
			    <firstteam-player id="12">
		    	    <link rel="self" href="/firstteam-players/12"/>
		    	    ...
			    </firstteam-player>


			</firstteam-players>


		#REPRESENTATION FOR SINGLETON RESOURCE - FIRST TEAM PLAYER
			
			<firstteam-player id="11">
			    <link rel="self" href="/firstteam-players/11"/>
			    ...
			 
			    <matches-played size="2">
		   		    <link rel="self" href="/matches-played"/>


				    <match-played id="567">
		   	   		    <link rel="self" href="/matches-played/567"/>
				    </match-played>

				    
				    <match-played id="789">
		   	   		    <link rel="self" href="/matches-played/789"/>
				    </match-played>

			    </matches-played>


			</firstteam-player>


		#REPRESENTATION FOR SUB COLLECTION RESOURCE - MATCHES PLAYED

			<matches-played size="38">
			    <link rel="self" href="/matches-played"/>
			 

			    <match-played id="001">
		    	    <link rel="self" href="/matches-played/001"/>
			    	...
			    </match-played>

			    
			    <match-played id="002">
		    	    <link rel="self" href="/matches-played/002"/>
			    	...
			    </match-played>


			    ...


			    ...


			</matches-played>


		#REPRESENTATION FOR SINGLETON RESOURCE IN SUB COLLECTION RESOURCE - MATCH PLAYED

		    <match-played id="001">
			    <link rel="self" href="/matches-played/001"/>
			    ...
			    <link rel="match-outcome" href="/matches-played/001/match-outcome"/>

			
			</match-played>


		#REPRESENTATION FOR SUB COLLECTION RESOURCE UNDER SINGLETON RESOURCE - MATCHES PLAYED UNDER SINGLE PLAYER

			<matches-played size="38">
			    <link rel="self" href="/firstteam-players/11/matches-played"/>
			 

			    <match-played id="001">
		    	    <link rel="self" href="/firstteam-players/11/matches-played/001"/>
		       	    <link rel="detail" href="/matches-played/001"/>
			    	...
			    </match-played>

			    
			    <match-played id="002">
			    	<link rel="self" href="/firstteam-players/11/matches-played/002"/>
		       	    <link rel="detail" href="/matches-played/002"/>
			    	...
			    </match-played>


			    ...


			    ...


			</matches-played>


		#REPRESENTATION FOR SINGLETON RESOURCE UNDER SINGLETON RESOURCE - MATCH PLAYED UNDER SINGLE PLAYER

		    <match-played id="001">
		    	<link rel="self" href="/firstteam-players/11/matches-played/001"/>
			    <link rel="detail" href="/matches-played/001"/>
			    ...
			    <link rel="match-outcome" href="/matches-played/001/match-outcome"/>

			
			</match-played>	





	#ASSIGN HTTP METHODS 		

	# what do i write (and where do i write it) to map http operations to the appropriate URIs????


		#GET
		#POST
		#PUT
		#DELETE


		# Browse all firstteam-players or matches-played [Primary Collection]
		
			HTTP GET /firstteam-players
			HTTP GET /matches-played

				#apply paging and filtering

					HTTP GET /firstteam-players?startIndex=0&size=20
					HTTP GET /matches-played?startIndex=0&size=20


			# browse all matches-played [Secondary Collection]

				HTTP GET /firstteam-players/{id}/matches-played


			# browse a single firstteam-player or match-played [Primary Collection]

				HTTP GET /firstteam-players/{id}
				HTTP GET /matches-played/{id}


			# browse a single match-played [Secondary Collection]

				HTTP GET /firstteam-players/{id}/matches-played/{id}


		# Create a firstteam-player or match-played

			HTTP POST /firstteam-players
			HTTP POST /matches-played

			# the request payload will not contain any id attribute, as the server is responsible for deciding the id(?)


		# Update a firstteam-player or match-played

			HTTP PUT /firstteam-players/{id}
			HTTP PUT /matches-played/{id}


		# Delete a firstteam-player or match-played

			HTTP DELETE /firstteam-players/{id}
			HTTP DELETE /matches-played/{id}
		

		# Applying or removing a match played to/from a player

			# Applying

			HTTP PUT /firstteam-players/{id}/matches-played 	#no {id} specified for matches-played: should this be PUT or POST??????
 
			# Removing


			HTTP DELETE /firstteam-players/{id}/matches-played/{id} 




	#LOGGING
	#SECURITY
	#DISCOVERY

'''

		

#import libraries

from flask import Flask, request
from flask_restful import Resource, Api





#create your app and api objects

app = Flask(__name__)
api = Api(app)





#create your resources

class ViewPlayer12(Resource):

	def get(self):
		return{'player':'danny welbeck'}


class UpdatePlayer12(Resource):

	def post(self):
		message = request.get_json()
		return{'you have posted:':message}


class ViewPlayer11(Resource):

	def get(self):
		return{'player':'petr cech'}


class UpdatePlayer11(Resource):

	def post(self):
		message = request.get_json()
		return{'you have posted:':message}




#add your resources and URIs to your api

# api.add_resource(resource, URI)

api.add_resource(ViewPlayer12, '/player-management/firstteam-players/12')
api.add_resource(UpdatePlayer12, '/player-management/firstteam-players/12')

api.add_resource(ViewPlayer11, '/player-management/firstteam-players/11')
api.add_resource(UpdatePlayer11, '/player-management/firstteam-players/11')





#run in debug mode

if __name__=='__main__':
	app.run(debug=True, port=8080)