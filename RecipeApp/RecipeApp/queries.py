import mysql.connector

#Connect to sql database here
config = {
  'user': 'msegan',
  'password': '50235812',
  'host': 'oceanus.cse.buffalo.edu',
  'database': 'cse442_2022_spring_team_e_db',
  'raise_on_warnings': True,
  'autocommit' : True
}
conn = mysql.connector.connect(**config)

#Notes about how data is stored:
# Inside profiles table, savedrecipe_ids is a single string with ',' as delimiter for each id.
# userObject parameter is equal to request.user in views.py


#input is djangos user object. It initialzies a row in profiles table for this newly registered user
def addNewProfile(userObject):
    username=str("'"+userObject.get_username()+"'")
    userid=str("'"+str(userObject.id)+"'")
    default_savedrecipe_ids="' '"
    cursor=conn.cursor()
    cursor.execute("INSERT INTO profiles (userid, username, savedrecipe_ids) VALUES ("+userid+", "+username+ ", "+ default_savedrecipe_ids +");")



#input username and recipeid string. recipeid will be added to users savedrecipe_ids in proifles table. Nothing is returned.
def saveRecipeToProfile(userObject, recipeid):
    username=str("'"+userObject.get_username()+"'")
    userid=str("'"+str(userObject.id)+"'")

    cursor=conn.cursor()
    ids=getUsersSavedRecipeIds(userObject)
    ids.append(recipeid) #list of ids now has input recipeid removed
    idsString="'"+ (','.join(ids)) +"'"
    cursor.execute("UPDATE profiles SET savedrecipes_ids="+idsString +" WHERE userid='"+userid +"';")


#input user object, returns a list of strings representing recipe ids user has saved.
def getUsersSavedRecipeIds(userObject):
    username=str("'"+userObject.get_username()+"'")
    userid=str("'"+str(userObject.id)+"'")
    cursor=conn.cursor()
    cursor.execute("SELECT savedrecipe_ids FROM profiles WHERE userid=" + userid +";") 
    row = cursor.fetchone() #comma sep string containing ids
    recipeids=row.split(",") #list of recipe ids
    cursor.close()
    return recipeids



#input a recipeID string, return the title string associated to that id in recipes db table
def getRecipeTitle(recipeID):
    cursor=conn.cursor()
    cursor.execute("SELECT title FROM recipes WHERE recipeid='" + recipeID +"';")
    title=cursor.fetchone()
    return title



#input username and recipeid string. recipeid will be removed from users savedrecipe_ids in profiles table. Nothing is returned. 
def removeSavedRecipeFromProfile(userObject, recipeid):
    username=str("'"+userObject.get_username()+"'")
    userid=str("'"+str(userObject.id)+"'")
    cursor=conn.cursor()
    ids=getUsersSavedRecipeIds(userObject)
    ids.remove(recipeid) #list of ids now has input recipeid removed
    idsString=','.join(ids)
    cursor.execute("UPDATE profiles SET savedrecipes_ids="+idsString +"WHERE userid="+userid +";")
