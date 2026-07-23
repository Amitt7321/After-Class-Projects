class Robot:
    type ="Robot"
    name ="Biton"
    year = 2026

    def __init__(self, type,name,year):
           self.type=type
           self.name=name
           self.year=year
        
biton = Robot("Robot","Biton",2026)

print("Biton is a {}".format(biton.type))


print("{} is made in {}".format (biton.name,biton.year))