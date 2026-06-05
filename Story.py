# Story

creds = 0
secrets = 0
name = [] 
knowledge = []
print("\nWelcome to Stream!")  
wanderer = input("\nWhat is your Name? ").strip()
if wanderer == "":
    wanderer = "Stranger"
elif len(wanderer) > 15:
    wanderer = wanderer [:15]
    

print(""" 
The air feels thick, a breath from the city itself. 

Sweat is already forming on your back.
      
A child is staring at you with head slightly tilted to the left.
      
“You just arrived from the nothing? Are you a ghost?”
      
“Don’t be silly, ” said their twin walking up from behind, “Ghosts are made of stone. They look squishy. And they are sweating.” 

“Maybe you are forming.” said the first.

“Or dying?” said the second.
""")  

print("What do you say?")  

print ("1. I don’t know.")

print ("2. Where am I?")

print ("3. Who are you?")

print("4. I like your No-Face tee-shirts.")

choice = input ("\n" + wanderer + ", what is your response? ")

if choice == "1" :
    print ("That's ok.") 
    print (""" 
"That's ok. It doesn’t really make much of a difference, anyway.” said the first.
     """)
elif choice == "2" :
    print("""“
Stream.” they say in unison. 

The neon creates a light that is both bright and dark at once. The building are massive and sky bridges criss cross the sky. “I don’t know this city." you say quietly suddenly realizing the sound of the stream around you.

“Just Stream, not Stream City.” says the second say slowly and carefully, obviously concluding you are a bit slow. 
            """)
elif choice == "3" :
    print ("""
They approach close on either side of you and beckon to you with hooked fingers to bend down so they can whisper a secret. 

With cupped hands against your ears they whisper a dream. 

You raise up slowly. You know knowledge is shared but your mind can neither hear nor understood what was said.
           """)
elif choice == "4" :
    print (""" 
The twins turn to face each other and look at the others tee-shirts. 

“I do like your shirt.”

“I like your too!”

The give a small laugh. Surprisingly discordant.

Without turning their bodies they turn their heads to look at you. The first looks concerned.  
           
“You shouldn't wear black here, not when your are new.”
           

“It’s too easy to fade.” 

You are, in fact, wearing a plain black tee.
""")
else :
    print("""
The twins look for a moment longer.  The second says "Sqishy has turned back to stone it seems." 
    """)

print ("When you look up the twins had already started running down the street laughing, their yellow tee-shirts shifting colors in the neon lights all around. ")

print ("""
You can’t place the city that surrounds you though it is frustratingly familiar.  Massive building scratch at the sky and create corridors of streets.  There are no stars and clouds hang low obscuring the tops of some building giving an illusion that they climb forever.  Windows disappearing into the clouds with light dispersed look like rows of small suns, loosing intensity as they fall into the night sky.

It obviously raided, and given the heavy sky it feels like it may again. Still the road glistens as the water dances with neon light. Small pacts of rainbow colors against the blacktop – one of Rothko’s half-remembered dream.

Looking in the direction the twins took you see the neon lights seem to intensify, more densely packed signage, lights spilling from store fronts, traffic and street lights. At the corner of the street in the opposite direction is a diner. Light reluctantly emits from the mostly glass walls, it’s hard to tell if it’s because the lights are dim or the windows tinted.  Across the street a stairway leads down.  A large reflective white M hangs above it. The reflective paint gives it a light house strobing effect as cars drive by.
""")
print("\nYou can: ")  

print("""
1. Head in the same directions as the twins towards the brighter lights

2. Enter the diner

3. Descend the stairs
""")

choice = input ("Where to? ")