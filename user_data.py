# Storing user data in discord.py using a dictionary
async def user_data(ctx):  
  user_data = {}
  # Storing user data based on user id
  
  user = (ctx.author)
  user_data[user.id] = {
      "username": user.name,
      "Qi" : 0,
      "Qi_Max" : 100,
      "Base" : 1,
      "Multiplier" : 1,
      "Talent" : 1,
      "Talent_Max" : 100,
      "Qi Gain Speed" : 100,
  }