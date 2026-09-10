user_choice = None

story = """ Raphael is presenting a project about biology in science class when an alarm suddenly begins blaring throughout the school.

A swarm of black suited men from NASA grab him and take him to a space station.

As they ride they debrief him. In short, he needs to check some things out 'cause hes soooo good at bio.

The rocket launches successfully and reaches orbit.

Mission Control contacts Raphael.

"Raphael, we have two important tasks for you."

"Which would you like to investigate first?"

A : A mysterious organism found on the moon.
OR
B : A satellite that has been taken over by a dark organism.
"""

print(story)

user_choice = input().lower()

if user_choice == "a":
    story = """Raphael lands close the area the organism is resting.

He inches closer slowly to avoid agitating it.

"It looks like a...massive tiger with stars as fur", he whispers

Should he:

A : Try to draw some blood.
OR
B : Throw a rock at it to wake it up and ask what it wants.
"""
    print(story)

    user_choice = input().lower()

    if user_choice == "a":
        story = """ He moves ever closer, and slowly pulls out a syringe.
        
He stab into the space tiger's butt with precision and force. Its blood is like that of a starry sky

The space tiger wakes up as he finishes drawing. 

It stares at him with a mix of anger and irritation.

Does Raphael


A : Run away.
OR
B : Explain the situation to an organism that likely does not speak English...
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """The tiger roars and chases after him

It catches him in a swift 2 seconds and Raphael is... Use your imagination.

In his final moments he wondered if he actually benefited humanity or was expendable for NASA to use.

Low-key some deep final thoughts.

THE END
"""
            print(story)
        else:
            story = """Raphael explains the situation to the tiger in under 20 sentences.

He ends by begging the tiger to spare his life. The tiger laughs. At least he knows it can understand english!

While the tiger is distracted, he sends the tiger blood back to NASA in a capsule in the hope that it may help with something. 

He sees it fly off into the distance before the tiger yeets him up and swallows him whole like a gummy.

THE END
"""
            print(story)

    else:
        story = """He picks up the biggest throwable rock he can find and guns it straight at the sleeping tiger. 
        
The tiger is abruptly woken up, and, perplexed, searches for who woke it up from its nap.

Upon gazing at the tigers full size, he realizes that waking it up with such a method may not have been the smartest idea.

Does he:
A : Run away sneakily.
OR
B : Hide, hoping the organism cannot smell or see him.

"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """He sets his suit to camouflage mode, blending in with the surface of the moon.
            
        He treads the moons surface until he find the space ship that brought him there.
        
         In the distance however, the tiger, having spotted him somehow, is running towards the shuttle.
         
          After powering some boosters or moving some levers, IDK, the ship rises above the surface of the moon. 
          
          He's safe from the tigers grasp.
        
        Until the tiger jumps up and brings the ship down thanks to its weight.
        
        In his final moments, he can't being to help but wonder why he made such a dumb decision...
        
        Its almost like someone was controlling his actions... His very being. Too late for such thoughts
        

THE END
"""
            print(story)
        else:
            story = """He cowers behind a rock to no avail. The tiger, sensing him with some galactic power, pulls 
            
            away at the rock he's hiding under with such force, it knocks him back 20 fee. 
            
            He beings to cry as the tiger approaches, already accepting his fate.
            
                 What happens next, I'm not sure I can say, but Raphael's presence ceased to exist that day.

THE END
"""
            print(story)

else:
    story = """Raphael docks the satellite.

A maintenance hatch is hanging open.

Inside he see's the dark organism...It looks like a symbiote.

It's eating wires.

A : Attempt to communicate with the symbiote.
OR
B : Chase the symbiote.
"""
    print(story)

    user_choice = input().lower()

    if user_choice == "a":
        story = """Surprisingly, the symbiote responds.

"Finally. Someone reasonable."

The symbiote explains that it accidentally found this satellite while floating in space.

A : Help the symbiote get accommodated on Earth.
OR
B : Let the symbiote stay.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """The symbiote safely returns to Earth and becomes an international celebrity.

Its autobiography, Slime Lyfe, becomes a bestseller.

THE END
"""
            print(story)
        else:
            story = """The symbiote remains in orbit and eventually fuses with the satellite to become a cool satellite symbiote thing with infinite data and signal and other phone stuff.

THE END
"""
            print(story)

    else:
        story = """The symbiote flees through the satellite.

During the chase, Raphael discovers a hidden room.

Inside the symbiote hides in a corner, looking scared.

A : Attempt to communicate with it (THINK ABOUT IT! REALLY THINK!)
OR
B : Try to catch the symbiote (IS IT WORTH IT?? FOR REAL??)
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """Raphael says hello the symbiote. 
            
            Puzzled it turned humanoid and responds with a greeting.

It simply says:

""Hi""

You becomes friends and take it back home. You both act in a movie called Poison 
(If you get it, you get it. No copyright!)

THE END
"""
            print(story)
        else:
            story = """ It eats you...
            
            
            
            (Told you it wasn't worth it😒)

THE END
"""
            print(story)