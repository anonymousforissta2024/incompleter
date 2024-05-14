#Source: https://stackoverflow.com/questions/71639002/supabase-py-typeerror-init-got-an-unexpected-keyword-argument-headers
from supabase import create_client, Client
supabaseUrl = 'REDACTED'
supabaseKey = 'REDACTED'
supabase = create_client(supabaseUrl, supabaseKey)
path_data = supabase.table('otto').select('*').execute()
print(path_data)