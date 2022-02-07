from atlassian import Confluence
import bookstack
import json
import configparser

config = configparser.RawConfigParser()
config.read('config.properties')

confluence_config = dict(config.items('Confluence'))
bookstack_config = dict(config.items('Bookstack'))

confluence = Confluence(url=confluence_config.get('url'), username=confluence_config.get('username'), password=confluence_config.get('password'))
bookStackInstance = bookstack.BookStack(base_url =bookstack_config.get('base_url'), token_id = bookstack_config.get('token_id'), token_secret = bookstack_config.get('token_secret'))

print(bookStackInstance.generate_api_methods())
print('BOOKSTACK\n')

allSpaces = confluence.get_all_spaces(start=0, limit=500, expand=None)
results = allSpaces.get('results')
print(results)

print('\nCONFLUENCE\n')

for Result in results:
   postArray = { "name" : Result.get('name'), "description" : 'Automated Import', "books" : []}
   print(postArray)