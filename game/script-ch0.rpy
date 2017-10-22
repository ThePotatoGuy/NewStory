label ch0_main:
    stop music fadeout 2.0
    scene bg club
    with dissolve_scene_full
    play music t8
    
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ s_name = "Sayori"
    $ y_name = "Yuri"
    
    "Well, that about wraps up the club meeting for today."
    "Natsuki and Yuri have already left the club room, and Monika's in the closet reorganizing the shelves. Which leaves..."
    show sayori 1a at t11 zorder 2
    s "Ready to go?"
    mc "Yep, I've just been waiting on you, slowpoke."
    show sayori 5c at s11 zorder 2
    s "I'm not slow, meanie."
    "I chuckle a bit and pull her into a one-armed hug, instantly cheering her up."
    show sayori 4q at t11 zorder 2    
    "It actually surprises me a little how easily we've fallen into this sort of routine."
    "It seriously only feels like yesterday that we exchanged tearful confessions outside my house."
    show sayori 3a at t42 zorder 2
    show monika 2j at d44 zorder 2
    "I release her and bend down to pick up my bag. Monika seems to have finished with the closet, so I give her a wave that she returns with a smile."
    s "See you tomorrow, Monika!"
    mc "Yeah, don't overwork yourself, alright?"
    m 4k "Ahaha, you two. You know I can handle it."
    m "Have a good evening!"
    show monika at thide zorder 1
    hide monika
    "We both nod and I give her another wave as we exit the club room."
    
    stop music fadeout 2.0
    scene bg house_sunset
    with wipeleft_scene
    play music t9
    
    "As we approach her house, Sayori turns to me."
    show sayori 3q at t11 zorder 2
    s "Thanks for walking me home again, [player]."
    mc "You say that like I don't do it every day."
    show sayori 5a at s11 zorder 2
    s "Well, it really means a lot to me, you know?"
    mc "Jeez, don't make such a big deal out of it."
    "I say that, but I can't help but smile warmly at her."
    show sayori 1a at t11 zorder 2
    s "Hey, [player]?"
    mc "Hm?"
    s 1y "Do you maybe want to spend the night?"
    "I roll my eyes slightly, but the smile never fades from my face."
    mc "Honestly, we've known each other how long?"
    show sayori 1e at t11 zorder 2
    "Sayori looks at me slightly confused, and possibly worried?"
    mc "Sayori, just because we're a couple now doesn't mean we have to tiptoe around things like this."
    "As if to demonstrate the point, I pull her into another hug, with both arms this time."
    "Satisfied with my answer, she visibly calms down."
    show sayori 1d at t11 zorder 2
    mc "Well, we're not going to spend any nights together if we stay outside all night."
    s 1r "Ehehe! Well come on in then, silly!"
    s 3a "Ooh, that reminds me!"
    s "Natsuki showed me a new recipe that I haven't tried out yet."
    s 4x "You'll help me make it, won't you?"
    "How can I say no to that face?"
    mc "Help my girlfriend bake sweet treats? Only if you twist my arm."
    show sayori 4s at t11 zorder 2
    "She giggles again, this time a bit more flustered."
    "I'd poke fun at her for not being used to it yet, but even I can't help but feel a little giddy every time I say it."
    show sayori at thide zorder 1
    hide sayori
    "In fact, as I step over the threshold, I feel inspiration bubbling inside my head."
    "I'll have to write this down."
    
    return