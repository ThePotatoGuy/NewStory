#init python:
#    import random
    
#    #This class holds a word, and point values for each of the four heroines
#    class PoemWord:
#        def __init__(self, word, mPoint, nPoint, sPoint, yPoint):
#            self.word = word
#            self.mPoint = mPoint
#            self.nPoint = nPoint
#            self.sPoint = sPoint
#            self.yPoint = yPoint
            
#    #Static variables for the characters' poem appeal: Dislike, Neutral, Like
#    POEM_DISLIKE_THRESHOLD = 29
#    POEM_LIKE_THRESHOLD = 45
    
#    #Building the word list
#    full_wordlist = []
#    with renpy.file('poemwords.txt') as wordfile:
#        for line in wordfile:
#            #Ignore lines beginning with '#' and empty lines
#            line = line.strip()
            
#            if line == '' or line[0] == '#': continue
            
#            #File format: word,mPoint,nPoint,sPoint,yPoint
#            x = line.split(',')
#            full_wordlist.append(PoemWord(x[0], float(x[1]), float(x[2]), float(x[3])))
            
#    monikaTime = renpy.random.random() * 4 + 4
#    natsukiTime = renpy.random.random() * 4 + 4
#    sayoriTime = renpy.random.random() * 4 + 4
#    yuriTime = renpy.random.random() * 4 + 4
#    monikaPos = 0
#    natsukiPos = 0
#    sayoriPos = 0
#    yuriPos = 0
#    monikaOffset = 0
#    natsukiOffset = 0
#    sayoriOffset = 0
#    yuriOffset = 0
#    monikaZoom = 1
#    natsukiZoom = 1
#    sayoriZoom = 1
#    yuriZoom = 1
    
#    def randomPauseSayori(trans, st, at):
#        if st > SayoriTime:
#            global sayoriTime
#            sayoriTime = renpy.random.random() * 4 + 4
#            return None
#        return 0
        
#    def randomPauseNatsuki(trans, st, at):
#        if st > natsukiTime:
#            global natsukiTime
#            natsukiTime = renpy.random.random() * 4 + 4
#            return None
#        return 0

#    def randomPauseYuri(trans, st, at):
#        if st > yuriTime:
#            global yuriTime
#            yuriTime = renpy.random.random() * 4 + 4
#            return None
#        return 0

#    def randomPauseMonika(trans, st, at):
#        if st > monikaTime:
#            global monikaTime
#            monikaTime = renpy.random.random() * 4 + 4
#            return None
#        return 0
        
#    def randomMoveMonika(trans, st, at):
#        global monikaPos
#        global monikaOffset
#        global monikaZoom
#        if st > .16:
#            if monikaPos > 0:
#                monikaPos = renpy.random.randint(-1,0)
#            elif monikaPos < 0:
#                monikaPos = renpy.random.randint(0,1)
#            else:
#                monikaPos = renpy.random.randint(-1,1)
#            if trans.xoffset * monikaPos > 5: monikaPos *= -1
#            return None
#        if monikaPos > 0:
#            trans.xzoom = -1
#        elif monikaPos < 0:
#            trans.xzoom = 1
#        trans.xoffset += .16 * 10 * monikaPos
#        monikaOffset = trans.xoffset
#        monikaZoom = trans.xzoom
#        return 0
        
#    def randomMoveNatsuki(trans, st, at):
#        global natsukiPos
#        global natsukiOffset
#        global natsukiZoom
#        if st > .16:
#            if natsukiPos > 0:
#                natsukiPos = renpy.random.randint(-1,0)
#            elif natsukiPos < 0:
#                natsukiPos = renpy.random.randint(0,1)
#            else:
#                natsukiPos = renpy.random.randint(-1,1)
#            if trans.xoffset * natsukiPos > 5: natsukiPos *= -1
#            return None
#        if natsukiPos > 0:
#            trans.xzoom = -1
#        elif natsukiPos < 0:
#            trans.xzoom = 1
#        trans.xoffset += .16 * 10 * natsukiPos
#        natsukiOffset = trans.xoffset
#        natsukiZoom = trans.xzoom
#        return 0
        
#    def randomMoveSayori(trans, st, at):
#        global sayoriPos
#        global sayoriOffset
#        global sayoriZoom
#        if st > .16:
#            if sayoriPos > 0:
#                sayoriPos = renpy.random.randint(-1,0)
#            elif sayoriPos < 0:
#                sayoriPos = renpy.random.randint(0,1)
#            else:
#                sayoriPos = renpy.random.randint(-1,1)
#            if trans.xoffset * sayoriPos > 5: sayoriPos *= -1
#            return None
#        if sayoriPos > 0:
#            trans.xzoom = -1
#        elif sayoriPos < 0:
#            trans.xzoom = 1
#        trans.xoffset += .16 * 10 * sayoriPos
#        sayoriOffset = trans.xoffset
#        sayoriZoom = trans.xzoom
#        return 0
        
#    def randomMoveYuri(trans, st, at):
#        global yuriPos
#        global yuriOffset
#        global yuriZoom
#        if st > .16:
#            if yuriPos > 0:
#                yuriPos = renpy.random.randint(-1,0)
#            elif yuriPos < 0:
#                yuriPos = renpy.random.randint(0,1)
#            else:
#                yuriPos = renpy.random.randint(-1,1)
#            if trans.xoffset * yuriPos > 5: yuriPos *= -1
#            return None
#        if yuriPos > 0:
#            trans.xzoom = -1
#        elif yuriPos < 0:
#            trans.xzoom = 1
#        trans.xoffset += .16 * 10 * yuriPos
#        yuriOffset = trans.xoffset
#        yuriZoom = trans.xzoom
#        return 0
        
#label poem(transition=True):
#    stop music fadeout 2.0
#    scene bg notebook
#    show screen quick_menu
#    if persistent.mEE == True:
#        show m_sticker at sticker1
#        show n_sticker at sticker2
#        show s_sticker at sticker3
#        show y_sticker at sticker4
#    else:
#        show n_sticker at stickerL
#        show s_sticker at stickerM
#        show y_sticker at stickerR
#    if transition:
#        with dissolve_scene_full
#        play music t4
#    $ config.skipping = False
#    $ config.allow_skipping = False
#    $ allow_skipping = False
#    if chapter == 0:
#        call screen dialog("It's time to write!\n\nPick words and fuck off.", ok_action=Return())
#    python:
#        progress = 1