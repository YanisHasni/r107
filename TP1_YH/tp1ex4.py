MinuteEcoule = int(input("Entrez le nombre de minutes ecoulées."))
heure = (MinuteEcoule //60 ) % 24
jour = (MinuteEcoule // 60) //24
minute = (MinuteEcoule % 60)
print( " La date associée aux minutes écoulées est le: " , jour ,"à" , heure , "heure" , minute , "minutes")
