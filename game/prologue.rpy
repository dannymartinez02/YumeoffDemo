define n_nvl = Character("Kaori", kind=nvl, image="nighten", callback=Phone_SendSound)
define e_nvl = Character("Kuta", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

label ch0_main:
    scene mainbg

    if persistent.povname:
        "Hola de nuevo, [persistent.povname]."
    else:
        $ povname = renpy.input("¿Cuál es tu nombre?", length=32)
        $ povname = povname.strip()
        if not povname:
            $ povname = "Aoyama"
        "Mucho gusto, [povname]."
        $ persistent.povname = povname


stop music fadeout 1.0

label fakeer:
    scene fakeex
    play music "sfx/faterr.wav"
    pause 2.0


label kutamorn:
    
    scene kutaroom
    with fade 
    play music "audio/dlife.mp3"
    
    "Hay días en los que parece que nos hundimos en la monotonía, y a la vez, creemos que nuestros esfuerzos solamente no valen la pena."

    "Bueno, pues esos días han acabado para mí, hace una semana, tuve la enorme suerte de encontrarme con Kaori."
    "Una amiga antigua que no veía desde que tenia 15 años, conociéndola, seguro les hablo de mi a todos."

    "Es una persona muy animada, y mantiene en alta estima a sus amigos, sin embargo..."

    "Debería pedirle una disculpa ya que nunca pude contactar con ella nuevamente desde que me mude hace tanto tiempo..."

    "Justo antes de salir de mi apartamento, recibo unos mensajes en mi teléfono."



label phone_1:
    scene kutaroom with dissolve
    pause 1.0

  

    nvl_narrator "Lunes"
    n_nvl e2m2_b "HOLAAAAA [persistent.povname], ¿listo para tu primer día novato?."
    e_nvl "Claro, aunque realmente tengamos puestos similares de trabajo..."
    n_nvl e2m1_b b " Eso no es justo, solo porque llevaras tanto tiempo no significa que merecieras ser ascendido desde la contratación."
    e_nvl "Deberías pensar mejor en lo que dices, tu tambien estas en la misma categoría de ascendencia..."
    n_nvl e2m1_b b "Espero estes a la altura, nos vemos en la entrada."

    "¿[persistent.povname]? Ella me pone apodos raros toda la vida, ¿Porque me sorprendo?."

label build1:
    scene build1 with dissolve

    "Al llegar a la entrada del edificio, me doy cuenta de que el lugar es mas elegante de lo que
    esperaría." 

    show kaori_hap2 at center
    with dissolve
    
    "Observo a una chica cuyo tinte podrías ver a Kilómetros de distancia, y la cual no parece
    en lo absoluto a la persona que conocía de 15 años."

    ku "Mira a quien tenemos, aunque..."

    ku "Oye tu tinte rosa se ve mucho más brillante que en la foto de SNS, gracias nuevamente por hablar por mí, seguro fue un rollo enorme hablar con tu jefe."

    hide kaori_hap2

    show kaori_hap3 at center
    with dissolve

    "Ella se ríe un poco al escucharlo."

    hide kaori_hap3

    show kaori_hap4 at center
    with dissolve

    ka "Jejeje, ¡Gracias! Es que terminé aburrida por el color natural, por eso se ve más brillante."

    ka "Aunque me sentí un poco nerviosa al ir a hablar con el jefe, era por ti, asi que valía la pena."

    ku "¿Podríamos ir al piso de nuestra oficina? Estoy emocionado por ver que hay ahí."
    hide kaori_hap4

    show kaori_hap3 at center
    with dissolve

    ka "Claro, ven ven."

    hide kaori_hap3
    with moveoutleft

    "Kaori asiente muy entusiasmada, y me toma de la mano para llevarme al elevador." 

    "Los guardias solo la saludan al verla correr y les muestra la identificación, 
    asi que la dejan pasar sin pensar demasiado."

label kaoof:
    scene kaoof with dissolve

    "Al llegar al piso de nuestro trabajo, lo primero que hace al llegar, es mostrarme su oficina."

    "Es como un cuarto lugar con la PC, un par de libros, bolígrafos, etc." 
    
    "Está bastante ordenado..."
    
    "Lo cual me sorprende viniendo de ella, suele ser muy desorganizada."

    ku "Me sorprende que seas tan organizada... Cuando tenías 15 no solías ser nada organizada con tus cosas, ni siquiera con tu lápiz y borrador..."

    show kao_sorp2 at center
    with dissolve

    "Al decirlo Kaori infla sus mejillas en señal de descontento."

    "En ese momento ella tiene una expresion de vergüenza, ya que parece recordar cómo era en la escuela y se pone un poco nerviosa, y no sabe que decir..." 
    
    "Pero decide sincerarse..."

    hide kao_sorp2

    show kao_sorp at center
    with dissolve

    
    ka "En ese entonces me importaban muy poco las cosas y no me esforzaba para tener algo organizado en mi escritorio..." 

    hide kao_sorp

    show kao_star at center
    with dissolve
    
    ka "Ademas nada parecia tener sentido... Pero eso ya quedo en el pasado."

    ku "Bueno, eso es bastante motivador, además veo que tienes diversas pinturas colgadas ¿Las pintaste tu?."

    hide kao_star
    
    show kao_hap3 at center
    with dissolve
    
    "Ella asiente y presume un poco..."

    hide kao_hap3

    show kaori_hap4 at center
    with dissolve

    ka "Si, las pinturas las hice yo, son cosas que me motivan y en realidad tengo más de ellas, 
    solo que algunas están guardadas en un maletin por ahora."

    "Ella saca de una caja los pinceles, tintes, y todas otras cosas de arte que ella usa, 
    además unas pinturas que tiene en su escritorio, se nota orgullosa de sus pinturas."

    hide kaori_hap4

    show kao_hap4 at center
    with dissolve    

    ka "Además tengo varias guardadas en mi casa, estos suplementos de arte son muy básicos y baratos, 
    usualmente uso de mayor categoría, pero no veo conveniente traerlas a la oficina."

    "Sonrió porque parece que todo continua con la normalidad habitual de hace años, 
    y luego de mostrarme toda su oficina, creo que es momento de ver la mía, y empezar a ordenarla."
    
    ku "¿Puedes mostrarme mi oficina? Muero de ganas por verla."

    hide kao_hap4

    show kao_hap3 at center
    with dissolve

    ka "Claro, vamos a verla ahora mismo."

label kutaoff:
    scene kutaoff with dissolve

    "Me lleva rápidamente, solo para darme cuenta de que la mayor parte de ella ya esta ordenada." 

    "Lo peor de ello, es que me agrada su orden, lo cual solo me hace pensar que ella se tomo el tiempo para dejarla cómoda..."

    show kao_happ2 at center
    with dissolve

    ka "Que te parece el lugar."

    hide kao_happ2

    show kaori_sor2 at center
    with dissolve
    
    "Veo que ella no quiere voltear a verme, parece que se dio cuenta que me entere de su labor de
    ordenar por mí." 
    
    "Algo irónico, porque antes ella solía ordenar todo por mi sin que se lo pidiera, 
    pero no podía mantener un lápiz por una semana sin perderlo..."

    ku "¿Segura que asi son todas las oficinas de este lugar?..."

    hide kaori_sor2

    show kao_sorp2 at center
    with dissolve

    "Ella empieza a verse nerviosa, asi que vuelve a inflar las mejillas..."

    hide kao_sorp2

    show kao_sorp at center
    with dissolve

    ka "Sabes, deberías al menos agradecer que intente hacerte un pequeño favor..."

    ku "Claro, claro, lo agradezco"

    "Termino dándole palmadas en la cabeza para que se sienta mejor, al final termina perdonando."

    hide kao_sorp

    show kaori_hap at center
    with dissolve

    ka "Podríamos ir a conocer todas las zonas en las que tendrás que estar movilizándote a lo largo de tu jornada, 
    solo sígueme, yo te guio."

label eatroom:
    scene eatroom with dissolve

    "Sigo a Kaori por las zonas más concurridas, parece que hay mas movimiento del que pensé."

    "Kaori me deja solo durante un rato, un par de chicos la han abordado para pedirle un par de
    consejos." 
    
    "Me sorprende lo profesional que puede llegar a ser fuera de su ambiente informal,
    realmente veo que le apasiona su trabajo..."

    "Volteo y veo varias maquinas expendedoras en una de las paredes de esta sala de almuerzos, asi
    que voy y tomo un café helado para mantenerme un tanto distraído, pero cuando llego..." 

    show miko_ner2 at center
    with dissolve

    "Observo a una chica de cabello verde, bastante alborotado, llevando una pila enorme de papeles..." 
    
    "Parece que
    necesita ayuda, pero antes de poder ofrecérsela empieza a caminar mas rápido." 
    
    "No parece tener tiempo para poder si quiera pedir auxilio..."

label genoff:
    scene genoff with dissolve

    stop music fadeout 1.0
    
    "Kaori me hace un par de gestos para que la siga, nos movemos por un lugar donde están todas las
    computadoras y cubículos de empleados." 

    "Un lugar del que me recuerda que de ahí recién acabo de escapar..."

    "En perspectiva de mi anterior lugar de trabajo, todos parecen muy animados."

    "A comparación mía..."

    "Parecía que todo lo que hacia era una rutina robótica..."

    "Parecía que no hacia demasiado..."

    "Kaori me ve con la mirada algo disgustada y como si me leyera mi mente dice:"


    stop music fadeout 1.0
    play music "audio/offnois.mp3"
    pause 2.0

    show kaori_stare at center
    with dissolve

    ka "Aunque suene tonto, y aunque sientas que todo lo que hiciste en un empleo pasado solo
    fueron darte y darles molestias a algunos de tus jefes." 

    hide kaori_stare 

    show kaori_sor at center
    with dissolve

    ka "O incluso compañeros, aquí intentamos
    apreciar esas pequeñas contribuciones que todos realizan." 

    hide kaori_sor

    show kao_hap at center
    with dissolve
    
    ka "Yo misma acepto que a veces ver esos
    esfuerzos se me hace complicado, y se que no es correcto"

    hide kao_hap

    show kao_hap2 at center
    with dissolve
    
    ka "Pero intento que su trabajo no se haga
    una carga, o intentar abusar de su confianza pidiendoles imposibles."

    hide kao_hap2

    show kaori_hap4 at center
    with dissolve
    
    ka "Espero que recuerdes eso, de esa manera podrás tratar a los que estén bajo tu cargo dentro
    de poco."

    "Me sorprendo del nivel de profesionalismo que Kaori puede mantener en momentos como estos,
    pero al comprender lo que menciono tiene todo el sentido del mundo." 
    
    "Antes era una persona... Que llevaba cafés de un lado para otro..."
    
    "Pase mas de 2 años limpiando mesas, aunque
    debía realizar registros, o cosas mas importantes..." 
    
    "Y nadie tomaba enserio las cosas
    que realizaba." 
    
    "Si no fuera por ella, estaría aun continuaria en ese lugar tan abrumante"

    hide kaori_hap4 
    with dissolve

    "Luego de permanecer un tiempo parados observando como todos se mueven de lado a lado como
    hormigas." 
    
    "Nos empezamos a mover a otra de las zonas importantes, pero no sin
    antes ver pasar a una chica muy alta." 
    
    show tsukasa_stare at center 
    with dissolve

    "De lentes, siendo acompañada por dos chicas más que le
    dictan cosas que ella anota en su laptop, es totalmente inmutable." 
    
    "Y no para de teclear mientras
    se mueve con una mirada bastante fría..." 
    
    "Acepto que es muy linda, pero antes que pueda ver a
    donde se dirige, nos adentramos a un salón de conferencia." 

    scene conference with dissolve
    
    "Es un salón enorme, hay muchísimas
    sillas, y una muy larga mesa de madera." 
    
    "Es quizás la sala mas amplia que he visto en toda mi vida,
    además de tener muchas ventanas..."

    show erika_stare at center
    with moveinright

    "Pero antes de entrar una chica con coletas amarillas salió rápidamente, sin voltear a vernos
    saliendo a toda prisa."

    hide erika_stare
    with moveoutleft

    
    "Tanta que Kaori se sorprendió, ya que levanto su mano para saludarla,
    pero no le dio un poco de atención..."

    show kaori_di at center
    with dissolve

    ka "Ay vaya... Parece que otra vez esta algo retrasada..."

    ku "Parece que todos están ocupadísimos hoy."

    hide kaori_di 

    show kaori_di2 at center
    with dissolve

    ka "Ah... Pues sí, la verdad llegas como anillo al dedo, estamos en el cierre contable, todos
    estamos moviéndonos de lado a lado, la sección de marketing tuvo gastos altísimos." 
    
    hide kaori_di2

    show kao_hap4 at center
    with dissolve

    ka "Pero la recuperación fue tan amplia que no necesite explicar el porque de tanto gasto, después de todo,
    siempre he intentado ser la mejor en todo."

    "Kaori se ve orgullosa con su trabajo, asi que le doy unas palmadas, ella parece bastante alegre con
    la acción, pero no pasan ni 10 segundos para que me llevara a una bodega."

    scene woff with dissolve
    
    "Parece que ahí está todo con
    respecto a la papelería del lugar, moviéndome por un par de pasillos, ella es abordada por otra
    chica."
    
    "No parece que tenga problemas con dejarme solo, pero en mi exploración, en un
    pasillo, veo a una chica comiendo sola." 

    show rin_ser at center
    with dissolve
    
    "Parece que esta disfrutando su comida..." 
    
    "Al verme no hace
    ninguna reacción, solo sigue comiendo tranquilamente." 
    
    "Como si no hubiera nadie frente a ella,
    hago caso omiso de su presencia, y solo tomo camino a otro pasillo..."

    scene genoff with fade

    "Luego del leve recorrido, procedo a ir a observar a los chicos en los cubículos, parece que todos
    requieren ayuda, y no le niego a nadie una pequeña asistencia..."

stop music


label build2:
    scene build2 with dissolve

    "Cuando menos espero, ya es de noche, parece que todos terminaron más rápido este día."

    show kao_hap4 at center
    with dissolve

    ka "Mírate, has ayudado a todos en tu primer día, me sorprende que te hayas adaptado a todo
    tan rápido."

    ku "Realmente fue más agotador de lo que parece, pero intente hacer mi mayor esfuerzo para
    no estorbar..."

    "Sin embargo el desgaste no es el mismo que sentía en esos cubículos, es un cansancio
    satisfactorio, realmente quiero volver aquí mañana..."
    
    ku "Realmente estoy emocionado por esto, de nuevo te agradezco enormemente tu apoyo por
    ello."

    hide kao_hap4

    show kao_sorp2 at center
    with dissolve

    "Kaori se sonroja, como siempre nada acostumbrada a los halagos..."

    hide kao_sorp2

    show kaori_sor at center
    with dissolve

    ka "B... Bien, comprendo, solo que mañana debes estar un poco más temprano, nadie sabe que
    contratiempos pueden surgir..." 

    hide kaori_sor

    show kaori_hap2 at center
    with dissolve
    
    ka "Aunque realmente debo agradecerte por ayudarme, normalmente
    me encargo de los chicos de acá yo sola." 
    
    ka "Mañana aprenderás más, pero ahora es momento de
    irnos a casa, podríamos ir a cenar en un lugar que conozco ¿Que dices?."

    menu:
        "No deberia haber problemas":
            jump barlab

        "Lo mejor es volver a casa":
            jump home

label home:  

    
    ku "Lo siento Kaori, realmente hubiera querido aceptar tu invitación, pero tengo mucho
    cansancio en este momento..."

    hide kaori_hap2

    show kaori_di at center
    with dissolve

    "Kaori no parece tan alegre pero luego de unos segundos parece aceptar que no tengo tanta
    energía."

    hide kaori_di

    show kaori_stare at center
    with dissolve

    ka "Bien bien, será otro día... Pero duerme [persistent.povname] no sabes que puede pasar de camino a tu trabajo, nos
    vemos mañana."

    hide kaori_stare

    scene kutaroom with dissolve

    "Al ir caminando en la noche a mi apartamento, observo las estrellas, y pienso que hoy fue un
    excelente día, no fue abrumante, al contrario..."

    ku "Podría hacer esto por mucho tiempo..."

    "Al llegar a mi cuarto, tomo mi laptop, y empiezo a hacer un informe que seguro hará que baje la
    carga de trabajo el día siguiente... Y luego me quedo dormido antes de la media noche."

    jump mood_sys

return

label barlab:

    ku "De acuerdo, podemos ir si así lo deseas..."

    hide kaori_hap2

    show kaori_hap3 at center
    with dissolve

    "Kaori muestra una sonrisa amplia con esta confirmación."

    ka "Yeeey, entonces vamos, está cerca de aquí, a menos de 1 cuadra."

    hide kaori_hap2

    scene barr with dissolve

    "Al salir del edificio soy guiado a un bar con diversos platos, al final termino pidiendo cosas
    bastante ligeras, y nada de alcohol..." 

    "A diferencia de Kaori que parece que no tiene fondo para las
    cervezas..."

    scene kutaroom with dissolve

    "Luego de pedir un taxi para ella, me retiro a mi apartamento... Bastante pasada la noche..."

    ku "Ah, maldición, estoy muy exhausto... Pero..."

    "Podría continuar con esto..."

    jump mood_sys


return

label mood_sys:
    scene mood with dissolve

    "El sistema de Animo, es una forma aleatoria de definir como estará una chica."

    "Si tienes suerte, su estado de humor será el mejor."

    "De lo contrario, mucha suerte en tu día."

    "En esta demo, solo están disponibles 3 de los 5 posibles resultados."

    "Sin más que agregar, aquí vamos."

return