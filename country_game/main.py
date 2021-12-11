import turtle
import pandas
screen = turtle.Screen()
screen.title("Cameroon Regions")
image = "cameroon.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("regions.csv")
all_regions = data.regions.to_list()
guessed_region = []

while len(guessed_region) < 10:
    answer_region = screen.textinput(title=f"{len(guessed_region)}/10 guessed regions", prompt="Whats other"
                                                                                               " region").title()
    print(answer_region)
    if answer_region == "Exit":
        missing_region = []
        for regions in all_regions:
            if regions not in guessed_region:
                missing_region.append(regions)
        break
    if answer_region in all_regions:
        guessed_region.append(answer_region)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        region_data = data[data.regions == answer_region]
        t.goto(int(region_data.x), int(region_data.y))
        t.write(answer_region)




