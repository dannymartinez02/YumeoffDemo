#Moods of week, in this case Tsukasa
#All girls have this programation

label ch1_main:

     
    $ randomnum = renpy.random.randint(1,5) 
    if randomnum==1:

        $ renpy.movie_cutscene("cutscenes/Tangry.avi")

        jump tsukasavar1

    elif randomnum==2:

        $ renpy.movie_cutscene("cutscenes/Thappy.avi")

        jump tsukasavar2
        
    elif randomnum==3:

        $ renpy.movie_cutscene("cutscenes/Tsad.avi")

        jump tsukasavar3
        
    elif randomnum==4:
        
        $ renpy.movie_cutscene("cutscenes/Tperiod.avi")
        
        jump tsukasavar4

    elif randomnum==5:


        $ renpy.movie_cutscene("cutscenes/Tserious.avi")
        
        jump tsukasavar5



label tsukasavar1:
    scene kutaroom with dissolve
    

    "La alarma suena varias veces, y me levanto de mi cama..."

    "Me levanto bastante agotado y salgo de mi apartamento..."

    "Antes de llegar al edificio, Kaori me informa que no podrá esperarme está semana entera, ya que
    estará en reuniones desde la mañana hasta la salida, y que lamenta el inconveniente..."

    "Bueno... De todos modos, solo haré lo que hice el día de ayer... Y todo estará bien..."

    scene elevator2 with fade
    play music "audio/dlife.mp3"

    "Mientras subo en el elevador, me doy cuenta de que no hay mucho protocolo de bienvenida, pero
    mis dudas se apartan cuando recuerdo que ayer, Kaori me menciono el cierre contable..."

    scene kutaoff with fade

    "Apenas inicia mi mañana, ya hay una enorme pila de trabajo en mi oficina que debo revisar
    Termino más rápido de lo que yo creí avanzar..." 

    "Así que me quedo media hora sentado esperando
    luego de entregarlos a la chica que lleva un carrito para entregarlos a la siguiente oficina..."

    "En esa media hora empiezo a aburrirme ya que realmente... Terminar rápido no es beneficioso a
    veces..."

    scene genoff with fade

    "Salgo de mi oficina y veo a todos atareados, así que empiezo a ayudarlos..."

    "Cuando menos lo espero todos están casi terminando sus labores gracias a mi cooperación, así
    que nuevamente me quedo sin mucho que hacer..."

    "Sin embargo, veo a la chica alta que se acerca a mí con una taza de café que huele a kilómetros... Y
    que de hecho... Huele muy fuerte, más que un café normal... Creo que es un expreso..."

return

label tsukasavar2:
    scene kutaroom with dissolve
    

    "La alarma suena varias veces, y me levanto de mi cama..."

    "Me levanto bastante agotado y salgo de mi apartamento..."

    "Antes de llegar al edificio, Kaori me informa que no podrá esperarme está semana entera, ya que
    estará en reuniones desde la mañana hasta la salida, y que lamenta el inconveniente..."

    "Bueno... De todos modos, solo haré lo que hice el día de ayer... Y todo estará bien..."

label offtsuka:
    scene elevator2 with fade
    play music "audio/dlife.mp3"

    "Mientras subo en el elevador, me doy cuenta de que no hay mucho protocolo de bienvenida, pero
    mis dudas se apartan cuando recuerdo que ayer, Kaori me menciono el cierre contable..."

    scene kutaoff with fade

    "Apenas inicia mi mañana, ya hay una enorme pila de trabajo en mi oficina que debo revisar
    Termino más rápido de lo que yo creí avanzar..." 

    "Así que me quedo media hora sentado esperando
    luego de entregarlos a la chica que lleva un carrito para entregarlos a la siguiente oficina..."

    "En esa media hora empiezo a aburrirme ya que realmente... Terminar rápido no es beneficioso a
    veces..."

    scene genoff with fade

    "Salgo de mi oficina y veo a todos atareados, así que empiezo a ayudarlos..."

    "Cuando menos lo espero todos están casi terminando sus labores gracias a mi cooperación, así
    que nuevamente me quedo sin mucho que hacer..."

    "Sin embargo, veo a la chica alta que se acerca a mí con una taza de café que huele a kilómetros... Y
    que de hecho... Huele muy fuerte, más que un café normal..." 
    
    "Creo que es un expreso..."

    show tsukasa_stare at center
    with dissolve

    "Al llegar a mi lado, solo me observa por unos segundos y sonríe." 

    hide tsukasa_stare

    show tsukasa_Happy2 at center
    with dissolve

    t "¿Sucede algo?"

    "Una pregunta que me deja un tanto perplejo."

    ku "En realidad no, gracias por preguntar."

    hide tsukasa_Happy2

    show tsukasa_happy3 at center
    with dissolve

    t "Ah, en todo caso... ¿Podrías ayudarme con un par de cosas en mi oficina?."

    hide tsukasa_happy3

    show tsukasa_p at center
    with dissolve

    t "No tomará mucho tiempo, asi que esperare en mi oficina."

    ku "Claro, estaré ahí en un par de minutos..."

    hide tsukasa_p

    show tsukasa_Happy2 at center
    with dissolve

    t "Oye ¿Quieres un consejo?."

    ku "Claro... No veo porque no."



    "Se acerca un poco y me dice al oído:"

    t "La cafetería está dando frappe de café a la gerencia, di que vas de mi parte y aprovecha a pedir uno para ti." 

    "Vaya... Definitivamente que es fan de esto, ya que su secreto dejo un aroma a café en el ambiente..." 

    ku "Comprendo, iré de inmediato..."

    "Ella ríe y se va tranquilamente a su oficina, 
    ignorando que soy de gerencia y que mi ficha de empleado lo dice seguramente." 

    scene tsukasaoff with dissolve

    "Luego de ir a la cafetería y volver a su oficina, la cual está muy ordenada, 
    me la encuentro viendo un video sobre café en su computadora..."

    "A la vez que veo una enorme pila de papeles seguramente sin terminar en su escritorio ¿Porque siento que se cómo acabará esto?."

    "Al verme sonríe y parece que los ojos le brillan al ver el vaso."

    t "Adelante, quiero que me ayudes con un par de documentos."

    "¿Un par?."

    t "Al final sí que aprovechaste en pedir uno para ti, pero no te culpo, estas cosas animan hasta a la persona más malhumorada."

    ku "Si, de hecho, eso quería hablar con usted..."

    ts "Puedes decirme Tsukasa, es un gusto." 

    ku "Ah, entiendo, mi nombre es Kuta, Aoyama Kuta, quisiera que sepa, superior Tsukasa... 
    Que en realidad soy parte de la gerencia" 

    "Ella tiene una expresión de sorpresa y un tanto ¿sonrojada?."

    ts "Ah... Asi que eres el amigo de Kaori, no espere toparme contigo tan rápido."

    "Sin embargo, yo la había visto en la oficina general antes el día de ayer..."

    ts "En todo caso es un gusto conocerte, pero realmente quisiera un favor, quiero que leas y selles esto, 
    sé que es mucho trabajo, pero no es complicado de terminar."

    "Parece que lo pide de todo corazón..."

    ku "No veo el problema, técnicamente termine mi parte, puedo apoyar un poco más."

    "Ella sonríe de oreja a oreja viendo que parte de su trabajo ya está resuelto, y además le da un sorbo a su café..."

    ts "Te agradezco genuinamente tu apoyo, este lugar es un desastre estos días... Imagino que sabes el porqué."

    ku "Si, los cierres contables son un dolor de cabeza, pero creo que puedo adaptarme a ello..."


    ts "Dime una cosa ¿Desde cuándo se conocen Kaori y tú?."

    ku "Desde que tengo memoria, pero por temas personales, no la veía desde mis 15 años."

    "Ella parece intrigada por ese comentario."

    ts "¿A qué te refieres con eso? "

    ku "En su momento ella era relativamente muy desordenada, siempre tenía que recordarle donde dejaba su lápiz."

    "Ella vuelve a reír" 


    ts "La Kaori que conozco, me hablaba un poco de ti, aunque honestamente, había olvidado tu nombre, lo siento."

    "Un punto para mi."

    ts "Sin embargo, acepto que saber que se conocen de tanto tiempo me resultó en mayor sorpresa de lo que esperaba, 
    ella hablaba mucho de ti cuando de pronto logro entrar en contacto contigo."

    "Un hecho que me toma por sorpresa, y creo que lo nota..."

    ts "Te sonrojas rápido sabes... Me resulta divertido conocer a alguien así."

    "Esconder mis emociones no es mi mayor atributo, 
    algo que siempre resultaba en una burla de parte de mis compañeros de instituto." 

    ku "Si... Supongo que no soy bueno escondiendo mis reacciones a los cumplidos o bromas."

    ts "Lo siento, lo siento, pero debía hacerlo."

    "Y sin embargo hemos hablado bastante y no hemos avanzado con los documentos, 
    cosa que nota y termina haciendo que nos separemos a nuestras propias oficinas..."

    scene genoff with dissolve

    ku "Oye, este café está muy bueno..."

    scene kutaoff with dissolve

    "Mientras termino de sellar los documentos un ente malvado aparece en mi oficina"

    ka "HOLAAAAAAA"

    ka "Oye oye, mira lo que encon... ¿Estos no son documentos de Recursos humanos?."

    ku "Si, parece que la adicta al café tenía cosas un tanto atrasadas." 

    "Ahhh, ¿La superior Tsukasa?" 

    "Lo dice con un tono avergonzado."

    ka "Normalmente ella siempre se ve muy seria, pero en días como los que encuentra café se pone de excelente humor, 
    diría que es alguien muy simple." 

    ku "No lo parecía mientras veía videos en su computadora."

    ka "Jajajajaja, ella siempre es así, pero descuida, rara vez deja a alguien hacer su trabajo, ya veras porque."

    "A lo cual sale y me deja con más intriga de lo que esperaba."

    scene genoff with dissolve

    "Termino en relativo poco tiempo, sin embargo, encuentro a la superior en el pasillo."

    ts "Ah, gracias por terminar, iré a revisarlos, por cierto, ¿Quieres almorzar ya? Creo que solo faltan 10 minutos para terminar." 

    ku "Claro." 

    scene eatroom with dissolve

    "Al final termino encontrándome en una mesa con ella nuevamente mientras veo como saca su almuerzo muy ordenado... 
    No hay un solo grano de arroz que toque otro alimento en ese bento." 

    ku "Eres muy organizada por lo que veo..."

    ts "En efecto, de hecho, al ver tus documentos, quiero que sepas que hay cosas que podrías mejorar sabes, 
    pero no son detalles tan grandes."

    "A lo cual ella se lanza a comer con mucho ánimo."

    ts "La comida sabe mejor en días como estos."

    "En verdad esta de buen humor..."

    scene build2 with dissolve

    "Al final del día, termino encontrándome con Kaori y comentando lo que ha pasado."

    ka "Definitivamente has tenido buena suerte, otro día pudo haber sido muy muy severa... Asi que mejor no enojarla..."

    "Lo dice con una especie de nerviosismo que creo entender... sin embargo."

    scene kutaroom with dissolve

    "No niego que haya sido un muy buen día."


return

label tsukasavar3:
    scene kutaroom with dissolve
    
    "La alarma suena varias veces, y me levanto de mi cama..."

    "Me levanto bastante agotado y salgo de mi apartamento..."

    "Antes de llegar al edificio, Kaori me informa que no podrá esperarme está semana entera, ya que
    estará en reuniones desde la mañana hasta la salida, y que lamenta el inconveniente..."

    "Bueno... De todos modos, solo haré lo que hice el día de ayer... Y todo estará bien..."

    scene elevator2 with fade
    play music "audio/dlife.mp3"

    "Mientras subo en el elevador, me doy cuenta de que no hay mucho protocolo de bienvenida, pero
    mis dudas se apartan cuando recuerdo que ayer, Kaori me menciono el cierre contable..."

    scene kutaoff with fade

    "Apenas inicia mi mañana, ya hay una enorme pila de trabajo en mi oficina que debo revisar
    Termino más rápido de lo que yo creí avanzar..." 

    "Así que me quedo media hora sentado esperando
    luego de entregarlos a la chica que lleva un carrito para entregarlos a la siguiente oficina..."

    "En esa media hora empiezo a aburrirme ya que realmente... Terminar rápido no es beneficioso a
    veces..."

    scene genoff with fade

    "Salgo de mi oficina y veo a todos atareados, así que empiezo a ayudarlos..."

    "Cuando menos lo espero todos están casi terminando sus labores gracias a mi cooperación, así
    que nuevamente me quedo sin mucho que hacer..."

    "Sin embargo, veo a la chica alta que se acerca a mí con una taza de café que huele a kilómetros... Y
    que de hecho... Huele muy fuerte, más que un café normal..." 
    
    "Creo que es un expreso..."

    "Pero parece que solo va de largo, con una mirada relativamente triste, lo cual me hace pensar que no es su mejor momento."

    "Sin embargo, al verme se acerca a mi."

    t "Oye puedes hacerme un favor, ven a mi oficina, quiero que revises unas cosas por mi..."

    "¿Ah?."

    t "No tomará mucho tiempo, asi que esperare en mi oficina..."

    "Ella se va y por simple cortesía, no realizo una objeción, al menos en voz alta..."

    "Al llegar a su despacho, veo todo muy ordenado, milimétricamente, casi que enfermizo..."

    "Al observar a la chica de mucha altura, acostada en su escritorio, parece que de verdad no debería molestarla."

    "Sin embargo, tocó la puerta de forma apacible y despierta relativamente rápido."

    "Mientras despierta, casi en automático toca una pila de papeles que tienen una nota, y vuelve a dormir..." 

    "¿Puedes hacer esto por mí?"

    "Vaya, parece que no era tan 'poco trabajo' pero al ver que ni siquiera le tomo 1 minuto volver a dormir decido ayudar, y le dejo una nota: "

    "Me llamo Kuta, soy el nuevo gerente de contabilidad"

    "Y me retiro de la oficina silenciosamente."

    "Al terminar los papeles que parecen planos de una estación espacial, 
    por lo ridículamente ordenados que están, los llevo a la oficina de la chica."

    "Al entrar sin tocar, está ahí aun durmiendo, pero la nota que estaba puesta en su escritorio, 
    parece haber sido movida un par de centímetros, así que la reviso."

    "Soy Tsukasa, jefa de recursos humanos, lamento que tengas que hacer esto por mí, te deje un par más, lo siento"

    "Dejo los papeles y dejo otra nota:"

    "Intentaré hacerlo como tú, lamento si no están exactamente igual"


    "Me llevo nuevamente los documentos y termino dejando la oficina."


    "Al terminar los documentos, parece que se hace la hora del almuerzo."

    "Termino dejando los papeles en la oficina, y parece que no hay nadie, solo la nota nuevamente con más información" 

    "¿Podrías venir a la cafetería?"

    "Me muevo y guardo el papel por si acaso"

    "Al llegar la chica está tomando un frappe de café, huele a kilómetros, 
    parece que no es de una marca en particular, se ve más casero que comercial..."

    ts "Hola Kuta, que tal tu día ayudando a la pobre jefa de recursos humanos."

    "Parece que se victimiza en son de broma..."

    ku "Indiscutible abuso al empleado sabes..."

    "Ella se ríe un tanto melancólica" 

    ts "Sabes realmente agradezco tu apoyo, este no es mi día para nada."


    "Claramente puedo notarlo..."

    ts "Estos días normalmente me los paso en casa, pero hoy estamos tan cerca de fechas limites, 
    así que necesitaba estar aquí bajo cualquier circunstancia." 

    "Definitivamente aplicada a su empleo..."

    ts "Aunque admito que no están tan ordenados como esperaría, tu trabajo es bueno, quizás a veces soy muy perfeccionista." 

    ku "Nah, estaban muy detallados, era sencillo de entender, 
    solo que no puedo seguir el ritmo de tu organización..."
    
    ku "si quieres llamarlo de alguna forma... Llámalo mal necesario." 

    "Ella solo sonríe por mi comentario." 

    ts "Podrías mejorar tu orden, si quieres algún otro día podríamos discutirlo." 


    "Efectivamente halagado"

    ku "Claro, estaría encantado"

    "Ella sonríe mucho más cuando le respondo eso."

    ts "Dime una cosa ¿Desde cuándo se conocen Kaori y tú?."

    ku "Desde que tengo memoria, pero por temas personales, no la veía desde mis 15 años, vaya que ha cambiado."

    "Ella parece intrigada por ese comentario."

    ts "¿A qué te refieres con eso?."

    ku "En su momento ella era relativamente muy desordenada, siempre tenía que recordarle donde dejaba su lápiz."

    "Ella vuelve a reír." 


    ts "La Kaori que conozco, me hablaba un poco de ti, aunque honestamente,
    abía olvidado tu nombre, le pregunté justo cuando llegué aquí." 

    "Ah... Así que por eso lo pregunto." 

    ts "Sin embargo, acepto que saber que se conocen de tanto tiempo me resultó en mayor sorpresa de lo que esperaba, 
    ella hablaba mucho de ti cuando de pronto logro entrar en contacto contigo."

    "Un hecho que me toma por sorpresa, y creo que lo nota..."

    ts "Te sonrojas rápido sabes... Me resulta divertido conocer a alguien así."

    "Esconder mis emociones no es mi mayor atributo, 
    algo que siempre resultaba en una burla de parte de mis compañeros de instituto." 

    ku "Si... Supongo que no soy bueno escondiendo mis reacciones a los cumplidos o bromas."

    ts "Lo siento, lo siento, pero debía hacerlo."

    "La hora del almuerzo pasa volando para mí y para Tsukasa, hablando de todo y a la vez nada."

    ts "Oye gracias por levantarme el ánimo, realmente aprecio esta charla, espero volver a conversar contigo nuevamente."

    ku "Digo lo mismo, nos vemos luego."

    "Me dirijo a mi oficina a terminar un par de documentos que me hacen llegar para cuando vuelvo a entrar." 

    "Y alguien extraño aparece en mi oficina." 

    ka "¡¡¡¡¡HOLAAAAAA!!!!!."

    "Kaori hace acto de presencia de manera muy estruendosa." 

    ka "Oye oye, quiero que me hagas un favor, ya que veo que te llevas muy bien con la superior Tsukasa."

    "Aquí vamos de nuevo..."

    ka "Pídele un aumento por mi ¿Sí?."

    "Ah... Creí que sería esa clase de broma donde te emparejan por una simple interacción..."

    ku "Intentaré abogar por ti, aunque no me hago responsable por despidos inesperados..."

    "Ella solo me saca la lengua para decirme luego que vayamos a casa juntos como ayer."

    "Asi que nos vemos en la salida nuevamente."



    ka "Yeeei, hoy fue un buen día, parece que la Superior estaba de buen humor ahora luego del almuerzo, 
    ¿Que hiciste para que cambiará tanto de humor?."

    ku "Solo hable de nosotros dos, y de cómo nos conocimos."

    ka "Ahhh, tiene sentido, por eso es por lo que soy tan impresionante."

    "Ambos terminamos yéndonos a casa y yo caigo rendido en mi futón..."

    "Bueno, este día pudo ser peor."


return

label tsukasavar4:
    scene kutaroom with dissolve
    "La alarma suena varias veces, y me levanto de mi cama..."

    "Me levanto bastante agotado y salgo de mi apartamento..."

    "Antes de llegar al edificio, Kaori me informa que no podrá esperarme está semana entera, 
    ya que estará en reuniones desde la mañana hasta la salida, y que lamenta el inconveniente..."

    "Bueno... De todos modos, solo haré lo que hice el día de ayer... Y todo estará bien..."

    scene elevator2 with fade
    play music "audio/dlife.mp3"

    "Mientras subo en el elevador, me doy cuenta de que no hay mucho protocolo de bienvenida, pero
    mis dudas se apartan cuando recuerdo que ayer, Kaori me menciono el cierre contable..."

    scene kutaoff with fade

    "Apenas inicia mi mañana, ya hay una enorme pila de trabajo en mi oficina que debo revisar
    Termino más rápido de lo que yo creí avanzar..." 

    "Así que me quedo media hora sentado esperando
    luego de entregarlos a la chica que lleva un carrito para entregarlos a la siguiente oficina..."

    "En esa media hora empiezo a aburrirme ya que realmente... Terminar rápido no es beneficioso a
    veces..."

    scene genoff with fade

    "Salgo de mi oficina y veo a todos atareados, así que empiezo a ayudarlos..."

    "Cuando menos lo espero todos están casi terminando sus labores gracias a mi cooperación, así
    que nuevamente me quedo sin mucho que hacer..."

    "Sin embargo, veo a la chica alta que se acerca a mí con una taza de café que huele a kilómetros... Y
    que de hecho... Huele muy fuerte, más que un café normal..." 
    
    "Creo que es un expreso..."

    show genoff
    with None

    show tsukasa_ag at center
    with moveinleft 
    pause 1.0

    stop music fadeout 1.0

    "Además, rodeada de 4 personas, y la chica del correo a su lado tiene una expresión que suplica 
    porque huya del lugar antes que se acerque a mi."
    
    "Sin embargo, me doy cuenta muy tarde..."

    t "Maldita sea… Pueden de una vez terminar esos reportes, es lo más sencillo en lo que pueden ayudarme." 
    
    "Además no parece que se lo tomen enserio...
    Mira esto, esta tan desordenado… Si no puedes ayudarme, lo hare yo misma... ¿Quedo claro?."

    "Wow que carácter, espera... ¿No era la chica que vi en mi primer día?... Oye, si lo es..."

    hide tsukasa_ag

    show tsukasa_angry at center
    with dissolve
    

    t "Chico, no me interesa que estes haciendo, ayúdame con una de estas pilas de documentos, ahora."

    play music "audio/miscal.mp3"

    ku "E-espera, yo..."

    t "No quiero repetirlo dos veces, asi que hazme el favor que te he pedido con anterioridad, realmente no es mi mejor día..."

    "Luego de recibir órdenes tan concisas, y tan estructuradas con las que fácilmente podría armar una bomba termonuclear."

    "Me dirijo a mi oficina, y la chica del correo toca a mi puerta para pedir que sea terminado en 30 minutos... 
    Cosa que se ve totalmente imposible..."

    scene kutaoff with dissolve

    "Sin embargo, y viendo el ambiente que rodea el lugar, entro en alguna especie de trance y termino todo más agotado
    de lo que yo podría considerar en mi segundo día, esos 30 minutos parecieron 2 horas..."

    show tsukasa_angry at center
    with moveinleft
    pause 1.5

    "Apenas empiezo a salir de mi oficina, la misma chica termina azotando la puerta, afortunadamente 
    no hace que la enorme pila que llevaba entre manos caiga al suelo." 
    
    "Pero una más grande se acerca de las manos de la chica del correo, y las pone en mi escritorio, 
    la chica alta toma sin voltear a verme..."

    "Justo antes que cruce la puerta ella se detiene y voltea con una expresión de horror, digna de una reacción de película de horror." 

    hide tsukasa_angry

    show tsukasa_anger at center
    with dissolve

    t "¡¡P... PERO QUE ES ESTO!!"

    "Su reacción retumba en todo el escenario, la chica del correo se ve como si supiera que pronto se acerca una tormenta..."

    "Sin embargo, ella toma aire, y de un segundo para otro, empieza a conservar la calma."

    hide tsukasa_anger

    show tsukasa_y1 at center
    with dissolve

    t "Oye… ¿Este es tu primer empleo no?..."

    "Mi mente en blanco no me permite responder ante la reacción anterior." 
    
    "Cuando ella estallo observe toda mi vida en un segundo, 
    pero tomo conciencia de la situación y empiezo a gesticular una respuesta..."

    ku "No... Soy un nuevo gerente del área de contabilidad..."

    "Ella queda un tanto en shock por esa declaración." 
    
    "Se acomoda sus lentes y le da un sorbo a su café, 
    que parece que esta algo helado por su reacción luego de beberlo..."

    hide tsukasa_y1

    show tsukasa_d1 at center
    with dissolve

    t "Dame una hora exacta, ya que pronto es la hora del almuerzo ven a verme a mi oficina y..."

    hide tsukasa_d1

    show tsukasa_d2 at center
    with dissolve

    "Con una cambiada expresión de enojo a melancolía... ¿O tristeza?… No estoy seguro..."

    t "Por favor termina esos documentos de la manera mas ordenada posible..."

    "Se va con rapidez, y la chica del correo solamente levanta los hombros y se va tranquilamente..."

    hide tsukasa_d2 
    with moveoutright

    stop music fadeout 1.0

    "Logro terminar los documentos que resultan siendo del área de recursos humanos, 
    lo cual me sorprende porque no se que hago resolviendo estas encrucijadas al no ser de mi área..."

    "Pero supongo que no puedo ser tan mala persona en mi primera semana..."

    "La hora del almuerzo llega y me dirijo a la oficina de mi jefa."

    scene tsukasaoff with dissolve

    show tsukasa_d1 at center
    with dissolve
    pause 1.0
    
    "Llamo a la puerta y entro sin esperar respuesta. Mi jefa está sentada en su escritorio, 
    revisando unos documentos con el ceño fruncido."

    ku "Te veo muy ocupada."

    hide tsukasa_d1

    show tsukasa_d3 at center
    with dissolve

    "Ella me mira y suspira." 
    
    t "Sí, estoy hasta el cuello de trabajo. ¿Puedes sentarte un momento?."

    "Me siento en la silla frente a su escritorio y espero a que hable."

    hide tsukasa_d3

    show tsukasa_stare at center
    with dissolve

    t "Mira, sé que esto es nuevo para ti, y que estás tratando de adaptarte...
    Pero debes ser más cuidadoso con los documentos que manejas."
    
    t "No puedes simplemente entregar cualquier cosa sin saber a quién le corresponde o cómo está organizada...
    Eso es simplemente irresponsable"

    "Asiento sintiéndome culpable por mi error." 
    
    ku "Lo siento mucho. No volverá a pasar."

    hide tsukasa_stare

    show tsukasa_d4 at center
    with dissolve

    t "Bueno, espero que no..." 

    hide tsukasa_d4

    show tsukasa_stare at center
    with dissolve
    
    t "Pero no quiero que te sientas abrumado."

    t "Si necesitas ayuda con algo, no dudes en pedirme... Después de todo, es mi trabajo ayudarte a ti y a todos los demás en el equipo."

    ku "Gracias, lo apreciaré."

    hide tsukasa_stare

    show tsukasa_st at center
    with dissolve

    t "Bien, eso es todo. ¿Tienes alguna pregunta antes de que nos vayamos a almorzar?."

    ku "Sí, ¿puedo hacer algo para ayudar a organizar mejor los documentos del futuro?."

    hide tsukasa_st

    show tsukasa_p at center
    with dissolve

    t "Definitivamente."
    
    "Dice sonriendo por primera vez."

    hide tsukasa_p

    show tsukasa_happy at center
    with dissolve
    
    t "Hablemos de ello durante el almuerzo. Ahora, ¿por qué no vamos a buscar algo de comer?."

    scene eatroom with dissolve

    "Salimos juntos de la oficina y me siento aliviado de que hayamos podido resolver el problema sin incidentes mayores."

    "Además de enterarme cual es su nombre, se llama Tsukasa, la superior en realidad es muy amable." 
    
    "Aprendí una valiosa lección sobre la responsabilidad en el trabajo y estoy decidido a ser más cuidadoso en el futuro."

    scene build2 with dissolve

    "Al final del día me encuentro con Kaori en la salida del empleo..."

    "Veo a Kaori mientras caminamos hacia nuestros apartamentos."

    ku "Oye, ¿estás bien?."

    ka "Sí, estoy bien."
    
    ka "Es solo que vi algo en mi calendario y me recordó algo que sucede en estas fechas..."

    ku "¿Qué es?."

    ka "Oh, nada importante."
    
    ka "Solo una cosa personal."

    "Decido no insistir y cambiamos de tema. Hablamos de mi día en el trabajo y de cómo manejé el problema con Tsukasa."

    ka "Eso es impresionante."
    
    ka "Eres un gerente nuevo y ya te estás enfrentando a problemas... Pero estoy segura de que lo manejarás bien."

    "Le agradezco sus palabras y nos sentamos a comer un helado..." 
    
    "Mientras comemos, 
    noto que Kaori sigue pareciendo distraída y un poco alterada... Me pregunto qué puede ser lo que la está molestando."

    scene kutaroom with dissolve

    "Sin embargo, al final terminamos separándonos al final del camino, llego a casa, 
    y aunque el día no fue el mejor de mi semana… Supongo que pudo ser peor..."


return

label tsukasavar5:
    scene kutaroom with dissolve
    

    "La alarma suena varias veces, y me levanto de mi cama..."

    "Me levanto bastante agotado y salgo de mi apartamento..."

    "Antes de llegar al edificio, Kaori me informa que no podrá esperarme está semana entera, ya que
    estará en reuniones desde la mañana hasta la salida, y que lamenta el inconveniente..."

    "Bueno... De todos modos, solo haré lo que hice el día de ayer... Y todo estará bien..."

    scene elevator2 with fade
    play music "audio/dlife.mp3"

    "Mientras subo en el elevador, me doy cuenta de que no hay mucho protocolo de bienvenida, pero
    mis dudas se apartan cuando recuerdo que ayer, Kaori me menciono el cierre contable..."

    scene kutaoff with fade

    "Apenas inicia mi mañana, ya hay una enorme pila de trabajo en mi oficina que debo revisar
    Termino más rápido de lo que yo creí avanzar..." 

    "Así que me quedo media hora sentado esperando
    luego de entregarlos a la chica que lleva un carrito para entregarlos a la siguiente oficina..."

    "En esa media hora empiezo a aburrirme ya que realmente... Terminar rápido no es beneficioso a
    veces..."

    scene genoff with fade

    "Salgo de mi oficina y veo a todos atareados, así que empiezo a ayudarlos..."

    "Cuando menos lo espero todos están casi terminando sus labores gracias a mi cooperación, así
    que nuevamente me quedo sin mucho que hacer..."

    "Sin embargo, veo a la chica alta que se acerca a mí con una taza de café que huele a kilómetros... Y
    que de hecho... Huele muy fuerte, más que un café normal..." 
    
    "Creo que es un expreso..."

    t "Ah... Tu eres el becario nuevo ¿No?."

    play music "audio/miscal.mp3"

    "¿¿¿Ahhhhh???"

    t "Mira... Esto es lo del día de hoy... Seguro no estás tan familiarizado con lo que te pediré, pero
    necesito que termines de cuadrar los pagos para los chicos del área de software." 
    
    t "Todos están
    esperando su sueldo hace 2 días, y realmente no puedo estar más atareada... Te dejo..."

    "Mientras lo dice atiende una llamada desde su teléfono... La pila de trabajo que me deja la chica
    del carrito es más grande de lo que espere..."

    "Ella solo levanta los hombros y procede a irse riéndose... Creo que esto ya es costumbre..."

    scene kutaoff with fade

    "Aunque a veces no comprendo lo espantosamente meticuloso y detallado orden de los
    documentos... Logro darles forma un poco aturdido..."

    scene genoff with fade

    "Cuando veo a la chica nuevamente, intento decir algo..."

    ku "Oye... Acabo de..."

    t "Ah, perfecto, leeré los documentos, y te encargo más..."

    "Acto seguido termina corriendo con los documentos al área de recursos humanos... Parece que es
    costumbre de esa área el ser tan fríos... ¿Uh?..."

    scene kutaoff with fade

    "Nuevamente paso 1 hora tratando de resolver el orden en el que están estás planillas... Pero
    termino más abrumado que la vez anterior..."

    scene tsukasaoff with fade

    "Sin embargo, termino todo y llevo mis resultados a la sala de la chica..."


    ku "Oye... Termine todo lo que me pediste, puedes echarles un ojo..."

    t "Si, pues eso debo tratar contigo... Creo que dejaste un poco desordenados algunos detalles..."

    t "Mira... Esto tiene que estar más centrado, debes usar únicamente tinta, no uses lápiz, debes tener
    un poco más de consideración para evitarme más trabajo, seguro eres nuevo, asi que lo dejaré
    pasar por esta ocasión."

    "Y lo dice con una sonrisa de oreja a oreja, parece que hoy está de muy buen humor..."

    ku "Oye... Emmm solo un detallito, primero quiero saber cuál es tu nombre..."

    ts "Ah, lo lamento, mi nombre es Tsukasa Kimura, y tengo 25 años, creo que soy mayor que tú, es un
    placer."

    ku "Bien, superior Tsukasa, quiero decirte que no soy precisamente un becario..."

    "Ella queda un tanto asombrada por mi declaración..."

    ku "Soy el nuevo gerente del área de contabilidad general, y quería mencionar que a pesar de que no
    es mi área atender planillas de la zona de recursos humanos." 
    
    ku "Estaré encantado de ser de ayuda
    para todo lo que tengas en mente... Solo que... Emmm quería aclarar ese punto..."

    "Ella se ve bastante satisfecha con mi respuesta..."

    ts "Okey, lamentablemente y como observas, todo últimamente está muy movido, espero que no
    haya sido incómodo, dime tú nombre..."

    ku "Mi nombre es Ku..."

    ku "Mi nombre es [persistent.povname]]"

    ts "[persistent.povname] lindo nombre, espero podamos vernos más seguido pronto."

    ku "Igualmente lo espero..."

    scene genoff with fade

    "Salgo de la puerta pensando que pudo ser un momento más incómodo sin embargo, esto fue muy
    grato."

    scene eatroom with fade

    "Al llegar a la zona de almuerzos, observó a Tsukasa acercarse a mí, con una mirada un tanto sería,
    pero no enojada..."

    ts "[persistent.povname], quiero mencionarte algo... Sobre tus planillas... Ammm, he notado un desorden
    serio en esta parte..."

    "Ella señala todos los errores, y la verdad es que, comparado al orden de ella, no es precisamente lo
    mejor que he hecho en toda mi carrera..."

    ku "Lamento que haya sido tan descuidado, la prisa me tomo por sorpresa, te aseguro que no ocurrirá
    nuevamente."

    "A ella parece agradarle está respuesta y solo se levanta y asiente con una sonrisa para luego
    contestar una llamada, por mi parte termino mi almuerzo."

    scene build2  with fade
    
    pause 1.0

    "Al final del día le menciono lo ocurrido a Kaori..."


    ka "Oye, pues realmente has tenido suerte... Está muy frío el día de hoy, ella es una amante
    de este clima, así que es mejor que lo tomes en cuenta si algún día vuelves a tener esos
    problemas de orden con ella." 
    
    ka "Tiende a ser un tanto excesiva con el tema, pero gracias a ello
    tenemos muy buena organización en las partes administrativas y de gestión de empleados."

    ka "Podría decirse que es un pequeño mal necesario."

    "Realmente es una persona curiosa... Pero supongo que no será la última vez que la vea, o la última
    que tenga que lidiar con su orden, solo espero que sea de su agrado."

    "Ambos terminamos saliendo a la hora normal, y terminamos yendo a casa sin desviarnos para
    tomar o comer algo."

    scene kutaroom with fade
    pause 1.0

    "Al llegar a mi casa, solo pienso que para ser el segundo día... No estuvo mal..."
    

return