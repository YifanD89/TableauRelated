import tableauserverclient as TSC

tableau_auth = TSC.TableauAuth('username', 'password','site')
server = TSC.server('server_url')

with server.auth.sign_in(tableau_auth):
	all_datasources, pagination_item = server.datasources.get()
	print([datasource.name for datasource in all_datasources])
	print()

	all_projects,pagination_item = server.projects.get()
	print([project.name,project.id for project in all_projects])

	project_id = 'project_id'
	file_path = 'hyperfileName.hyper'
	new_datasource = TSC.DatabaseItem(project_id)
	new_datasource = server.datasources.publish(
						new_datasource,file_path,'CreateNew')