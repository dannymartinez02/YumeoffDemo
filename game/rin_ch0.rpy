label ch3_main:

     
    $ randomnum = renpy.random.randint(1,5) 
    if randomnum==1:

        $renpy.movie_cutscene("cutscenes/Rangry.avi")

        jump rinvar1

    elif randomnum==2:

        $renpy.movie_cutscene("cutscenes/Rperiod.avi")

        jump rinvar2
        
    elif randomnum==3:

        $renpy.movie_cutscene("cutscenes/Rsad.avi")

        jump rinvar3
        


label rinvar1:
    scene kutaroom with dissolve
    "Tercer día, llegó con más que tiempo para poder empezar a terminar las labores que debía, como
    siempre es un día movido, sin embargo, puedo mantener la compostura lo suficiente para apoyar"

    "Tanto a la Superior Tsukasa, Kaori y Miko, tres cosas a la vez por un día, deberían darme un
    aumento..."

    "Caminando por las partes más oscuras de un almacén, realmente me encuentro con cosas muy
    especiales, entre ellas diversos pinceles que seguro son de Kaori"
    
    "y una taza de café algo sucia, y
    otra taza también del mismo tamaño, pero rota..." 
    
    "Poco a poco esos pequeños detalles empiezan a
    familiarizarme con la gente en este lugar"




    scene genoff with dissolve

    ku "Que chica más rara..."

    ka "Quien es rara"

    "Kaori entra en escena y parece que quiere saber que ha pasado ahí dentro"

    r "Holaaaaa"

    "Rin sale con una cara muy seria, bueno hasta ahora es su cara habitual..."

    "Kaori no parece tan feliz..."

    ka "Hola... Señorita Rin..."

    r "Hola"

    "El ambiente se tornó serio de la nada..."

    ka "Podría decirme cómo está manejando su papeleo está semana"

    r "Lo tendré listo mañana, seguramente..."

    ka "Seguramente no es una opción, quisiera ver más acción dentro de su oficina"

    r "Dudo poder dársela, seguro sería mejor ir a ver una película para ello..."

    "Kaori parece no tan contenta con esa respuesta..."

    ka "Co... Cómo sea, quisiera ver ese trabajo terminado mañana"

    "Kaori toma mi manga y me arrastra, mientras rin solo voltea y se va a dónde la lleve el viento..."

    scene build2 with dissolve

    "A la hora de salida le pregunto a Kaori sobre lo que sucedió está mañana"

    ka "A veces esa chica es insoportable, no puedo entender lo que sucede en su cabeza, es rara e
    inexpresiva, porque siempre me toca trabajar con gente como ella..."

    "Mis pensamientos no eran nada alejados de la realidad"

    ku "Supongo que tendrá sus motivos para ello..."
    
    ka "No me importa"
    
    "Parece que encontré la fibra sensible de Kaori, en todo caso..."
    
    "No puedo digerir tan rápido como todo paso en una sola mañana, sobre todo con Rin, ella es misteriosa..."
    
    "Sería interesante saber
    que está pensando realmente..."


return

label rinvar2:
    scene genoff with dissolve

    play music "audio/dlife.mp3"
    "Tercer día, llegó con más que tiempo para poder empezar a terminar las labores que debía, como
    siempre es un día movido, sin embargo, puedo mantener la compostura lo suficiente para apoyar"

    "Tanto a la Superior Tsukasa, Kaori y Miko, tres cosas a la vez por un día, deberían darme un
    aumento..."

    scene woff with dissolve

    "Caminando por las partes más oscuras de un almacén, realmente me encuentro con cosas muy
    especiales, entre ellas diversos pinceles que seguro son de Kaori"
    
    "y una taza de café algo sucia, y
    otra taza también del mismo tamaño, pero rota..." 
    
    "Poco a poco esos pequeños detalles empiezan a
    familiarizarme con la gente en este lugar"

    ri "Mmmmm"

    "Escucho un raro quejido viniendo de una parte del almacén, pero intento ignorarlo..."

    "Paso 5 minutos en el lugar y los extraños quejidos desaparecen, pero siento que estoy siendo
    vigilado..."

    "Así que salgo del lugar un tanto preocupado por la sensación" 

    scene genoff with dissolve
    
    "Al salir me encuentro con la superior
    Tsukasa y me menciona que debo ir a dejar esos papeles a la oficina de la señorita Rin, la cual no
    conozco para nada..."

    scene rinoff with dissolve

    "Al llegar a la oficina que está convenientemente a dos puertas de acá, no parece que se encuentre
    alguien dentro así que paso adelante sin tocar"

    "Al entrar, me doy cuenta de que todo está horriblemente puesto en su sitio"

    "Encontrarme con una supervisora más sería mi fin..."

    "Al decir eso me siento nuevamente observado y escucho pasos detrás mío, y empiezo a creer que
    entrar no fue una buena idea"

    "Y la puerta se cierra de golpe, no quiero voltear a ver ya que todo
    pasa muy rápido, cuando menos lo espero siento una mano en mi espalda..."

    r "Holaaaaa"

    show rin_serious at center
    with dissolve
    pause 1.5

    "Con una voz muy apagada y serena, al voltear observo una chica de baja estatura"

    r "Holaaaaaa"

    play music "audio/cgirl.mp3"

    ku "Ho... hola... Que susto"

    show rin_h at center
    with dissolve
    pause 0.5

    r "Mmm, no creo que sea la chica que, de más miedo de aquí, apenas puedo hacer más que terminar
    mi trabajo"
    
    r "Que me dices de ti, ya has asustado a alguien? No parece que asustes a alguien tan
    fácilmente, de hecho, me pareces simpático..."

    "Un cumplido que evidentemente me deja algo atónito, pero más atónito es ver qué apenas nos
    conozcamos y de esa clase de cumplidos"

    ku "¿Tu debes ser Rin no es así?"

    r "Si, soy esa persona, me preguntó cómo se verá una Rin, no yo, si no como se verá una Rin, como
    cosa o un objeto, es como cuando le damos formas a las nubes"
    r "Pero no sabemos cómo será la
    forma real y absoluta de una nube, me gustaría saberlo, seguro vea nubes al salir de mi trabajo"

    ku "Se... seguro ..."

    r "Esos papeles seguro son para mí, porque otra razón estarías aquí, ponlos en la mesa, los revisaré
    más tarde, cuando pueda..."
    
    r "O cuando quiera, puede que lo olvide, le pediré a mi asistente virtual
    que me lo recuerde..."

    "Definitivamente es una persona muy... singular..."

    r "Espera, no me has dicho tu nombre, seguro no tendrás el que me imagino, y cuando me lo digas
    intentaré pensar en cómo sería tu nombre en una cosa, me da curiosidad"

    ku "Me llamo Kuta, y soy uno de los nuevos gerentes..."

    r "Ehh... Ya veo, te veía una cara de un... Saito, o un Kazuma... "
    
    r "Pero esos nombres tienden a ser
    bastante diferentes en quienes me imagino, podrías intentar cambiar tu nombre"

    ku "No gracias, creo que me gusta el que tengo ahora... Además, es la primera vez que me cambian el
    mío por apariencia..."

    r "Todo el mundo dice que nos parecemos a nuestro nombre, pero si me preguntas eso, como
    debería llamarse un perro, ¿guau guau?"

    ku "Quien sabe, podrías ponerle ese nombre a uno"

    r "No puedo"

    ku "¿Porque no?"

    r "Porque eso haría que se pareciera a todos en general, el mío debería ser único, pero igualmente
    no podría decir sencillamente que tipo de nombre podría ser el indicado"
    
    r "Eso sería compararlo a
    los demás nombres y no saldría de nada"

    ku "Pero a fin de cuentas igual existen otras Rin, y no se parecen tanto entre si"

    "Su cara parece torcerse ante la cuestión"

    r "Puede que tengas razón, pero como siempre dicen, no puedes dejar de pensarlo hasta
    comprobarlo, aunque me tomara años"
    
    r "Quizás algún día encuentre a más Rin, y al final haya un
    torneo de quién se queda con el nombre al final de todos"

    ku "Interesante idea..."

    "Realmente predecir lo que dirá luego de esto es complicado..."

    r "Puedes irte ya, de todos modos, tienes tu trabajo, quizás luego nos veamos... Quien sabe... La vida
    es rara, suerte en tu día"

    ku "Igualmente..."

    stop music fadeout 1.0

    scene genoff with dissolve

    ku "Que chica más rara..."

    ka "Quien es rara"

    "Kaori entra en escena y parece que quiere saber que ha pasado ahí dentro"

    r "Holaaaaa"

    "Rin sale con una cara muy seria, bueno hasta ahora es su cara habitual..."

    "Kaori no parece tan feliz..."

    play music "audio/miscal.mp3"

    ka "Hola... Señorita Rin..."

    r "Hola"

    "El ambiente se tornó serio de la nada..."

    ka "Podría decirme cómo está manejando su papeleo está semana"

    r "Lo tendré listo mañana, seguramente..."

    ka "Seguramente no es una opción, quisiera ver más acción dentro de su oficina"

    r "Dudo poder dársela, seguro sería mejor ir a ver una película para ello..."

    "Kaori parece no tan contenta con esa respuesta..."

    ka "Co... Cómo sea, quisiera ver ese trabajo terminado mañana"

    "Kaori toma mi manga y me arrastra, mientras rin solo voltea y se va a dónde la lleve el viento..."

    scene build2 with dissolve

    "A la hora de salida le pregunto a Kaori sobre lo que sucedió está mañana"

    ka "A veces esa chica es insoportable, no puedo entender lo que sucede en su cabeza, es rara e
    inexpresiva, porque siempre me toca trabajar con gente como ella..."

    "Mis pensamientos no eran nada alejados de la realidad"

    ku "Supongo que tendrá sus motivos para ello..."
    
    ka "No me importa"
    
    "Parece que encontré la fibra sensible de Kaori, en todo caso..."

    scene kutaroom with dissolve
    stop music fadeout 1.0
    
    "No puedo digerir tan rápido como todo paso en una sola mañana, sobre todo con Rin, ella es misteriosa..."
    
    "Sería interesante saber
    que está pensando realmente..."


return

label rinvar3:
    scene kutaroom with dissolve
    "Tercer día, llegó con más que tiempo para poder empezar a terminar las labores que debía, como
    siempre es un día movido, sin embargo, puedo mantener la compostura lo suficiente para apoyar"

    "Tanto a la Superior Tsukasa, Kaori y Miko, tres cosas a la vez por un día, deberían darme un
    aumento..."

    "Caminando por las partes más oscuras de un almacén, realmente me encuentro con cosas muy
    especiales, entre ellas diversos pinceles que seguro son de Kaori"
    
    "y una taza de café algo sucia, y
    otra taza también del mismo tamaño, pero rota..." 
    
    "Poco a poco esos pequeños detalles empiezan a
    familiarizarme con la gente en este lugar"



    scene genoff with dissolve

    ku "Que chica más rara..."

    ka "Quien es rara"

    "Kaori entra en escena y parece que quiere saber que ha pasado ahí dentro"

    r "Holaaaaa"

    "Rin sale con una cara muy seria, bueno hasta ahora es su cara habitual..."

    "Kaori no parece tan feliz..."

    ka "Hola... Señorita Rin..."

    r "Hola"

    "El ambiente se tornó serio de la nada..."

    ka "Podría decirme cómo está manejando su papeleo está semana"

    r "Lo tendré listo mañana, seguramente..."

    ka "Seguramente no es una opción, quisiera ver más acción dentro de su oficina"

    r "Dudo poder dársela, seguro sería mejor ir a ver una película para ello..."

    "Kaori parece no tan contenta con esa respuesta..."

    ka "Co... Cómo sea, quisiera ver ese trabajo terminado mañana"

    "Kaori toma mi manga y me arrastra, mientras rin solo voltea y se va a dónde la lleve el viento..."

    scene build2 with dissolve

    "A la hora de salida le pregunto a Kaori sobre lo que sucedió está mañana"

    ka "A veces esa chica es insoportable, no puedo entender lo que sucede en su cabeza, es rara e
    inexpresiva, porque siempre me toca trabajar con gente como ella..."

    "Mis pensamientos no eran nada alejados de la realidad"

    ku "Supongo que tendrá sus motivos para ello..."
    
    ka "No me importa"
    
    "Parece que encontré la fibra sensible de Kaori, en todo caso..."
    
    "No puedo digerir tan rápido como todo paso en una sola mañana, sobre todo con Rin, ella es misteriosa..."
    
    "Sería interesante saber
    que está pensando realmente..."


return

