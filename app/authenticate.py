from app import routes

def is_authenticated():
	print(routes.get_user())