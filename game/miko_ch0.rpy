label ch2_main:

     
    $ randomnum = renpy.random.randint(1,5) 
    if randomnum==1:

        $ renpy.movie_cutscene("cutscenes/Mangry.avi")

        jump mikovar1

    elif randomnum==2:

        $ renpy.movie_cutscene("cutscenes/Mhappy.avi")

        jump mikovar2
        
    elif randomnum==3:

        $ renpy.movie_cutscene("cutscenes/Msad.avi")

        jump mikovar3
        
    elif randomnum==4:
        
        $renpy.movie_cutscene("cutscenes/Mperiod.avi")
        
        jump mikovar4

    elif randomnum==5:

        $ renpy.movie_cutscene("cutscenes/Mserious.avi")

        jump mikovar5



label mikovar1:
    scene kutaroom with dissolve

    "Amanece y estoy un poco agobiado por el día anterior, pero hoy intentaré que sea un excelente
    día..."

    "Pero tras decir eso me encuentro con que hay un embotellamiento muy amplio en la calle a la
    oficina..."

    "Maldita sea, ¿No pudo ser en una semana menos abrumante?..."

    "Llegó relativamente puntual, diría que me atrase únicamente un par de minutos"

    "Corriendo al elevador, una chica pide ayuda para dejar abierta la puerta del elevador y asi poder
    entrar"
    
    "Antes que pueda presionar el botón de parada la puerta se cierra y oigo un golpe del lado
    exterior de la puerta"


return

label mikovar2:
    scene kutaroom with dissolve

    "Amanece y estoy un poco agobiado por el día anterior, pero hoy intentaré que sea un excelente
    día..."

    scene build1 with dissolve

    "Pero tras decir eso me encuentro con que hay un embotellamiento muy amplio en la calle a la
    oficina..."

    "Maldita sea, ¿No pudo ser en una semana menos abrumante?..."

    "Llegó relativamente puntual, diría que me atrase únicamente un par de minutos"

    scene elevator2 with dissolve

    "Corriendo al elevador, una chica pide ayuda para dejar abierta la puerta del elevador y asi poder
    entrar"
    
    "Antes que pueda presionar el botón de parada la puerta se cierra y oigo un golpe del lado
    exterior de la puerta"

    "Presionó el botón de emergencia y el elevador para y abre sus puertas"

    "Al observar quien era, veo a la chica de cabello verde que anteriormente llevaba una pila enorme
    de papeles hace 2 días..."

    ku "O...oye... ¿Estás bien?..."

    "Ella solo hace un sonido de molestia... Así que le ayudo a hacer la pila de papeles nuevamente"

    "Asi que pronto se levanta y se coloca los lentes nuevamente"

    "Y al verme ella empieza a sonrojarse mucho..."

    m "Yo... Esto..."

    "No parece que sea la mejor para tener conversaciones luego de un accidente de esta clase... Por
    otro lado, yo tampoco tendría muchas ganas de hacerlo..."

    ku "Descuida, solo quería saber si estabas bien"

    m "Si... Lo estoy..."

    "Lo dice en un tono de voz muy bajo"

    ku "Ah, mi nombre es Kuta, cuál es el tuyo"

    "Antes de que pueda terminar de decir la pregunta ella responde levantándose rápidamente y
    haciendo una reverencia"

    mk "Mi nombre es Miko, Miko Murakami, estoy aquí desde hace poco tiempo, fui contratada por
    la superior Tsukasa..."
    
    mk "Y esto... Lamento los inconvenientes de este momento...
    Parece que es más tímida de lo que creí..."

    ku "No no, todos podemos tener estos accidentes..."

    "Ella vuelve a hacer una reverencia"

    mk "Pero... No sería la primera vez está semana..."

    "Bueno, no me sorprende tras ver esa enorme pila de papeles que tiene... Espera, esos son los
    reportes del día anterior... "
    
    "Yo mismo los hice el día de ayer... Rayos, si los arruina tendré
    problemas..."

    ku "Oye, te molestaría que te ayude a llevarlos a... ¿Dónde los llevas Murakami?"

    "Ella se sorprende"

    mk "Esto... A mí oficina, y... Puedes... Puedes llamarme Miko, aquí todos me llaman por mi nombre..."

    "Bueno, eso sería incómodo en otras instancias... Pero suponiendo que nos veremos a menudo..."

    ku "De acuerdo Miko, vamos, te ayudaré"

    "Procedo a llevar la mitad de los documentos, son muchos más de lo que creí, pero solo debo
    asegurarme de que esto no sea un desastre para ambos..."

    scene mikooff with dissolve

    "Cuando llegamos a su oficina me doy cuenta de que todo parece estar en entero orden, me
    sorprende que para tener tanta mala suerte pueda mantenerlo todo de manera correcta"

    ku "Oye, Miko, quiero preguntar cómo... Ammm"

    "Las palabras no aparecen y no quiero ser tan brusco o crítico..."

    ku "Quería saber desde cuándo trabajas aquí..."

    "Una buena manera de evitar cualquier problema..."

    "Pero ella parece sonrojarse un poco con la pregunta... Rayos parece que no lo dije bien..."

    mk "Yo... Esto... Llevo acá apenas 3 meses... Este mes firmó mi contrato..."

    "Ah ... Es nueva, supongo que pueden ser algo permisivos con ella... Pero ya son 3 meses..."

    ku "Ya veo, como terminaste aquí, no lo malinterpretes, solo quiero saber cómo conociste esta
    empresa..."

    "Ella toma aire y empieza a contarme..."

    mk "Conocí a... Tsukasa senpai... En una pequeña cafetería, trabajaba ahí y yo sin querer... "
    
    mk "Esto... Yo
    tire su café... "
    
    mk "Pero ella no se enojó, solo me dijo que si quería salir de aquí le llamara, me dio una
    tarjeta y ahora estoy aquí..."

    "Una historia que parece salida de un manga muy cliché... Pero supongo que a cualquier persona
    podría pasarle algo así ..."

    ku "Kukukukukuku... Player, me puedes llamar por mi nombre también, supongo que nos veremos
    habitualmente"

    "Ella sonríe y asiente"

    ku "Podría ayudarte con tus papeles, llevo tiempo de sobra para los míos…"

    "Parece que será lo mejor si no quiero que terminen llenos de café…"

    scene genoff with dissolve

    "Al final del día termino todos los papeles que puedo de su parte, y ella me prometió terminar los
    que restaban para mañana"
    
    "Por precaución le digo a la superior Tsukasa que lleve los que están
    terminados…"

    scene build2 with dissolve

    "A la salida me encuentro con Kaori, y termino contándole a detalle el suceso…"

    ka "Ahhh… Miko es… Supongo que es especial…"

    "Un termino definitivamente no ofensivo, al menos no de manera directa…"

    ka "Ella en particular siempre ha sido bastante torpe… No es mala en su trabajo, es relativamente
    poco el que realiza… "
    
    ka "Pero el poco que hace siempre termina algo arrugado en el mejor de los
    casos… "
    
    ka "Tomando en cuenta lo estricta que puede ser la Superior Tsukasa, no entiendo como la ha
    podido soportar mas de un par de meses…"

    "Un caso complicado no… Supongo que tendré que adaptarme a ella…"

    scene kutaroom with dissolve

    "Un día mas terminado… no puedo decir con certeza que es lo que paso, pero… Creo que fue bueno
    que estuviera ahí…"


return

label mikovar3:
    scene kutaroom with dissolve
    "Amanece y estoy un poco agobiado por el día anterior, pero hoy intentaré que sea un excelente
    día..."

    "Pero tras decir eso me encuentro con que hay un embotellamiento muy amplio en la calle a la
    oficina..."

    "Maldita sea, ¿No pudo ser en una semana menos abrumante?..."

    "Llegó relativamente puntual, diría que me atrase únicamente un par de minutos"

    "Corriendo al elevador, una chica pide ayuda para dejar abierta la puerta del elevador y asi poder
    entrar"
    
    "Antes que pueda presionar el botón de parada la puerta se cierra y oigo un golpe del lado
    exterior de la puerta"


return

label mikovar4:
    scene kutaroom with dissolve
    "Amanece y estoy un poco agobiado por el día anterior, pero hoy intentaré que sea un excelente
    día..."

    "Pero tras decir eso me encuentro con que hay un embotellamiento muy amplio en la calle a la
    oficina..."

    "Maldita sea, ¿No pudo ser en una semana menos abrumante?..."

    "Llegó relativamente puntual, diría que me atrase únicamente un par de minutos"

    "Corriendo al elevador, una chica pide ayuda para dejar abierta la puerta del elevador y asi poder
    entrar"
    
    "Antes que pueda presionar el botón de parada la puerta se cierra y oigo un golpe del lado
    exterior de la puerta"


return

label mikovar5:
    scene kutaroom with dissolve
    "Amanece y estoy un poco agobiado por el día anterior, pero hoy intentaré que sea un excelente
    día..."

    "Pero tras decir eso me encuentro con que hay un embotellamiento muy amplio en la calle a la
    oficina..."

    "Maldita sea, ¿No pudo ser en una semana menos abrumante?..."

    "Llegó relativamente puntual, diría que me atrase únicamente un par de minutos"

    "Corriendo al elevador, una chica pide ayuda para dejar abierta la puerta del elevador y asi poder
    entrar"
    
    "Antes que pueda presionar el botón de parada la puerta se cierra y oigo un golpe del lado
    exterior de la puerta"


return