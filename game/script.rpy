# The script of the game goes in this file.
# Should not include any actual events or scripting; only logic and calling other labels.

label start:

    #Chapter Tracker
    $ chapter = 0
    
    #Girls' names before you learn them
    $ s_name = "???"
    $ m_name = "???"
    $ n_name = "???"
    $ y_name = "???"
    
    $quick_menu = True
    $ style.say_dialogue = style.normal
    $ allow_skipping = True
    $ config.allow_skipping = True
    
    #Intro
    $ chapter = 0
    call ch0_main
    
    call poem
    
    call endgame
    
    $ renpy.full_restart(transition=None, label="splashscreen")

    return

label endgame(pause_length=2.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return