init python:
    import random
    
    #This class holds a word, and point values for each of the four heroines
    class PoemWord:
        def __init__(self, word, mPoint, nPoint, sPoint, yPoint):
            self.word = word
            self.mPoint = mPoint
            self.nPoint = nPoint
            self.sPoint = sPoint
            self.yPoint = yPoint
            
    #Static variables for the characters' poem appeal: Dislike, Neutral, Like
    POEM_DISLIKE_THRESHOLD = 29
    POEM_LIKE_THRESHOLD = 45
    
    #Building the word list
    full_wordlist = []
    with renpy.file('poemwords.txt') as wordfile:
        for line in wordfile:
            #Ignore lines beginning with '#' and empty lines
            line = line.strip()
            
            if line == '' or line[0] == '#': continue
            
            #File format: word,mPoint,nPoint,sPoint,yPoint
            x = line.split(',')
            full_wordlist.append(PoemWord(x[0], float(x[1]), float(x[2]), float(x[3]), float(x[4])))
            
            
    monikaTime = renpy.random.random() * 4 + 4
    natsukiTime = renpy.random.random() * 4 + 4
    sayoriTime = renpy.random.random() * 4 + 4
    yuriTime = renpy.random.random() * 4 + 4
    monikaPos = 0
    natsukiPos = 0
    sayoriPos = 0
    yuriPos = 0
    monikaOffset = 0
    natsukiOffset = 0
    sayoriOffset = 0
    yuriOffset = 0
    monikaZoom = 1
    natsukiZoom = 1
    sayoriZoom = 1
    yuriZoom = 1
    
    def randomPauseSayori(trans, st, at):
        if st > sayoriTime:
            global sayoriTime
            sayoriTime = renpy.random.random() * 4 + 4
            return None
        return 0
        
    def randomPauseNatsuki(trans, st, at):
        if st > natsukiTime:
            global natsukiTime
            natsukiTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseYuri(trans, st, at):
        if st > yuriTime:
            global yuriTime
            yuriTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseMonika(trans, st, at):
        if st > monikaTime:
            global monikaTime
            monikaTime = renpy.random.random() * 4 + 4
            return None
        return 0
        
    def randomMoveMonika(trans, st, at):
        global monikaPos
        global monikaOffset
        global monikaZoom
        if st > .16:
            if monikaPos > 0:
                monikaPos = renpy.random.randint(-1,0)
            elif monikaPos < 0:
                monikaPos = renpy.random.randint(0,1)
            else:
                monikaPos = renpy.random.randint(-1,1)
            if trans.xoffset * monikaPos > 5: monikaPos *= -1
            return None
        if monikaPos > 0:
            trans.xzoom = -1
        elif monikaPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * monikaPos
        monikaOffset = trans.xoffset
        monikaZoom = trans.xzoom
        return 0
        
    def randomMoveNatsuki(trans, st, at):
        global natsukiPos
        global natsukiOffset
        global natsukiZoom
        if st > .16:
            if natsukiPos > 0:
                natsukiPos = renpy.random.randint(-1,0)
            elif natsukiPos < 0:
                natsukiPos = renpy.random.randint(0,1)
            else:
                natsukiPos = renpy.random.randint(-1,1)
            if trans.xoffset * natsukiPos > 5: natsukiPos *= -1
            return None
        if natsukiPos > 0:
            trans.xzoom = -1
        elif natsukiPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * natsukiPos
        natsukiOffset = trans.xoffset
        natsukiZoom = trans.xzoom
        return 0
        
    def randomMoveSayori(trans, st, at):
        global sayoriPos
        global sayoriOffset
        global sayoriZoom
        if st > .16:
            if sayoriPos > 0:
                sayoriPos = renpy.random.randint(-1,0)
            elif sayoriPos < 0:
                sayoriPos = renpy.random.randint(0,1)
            else:
                sayoriPos = renpy.random.randint(-1,1)
            if trans.xoffset * sayoriPos > 5: sayoriPos *= -1
            return None
        if sayoriPos > 0:
            trans.xzoom = -1
        elif sayoriPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * sayoriPos
        sayoriOffset = trans.xoffset
        sayoriZoom = trans.xzoom
        return 0
        
    def randomMoveYuri(trans, st, at):
        global yuriPos
        global yuriOffset
        global yuriZoom
        if st > .16:
            if yuriPos > 0:
                yuriPos = renpy.random.randint(-1,0)
            elif yuriPos < 0:
                yuriPos = renpy.random.randint(0,1)
            else:
                yuriPos = renpy.random.randint(-1,1)
            if trans.xoffset * yuriPos > 5: yuriPos *= -1
            return None
        if yuriPos > 0:
            trans.xzoom = -1
        elif yuriPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * yuriPos
        yuriOffset = trans.xoffset
        yuriZoom = trans.xzoom
        return 0
        
label poem(transition=True):
    stop music fadeout 2.0
    scene bg notebook
    show screen quick_menu
    show m_sticker at sticker1
    show n_sticker at sticker2
    show s_sticker at sticker3
    show y_sticker at sticker4
    if transition:
        with dissolve_scene_full
        play music t4
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    if chapter == 0:
        call screen dialog("It's time to write!\n\nPick words you think your favorite club member\nwill like. Once you finish, make sure to\nread over what you wrote.\n\nRemember, whoever likes your work the most\nwill take an interest in you!", ok_action=Return())
    python:
        progress = 1
        numWords = 20
        mPointTotal = 0
        nPointTotal = 0
        sPointTotal = 0
        yPointTotal = 0
        wordlist = list(full_wordlist)
        
        monikaTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        sayoriTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        monikaPos = renpy.random.randint(-1,1)
        natsukiPos = renpy.random.randint(-1,1)
        sayoriPos = renpy.random.randint(-1,1)
        yuriPos = renpy.random.randint(-1,1)
        monikaOffset = 0
        natsukiOffset = 0
        sayoriOffset = 0
        yuriOffset = 0
        monikaZoom = 1
        natsukiZoom = 1
        sayoriZoom = 1
        yuriZoom = 1
        
        
        
        
        # Main loop for drawing and selecting words
        madlibs = []
        while True:
            ystart = 160
            pstring = str(progress)
            ui.text(pstring + "/" + str(numWords), style="poemgame_text", xpos=810, ypos=80, color='#000')
            for j in range(2):
                if j == 0: x = 440
                else: x = 680
                ui.vbox()
                for i in range(5):
                    word = random.choice(wordlist)
                    wordlist.remove(word)
                    ui.textbutton(word.word, clicked=ui.returns(word), text_style="poemgame_text", xpos=x, ypos=i * 56 + ystart)
                    madlibs.append(word)
                ui.close()
        
            t = ui.interact()
            if t.mPoint >= 3:
                renpy.show("m_sticker hop")
            if t.nPoint >= 3:
                renpy.show("n_sticker hop")
            if t.sPoint >= 3:
                renpy.show("s_sticker hop")
            if t.yPoint >= 3:
                renpy.show("y_sticker hop")
            mPointTotal += t.mPoint
            nPointTotal += t.nPoint
            sPointTotal += t.sPoint
            yPointTotal += t.yPoint
            progress += 1
            if progress > numWords:
                break
        
        
        #Logic for assigning poem appeal and scene order
        unsorted_pointlist = {"monika": mPointTotal, "natsuki": nPointTotal, "sayori": sPointTotal, "yuri": yPointTotal}
        pointlist = sorted(unsorted_pointlist, key=unsorted_pointlist.get)
        
        #Set poemwinner to the highest scorer
        poemwinner[chapter] = pointlist[3]
        
        #Add appeal point based on poem winner
        exec(poemwinner[chapter][0] + "_appeal += 1")
        
        #Set appeal
        if mPointTotal < POEM_DISLIKE_THRESHOLD: s_poemappeal[chapter] = -1
        elif mPointTotal > POEM_LIKE_THRESHOLD: s_poemappeal[chapter] = 1
        if nPointTotal < POEM_DISLIKE_THRESHOLD: n_poemappeal[chapter] = -1
        elif nPointTotal > POEM_LIKE_THRESHOLD: n_poemappeal[chapter] = 1
        if sPointTotal < POEM_DISLIKE_THRESHOLD: s_poemappeal[chapter] = -1
        elif sPointTotal > POEM_LIKE_THRESHOLD: s_poemappeal[chapter] = 1
        if yPointTotal < POEM_DISLIKE_THRESHOLD: y_poemappeal[chapter] = -1
        elif yPointTotal > POEM_LIKE_THRESHOLD: y_poemappeal[chapter] = 1        
        
        #Poem winner always loves
        exec(poemwinner[chapter][0] + "_poemappeal[chapter] = 1")
        
    call showpoem(poem_mc1)
    
    $ config.allow_skipping = True
    $ allow_skipping = True
    stop music fadeout 2.0
    show black as fadeout:
        alpha 0
        linear 1.0 alpha 1.0
    pause 1.0
    return
    
image s_sticker:
    "gui/poemgame/s_sticker_1.png"
    xoffset sayoriOffset xzoom sayoriZoom
    block:
        function randomPauseSayori
        parallel:
            sticker_move_n
        parallel:
            function randomMoveSayori
        repeat

image n_sticker:
    "gui/poemgame/n_sticker_1.png"
    xoffset natsukiOffset xzoom natsukiZoom
    block:
        function randomPauseNatsuki
        parallel:
            sticker_move_n
        parallel:
            function randomMoveNatsuki
        repeat

image y_sticker:
    "gui/poemgame/y_sticker_1.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image m_sticker:
    "gui/poemgame/m_sticker_1.png"
    xoffset monikaOffset xzoom monikaZoom
    block:
        function randomPauseMonika
        parallel:
            sticker_move_n
        parallel:
            function randomMoveMonika
        repeat
        
image s_sticker hop:
    "gui/poemgame/s_sticker_2.png"
    xoffset sayoriOffset xzoom sayoriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "s_sticker"

image n_sticker hop:
    "gui/poemgame/n_sticker_2.png"
    xoffset natsukiOffset xzoom natsukiZoom
    sticker_hop
    xoffset 0 xzoom 1
    "n_sticker"

image y_sticker hop:
    "gui/poemgame/y_sticker_2.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image m_sticker hop:
    "gui/poemgame/m_sticker_2.png"
    xoffset monikaOffset xzoom monikaZoom
    sticker_hop
    xoffset 0 xzoom 1
    "m_sticker"
    
transform sticker1:
    xcenter 75 yalign 0.9 subpixel True

transform sticker2:
    xcenter 160 yalign 0.9 subpixel True

transform sticker3:
    xcenter 245 yalign 0.9 subpixel True

transform sticker4:
    xcenter 330 yalign 0.9 subpixel True
    
transform sticker_move_n:
    easein_quad .08 yoffset -15
    easeout_quad .08 yoffset 0

transform sticker_hop:
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0