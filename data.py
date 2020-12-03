import json

with open('directories.json') as direc:
    direc_dict = json.load(direc)
with open(direc_dict["apis"], 'r') as apis:
    apis_dict = json.load(apis)
with open(direc_dict["gfys"], 'r') as gfys:
    gfys_dict = json.load(gfys)
with open(direc_dict["levels"], 'r') as usrs:
    users = json.load(usrs)
with open(direc_dict["recents"], 'r') as rece:
    recent_dict = json.load(rece)
with open(direc_dict["contri"], 'r') as cont:
    contri_dict = json.load(cont)
with open(direc_dict["custom"], 'r') as cus:
    custom_dict = json.load(cus)
with open(direc_dict["reddit"], 'r') as redd:
    reddit_dict = json.load(redd)