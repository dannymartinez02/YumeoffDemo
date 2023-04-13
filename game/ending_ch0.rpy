label ch5_main:
    scene genoff with fade

    "AHHHHHHHHHHH, TODOS APARTENSE DE MI LADO, PROBLEMAS EN LA OFICINA"

    "Kaori no parece ser un ser humano pensante justo ahora…"

    "Auch…"

    ku "Eso no fue nada agradable…"

    ka "Ay… Ay… Ay… AHHHHH LOS PAPELES"

    "Quien diría que Miko no es la única que causa estos accidentes…"

    stop music fadeout 1.0

    "Y un sonido de cerámica suena a lo lejos… 
    Y precisamente la chica de cabello rubio y su acompañante de color verde aparece en escena…"

    mk "Ahhh… Lo siento… Lo siento"

    e "Miko, te repetí dos veces que no es tu culpa, todo está bien, definitivamente podrás 
    demostrarlo cuando me devuelvas el coste de mi taza a final de mes…"

    play music "audio/miscal.mp3"

    "Enserio… "

    ts "Señorita Miko… Señorita Kaori… Señorita Erika… Señorita Rin… A mi oficina por favor…"

    ku "Ah, parece que tengo una llamada de mi madr…"

    ts "Señor Kuta, por favor puede venir…"

    "Y mis posibilidades de escape se van por la borda…"

    scene tsukasaoff with dissolve

    "Al finalizar tras una breve reunión de… 5 minutos termino quedando solo con la superior"

    ts "Escucha eres nuevo lo sé, y estas haciendo un trabajo maravilloso sabes… Esto…"

    "Si, seguro dirá que lamenta pedirme lo siguiente…"

    ts "Pero lamento pedirte esto…"

    "Bingo"

    ts "Pero quiero que ayudes a alguna de las chicas aquí, definitivamente el trabajo se acumulo por alguna razón, 
    aun sabiendo que estas fechas ya no son precisamente las mas saturadas de trabajo" 
    
    ts "Asi que por esa razón quiero que elijas una compañera…"

    "Entonces… Que debería hacer…"

    menu:
        "Ayudar a Kaori":
            jump error

        "Ayudar a Miko":
            jump error
        
        "Ayudar a Rin":
            jump error

        "Ayudar a Erika":
            jump error

        "Podria ayudarla a Usted":
            jump error

label error:
    pause 1.0

    
    "Entonces… Que debería hacer…"

    menu:
        "Ayudar a Kaori":
            jump error2

        "Ayudar a Miko":
            jump error2
        
        "Ayudar a Rin":
            jump error2

        "Ayudar a Erika":
            jump error

        "Podria ayudarla a Usted":
            jump error2

label error2:
    pause 1.0
    
    "Entonces… Que debería hacer…"

    menu:
        "Ayudar a Kaori":
            jump error3

        "Ayudar a Miko":
            jump error3
        
        "Ayudar a Rin":
            jump error

        "Ayudar a Erika":
            jump error3

        "Podria ayudarla a Usted":
            jump error3

label error3:
    pause 1.0
    
    "Entonces… Que debería hacer…"

    menu:
        "Ayudar a Kaori":
            jump error4

        "Ayudar a Miko":
            jump error4
        
        "Ayudar a Rin":
            jump error4

        "Ayudar a Erika":
            jump error4

        "Podria ayudarla a Usted":
            jump error4

label error4:
    pause 1.0
    
    "Entonces… Que debería hacer…"

    menu:
        "Ayudar a Kaori":
            jump error5

        "Ayudar a Miko":
            jump error5
        
        "Ayudar a Rin":
            jump error5

        "Ayudar a Erika":
            jump error5

        "Podria ayudarla a Usted":
            jump error5

label error5:

    stop music fadeout 1.0
    pause 2.0
    
    "Eh… No has aprendido a leer…"

    play music "audio/ia1.mp3"

    pause 2.0

    "Ahí dice que no puedes pasar…"

    pause 2.0

    "Ah, sigues intentando… Bueno no te juzgo, seguro tus ganas de saber que pasara serán 
    útiles cuando todo esté listo… Parece que añadí un par de líneas de código erróneas a este sistema…"

    pause 2.0
        
    "Ah, y no te preocupes, recordare quién eres… Asi que te daré una breve advertencia…"

    pause 2.0

    "Si no vuelves, yo hare que lo hagas…"

    "No importa que tan lejos intentes ir, te vigilare, asi que prométeme que volverás…"

    menu:
        "Si...":
            jump yesu

        "No...":
            jump nou


label yesu:

    "Bien, es la respuesta que esperaba"

    "No decepcionas nunca…"

    "Asi que esto, es todo mientras tanto, vuelve pronto…"

return

label nou:

    python:
        import os
        lista_grabacion = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe"]
        lista_procesos = os.popen('wmic process get description').read().split()

    if list(set(lista_procesos).intersection(lista_grabacion)):
        call grabacion
        #pass #Pass es no hacer nada

    "Parece que alguien no comprendido que esto no es una broma"
    
    "No importa quien seas… Te encontrare… Asi que…"

    "Eso es todo, te espero"

return

label grabacion:
    
    "Parece que alguien no comprendido que esto no es una broma, no sé cuántas personas estén viendo esto…"

    "Mientras lo transmites ¿no?"

    "Pero ellos lo recordaran, jaja…"

    "Asi que esto, es todo mientras tanto, vuelve pronto…"

return