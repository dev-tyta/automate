import shelve

shelfData = shelve.open("mydata")
musicians = ["Khalid", "Wizkid", "James Arthur", "Lewis Capaldi", "Jacob Banks"]

shelfData["musicians"] = musicians
shelfData.close()
