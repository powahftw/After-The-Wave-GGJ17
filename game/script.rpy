init python hide:
    import pygame
    pygame.font.init()

init :
    # The script of the game goes in this file.

    define config.name = _("After The Wave")
    define gui.about = _("Created as part of PoliMi GameJam")

    ##
    ## FONT
    ##

    define gui.interface_font = "fm.otf"
    define gui.default_font = "fm.otf"
    define gui.button_text_font = gui.interface_font

    ##
    ## CHARACTER ##
    ##
     
    # NAME

    define pa = Character("Pantalone")
    define pi = Character("Pierrot")
    define co = Character("Colombina")
    define me = Character("Medico")

    # SPRITES

    image pierrot_base = "personaggi/pierrot.png"
    image medico_base = "personaggi/dottoresinistra.png"
    image medico_frontale = "personaggi/dottorefrontale.png"
    image pianeta = "personaggi/pianeta.png"
    image pierrot_happy = "personaggi/pierrot_happy.png"


    ##
    #PLACES
    ##

    image bg ven = "backgrounds/veneziasecca.png"
    image bg pds = "backgrounds/pontedeisospiri.png"
    image bg psm = "backgrounds/piazzasanmarco.png"
    image bg fumo = "backgrounds/bgfumoso.png"
    image bg arlecchino = "backgrounds/arlecchino.png"
    image bg arlecchino2 = "backgrounds/arlecchino2.png"
    image bg badend = "backgrounds/badend.png"
    image bg docgondola = "backgrounds/dottoregondola.png"
    image bg arlecchinounmask = "backgrounds/arlecchinounmask.png"
    ##
    #GIOCO
    ##
    
    $ import afterthewave


# The game starts here.

label splashscreen:

    queue sound "sound/atw.mp3" loop

    scene black
    with Pause(1)

    show text "STORtY Presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

label start:
    
    style say_label font "fm.otf"

    scene black

    # These display lines of dialogue.

    transform testo:
        xalign .5
        yalign .4

    transform testo1:
        xalign .5
        yalign .435

    transform testo2:
        xalign .5
        yalign .48


    show text "Da queste parti tutti cadono, prima o poi." at testo
    with dissolve
    with Pause(2)
    
    show text "Da queste parti tutti cadono, prima o poi. \n\n Le maschere, i canali, le gondole, il mare." at testo1
    with dissolve
    with Pause(2) 

    show text "Da queste parti tutti cadono, prima o poi. \n\n Le maschere, i canali, le gondole, il mare. \n\n Da queste parti tutti cadono. Alcuni di proposito."  at testo2
    with dissolve
    with Pause(2)

label prologue:
    
    scene bg psm

    "Un giorno ci svegliammo in pendenza, come sul fianco di una montagna."
    "All’improvviso, il nord era diventato il su e il sud era il giù."
    "Quasi tutti cominciarono a cadere, chi era nelle latitudini inferiori perse la vita. Ma non era finita."

    scene bg fumo

    transform pos:
        xalign .2
        yalign .5

    show pianeta at pos

    "Per noi che sopravvivemmo, a quel punto arrivò l’Onda."
    "Da nord piovve un fronte rotolante di pietre, automobili, e ogni altro oggetto che prima non fosse fissato al suolo." 
    "Anche i mari caddero." 
    "E gli oceani."

    "Per Cassandro a cambiare la forza di gravità è stato un paradosso spazio-temporale." 
    "Secondo Balanzone, invece, il fronte d’onda della collisione di due galassie supermassive." 
    "Quisquilie retrograde: il mondo era già storto prima dell’inizio di tutto questo."
    "Quel che ha fatto è stato semplicemente togliersi la maschera."

    scene bg psm

    "Adoro Venezia. Col suo culto del carnevale e le sue maschere è sempre stata una città più onesta delle altre. Si trova qui, al parallelo 45 nord."
    "È il limite estremo della tollerabilità: un solo passo fuori e cominciano le capriole eterne." 
    "Il posto preferito di coloro che, per un motivo o per l’altro, decidono di levarsi la maschera." 

    scene bg arlecchino

    "Se sono sfortunati, tra i canali si imbattono nella maschera pazza: in quel caso, non giungono mai da me." 

    scene bg pds
    "Altrimenti, è qui che li incontro sempre. Al Ponte dei Sospiri. È qui che io vivo: a volte riesco a fare la differenza per loro. È questo il mio ruolo."

label scena_pierrot1:

    scene bg pds

    show medico_base at left
    with dissolve

    me "Fermati, ragazzo. Parliamo un istante. Come ti chiami?"

    hide medico_base
    show pierrot_base at right

    pi "…"

    hide pierrot_base
    show medico_base at left

    me "Va bene, parlerò io. Il mondo è un vasto teatro in cui ognuno interpreta la sua parte, ciascuno con una maschera sul naso."
    me "Fatti guardare… Lacrimazione ipertrofica, rughe di tristezza, pallore ceruleo…"
    me "...e in quella gola non hai corde vocali per esprimere come ti senti, vero?"

    hide medico_base
    show pierrot_base at right

    pi "…"

    hide pierrot_base
    show medico_base at left
    
    me "Posso curarti, se mi permetti di stabilire un contatto. Spesso anche la realtà indossa maschere. Lascia che ti aiuti."

label minigame:

    $ renpy.free_memory()
    $ successo = afterthewave.main()

    if successo == True:
        jump good_end

    if successo == False:
        jump bad_end

label bad_end:
    
    hide medico_base

    show bg badend
    with Pause(2)

    scene black

    show text "Da queste parti tutti cadono, prima o poi. \n\n Le maschere, i canali, le gondole, il mare. \n\n Da queste parti tutti cadono. Alcuni di proposito." at testo2
    with Pause(2)


    show text "GAME OVER"
    with Pause(3)
    with dissolve

    return

label good_end:

    scene black

    show text "Sincronizzazione onde cerebrali in corso… "
    with Pause(3)
    show text "EMPATIA STABILITA"
    with Pause(3)

label continuo:

    scene bg pds

    show medico_base at left
    with dissolve

    me "Possiamo parlare, ora. Qual è il tuo nome?"

    hide medico_base
    show pierrot_base at right

    pi "Mi chiamo Pierrot. Non voglio stare qui a parlare con te, nessuno può consolare la mia tristezza infinita."

    hide pierrot_base
    show medico_base at left

    me "Racconta la tua storia, Pierrot. Se poi vorrai, potrai ruzzolare in eterno giù dal ponte. Non te lo impedirò. Perché sei triste?" 

    hide medico_base
    show pierrot_base at right

    pi "(Sospira) Per via di un amore impossibile. Presto morirò, perché vengo tenuto lontano dalla mia amata. Lei è tutta la mia vita."
    pi "Se i nostri cuori non possono pulsare all’unisono, beh, allora che non pulsino affatto! Sono venuto a Venezia per trovare la Morte, che mi ridarà il sorriso." 

    hide pierrot_base
    show medico_base at left

    me "Parli così perché Arlecchino non ti ha trovato." 

    hide medico_base
    show pierrot_base at right

    pi "Chi è Arlecchino?"

    hide pierrot_base

    show bg arlecchino2

    me "La maschera assassina. Odia che io guarisca persone come te. Ogni settimana lancia nella mia gondola la pelle scuoiata delle sue vittime, dipinta con i colori d’inferno." 

    show pierrot_base at right

    pi "Che malvagità… ma penso che accetterei anche quella sorte, per far tacere il mio dolore."

    show bg pds
    hide pierrot_base
    show medico_base at left

    me "Dimmi, chi è colei che ami?"

    hide medico_base
    show pierrot_base at right

    pi "La più bella fanciulla del mondo, che per miracolo mi ama a sua volta!"
    pi " Colombina figlia di Pantalone, il possidente terriero che controlla le Terre Piatte al polo nord."
    pi "Lei mi ama, ma… suo padre mi ha esiliato dalle terre pianeggianti del Polo Nord, che sono di sua proprietà."
    pi "E ora è il momento di dirsi addio. Grazie per le tue parole, dottore."

    hide pierrot_base
    show medico_base at left

    me "Aspetta. Devi ascoltarmi, è importante… "

label minigame2:

    $ renpy.free_memory()
    $ successo = afterthewave.main()

    if successo == True:
        jump good_end2

    if successo == False:
        jump bad_end

label good_end2:

    scene black

    show text "Sincronizzazione onde cerebrali in corso… "
    show text "EMPATIA STABILITA"

    show bg pds

    show medico_base at left
    with dissolve

    me "Finalmente ti ho compreso, Pierrot. Una maschera dice più di una faccia."
    me "Tu sei un codardo. Un codardo e un futuro assassino."

    hide medico_base
    show pierrot_base at right

    pi "Come!? Che dici?"

    hide pierrot_base
    show medico_base at left

    me "Come pensi che reagirà il cuore della bella Colombina, se decidi di tuffarti?"
    me "Quanto pensi che passerà, prima che io me la trovi qui, dove ora ti trovi tu?"

    hide medico_base
    show pierrot_base at right

    pi "…"

    hide pierrot_base

label arlecchino:

    show bg arlecchino2
    show medico_base at right

    me "Sempre che non la incontri Arlecchino. Chissà che malefatte escogiterebbe per la più bella fanciulla del mondo…"

    hide medico_base
    show pierrot_base at right

    pi "No! No, non voglio nemmeno pensare a una cosa del genere…"

    hide pierrot_base
    show medico_base at left

    me "Allora devi rinunciare a te stesso, Pierrot. Asciugati quella lacrima."
    me "Realizza il sogno di Colombina, invece di trascinarla con te nelle eterne capriole!"

label end:

    show bg pds

    hide medico_base
    show pierrot_base at right

    pi "Io… che mai posso fare? Sono solo Pierrot, lui è… Pantalone!"

    hide pierrot_base

    me "(mano sul viso di Pierrot): Solo un Carnevale può salvarti. Rinuncia alla tua identità e indossa la maschera che vuoi essere."

    show pierrot_happy
    with Pause(2)

    show bg docgondola

    hide medico_base
    hide pierrot_happy
    
    show bg arlecchinounmask
    with dissolve
    
    "Amo Venezia e il suo Carnevale." 
    "Il Carnevale è il rovesciamento, lo sfogo capace di raddrizzare ogni stortura."
    "L’onda del caos che spazza via l’identità."
    "Oggi ho conosciuto Pierrot, e ho saputo di Colombina." 
    "E presto sarà carnevale anche per me."