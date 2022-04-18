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
# Inside profiles table, savedrecipe_ids is a single string with '|' as delimiter for each id.
# userObject parameter is equal to request.user in views.py
#recipeID=Recipe title. In recipes table, title is used as primary key since we dont want duplicate titles anyways.

#input is djangos user object. It initialzies a row in profiles table for this newly registered user
def addNewProfile(userObject):
    username=str("'"+userObject.get_username()+"'")
    userid=str(userObject.id)
    default_savedrecipe_ids="''"
    default_createdrecipe_ids="''"
    cursor=conn.cursor()
    cursor.execute("INSERT INTO profiles (userid, username, savedrecipe_ids, createdrecipe_ids) VALUES ("+userid+", "+username+ ", "+ default_savedrecipe_ids+ ", "+default_createdrecipe_ids +");")



#input username and recipeid string. recipeid will be added to users savedrecipe_ids in proifles table. Nothing is returned.
def saveRecipeToProfile(userObject, recipeid):
    username=str("'"+userObject.get_username()+"'")

    cursor=conn.cursor()
    ids=getUsersSavedRecipeIds(userObject)
    ids.append(recipeid) 
    idsString="'"+ ('|'.join(ids)) +"'"
    print("SAVING RECIPE TO PROFILE with saved ids: "+idsString +"and username: "+username)
    cursor.execute("UPDATE profiles SET savedrecipe_ids="+idsString +"WHERE username="+username +";")


#input user object, returns a list of strings representing recipe ids user has saved.
def getUsersSavedRecipeIds(userObject):
    username=str("'"+userObject.get_username()+"'")
    cursor=conn.cursor()
    cursor.execute("SELECT savedrecipe_ids FROM profiles WHERE username=" + username +";") 
    row = cursor.fetchone()[0] #| sep string containing ids
    if row != None:
        recipeids=row.split("|") #list of recipe ids
        cursor.close()
        if "" in recipeids:
            recipeids.remove("")
        return recipeids
    else:
        return []



#input a recipeID string, return the title string associated to that id in recipes db table
def getRecipeTitle(recipeID):
    cursor=conn.cursor()
    cursor.execute("SELECT title FROM recipes WHERE recipeid='" + recipeID +"';")
    title=cursor.fetchone()[0]
    return title



#input username and recipeid string. recipeid will be removed from users savedrecipe_ids in profiles table. Nothing is returned. 
def removeSavedRecipeFromProfile(userObject, recipeid):
    username=str("'"+userObject.get_username()+"'")
    cursor=conn.cursor()
    ids=getUsersSavedRecipeIds(userObject)
    ids.remove(recipeid) #list of ids now has input recipeid removed
    idsString='|'.join(ids)
    cursor.execute("UPDATE profiles SET savedrecipe_ids='"+idsString +"' WHERE username='"+username +"';")


#input user object, returns a list of strings representing recipe ids user has saved.
def getUsersCreatedRecipeIds(username):
    cursor=conn.cursor()
    cursor.execute("SELECT createdrecipe_ids FROM profiles WHERE username='" + username +"';") 
    row = cursor.fetchone()[0] #| sep string containing ids
    if row != None:
        recipeids=row.split("|") #list of recipe ids
        cursor.close()
        if '' in recipeids:
            recipeids.remove('')
        return recipeids
    else:
        return []

#add a new user created recipe to recipes table.
def addNewUserCreatedRecipe(title,ingredientsStr,instructionsStr, userCreated):
    cursor=conn.cursor()
    #add to sites recipes table
    cursor.execute("INSERT INTO recipes (title, ingredients, instructions, userCreated) VALUES ('"+title+"','"+ingredientsStr+"','"+instructionsStr+"','"+userCreated+"');")
    cursor.close()
    #add to profiles created recipes
    cursor2=conn.cursor()
    ids=getUsersCreatedRecipeIds(userCreated)
    ids.append(title) #append new title id
    idsString='|'.join(ids)
    print("USER CREATED idstring: "+idsString)
    cursor2.execute("UPDATE profiles SET createdrecipe_ids='"+idsString +"' WHERE username='"+userCreated +"';")
    cursor2.close()
