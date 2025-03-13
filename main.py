#Talking Data

#Setting up the program
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')

#create 3 favorite movie variables & print
favDramaMovie = "Baby Driver"
favMusicalMovie = "Mamma Mia!"
favAnimationMovie = "How the Grinch Stole Christmas"

print("My favorite Drama movie is " + favDramaMovie)
print("My favorite Musical & Performing Arts movie is " + favMusicalMovie)
print("My favorite Animation movie is " + favAnimationMovie)

#Investigate the data

#Filter drama data
print("\nThe data for my favorite Drama movie is:\n")
#Create a new variable to store your favorite Drama movie information
favDramaMovieBooleanList = movieData["movie_title"] == favDramaMovie
#print(favDramaMovieBooleanList)
faveDramaMovieData = movieData.loc[favDramaMovieBooleanList]
print(faveDramaMovieData)

print("\n\n")

#Filter Musical data
print("\nThe data for my favorite Musical & Performing Arts movie is:\n")

#Create a new variable to store your favorite Musical movie information
favMusicalMovieBooleanList = movieData["movie_title"] == favMusicalMovie

faveMusicalMovieData = movieData.loc[favMusicalMovieBooleanList]
print(faveMusicalMovieData)

print("\n\n")

#Filter Animation data
print("\nThe data for my favorite Animation movie is:\n")

#Create a new variable to store your favorite Animation movie information
favAnimationMovieBooleanList = movieData["movie_title"] == favAnimationMovie

faveAnimationMovieData = movieData.loc[favAnimationMovieBooleanList]
print(faveAnimationMovieData)

print("\n\n")

#Create a new variable to store a new data set with a Drama genre
dramaBooleanList = movieData["genres"].str.contains("Drama")
dramaMovieData = movieData.loc[dramaBooleanList]
numOfDramaMovies = dramaMovieData.shape[0]

#Create a new variable to store a new data set with a Musical & Performing Arts genre
musicalBooleanList = movieData["genres"].str.contains("Musical & Performing Arts")
musicalMovieData = movieData.loc[musicalBooleanList]
numOfMusicalMovies = musicalMovieData.shape[0]

#Create a new variable to store a new data set with a Animation genre
animationBooleanList = movieData["genres"].str.contains("Animation")
animationMovieData = movieData.loc[animationBooleanList]
numOfAnimationMovies = animationMovieData.shape[0]

print("We will be comparing " + favDramaMovie +
      ", " + favMusicalMovie + ", and " + favAnimationMovie + " to other movies released in their distinct genres.\n")
print("There are " + str(numOfDramaMovies) + " movies in the Drama genre. \n")
print("There are " + str(numOfMusicalMovies) + " movies in the Musical & Performing Arts genre. \n")
print("There are " + str(numOfAnimationMovies) + " movies in the Animation genre. \n")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favDramaMovie +
      ", " + favMusicalMovie + ", and " + favAnimationMovie +
      " compare to other movies in each of their genres.\n")

#Describe Drama data
#min
minDrama = dramaMovieData["audience_rating"].min()
print("The min audience rating of the Drama movie data set is: " + str(minDrama))
print(favDramaMovie + " is rated 82 points higher than the lowest rated Drama movie.")
print()

#find max
maxDrama = dramaMovieData["audience_rating"].max()
print("The max audience rating of the Drama movie data set is: " + str(maxDrama))
print(favDramaMovie + " is rated 14 points lower than the highest rated Drama movie.")
print()

#find mean
meanDrama = dramaMovieData["audience_rating"].mean()
print("The mean audience rating of the Drama movie data set is: " + str(meanDrama))
print(favDramaMovie + " is rated higher than the mean Drama movie rating.")
print()

#find median
medianDrama = dramaMovieData["audience_rating"].median()
print("The median audience rating of the Drama movie data set is: " + str(medianDrama))
print(favDramaMovie + " is rated higher than the median Drama movie rating.")
print()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

#Describe Musical & Performing Arts data
#min
minMusical = musicalMovieData["audience_rating"].min()
print("The min audience rating of the Musical & Performing Arts movie data set is: " + str(minMusical))
print(favMusicalMovie + " is rated 54 points higher than the lowest rated Musical & Performing Arts movie.")
print()

#find max
maxMusical = musicalMovieData["audience_rating"].max()
print("The max audience rating of the Musical & Performing Arts movie data set is: " + str(maxMusical))
print(favMusicalMovie + " is rated 34 points lower than the highest rated Musical & Performing Arts movie.")
print()

#find mean
meanMusical = musicalMovieData["audience_rating"].mean()
print("The mean audience rating of the Musical & Performing Arts movie data set is: " + str(meanMusical))
print(favMusicalMovie + " is rated lower than the mean Musical & Performing Arts movie rating.")
print()

#find median
medianMusical = musicalMovieData["audience_rating"].median()
print("The median audience rating of the Musical & Performing Arts movie data set is: " + str(medianMusical))
print(favMusicalMovie + " is rated lower than the median Musical & Performing Arts movie rating.")
print()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

#Describe Animation data
#min
minAnimation = animationMovieData["audience_rating"].min()
print("The min audience rating of the Animation movie data set is: " + str(minAnimation))
print(favAnimationMovie + " is rated 76 points higher than the lowest rated Animation movie.")
print()

#find max
maxAnimation = animationMovieData["audience_rating"].max()
print("The max audience rating of the Animation movie data set is: " + str(maxAnimation))
print(favAnimationMovie + " is rated 2 points lower than the highest rated Animation movie.")
print()

#find mean
meanAnimation = animationMovieData["audience_rating"].mean()
print("The mean audience rating of the Animation movie data set is: " + str(meanAnimation))
print(favAnimationMovie + " is rated higher than the mean Animation movie rating.")
print()

#find median
medianAnimation = animationMovieData["audience_rating"].median()
print("The median audience rating of the Animation movie data set is: " + str(medianAnimation))
print(favAnimationMovie + " is rated higher than the median Animation movie rating.")
print()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Create drama graphs
#Create drama histogram
plt.hist(dramaMovieData["audience_rating"], range = (0,100), bins=20)

#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Drama Movies Histogram")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Drama Movies")

#Prints interpretation of histogram
print(
  "According to the histogram, there is one movie with an audience rating of 4"
)
print("Close the graph by pressing the 'X' in the top right corner.")
print()

#Show histogram
plt.show()

#Create scatterplot
plt.scatter(data = dramaMovieData, x = "audience_rating", y = "critic_rating", label = "Drama Movies")
plt.legend()

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience Rating versus Critic Rating")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Prints interpretation of scatterplot
plt.scatter(data = faveDramaMovieData, x = "audience_rating", y = "critic_rating", label = favDramaMovie)
plt.legend()
print("According to the scatter plots, drama films were one of the most released genres before 2020")
print("Close the graph by pressing the 'X' in the top right corner.")
print()

#Show scatterplot
plt.show()

#Create Musical & Performing Arts graphs
#Create Musical & Performing Arts histogram
plt.hist(musicalMovieData["audience_rating"], range = (0,100), bins=20)

#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Musical & Performing Arts Movies Histogram")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Musical & Performing Arts Movies")

#Prints interpretation of histogram
print(
  "According to the histogram, there is one movie with an audience rating of 12"
)
print("Close the graph by pressing the 'X' in the top right corner.")
print()

#Show histogram
plt.show()

#Create scatterplot
plt.scatter(data = musicalMovieData, x = "audience_rating", y = "critic_rating", label = "Musical & Performing Arts Movies")
plt.legend()

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience Rating versus Critic Rating")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Prints interpretation of scatterplot
plt.scatter(data = faveMusicalMovieData, x = "audience_rating", y = "critic_rating", label = favMusicalMovie)
plt.legend()
print("According to the scatter plots, " + favMusicalMovie + " is less than the median rated films in both audience rating and critic rating")
print("Close the graph by pressing the 'X' in the top right corner.")
print()

#Show scatterplot
plt.show()

#Create Animation graphs
#Create Animation histogram
plt.hist(animationMovieData["audience_rating"], range = (0,100), bins=20)

#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Animation Movies Histogram")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Animation Movies")

#Prints interpretation of histogram
print(
  "According to the histogram, there is one movie with an audience rating of 22"
)
print("Close the graph by pressing the 'X' in the top right corner.")
print()

#Show histogram
plt.show()

#Create scatterplot
plt.scatter(data = animationMovieData, x = "audience_rating", y = "critic_rating", label = "Animation Movies")
plt.legend()

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience Rating versus Critic Rating")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Prints interpretation of scatterplot
plt.scatter(data = faveAnimationMovieData, x = "audience_rating", y = "critic_rating", label = favAnimationMovie)
plt.legend()
print("According to the scatter plots, " + favAnimationMovie + " is one of the best rated animated films in terms of both audience rating and critic rating")
print("Close the graph by pressing the 'X' in the top right corner.")
print()

#Show scatterplot
plt.show()

#Prints interpretation of scatterplot


print("\nThank you for reading through my data analysis!")
