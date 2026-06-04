# Story

creds = 0
secrets = 0
name = [] 
knowledge = []
print("Welcome to Stream!") 
wanderer = input("What is your Name?")

print(""" 
The air feels thick, a breath from the city itself. Sweat is already forming on your back.
      
A child is staring at you with head slightly tilted to the left.
      
“You just arrived from the nothing? Are you a ghost?”
      
“Don’t be silly, ” said their twin walking up from behind, “Ghosts are made of stone. They look squishy. And they are sweating.” 

“Maybe you are forming.” said the first.

“Or dying?” said the second.""")

print("What do you say?")

print ("1. I don’t know.")

print ("2. Where am I?")

print ("3. Who are you?")

print("4. I like your No-Face tee-shirts.")

choice = input (wanderer + ", what is your response?")

if choice == "1" :
    print ("That's ok.") 
    print (""" "It doesn’t make much of a difference, really.” said the first. """)
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
           
    “You should wear black here, not when your are new.”
           

    “It’s too easy to fade.” 

    You are in fact in a plain black tee.
    """)
else :
    print("""
           "The twins look for a moment longer.  The second says "Sqishy has turned back to stone it seems." """)