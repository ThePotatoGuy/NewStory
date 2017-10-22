init python:
    menu_trans_time = 1
    splash_message_default = "Here's lookin' at you, /ddlc/."
    splash_messages = [
    "Wait, you're not supposed to see this.\nForget this ever happened.",
    "Here's lookin' at you, /ddlc/."
    ]
    
image splash_warning = ParameterizedText(style="splash_text", xalign=0.5,yalign=0.5)

image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move
    
image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop
    
image menu_fade:
    "white"
    menu_fadeout
    
image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)
    
image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)
    
image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)
    
image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)
    
image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move
    
image menu_logo:
    "gui/logo.png"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move
    
image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=20, particleTime=2.0, particleXSpeed=6, particleYSpeed=4).sm
    particle_fadeout
    
transform particle_fadeout:
    easeout 1.5 alpha 0
    
transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500
        
transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    
transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0
    
transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0
    
transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0
    
transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0

image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5
    
label splashscreen:
    #Character file checking for easter eggs
    python:
        def slow_nodismiss(event, interact=True, **kwargs):
            try:
                renpy.file("../characters/monika.chr")
                persistent.mEE = True
            except:
                persistent.mEE = False
            try:
                renpy.file("../characters/natsuki.chr")
                persistent.nEE = True
            except:
                persistent.nEE = False
            try:
                renpy.file("../characters/sayori.chr")
                persistent.sEE = True
            except:
                persistent.sEE = False
            try:
                renpy.file("../characters/yuri.chr")
                persistent.yEE = True
            except:
                persistent.yEE = False                
        
    
    #Logic for detecting if the game has been reinstalled
    python:
        firstrun = ""
        try:
            firstrun = renpy.file("firstrun").read(1)
        except:
            with open(config.basedir + "/game/firstrun", "wb") as f:
                pass
    if not firstrun:
        if persistent.first_run and not persistent.do_not_delete:
            $ quick_menu = False
            scene black
            menu:
                "A previous save file has been found. Would you like to delete your save data and start over?"
                "Yes, delete my existing data.":
                    "Deleting save data...{nw}"
                    python:
                        delete_all_saves()
                        renpy.loadsave.location.unlink_persistent()
                        renpy.persistent.should_save_persistent = False
                        renpy.utter_restart()
                "No, continue where I left off.":
                    pass
                    
        python:
            if not firstrun:
                with open(config.basedir + "/game/firstrun", "w") as f:
                    f.write("1")
    
    #Start splash logic
    $ config.allow_skipping = False
    show white
    $ splash_message = splash_message_default
    $ config.main_menu_music = audio.t1
    $ renpy.music.play(config.main_menu_music)
    show intro with Dissolve(0.5, alpha=True)
    pause 2.5
    hide intro with Dissolve(0.5, alpha=True)
    if renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ config.allow_skipping = True
    return
    
label warningscreen:
    hide intro
    show warning
    pause 3.0
    
label after_load:
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ style.say_dialogue = style.normal
    
    $persistent.first_load = True
    call screen dialog("Remember: You can use the \"Skip\" button to\nfast-forward through text you've already read.", ok_action=Return())
    return
    
label before_main_menu:
    $ config.main_menu_music = audio.t1
    return