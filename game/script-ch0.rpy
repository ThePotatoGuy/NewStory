label ch0_main:
    stop music fadeout 2.0
    scene bg club
    with dissolve_scene_full
    play music t5
    
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ s_name = "Sayori"
    $ y_name = "Yuri"
    
    show monika 4j at f41 zorder 3
    m "Okay, everyone! Time to share your poems!"
    show monika 1a at t41 zorder 2
    show yuri 4b at t44 zorder 2
    show natsuki 4a at t43 zorder 2
    "Yuri looks apprehensive, as usual, but Natsuki seems more eager to share today."
    show sayori 1a at t42 zorder 2
    "Sayori, of course, is just happy to be here as always."
    show natsuki 4y at f11 zorder 3
    show monika at thide zorder 1
    show sayori at thide zorder 1
    show yuri at thide zorder 1
    hide monika
    hide sayori
    hide yuri
    n "I'll go first this time!"
    "...Much more eager."
    call showpoem(poem_n2)
    mc "Uh, wow..."
    n 5g "What do you mean, \"wow\"?"
    "It seems she picked up on my... displeased tone."
    n 5e "Give me that!"
    show natsuki 5s at t11 zorder 2
    "She snatches the poem from out of my hands and gives it a once-over."
    show natsuki 1p at f11 zorder 3
    n "...This isn't what I wrote!"
    show natsuki at t22 zorder 2
    show sayori 1c at f21 zorder 3
    s "What's wrong, Natsuki?"
    show sayori at t21 zorder 2
    show natsuki 12b at f22 zorder 3
    n "..."
    "Natsuki wordlessly gets up from her seat, leaving \"her\" poem behind."
    show natsuki 12d at thide zorder 1
    hide natsuki
    "...And then runs away."
    show sayori 1h at f21 zorder 3
    s "Huh? Was it something I said?"
    show sayori 1g at t21 zorder 2
    mc "Er, no. I think someone might have messed with her poem."
    show sayori 1d at t21 zorder 2
    "I pick up the poem in question, then fold it and tuck it into my pocket."
    mc "I'll go find her."
    
    return