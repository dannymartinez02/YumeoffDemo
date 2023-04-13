label splashscreen:
    jump expression renpy.random.choice(["splash1", "splash2", "splash3"])

label splash1:
    scene splashscreen with dissolve
    "No deberias abrir esto si estas triste..."
    return

label splash2:
    scene splashscreen with dissolve
    "DANGER"
    return

label splash3:
    scene splashscreen with dissolve
    "No deberias estar aqui..."
    return



label start:


    define pov = Character ("[povname]", color="#FF0000")
    define ka = Character("Kaori", who_color="#EA899A")
    define ts = Character("Tsukasa", who_color= "#7d2181")
    define mk = Character("Miko", who_color= "#568203")
    define r = Character("Rin", who_color= "#DC143C")
    define e = Character("Erika", who_color= "#ff7700")
    define ku = Character("Kuta", who_color= "#3b83bd")

    define t = Character("???", who_color= "#7d2181")
    define m = Character("???", who_color= "#568203")
    define ri = Character("???", who_color= "#DC143C")
    define ek = Character("???", who_color= "#ff7700")

    $ chapter = 0

    call ch0_main

    $ chapter = 1

    call ch1_main

    $ chapter = 2

    call ch2_main
    
    $ chapter = 3

    call ch3_main

    $ chapter = 4

    call ch4_main

    $ chapter = 5
    
    call ch5_main

return