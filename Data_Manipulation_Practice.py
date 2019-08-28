import numpy as np
import pandas as pd

FIFA = pd.read_csv('fifa.csv')
FIFA.rename(columns={' position':'position',' height':'height'}, inplace=True)

#You've contacted FIFA for some data and they handed you two some data. 

#Step1: Please select the two columns from FIFA dataframe: positions and heights

#positions = pd.read_csv("../fifa positions.csv")
#heights = pd.read_csv("../fifa heights.csv")

#np_positions = np.array(positions)
#np_heights = np.array(heights)

positions=np.array(FIFA.position)
heights=np.array(FIFA.height)

#Each element in the lists corresponds to a player. 
#The first list, positions, contains strings representing each player's position.
#The possible positions are: ' GK' (goalkeeper), ' M' (midfield), ' A' (attack) and ' D' (defense)

#The second list, heights, contains integers representing the height of the player in cm.

#You're fairly confident that the median height of goalkeepers is higher than that of other players 
#on the soccer field. Some of your friends don't believe you, so you are determined to show them using 
#the data you received  from FIFA and your newly acquired Python skills.

#Step2: Extract all the heights of the goalkeepers. 
# You can use a trick here: use positions == ' GK' as an index for heights. Assign the result to gk_heights
# Heights of the goalkeepers: gk_heights

gk_heights=heights[positions==' GK']

#Step3: Extract all the heights of all the other players. 
# This time use positions != ' GK' as an index for heights. Assign the result to other_heights
# Heights of the other players: other_heights`

other_heights=heights[positions!=' GK']

#Step4: Print out the median height of goalkeepers. Replace 'None' with the correct code
print("Median height of goalkeepers: "+str(np.median(gk_heights)))

#Step5: Print out the median height of other players. Replace 'None' with the correct code
print("Median height of other players: "+str(np.median(other_heights)))
