import requests
import json

class ApigeeAPI:

	headers = {'Authorization': 'Basic YXBpYWRtaW5AY2lyY3Vsb2RlY3JlZGl0by5jb20ubXg6cH0qR1EsIyFrIVNAOGFgIg=='}
	domain = "https://api.enterprise.apigee.com/v1/organizations/"

	def __init__(self,organizations,headers):
		self.headers = headers
		self.domain = self.domain+organizations

	def get_developers(self):
		payload = None
		url = self.domain+"/developers"

		response = requests.get(url, data=payload, headers=self.headers)

		return json.loads(response.content)

	def get_developers_app(self,dev):
		payload = None
		url = self.domain+"/developers/"+dev+"/apps"

		response = requests.get(url, data=payload, headers=self.headers)

		return json.loads(response.content)

	def get_developers_app_details(self,dev,app):
		payload = None
		url = self.domain+"/developers/"+dev+"/apps/"+app

		response = requests.get(url, data=payload, headers=self.headers)

		return json.loads(response.content)

	def list_developers_details_apps(self):
		developers = self.get_developers()
		for dev in developers:
			print "dev: "+dev
			apps = self.get_developers_app(dev)
			for app in apps:
				print "-app: "+app
				details_app = self.get_developers_app_details(dev,app)			
				print "--appId: "+details_app['appId']
				for credential in details_app['credentials']:
					print "--consumerKey: "+credential['consumerKey']

	def search_consumerKey(self,consumerKey):
		developers = self.get_developers()
		print len(developers),
		for dev in developers:
			print '.',
			apps = self.get_developers_app(dev)
			print len(apps),
			for app in apps:
				print '.',
				details_app = self.get_developers_app_details(dev,app)			
				print len(details_app['credentials']),
				for credential in details_app['credentials']:
					print '.',				
					if credential['consumerKey'] == consumerKey:
						return {
							"dev":dev,
							"app":app,
							"appId":details_app['appId'],
							"consumerKey":consumerKey
						}
				print '-'
		return None