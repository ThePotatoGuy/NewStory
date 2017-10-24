init python:
    class Poem:
        def __init__(self, author="", title="", text=""):
            self.author = author
            self.title = title
            self.text = text

    poem_mc1 = Poem(
    author = "mc",
    title = "Placeholder no. 1",
    text = """\
The first Placeholder.
This is just to hold a place.
Placeholder poem.

{0}
{1}
{2}
{3}
{4}
{5}
{6}
{7}
{8}
{9}
{10}
{11}
{12}
{13}
{14}
{15}
{16}
{17}
{18}
{19}"""
    
    formattedText = text.format(madlibs[0], madlibs[1], madlibs[2], madlibs[3], madlibs[4], madlibs[5], madlibs[6], madlibs[7], madlibs[8], madlibs[9], madlibs[10], madlibs[11], madlibs[12], madlibs[13], madlibs[14], madlibs[15], madlibs[16], madlibs[17], madlibs[18], madlibs[19])
    )
    
    poem_mc2 = Poem(
    author = "mc",
    title = "Placeholder no. 2",
    text = """\
Second Placeholder.
This is just to hold a place.
Placeholder poem.

[madlibs[0]]
[madlibs[1]]
[madlibs[2]]
[madlibs[3]]
[madlibs[4]]
[madlibs[5]]
[madlibs[6]]
[madlibs[7]]
[madlibs[8]]
[madlibs[9]]
[madlibs[10]]
[madlibs[11]]
[madlibs[12]]
[madlibs[13]]
[madlibs[14]]
[madlibs[15]]
[madlibs[16]]
[madlibs[17]]
[madlibs[18]]
[madlibs[19]]"""
    )

image paper =  "images/bg/poem.jpg"

transform paper_in:
    truecenter
    alpha 0
    linear 1.0 alpha 1

transform paper_out:
    alpha 1
    linear 1.0 alpha 0

screen poem(currentpoem, paper="paper"):
    style_prefix "poem"
    vbox:
        add paper
    viewport id "vp":
        child_size (710, None)
        mousewheel True
        draggable True
        vbox:
            null height 40
            if currentpoem.author == "yuri":
                text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text"
            elif currentpoem.author == "sayori":
                text "[currentpoem.title]\n\n[currentpoem.text]" style "sayori_text"
            elif currentpoem.author == "natsuki":
                text "[currentpoem.title]\n\n[currentpoem.text]" style "natsuki_text"
            elif currentpoem.author == "monika":
                text "[currentpoem.title]\n\n[currentpoem.text]" style "monika_text"
            elif currentpoem.author == "mc":
                text "[currentpoem.title]\n\n[currentpoem.text]" style "mc_text"
            null height 100
    vbar value YScrollValue(viewport="vp") style "poem_vbar"
    
style poem_vbox:
    xalign 0.5
style poem_viewport:
    xanchor 0
    xsize 720
    xpos 280
style poem_vbar is vscrollbar:
    xpos 1000
    yalign 0.5
    #xsize 18
    ysize 700
    #base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    #thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    #unscrollable "hide"
    #bar_invert True
    
style yuri_text:
    font "gui/font/y1.ttf"
    size 32
    color "#000"
    outlines []

style natsuki_text:
    font "gui/font/n1.ttf"
    size 28
    color "#000"
    outlines []
    line_leading 1

style sayori_text:
    font "gui/font/s1.ttf"
    size 34
    color "#000"
    outlines []

style monika_text:
    font "gui/font/m1.ttf"
    size 34
    color "#000"
    outlines []
    
style mc_text:
    font "gui/font/mc.ttf"
    size 24
    color "#000"
    outlines []

label showpoem(poem=None, music=True, track=None, revert_music=True, img=None, where=i11, paper=None):
    if poem == None:
        return
    play sound page_turn
    if music:
        $ currentpos = get_pos()
        if track:
            $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>" + track
        else:
            $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>bgm/5_" + poem.author + ".ogg"
        stop music fadeout 2.0
        $ renpy.music.play(audio.t5b, channel="music_poem", fadein=2.0, tight=True)
    window hide
    if paper:
        show screen poem(poem, paper=paper)
    else:
        show screen poem(poem)
    if not persistent.first_poem:
        $ persistent.first_poem = True
        show image "gui/poem_dismiss.png" as poem_dismiss:
            xpos 1050 ypos 590
    with Dissolve(1)
    $ pause()
    if img:
        $ renpy.hide(poem.author)
        $ renpy.show(img, at_list=[where])
    hide screen poem
    hide poem_dismiss
    with Dissolve(.5)
    window auto
    if music and revert_music:
        $ currentpos = get_pos(channel="music_poem")
        $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
        stop music_poem fadeout 2.0
        $ renpy.music.play(audio.t5c, fadein=2.0)
return