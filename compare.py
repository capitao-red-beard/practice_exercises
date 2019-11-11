local_campaigns = {'j_whitespace_test'}
google_campaigns = [
					{'id': 2030300590, 'name': 'some_campaign'},
				    {'id': 2030300591, 'name': 'j_whitespace_test'},
				    {'id': 2030300592, 'name': 'x_whitespace_test'},
				    {'id': 2030300593, 'name': 'a_whitespace_test'}
				   ]

result = [c for c in google_campaigns if c['name'] not in local_campaigns]
result.sort(key=lambda x: x['name'])

print(result)
