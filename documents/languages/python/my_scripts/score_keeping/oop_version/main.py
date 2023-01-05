from graphmaster import GraphMaster

graphmaster = GraphMaster()

while True:
    try:
        choice = input("What do you want to fill? 'pomokiller' or 'katamaster'? ")
        if choice == "pomokiller":
            pomos_killed = input("How many pomos have you killed today, sir? ")
            graphmaster.insert_pixel_in_pomokiller(pomos_killed)
        if choice == "katamaster":
            katas_trained = input("How many katas have you trained today, sir? ")
            graphmaster.insert_pixel_in_katamaster(katas_trained)
    except KeyboardInterrupt:
        print()
        print("Bye, sir.")
        exit()

    
