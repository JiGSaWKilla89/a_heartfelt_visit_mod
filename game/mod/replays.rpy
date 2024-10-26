
label galleryRename:
    default persistant.galleryRename = False
    default galleryMC = VariableInputValue("mc", default=True, returnable=False)
    return

default persistent._replay_name = "Robert"

init python:
    def set_replay_name():
        global mc
        persistent._replay_name = mc.name

    config.after_load_callbacks.append(set_replay_name)


    class ReplayData():
        ReplayList = []
        def __init__(self, image, label, title, description='', scope={}, locked=False):
            self.idle = Transform(image, zoom=0.23, matrixcolor=BrightnessMatrix(0.0))
            self.hover = Transform(image, zoom=0.23, matrixcolor=BrightnessMatrix(0.2))
            self.title = title
            self.label = label
            self.scope = scope
            self.locked = locked
            self.description = description
            ReplayData.ReplayList.append(self)

define replay_1 = ReplayData(
    "c1_sofa19", 
    "galleryscene1", 
    "Dream of Nina")

define replay_2 = ReplayData(
    "c1_backyard21", 
    "galleryscene2", 
    "Teasing Lana")

define replay_3 = ReplayData(
    "c1_lana34", 
    "galleryscene3", 
    "Lana Sex")
            

style replays_text:
    text_align 0.5
    align (0.5,0.5)
    outlines [(2, "#0009", 1 ,1)]

style replays_vbox:
    spacing 10

screen replays():
    $ tooltip = GetTooltip()
    style_prefix "replays"
    tag menu
    use game_menu(_("Replays"), scroll="viewport"):

        vpgrid:
            cols 3
            spacing 35
            #allow_underfull True
            
            for replay in ReplayData.ReplayList:
                vbox:
                    imagebutton:
                        idle replay.idle
                        hover replay.hover
                        action Replay(replay.label, scope=replay.scope, locked=replay.locked) tooltip replay.description
                    text replay.title

    if tooltip:
        ## Use With Renpy Version Below 7.5 and 8.0
        frame:
            style_prefix "tooltip"
            hbox:
                text tooltip
        ## Use With Renpy Version Above 7.5 and 8.0
        #nearrect:
        #    focus "tooltip"
        #    prefer_top True
        #    frame:
        #        at choice_appear(.5)
        #        style_prefix "tooltip"
        #        hbox:
        #            text tooltip


label galleryscene1:
    scene c1_sofa10 with fade
    $renpy.pause(0.3, hard=True)
    scene c1_black with fade
    $renpy.pause(0.3, hard=True)
    scene c1_sofa10 with fade
    $renpy.pause(0.3, hard=True)
    scene c1_black with fade
    $renpy.pause(0.3, hard=True)
    scene c1_black with fade
    play music "sfx/flow-211881.mp3"

    nina "How about kissing?"

    scene c1_sofa19 with dissolve

    mc "Wow, Nina."

    mc "When did you take your shirt off?"

    scene c1_sofa20 with dissolve

    nina  "Mwah"

    mc "Your lips are so soft."

    scene c1_sofa17 with dissolve

    nina  "I want you to get undressed."

    nina  "Please."

    scene c1_sofa18 with dissolve

    mc "Are you serious?"

    mc "Of course."

    mc "I'm going to take off my pants."

    scene c1_sofa21 with dissolve

    nina "I've been waiting for you to fuck me since the first day you arrived."

    nina "I can't wait to feel your cock inside me."

    scene c1_sofa14 with dissolve

    mc "Are you sure it's okay, Nina?"

    mc "What happens if Chloe comes into the living room?"

    mc "Or Nicholas?"

    scene c1_sofa24 with dissolve

    nina "I was never so sure."

    nina "Relax."

    nina "Let me do the work."

    scene c1_sofa16 with dissolve

    mc "Nina?"

    mc "Can you take it in your mouth?"

    scene c1_sofa15 with dissolve

    nina "Of course, baby!"

    nina "Let me take care of it.."

    scene c1_sofa22 with dissolve

    nina "Your cock is so big.."

    nina "And hard.."

    scene c1_sofa23 with dissolve

    nina "%(player_name)s..."

    nina "%(player_name)s...."

    nina "%(player_name)s....."

    mc "What?"

    scene c1_sofa10 with fade

    nina "You fell asleep?"

    nina "The movie is over."

    nina "It's late."

    nina "I have a little more work to do then I go to bed."

    nina "Thanks for keeping me company."
    $ renpy.end_replay()


label galleryscene2:
    scene c1_backyard20 with dissolve
    play music "sfx/flow-211881.mp3"
    mc "(That’s it, you’ve slipped up now.)"
    
    mc "(The taboo is broken, and you’re mine now.)"
    
    mc "(It’s only a matter of time.)"

    scene c1_backyard21 with dissolve

    mc "(No matter how old you are, your tits are screaming to be grabbed.)"
    
    mc "(That bombshell body’s not meant to waste away unused.)"

    lana "Mmph…!"

    scene c1_backyard22 with dissolve

    mc "(Come here, let’s get straight to the heart of the matter.)"

    lana "Mmmwah…! Wait… What are you doing?"

    mc "Do you want me to stop?"

    lana "No.. I.. Please don't."

    mc "I knew it."

    mc "Seeing just how desperate your body is for attention."

    mc "Come here. Get on the table."

    scene c1_backyard23 with dissolve

    show myvideo10

    mc "(Oh yeah. Look at that finely aged pussy.)"

    mc "(She’s been keeping herself real pure for a while.)"

    mc "I knew you were just waiting for something to happen to you."
    
    mc "You need some \"exercise\" to stay satiated, don’t you?"

    lana "That’s… that’s not true!"

    show myvideo10
    mc "It’s not?"
    
    mc "Then how do you explain how fast your heart is beating, or how wet your pussy is?"
    
    mc "And I don’t mean from the rain."

    mc "You’re a little naughty for a housewife, Lana."

    scene c1_backyard24 with dissolve

    lana "Why did you stop?"

    mc "You like it?"

    mc "Want me to continue?"

    lana "Well.."

    scene c1_backyard25 with dissolve

    lana "God.."

    lana "It feels so good."

    show myvideo10

    mc "This body is so lewd even despite your age."
    
    mc "You must take good care of yourself at home all day."

    mc "But that must also get to be a bit lonely, huh?"
    
    mc "Not having anyone to plow you when you get in the mood must suck."

    scene c1_backyard30 with dissolve
    
    lana "That’s not… I don’t…"

    lana "Ooh!"

    mc "What’s wrong?"

    mc "Mmph!"

    mc "(Damn, she really got riled up by that!)"

    mc "(So much to grab… What a killer body for a troubled housewife.)"

    scene c1_backyard31 with dissolve

    lana "We… We should stop."

    lana "Just… just go for now."

    lana "I need to get dressed…"

    mc "(Damn, not completely convinced yet.)"

    mc "(There she goes. Best to leave it at that for now.)"
    
    mc "(Let her doubts swirl around in her head till she comes to a favorable conclusion.)"

    mc "(Until then, let’s give her some space.)"
    $ renpy.end_replay()


label galleryscene3:
    scene c1_lana33 with dissolve
    menu:
        "Take her robe off":

            scene c1_lana34 with dissolve

            lana "What are you doing?"

            lana "I did not expect this."

            lana "You are more daring than I thought."

            scene c1_lana35 with dissolve

            mc "Am I?"

            mc "You haven't seen everything yet."

            lana "Are you sure you want to do this?"

            mc "I am."

            scene c1_lana36 with dissolve

            mc "(I'm actually taking her panties off now.)"

            mc "(This was easier than I expected.)"

            scene c1_lana37 with dissolve

            lana "Ah.."

            mc "You have such a beautiful ass."

            mc "Your husband is a lucky man."

            scene c1_lana1 with dissolve

            mc "(Oh, boy!)"

            mc "You're leaking like a faucet."

            mc "You seem to be as impatient as I am."

            scene c1_lana38 with dissolve

            lana "I want you inside me."

            scene c1_black with dissolve

            lana "Come here!"

            lana "Lie down."

            mc "Like this?"

            scene c1_lana46 with dissolve

            lana "I didn't expect you to be so.. big."

            lana "I can barely get it in."

            lana "Take it slowly, okay?"

            scene c1_lana45 with dissolve

            mc "Fuck"

            mc "Feels so good."

            mc "You are a bit tight."

            show myvideo8

            lana "You like it?"

            mc "Oh, god.."

            mc "Yes.."

            lana "Your cock feels so good."

            lana "It's stretching my pussy."

            mc "You like it, baby?"

            lana "I do."

            lana "Do you want me to do it faster?"

            mc "Don't."

            mc "I'm almost cumming."

            mc "I can barely hold it."

            mc "I want to continue."

            lana "Ah.."

            scene c1_lana42 with fade

            joe "I can't believe I forgot my lunch again."

            joe "Luckily I didn't get too far."

            scene c1_lana43 with dissolve

            joe ".."

            scene c1_lana45 with dissolve

            mc "I think I heard a noise."

            lana "Someone just entered the house."

            lana "It's most likely Joe."

            lana "Please keep your mouth shut."

            lana "Hide around here somewhere."

            lana "He will probably leave soon."

            mc "I don't think he's leaving."

            mc "I can hear him climbing the stairs right now."

            lana "Just keep your mouth shut."

            lana "Let me talk to him."

            scene c1_black

            mc "(Fuck.)"

            mc "(Lana ran to the door to talk to Joe.)"

            mc "I'm standing next to her, but her husband can't see me."

            scene c1_lana39

            joe "Hey honey!"

            lana "Already back?"

            joe "Yes.. I forgot my lunch."

            joe "I just came up to see what you're doing."

            joe "All good?"

            joe "Why are you naked?"

            scene c1_lana41

            mc "(Fuck.)"

            mc "(That ass.)"

            mc "(Can't take my eyes off it.)"

            mc "(What if I fuck her from behind..)"

            mc "Joe wouldn't even know."

            scene c1_lana40

            mc "She doesn't seem to fight back."

            mc "She is enjoying it."

            show myvideo7

            lana "Aaaah.."

            joe "Honey?"

            joe "Are you ok?"

            lana "Yes."

            lana "I'm just sleepy."

            lana "That's all."

            lana "Will you let me go back to bed?"

            joe "Sure."

            joe "But.."

            joe "You should get dressed. It's pretty cold in here."

            joe "You'll get sick."

            lana "Okay, honey."

            joe "Bye, sweetie."

            scene c1_lana2 with dissolve

            lana "You're so nasty."

            lana "I can't believe what you just did."

            lana "What would have happened if Joe came in?"
            scene c1_lana3 with dissolve

            mc "Sorry about it"

            mc "I was so horny that I couldn't help myself."

            scene c1_lana5 with dissolve
            lana "It's ok."

            lana "I'm horny too."

            lana "Although I came three times already"

            mc  "Put it in your mouth, baby."

            scene c1_lana4 with dissolve

            lana "Like this?"

            lana "You like it?"

            scene c1_lana6 with dissolve

            mc "I do."

            mc "I'm almost cumming."

            lana "Come inside my mouth."

            scene c1_lana7 with dissolve
            $renpy.pause(0.3, hard=True)
            scene c1_lana48 with dissolve
            $renpy.pause(0.3, hard=True)
            scene c1_lana7 with dissolve
            $renpy.pause(0.3, hard=True)
            scene c1_lana48 with dissolve
            mc "Aghh.."
            scene c1_lana8

            lana "So much cum."

            lana "You almost drowned me."

            mc "Ooops."

            mc "I'm sorry."

            stop music
    $ renpy.end_replay()


#label galleryscene4:
#    $ renpy.end_replay()


#label galleryscene5:
#    $ renpy.end_replay()


#label galleryscene6:
#    $ renpy.end_replay()


#label galleryscene7:
#    $ renpy.end_replay()


#label galleryscene8:
#    $ renpy.end_replay()

#label galleryscene9:
#    $ renpy.end_replay()
