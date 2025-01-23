greeting = "Hallo"
name = "Paul"
text = "Wollen wir uns am Wochenende treffen?"
finalization = "Bis Bald!"

message = "{} {}\n{} \n\n{}".format(greeting, name, text, finalization)

with open("D:\\Christoph\\Nebentätigkeit\\IU\\EP\\output.txt", "w") as file:
    file.write(message)
