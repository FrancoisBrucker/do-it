# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character('Arthur', color="#000000")
define e = Character('Elise', color="#0800ff")
define j = Character('Jeanne', color="#006416")
define s = Character('Sebastian', color="#ff5a35")
define c = Character('Carolina', color="#ca005b")
define t = Character('Tom', color = "#006f64")



# True if the player has decided to compare a VN to a book.
default affinity_with_arthur = 0
default choixsuite2_1 = False



# The game starts here.

label start:

    # Chapter 1
    show text "Part 1" with Pause(1.5)
    show text "Chapter 1" with Pause(1.5)
    scene black with dissolve

    #transition slide
    scene bg bus_stop_night
    with dissolve

    "The night breath began to feel cold on Jeanne's naked legs."
    "It's a dream." 
    "Sitting on the street adjacent to the club, her elbows on her knees, she gazed at the moon, and thought about the live show of her favorite idol she missed."
    "“The first party of the year's the best for socializing as no group was formed yet”, Arthur had said. Yet, people arrived in cliques, all drunkenly laughing, appearing to know each other from highschool and clubs and such. "
    "Well, it was only the first week, she still had time to make friends. She only needed one or two. If necessary, she'd take the initiative."

    show jeanne coldannoyed at left
    
    "A blonde woman with a dark blue dress sat beside her."
    
    show lise turtleblacksmile at right

    "Blonde" "Hey, are you going home too?"

    j "Yeah, waiting for the bus."

    "Jeanne squinted. This face. She would have remembered it if they had met before. It was the typical unapproachable girl guys would confess to before summer break just to get over their feelings."

    show jeanne cold smile at left

    e "I'm Elise. First year in Bachelor of Physics."
    j "Jeanne. Same as you."
    e "What courses have you chosen? I've never met you at school."

    "Jeanne scratched her head before clicking her tongue. Arthur's reflex whenever he was troubled had contaminated her."

    e "Sorry, maybe you wanted some quiet." #her head dropped a little with the sprite

    "Jeanne waved her hand as to dissipate the misunderstanding."

    j "So, about school. Yeah, I don't go to lectures."

    "A frown appeared on Elise's face, but Jeanne didn't catch it."
    
    e "But it hasn't even been two weeks. Did your parents force you to follow this Bachelor's degree?"
    j "No, no, I did. To chill."
    e "To chill?"
    j "To watch anime, K-dramas, Netflix shows. Read manga, webtoon. Play video games, sleep in, etc. You?"

    "Elise looked in the distance, a dreamy smile hung on her lips."

    e "I can't really 'chill'."

    "It was a beautiful smile, with complex undertones."

    j "That's sad."

    e "Is it? Don't you get bored sometimes from 'chilling'?"

    j "Can't deny it."

    "The moonlight stretched over the top of the church down the street, letting Jeanne see that it was already three in the morning."

    e "Isn't there something you would like to do? I don't know, a stupid goal?"

    j "I'd love to have something like that."

    "A round silence filled the space between the two of them before Jeanne decided to pop it."

    menu:

        "Prout.": 
            jump suite1_1_1 

        "Wanna be friends?": 
            jump suite1_1_2

    label suite1_1_1:

        j "Wanna be friends?"

        jump suite1_1_2

    label suite1_1_2:
        
        j "Like friends?" 
        

    "Elise let out a chuckle."

    e "Sorry. Sorry, I'm not laughing at you. It's just that I haven't been asked this since I was in middle school."
    j "That's sad, I'll be your friend."

    "Elise chuckled once again."

    e "I didn't mean it like that"

    #transition

    scene bg condo with dissolve

    "Months passed by in a blink of an eye and winter settled in London in a grey snow."
    "Christmas being around the corner, Jeanne would soon leave her warm blanket to visit her parents back in France. Of course, she was ecstatic at the idea of visiting them. But, she knew that the topic of studies would come out and she didn't want to talk about it."
    "Additionally, Elise's building heating conveniently broke yesterday, so she was looking for a place to stay and Jeanne was looking for a reason to stay. What kind of friend would she be if she left Elise to be freezing in her small studio?"
    
    show arthur normal at left 
    
    a "Are you sure you don't want to come with me? You could just leave your keys to Elise if she can't go back to her parents' during the time it's getting repaired."
    
    show jeanne casual smile at right

    j "You trust people too much."
    a "It's literally your friend."
    j "I met her four months ago. Anyway, she'll be there in a minute, I'll see you in a week."
    a "Say hello to her. She can use my bedroom, I've washed the sheets and all."
    j "Yes, sir."
    a "Make sure to thank her properly. She can use my closet. I've made some space. Also, I've transferred you extra money for you to have proper meals. Don't spend it all at once. And, always check if the hotplates are switched off after cooking."

    hide arthur with moveoutleft

    "He insisted one last time to call him if there was anything before going, although he'd be busy helping the parents moving out from their old apartment in Paris. Another reason as for why Jeanne didn't want to go back home too early, she would have been sure to be exploited."
    "The company he started in his senior year of high school was faring so well that he had enough cash flow to buy a modest house near Calais for their parents to fully enjoy their retirement. The azure seaside was more preferable than this polluted and crowded grey town."
    "His excitement was showing, he had completed one of his numerous life-long goals."
    "When the door rang, Jeanne rolled off the sofa and welcomed Elise as her eyes ran through the flat."

    show lise smile at left

    e "I didn't expect it to be so tidy and modern."
    j "My brother likes clean and lean. I guess it does change from your place."

    "Arthur had absolutely wanted a classic American-designed kitchen with a wooden counter connected to the living-room and at least two bedrooms. According to him, it was trendy and practical. After buying it at the cost of his soul, he renovated the bathroom to make an Italian shower and isolated the walls for thermic efficiency and sound, the sound isolation being for his snoring to not bother his guest if he had one."

    e "Where can I leave my suitcase?"
    j "In my brother's room since you'll sleep there. He changed the sheets and all. My brother's kind of a clean freak. So don't do anything naughty in his bed."
    
    "Elise clicked her tongue."

    e "Like I would."

    "All of a sudden, Beyoncé's infamous song, Single Ladies, blasted their ears."

    j "Sorry. My new ringtone."

    "She took the call."

    j "Speaking of the devil."
    e "Arthur?"

    "Her big brother wanted to make sure that Elise arrived. She passed her the phone, since she was eyeing her phone so badly. He could have called her directly."

    #transition
    scene black with dissolve
    scene bg condo with dissolve

    "They put their wet socks away before flopping down on the couch. Normally, the weather should improve from tonight, but for now, they were exhausted from shopping and walking under the rain."
    "She got the crumbled paper in her pocket out as Elise put the purchases in the fridge."

    show jeanne casual smile at left

    j "Food is so expensive. My credit card is literally crying."

    "Jeanne read the receipt again before throwing it in the bin."

    show lise smile at right

    e "You know, my café is recruiting new employees."
    j "It's always recruiting."
    e "One of my colleagues finally found an internship. I'm sure the owner would be happy to take you in."
    j "I'll think about it. Take you in. Like a stray dog. I'll take you in, you silly."
    e "Well, I don't know if Jeanne is suitable for a dog's name."
    j "Right, if I were a dog, I'd rather have an original name. Like 'Zeus'."
    e "How about 'Jesus'?"

    "Elise scoffed."

    e "Do you see yourself walking a dog named 'Jesus'? Jesus, sit. Jesus, give your paw. Jesus! Don't pee on this wall! Jesus, your thing's hanging."
    j "'Jesus'?  Do you see yourself walking a dog named 'Jesus'? Jesus, sit. Jesus, give your paw. Jesus! Don't pee on this wall! Jesus, your thing's hanging."

    "Elise bit her lips to contain her laughter while Jeanne burst out laughing."

    e "I'm not going to hell for your stupid jokes. Let's cook dinner instead.."

    "And like the students they were, they whipped up two plates of carbonara pasta and returned to the sofa."

    j "Is there something you want to watch?" 

    "Jeanne said as she connected her laptop to the TV."

    e "How about studying?"
    j "Studying."

    "Jeanne slapped her hand against her forehead."

    j "Dumbass, we're on vacation."
    e "Right. Duh. We got essays to write, presentations to do and exercises to solve."
    j "Can wait until tomorrow. What are you more into tonight? Comedy? Romance? Horror?"

    menu:

        "Horror.":
            jump suite1_2_1 

        "Romance.": 
            j "Cute. Romance will be the genre then." 

    label suite1_2_1:

        j "Liar. I know you have a specific genre."

        e "Why are you asking then?"

        "Elise rolled her eyes."


 
    

    #transition to Chapter 2
    scene black with dissolve
    #Chapter 2
    show text "Chapter 2" with Pause(1.5)
    scene black with dissolve
    
    scene bg room

    "Seven o'clock rang, Elise propped up in a daze."
    "She flicked her alarm off and drew open the curtains. They fluttered in the breeze as the dark streets of London welcomed its first inhabitants. Nightly light seeped into the simple and neat bedroom."
    "Responsible for the opening of the café, she had to be there at around eight thirty, so without wasting time, she prepared herself and headed out quietly. The café was a thirty minute walk from Jeanne's flat."
    
    scene bg cafe with dissolve

    "She unlocked the door of the café. The counter, the tables, the floor were itching to be cleaned and the fridges, coffee machines, to be filled."
    "At nine, her morning shift colleague joined her. Though Sebastian always looked indifferent, he was serious and serviable, and he enabled her to rest a little."
    "Time flew at the beginning, but at around ten thirty, it met a slump as there wasn't much activity. When there wasn't much to do, Elise used to read a book or chat with the regulars. But today, she felt too exhausted for anything."
    "Perhaps it was because she wasn't sleeping in her own bed. Or maybe taking a shift at the restaurant yesterday night was too much."
    
    show sebastian smile at left

    s "Have you had enough sleep? You look slightly off."

    show lise smile at right
    
    e "Haven't slept well these days."
    
    "Sebastian glanced at his watch."

    s "There aren't much people today. You can go."
    e "Are you sure? I'm not in a hurry or anything."
    s "Go. Take this with you."

    "He gave her a little blue box."

    s "Merry Christmas Elise."
    e "Really? You didn't have to. Thank you. It's not anything big, innit?"
    s "Just a small present since you gave me one too."
    e "Well, thanks." 
    s "I can't believe I'm going back to Portugal this week. Dama wants to organize a big family meeting."
    e "Sounds good. Like a real grandma."

    "Elise went to fetch her bag."

    e "Please tell her I said hi. Have a nice holiday."
    s "You too!"

    #transition
    scene bg condo with dissolve

    "As soon as Elise arrived, she could smell the mushrooms and the cooked rice. She took off her brown boots and peeked her head through the hallway."

    show jeanne casual smile at left
    show lise smile at right

    e "I'm home."
    j "Welcome back."

    "Elise beamed. Even though it has been a week now, hearing “welcome back” to her “I'm home” put her in a weirdly good mood. "
    "Jeanne had cooked a mushroom risotto. Proud of it, she described every step of the recipe and how she tweaked it to adapt it to her tasting buds. And indeed, she appeared to love each bite of it."

    j "You're hiding something, aren't you?"
    e "What? How did you know?"
    j "So, what's that blue box?"

    menu:

        "Not telling!":
            jump suite2_1_1

        "What? How did you know?":
            python:
                choixsuite2_1 = True
            
            jump suite2_1_2

    label suite2_1_1:

        e "Not telling."
        j "So secretive! So you're not telling me about your plans for Christas either?"
        e "This, I can."

    label suite2_1_2:
        
        
        if choixsuite2_1 == True:

            e "What? How did you know?" 
            j "It was sticking out from the pocket of your coat. So who's it from?"
            e "From Sebastian, but I haven't opened it yet."
            j "You traitor. Didn't you intend to become my step-sister?"

            "Jeanne sniffled."

            j "I lost a friend. A dear friend."
            e "You're so dramatic. Stop it."
            j "You work too much anyway. Like my brother. Wouldn't work out."
            e "I need to put food in my plate."
            j "I can do that."

            "Elise gave a tired smile."

            j "Let's open it then."
            e "Why? You don't need to known what's in there."
            j "Oh, come on."

            "Elise laughed and pulled it out from her coat."

            e "Here."

            "The opened box revealed a light blue braided bracelet."

            j "Blue like your eyes. My brother should take a page from his book."

            "Elise took her phone out."

            j "What are you doing?"
            e "I'm messaging Sebastian to tell him that I'm thankful, and that I'd be wearing it."
            j "How about Arthur?"
            e "It's not such a big deal."
            j "What if he likes you?"
            e "Not happening. So, what do I message him? For thanks?"
            j "Send what you said, it's that simple."

    "Jeanne went to the sink and rinsed the plates with cold water before placing them in the dishwasher."

    j "Do you have anything planned for Christmas?"


    j "If you want to, you can come over."
    e "I'm already sleeping in your brother's bedroom."
    j "So what? It was my brother who suggested you sleep over in case I pass out again like a dead sock. We never finish the food anyway. My mom does too much. My parents would be more than happy to welcome you again."
    e "I'll think about it."

    if choixsuite2_1 == True: 
        "Elise's fingers tapped on her screen, alternating between the delete and the space keys."

        j "Just send that damned text."
    

    #transition
    scene black with dissolve
    
    scene bg condo

    "Jeanne checked again if she didn't forget anything before telling Elise to do the same."

    j "Good. We're going. Don't forget the gift you bought, Elise."
    e "Not like I could forget it."  
    j "Right."

    "Jeanne shook her head helplessly."
     
    j "We could have taken another pair with another color."
    e "No."    
    j "So stubborn."

    "They had gone to the central mall last Friday, the only day Elise didn't have work. And they literally spent a whole afternoon looking for one specific color for this item. Overthinking as always, Elise was Elise after all"

    #transition
    scene black with dissolve

    "They arrived in Lille in an hour thanks to the efficiency of the Thalys, then with a regional train, they reached Calais where Arthur waited for them."
    
    #transition
    scene rain with fade
    show arthur smile

    "They exited the train station and saw him waving his hands. He was wearing a black sweatshirt, jogging, all smiles and all soaked. Jeanne noticed Elise's warm smile at his sight."

    a "I forgot to take an umbrella. We'll have to make a run for it. The car is only a minute away from the entrance of the railway station."

    "His hand pointed at a red family car."

    a "It's this one. Watch for other cars. Let's wait for this one to go. And this one."
    j "Wait, wait, it's not one minute away!"

    "A terrifying icy rain and more than three hundred meters separated them from the car."

    a "If you run, it is. Go!"

    "He sprinted away." 

    a "Go! Go!"

    "Jeanne screamed as she and Elise ran after him."

    #transition
    scene bg seaside with fade

    "In the car, protected from the hail, they exhaled a sigh of relief. The North's moody weather wasn't a laughing matter. It could go from sunny to a thunderstorm in a minute."

    "Arthur started the engine."

    a "Fasten your seatbelts, the kids at the back. Sorry for the run by the way, Elise."
    e "It's fine, it was fun."
    j "Why don't you say sorry to me too?"

    "Jeanne could see Arthur in the interior mirror smiling. She sighed."

    j "How was the move?"
    a "Done. Wasn't easy to drive a truck, but you know what? Nobody got hurt and we did it in one go. How about you two?"
    j "Slept twelve hours daily, watched whatever shows there were, paradise on earth."
    e "Thank you for lending me your bedroom. I'll clean it carefully when you come back."
    a "Don't bother. I'll do the laudry and clean up when I go home, so make yourself comfortable. I should be the one thanking you for taking care of my sister and our newly adopted dog."
    e "No biggie, really."
    j "Is it far? I'm hungry."
    a "The groceries are in the trunk. I bought chips for you."
    j "That's my big bro."

    "Jeanne tried to reach them, but with her seatbelt on, she couldn't get her hands on the yellow bag. If only she could…"

    menu:

        "Try to reach for it.":
            jump suite2_2_1

        "Give up on the chips.":
            j "It's too far. Nevermind. I'll die of hunger."

    label suite2_2_1:

        a "Don't unfasten your seatbelt."

        j "I wasn't going to do it."

        a "Elise, can you please help this shortie? Her arms are too short."

        j "You're the one who's short."

        a "You like walking under the rain, don't you?"

        j "Sorry, big bro."

    #transition
    scene bg mansion with fade

    "Arthur had called it a modest stone cottage, but it deserved to be called a mansion with its long porch, beautiful yard, and four floors with each of them having a bathroom and three rooms. On the ground floor, there was a large dining hall, a well-equipped kitchen and an enormous living-room."
    "The two upper floors were the bedrooms, and the latest floor was the attic. It kept all the souvenirs Jeanne's parents collected throughout their different jobs."
    
    scene bg livingroom with fade

    show jeanne casual smile at left
    show lise smile at right

    "Elise sank in couch, her puffed out face reflected on the large TV screen. Jeanne told her the truth. Her mother did cook too much."

    j "Found it."

    "Jeanne sat beside her and shared her plaid she just found."

    j "You didn't have to force yourself, you know."
    e "It's not every day that you get the chance to eat home cooked meals."

    "Elise stroked her bloated belly contentedly."

    e "What should I call him?"
    j "How do you know it's a boy?"
    e "Valid point. I should find two names."   
    j "You're wasted. I shouldn't have let you touch the bottle."

    "Elise rested her head on Jeanne's shoulder."

    e "I'm not."

    "Jeanne shrugged."

    j "Don't fall asleep."
    e "Why not? I know I'm heavy, but come on."
    j "Who said that?"
    e "My last ex."
    j "The one you dated at the start of the year?"
    e "Yes. Second job plus dating, plus partying, not doing that again. Awful breakup too."
    j "Awful? I thought you were doing just fine. Why didn't you call me?"
    e "We didn't know each other that much. And I would have bothered you."
    j "You wouldn't have bothered me."
    e "Would you leave your bed for me?"
    j "Yes I would."

    "Jeanne paused."

    j "First, reach out to your other friends, though."

    "They let out a little laugh"

    "And so, like every time they drank together, Jeanne fell asleep first. Her friend didn't have much resistance to alcohol and tiredness. Training didn't help either."
    "Her throat felt so dry to the point where she thought that the hangover would be fatal without water."

    scene black with dissolve

    default choice_2 = False 

    menu:

        "Go to the kitchen downstairs.":
            python:
                choice_2 = True
            jump suite2_3_2

            
        "Go to the bathroom.":
            
            scene black with dissolve
            "After drinking her fill, she walked to her bed and slept like a log."
        
    label suite2_3_2:
        if choice_2 == True:
            scene bg kitchen with fade

            "Elise snuck into the kitchen, but for some reason, the lights were on."
            
            a "Oh? You're not sleeping?"
            
            show arthur smile at center

            #fright

            "Elise almost drop her glass out of fright. She hadn't seen him and heard him. That was why the lights were on. Stupid."

            a "Haha, sorry."
            
            show arthur smile at right

            "His laptop was on the table."

            a "You should get to sleep."
            e "How about you?"

            show lise smile at left

            a "I'm answering questions from my master's students, and from you."

            "He smiled."

            "She nodded nervously as her heartbeat quickened."
            
            e "I shall accompany you then. Do you want some tea?"
            a "Sure. The tea is in the top right drawer. Mint for me. Thank you."

            "As the water was boiling, her brain was melting."
            "She placed the two teas on the table and sat on the chair opposite"

            a "You know what, I've changed my mind. Let's play a game."
            e "Are you sure? I didn't mean to disturb you."

            "She could feel the traits of her face moving, but couldn't imagine the expression she was making, nor she wanted to."

            a "I was here to get a snack, so might as well take a break. We should have a deck of cards."

            "He found two decks in one of the bottom drawers."

            a "Better two than one. How about a game of Slapjack?"

            "What he didn't know was that Elise was fond of games, especially card games. She might not be a genius player, but she might not be too far from it."
            "Her inner competitiveness took over her previous nervousness."
            "They played for an hour before he finally held his hands up to signify that he was giving up. She was just too good."
            "He refilled their mugs with mint tea."
            "The old clock hung on top of the fridge rang four in the morning. She had gotten so into the game that she didn't notice that it had gotten very late. The adrenaline was still rushing in her veins, erasing any traces of weariness."

            e "Let's change games. One that's easier on the reflexes and on the brain."
            a "I can't tell if you're being considerate or trash talking me."

            "Arthur laughed as his eyes drifted over her hands."
            
            a "Just choose a game where I don't have to worry about hitting your wrist."

            "He pointed at her bracelet."

            a "It suits you."

            "Mixed feelings filled her heart."

            e "Thanks."
            a "Well, if I win the next game, you'll go to sleep."

            "Elise remembered something."

            e "First, actually, I have a gift for you."
            a "Oh, I've got one for you too."
            e "Ah?"
            a "To thank you for taking care of my sister."

            #transition
            scene black with dissolve
            scene bg kitchen with fade


            "A minute later, they reappeared in the kitchen with their gifts. One was beautifully packed and the other was messily covered in black present wrap."

            show arthur smile at left
            show lise smile at right

            "Arthur scratched his head in embarrassment."

            a "I did my best with packaging. I hope you'll like it."

            "Elise unwrapped it carefully."

            a "Surprise? A dark blue waterproof coat for your family dog."

            "It'd look so cute. 'Can I hug you' was what she wanted to say, but all she could do was nodding with an awkward smile."

            "She gave him the present she prepared."

            "He opened the box."

            a "Reading glasses. A very considerate and useful gift."

            "He put them on."

            a "Do I look good?"

            "He chuckled."

            "Then he brought her into his arms."

            "She could feel his breath on her nape."

            a "Thank you, Elise."

            "He pulled back as her gaze stopped on his lips."

            python:
                affinity_with_arthur += 1

            
    
    

        
    #transition to Chapter 3
    scene black with dissolve
    #Chapter 3
    show text "Chapter 3" with Pause(1.5) 
    scene black with dissolve
    scene bg condo with fade
    
    "A few days ago, the two girls had returned to London after celebrating New Year's Eve at a common friend's house, for the start of the semester, and had found themselves mired in a deep pit of unmotivation."
    "Arthur would return home in a week so Jeanne insisted that Elise stayed home although the heating of her building had already been repaired." 
    "Elise could only agree. But, since she didn't do much, apart from going to work, class, and overthinking about her nonexistent love life, she was slowly getting depressed."
    "On the other hand, Jeanne was a slacker and a homebody by nature so she enjoyed going back to her life as a stay-at-home university student." 
    
    scene black with dissolve
    scene bg street_night with fade
    
    show jeanne casual smile at left
    show lise turtlevestsmile at right

    j "You're getting depressing, you know. Let's get snacks. You'll see that life isn't that bad."
    e "Should I text him?"
    j "Black hole-dense. For him, anything's a friendly gesture. I know it sounds contradictory. But he's the problem. He's a walking contradiction." 
    
    "Jeanne glanced at Elise."

    j "White doesn't look bad on you."
    e "It was pretty cheap, and the quality is amazing considering it's third-hand. It replaces my old torn jacket perfectly, don't you think?"
    j "As long as it keeps you warm."

    "Outside was as demoralizing as winter could get. No lights could illuminate these gloomy streets. Nobody smiled. Their eyes were glued to the ground like diamonds would emerge and free them from the capitalistic society."

    "On the way to the supermarket, Elise couldn't help but ask."

    e "Even if he's dense, how about a hug? Like a light hug?"

    "Jeanne stopped in her tracks. Her face was a mix of astonishment and disgust."

    j "What did you do to my brother?"
    e "He gave me a gift for Christmas."
    j "Yeah, the dog coat. I remember."
    e "Then, he hugged me."

    "Jeanne wheezed as her eyes sparkled."

    j "Did he? Bah. He hugs his friends too. Don't scare me like that."
    e "I should have kissed him."
    j "Wow. Wait. What if he had a girlfriend?"

    "Elise blankly stared at Jeanne."

    e "Does he have one?"
    j "How come you never asked him about it?"
    e "I don't know. I thought that maybe, you'd tell me if that was the case."

    scene black with dissolve
    scene bg backstreet with fade
    
    j "I guess so. Would you rather have chips or ice cream?"

    menu:

        "Chips.":
            j "That's why we can't be friends."

        "Ice cream.": 
            j "That's my friend." 

        "A sandwich.":
            j "Eh? Ok? Are you that hungry?"
        
            e "I guess so."


#appartment 

    scene black with dissolve
    scene bg condo with fade
    
    show lise turtlevestsmile at right

    "Elise woke up early to open the café. While she poured the boiling water into her green mug, she heard a door creaking."
    "Pink pajamas with winged pigs on it, disheveled black hair, yawning like a lion, Jeanne trudged to one of the kitchen chairs."

    show jeanne casual smile at left

    "Elise consulted the time on the clock, then on her phone. It was indeed seven in the morning. Jeanne put her head in their arms without a word and soon began to snore."

    e "What is she doing?"

    "Elise laughed before jumping at the sound of keys." #jumping

    show arthur normal with moveinright

    a "Oh home, sweet freaking home."
    a "Five damned pounds for a train ticket. And they still can't change their old weakass fucking trains."

    "Then he caught Elise's flabbergasted stare."

    a "Oh."
    j "You're finally home."

    "Jeanne had woken up."

    a "Hi. Sorry, Elise. Act like you didn't hear anything."

    "His hand arranged bits of his cute morning hair."

    j "Now, you know from whom I learnt my cursing habit."
    a "Are we throwing a welcome party?"
    j "I was waiting for my delivery man. Where is it? My limited edition light novel."
    a "What do you have in exchange?"

    "The negotiations went straight on full steam."
    
    "Meanwhile, Elise drank her black tea, and brushed her teeth. She was delighted to see Arthur again."

    scene black with dissolve
    scene bg condo with fade

    show lise turtlevestsmile at right

    "'I still would have loved a hug. Even a friendly one', Elise thought. 'I guess I'll go back home today.'"

    show jeanne casual smile with moveinright

    j "I'll tag along."

    "Elise frowned, but didn't ask why. Jeanne was Jeanne."

    e "Sure, suit yourself."
    j "My life as an unemployed incel reached its end. It pains me to say it. But. Please introduce me to your boss, Elise."
    e "No."
    j "Eh?"

    "Jeanne's jaw hit the floor."

    e "I'm kidding, you're in luck. The boss's son's here today."

    "Elise waited for Jeanne to get ready before calling the elevator."

    e "If I knew it was that easy to convince you to join the café."
    j "Time to use the social skills I honed over these hundreds of hours of dating simulator."
    e "I like the enthusiasm."
    j "Well, I'm not doing overtime. No giving up on hobbies."
    e "That's one thing I admire about you."

    "At the sudden compliment, Jeanne found herself speechless."

    e "You're cute when you get flustered."

    "Elise added with a cheeky smile on her face."

    #café

    scene black with dissolve
    scene bg cafe with fade

    "At the end, Jeanne accompanied Elise through her whole morning. It'd serve as a trial, the boss' son said." 
    "Contrary to his expectations based on what Elise shared about her, Jeanne proved to be quite competent with customers. During rush hours, she displayed remarkable composure and during the quieter times, she contributed to the joyful atmosphere of the café. "

    show jeanne casual smile at left
    show sebastian smile at right

    j "So, was my performance up to your standards, chief?"
    s "It was. Here. Read it and sign it."

    "He handed her two copies of the contract."
    "And, of course, Jeanne signed without reading."

    j "Easy-peasy, I can go back to being lazy. Thanks, Sebastian."
    s "You should thank Elise too for today's mentoring."
    j "Thanks bud."
    s "I'll see you two tomorrow. Don't be late."
    j "Sure, sure. Bye."

    "Jeanne dragged Elise through the exit door."

    hide jeanne with moveoutright

    #street
    scene black with dissolve
    scene bg street with fade

    show jeanne casual smile at left
    show lise smile at right

    j "He looks sad, doesn't he? Did you talk to him about your crush on Arthur?"
    e "I did, but I don't think that's the problem."
    j "How would you know?"
    e "Because he didn't show anything on his face and didn't mention it later. He just nodded."
    j "Right. Hard to tell what he thinks."
    e "Yes. But I do agree. He looked sad. Maybe, there's something I might have forgotten."
    j "If you, Elise, forget, I should get my brain checked."
    e "You should have gotten it checked ages ago."

    "Jeanne snorted."

    j "Now that I have a job, I'll be able to pay for my snacks and hobbies myself, since my brother is so unreliable."
    e "How come you sound so entitled and at the same time ironic?"

    "They chuckled."

    j "He wanted me to have better grades too."
    e "I want to have better grades too."

    "Jeanne rolled her eyes."

    j "As it was possible."

    #house
    scene black with dissolve
    scene bg room with fade

    "Elise glanced at Arthur's bedroom. In total, she had lived there for three weeks."
    "She had gotten used to smiling at the rows of romance novels sorted by their authors' name on the bookshelves; she had gotten used to seeing the folded men's shirt and pants in the wardrobe; and she had gotten used to sleeping in this single bed with a single pillow and a single duvet." 
    "She put the sheets in the laundry machine and waved goodbye to Jeanne who lazily waved her hand without detaching her eyes from the TV."

    scene black with dissolve

    #car
    "Arthur waited for her in his car." 
    "She put her suitcase in the trunk and sat beside him."
    "She typed her address on the board, she lived in Kensington which was on the other side of London, in the west."

    scene bg street_night with fade
    
    show arthur smile at left
    show lise smile at right

    "Elise asked Arthur about his holidays."
    "He thought long before speaking like he was recalling every detail and choosing the ones that would interest her. While his voice was full of energy, the strained traits of his face said otherwise."
    "He began by his family visit in Munich which was cut short, because he had to help with the cottage renovations."
    "As cliche as it sounded, over there, he had eaten kilograms and kilograms of sausages and potatoes, and speed-hiked a lot in the forests nearby. It had been arduous. Amidst that, they had a swim in the lake."

    j "Wasn't it frozen?"
    a "It was, but we dove head first, haha. You've got to try someday. I think that was the part I loved the most."

    "Afterwards, in Paris, he went to the football field where he started football and enjoyed a game with strangers. In the evening, he met with his highschool group of friends at a fairly affordable traditional French restaurant."
    "It had been hell to organize it as they all had their own personal lives and preoccupations, but the stories they shared made the trouble worthwhile."
    "Two years without seeing each other was a lot. Some were planning to marry while others had discovered what they wished to do in their lives."

    menu:

        "Ask a question about his future projects":
            jump suite3_2_1

        "Stay silent": 
            jump suite3_2_2
            
            
    label suite3_2_1:

        e "You mentioned that you were reviewing job interview questions at the cottage, don't you plan to continue building your company?"

        "He ran one hand through his hair."

        a "I'm still unsure. I don't know if it's the best way for me to be useful to the world. I'll have to think more about it."
        e "I'm sure you've created a positive impact."
        a "Thank you. Maybe, I'll join a charity association. Finally."

        "He said with a little smile."
        
        python:

            affinity_with_arthur += 1 

        jump suite3_2_2

    label suite3_2_2:

        "In the distance, an old woman looked troubled on the side of the road. The traffic lights flickered quickly to green letting cars go."
        "When they arrived at her level, Arthur stopped the car and let her pass. She gratefully bowed and gracefully crossed accompanied by the clapping of the horns behind them."
        "When she was gone, he restarted the engine and treaded tranquilly. He waited for the cacophony to end before talking again."

    a "How about you? Did you find your calling, Elise?"

    "She observed her faint reflection on the car window. Her calling? Could she sum up what she wanted to be, to do, to become in a single sentence?"

    e "I want to be able to support my future family. Not very interesting, innit?"

    "Her reply made Arthur's lips curl."

    a "No, it's an excellent answer."

    "The GPS notified them that they reached their destination. He parked the car near the block and accompanied her to the front door of her residence."

    scene bg someplace_usa_night with fade

    e "Thanks for the ride."
    a "A pleasure."
    e "See you."

    "Her arms wanted to reach for him, but they stayed aligned to her body. She bit her lips. What would she have to do to have a moment like that with him again? "

    a "See you, Elise."

    "Arthur waved at her."
    "She waved back."
    
    scene black with dissolve

    "She waited for the lift to arrive and politely greeted the random neighbors that waited with her. At the fourth floor, she left saying a small goodbye and walked to her door."
    "A shadow covered her face as her keys clicked." 
    "Elise put away her puffy jacket. "

    e "I'm home."

    "The sound of her steps and the wheels of her suitcase resonated in the small studio appartment. Nothing had changed from when she left apart from the layer of dust that had formed."
    "She took her phone and went on her message app, scrolled down to two numbers she never had the courage to block. She didn't receive any texts from them."
    "Elise retrieved her laptop and textbook from her school bag. One hour left, and she had to leave for the restaurant, so better make it productive."

    #café
    scene black with dissolve
    scene bg cafe with fade

    "Another day at the café, Jeanne bluntly pinned Sebastian's gaze when Elise went into the reserve to take a break because no one was coming into the café."

    show jeanne casual smile at left 
    show sebastian smile at right

    j "Are you okay? Like really okay?"

    "A crack formed in Sebastian's professional smile."

    s "There's really no use beating around the bush with you."
    j "If you aren't comfortable with sharing it, I will not press you."
    s "I appreciate it. It's just that, Dama, my grandma, is sick."
    j "Is it serious?"
    s "Kind of. I called her earlier, but I know that she loves to put up a brave front. We're waiting for more news. I'm flying back this weekend."

    "Jeanne patted him on the back."

    j "Well, she's gonna be fine with a grandson worrying over her like that."
    e "Thank you."
    
    "Judging from his tone, his mood had visibly improved."
    "Sharing your burden always lightened one's heart, but it meant that the listener would now have to carry this new weight on his shoulders, on her shoulders."
    "Jeanne reflected on her last words to her late grandmother as she wiped the cups clean."
    "That night, although she believed in no god, she'd pray for Sebastian grandmother's health."

#chapter 4
#café
    #transition to Chapter 4
    scene black with dissolve
    #Chapter 4
    show text "Chapter 4" with Pause(1.5)
    scene black with dissolve
    scene bg cafe with fade

    "The atmosphere at the café didn't change. It had shifted. Sebastian looked better. He even became more expressive. Her grandmother's condition had improved. On the other side, Elise sighed at every opportunity."

    #home

    scene black with dissolve
    scene bg condo with fade
    show jeanne casual smile at left
    show lise smile at right

    "Jeanne invited her home to discuss what bothered her. She made her sit in front of her at the kitchen table."
    "Next, she brought her bedside lamp and directed towards Elise who frowned, before switching on the living room lights and switching off the kitchen ones to create the desired and peculiar ambiance."

    j "First question. Is it related to Arthur?"
    e "Aren't you having too much fun?"
    
    "Elise glanced at Jeanne's detective cap and sunglasses."

    j "Answer, Miss Pellicer. Is it related to my brother?"
    e "No, it's not."

    "A shade of red colored her ears."

    j "Miss Pellicer. Why don't you just tell me the truth?"
    e "I'm telling the truth."

    "An extra shade cropped up."
    "Jeanne set up an imaginary mirror."

    j "Look for yourself. You can lie, but your body can't. Not for now at least." 
    e "I'd feel about if I don't talk now after you made all that effort."

    "Jeanne turned to the left and did an ok-sign with her fingers."

    j "I told you. I'm the best."
    e "What are you doing?"
    j "Telling my imaginary crew that our main culprit is ready to give her sources."

    "Elise almost laughed, before turning serious."

    e "Do you know a brunette that takes the bus to university?"
    j "Did you just describe three quarters of the school?"
    e "She's one of Arthur's friends, I assume, from the way they talked to each other. She's about five feet five. Long black hair tied into a ponytail. Her shoulders were large for a woman and she also had curves that fitted her body."
    j "That's a precise description. Five feet five?"
    
    "Jeanne converted the feet into centimeters on her phone."

    j "Oh, 1m65. Ok. You didn't follow them, did you?"
    e "Never. Only a stalker would do that. I went past them when I was going to class."
    j "I'll ask my brother about it."
    e "I feel like I'm prying into his personal life. I'd rather ask myself."
    j "Even though your interest would be made obvious?"
    
    "Elise nodded and gulped down the tea."

    e "It made me feel better to talk about it. Do you have other questions for me, officer?"
    j "The others are for Arthur."

    #home
    scene black with dissolve
    scene bg condo with fade

    "Arthur cooked dinner and watched an anime Jeanne chose while eating. Strangely enough, Jeanne dozed off during the show. She looked like she didn't enjoy it as much as before."
    "He took a sip of water when Jeanne suddenly pulled a brown cap and sunglasses from nowhere. A blinding light shone on his face as the lights of the living room were turned off."
    "What was up with her again?"

    show arthur smile at left
    show jeanne casual smile at right

    j "Hey. Big bro. Do you have someone you like?"

    "He choked on his drink."

    a "Wh-what?"
    j "A lover? I don't know, a friend, a colleague, maybe, someone who's around one meter sixty-five, brunette, with nice curves? I mean you're twenty-one, I wouldn't be surprised."
    a "You really ought to learn how to be tactful."
    j "I might have skipped that lesson when I skipped a year."
    a "How come I didn't? Anyway, I don't have anyone. Didn't Elise tell you? She asked me the same question earlier by text."
    j "Oh, did she? Interesting."
    a "Don't get any ideas."
    j "So who's that girl who's around one meter sixty-five, brunette, with nice curves? Someone to whom you gave something today?"
    a "Are you stalking me?"
    j "Nope. As a matter of fact, I didn't go out today except for going to the café. Like yesterday and the day before."
    a "Where's that café?"
    j "Next to the church."
    a "Oh. It should be the one near where I usually go. I'll come by."
    j "No, thank you. So, who is she?"
    a "A good friend."

    menu:
        "Continue the investigation.": 
            jump suite4_1_2

        "Stay silent.":
            jump suite4_1_1 


    label suite4_1_2:
        
        j "Wait, is it Carolina?"
        a "Yeah."
        j "Ah, I'm dumb. I should have guessed."
        a "Yup."
        j "Just to be sure. Don't you have anybody you fancy? Not love, but like?"
        a "Nope."
        j "Good. I'll go bck to my room to study."
        a "Sure you will weirdo."
        j "See you for dinner, weirdo number two."

    label suite4_1_1:

        "Jeanne sighed and rolled her eyes."


    #restaurant
    scene black with dissolve
    scene bg restaurant with fade

    "Elise put her phone back in her trousers and went out of the staff room. Her five-minute break was over."
    "He was not in a relationship."
    "She sighed in relief. She could work in an approximate peace of mind."
    "The restaurant was bustling like every night since last summer when an actor celebrity was sighted eating there. The fifteen tables inside were full, and the terrace too. Even then, there was a long queue outside waiting to taste the famous pizza that could even make celebrities break their diets."
    "The din was making her feel a bit faint tonight. Kids were stamping on the table with their cutlery; groups of friends were bursting in laughter; and a couple was arguing over the choice of the film they'll watch tonight."

    "A colleague bumped into her and profusely apologized. Fortunately, he managed to not drop anything."
    
    show lise turtleblacksmile at left

    e "It's ok. I wasn't looking."

    "The table 8 is waiting for order, I'm taking my break, he said before rushing off to the kitchen."

    "Focus, Elise."
    "She trotted her way to the table and took our her tablet."

    e "Hi, may I take your orders?"
    
    "Elise asked with the biggest smile she could muster."

    "She wrote down their orders and asked them if they wanted anything else to which they said no."
    "She retrieved the menu cards, and lifted her head up from the glowing screen, before squinting."

    show arthur gsmile at right

    "Arthur grinned with his teeth fully showing. He had combed his mid-long dark hair and was wearing a red tie with a white shirt, looking handsome and neat. In front of him, a man in his thirties in a black suit she didn't know was frowning, and asked if the terms of the contract were that bad."
    "Arthur said this wasn't that, before talking to her."

    a "I didn't know you worked there. How's your shift going?"
    
    "Elise thought of the texts they had just exchanged and blushed. She had been way too conspicuous."
    
    e "It's going well. Lots of people today."
    a "I see." 

    "His eyes went around the tables."

    a "I think the table next to the entrance is looking for your quality services."
    e "I'll be going then."
    a "See you in a second."
    e "See you."

    hide arthur

    "She said, shrieking inside."
    "'I didn't know you could be interested in anything other than your job,' she heard as she speedwalked away."
    "While taking the orders and serving others, she couldn't help but throw occasional glances at his table."

    "Arthur waved at her."

    default choice_4 = False

    menu:

       

        "Act like you didn't see it.":

            "Elise went to the next customer while sighing. She was such a coward sometimes."

        "Wave back.":
            python:
                choice_4 = True
            jump suite4_2_1

    label suite4_2_1:

        if choice_4 == True:
            "Elise waved back."

            python:
                affinity_with_arthur += 1 

            "He gave him a big smile."
        


    "When their order was ready, she hurried to their table. She put the two pizzas down, and Arthur chuckled."

    show arthur gsmile at right

    e "Something's wrong?"
    a "No, it's just nice to see you."

    "How could he say that with a straight face?"
    "His friend rolled his eyes."
    
    e "Well, enjoy your meal."
    a "Thanks Elise."

    "She escaped red, but alive."

    hide arthur

    "Eventually, they finished eating and looked for her eyes to pay the bill. But Elise was busy at another table, so another waiter came over. She pressed her lips together in regret."
    "When her night ended, the cook told her a duo ordered dessert for her before leaving. It was a dark chocolate tiramisu."
    "Elise held it like a treasure. She ate a spoonful of it and winced."

    "“Ah, I forgot that you didn't like coffee,” the cook said. “I should have made you another dessert.”"

    e "It's fine."
    "A bright smile hung on her lips."
    e "I like this one."

    scene black with dissolve
    scene bg bedroom with fade

    "Teasing Elise was one of Jeanne's favorite things to do, but now that her friend's feelings deepened, she didn't feel like doing it anymore. Jeanne simply watched as Elise took baby steps towards Arthur. Elise even refused her help, “It'd feel too forceful and fake”."
    "So Jeanne carried on her leisurely daily life."


    # "One day, she heard a feminine voice she didn't recognize in the kitchen. She had two alternatives. Investigate or stay holed up in her room. By now, you'd have guessed what she chose. She put on her headphones and resumed her anime."
    # "But then, someone knocked on her door. She ignored it, and she shouldn't have. Arthur slammed the door open and threw her pillow right on her face."

    # show arthur smile with moveinright

    # a "Grenade!"

    # "He shouted before running away."

    # hide arthur with moveoutright

    # j "Fuck you!"

    # "Jeanne leapt out of her bed with the pillow in hand."
    # "She went out of her comfortable room. Her mind was awake and ready. One last step and she'd have vision on the enemy territory."
    # "To surprise the enemy and to avoid any bullet coming her way, she rolled over and lifted her head up, prepared to fire at any threat, only to see a beautiful brunette with a cup of coffee in her hand. It was Carolina."

    # a "She skipped a year, so her mental age has a bit to catch up."

    # "Arthur said, his eyes devoid of any emotion, while the woman at his side was laughing out loud."

    # j "Like you."

    # "It was the woman Elise had told her about. Jeanne was sure of it. The brunette wiped her tears of laughter away and invited Jeanne to sit."

    # c "I've brought a chocolate cake from my parents' bakery. It's a rare opportunity. They often sell out. Your plate's the one who has been untouched."

    # "Jeanne put down the pillow and seated herself, before thanking her for the cake in the most natural way possible by bowing her head."

    # "She took a spoon from her plate."

    # j "Not bad. It's definitely one of the best Black Forest cakes I've eaten. So how do you do, Carolina?"
    # c "Same as usual. Business and management."

    # "Jeanne nodded seriously, pretending to be interested."

    # j "So, how do you like it so far?"
    # e "I'd rather have a coffee and a piece of cake at home."
    # j "Home?"
    # e "I've got my own place now. I was lucky and found one affordable flat in the southern suburbs. Living with other people is nice and all, but that's work in itself."
    # j "I totally feel you."
    # a "You've got the wrong idea, Jeanne. You don't like interacting with people, because you're lazy whereas she doesn't like interacting with people, because she feels superior to them and it'd be a waste of her time and energy."
    # c "Why do you have to word it like that?"
    # j "Yeah, why are you saying it in such a pejorative manner?"
    # a "Why are you banding together against me?"

    # "Carolina turned to Jeanne."
    
    # c "Your brother told me that you've chosen the Bachelor of Physics. Do you know which master program you'll apply to?"

    # "Jeanne filtered her inner monologue which went like this: first of all, this is not something you ask bachelor students when they just started."
    # "Not only you'll cause them a great amount of stress, but also you'll put them in a situation where they have to think about their future and nobody wants to do that." 
    # "Secondly, since I arrived in London four months ago, I've been attempting my best to adjust my life to this new city and country. Then, I got my part-time job." "Thirdly, I only applied for a Bachelor of Physics in the UK, because I was good in Physics and, to be honest, because I wanted to get away from my parents' expectations and French preparatory classes." 
    # "So, I'm not even set on studying for a master's degree, but I guess I'll still do it to get a 'proper diploma' and a proper 'job' in the eyes of my parents."

    # j "I haven't really pondered on it."
    # a "Don't stress about it. You still lots of time."
    # c "There's the option to take a gap year too."
    # a "We can take a look at the master's degrees given by the university. It's not like we had anything else to do."

    # "Arthur looked at Carolina."

    # a "We got nothing, right?"
    # c "Don't stare at me like that. You're the one who's always busy. And, I mean, it'd be interesting to see what kind of master our university offers."
    # j "Are you sure? I thought you had a bunch of things to do, Arthur."
    # a "And it's going to get worse. So, today's the best day. I can spare an hour or two for you."

    # "The random snack time transformed into an orientation session. Overwhelmed by the kindness and the amount of information, Jeanne felt more lost than ever, but she had faith that it'd work out eventually. Until then, she crawled to her bed as Arthur drove Carolina home."

    # #chapter 5
    # #transition to Chapter 5
    # scene black with dissolve
    # #Chapter 5
    # show text "Chapter 5" with Pause(1.5)
    # scene black with dissolve

    # scene bg school with fade

    # "Dogs weren't allowed in the main library which was a pity, because Jeanne reckoned that it would lift people's spirits up and thus improve their grades, increase their motivation, and overall their university's ranking." 
    # "They had booked a study room a month in advance to avoid having to fight for the library seats. Exam period was that dreadful." 
    # "The seats were nice and comfy. The tables were clean and well-lit. Come to think of it, there really were people whose jobs were to design chairs and tables. In order to pay them respect, she should take a picture of them, right?"

    # show lise smile at left
    # e "Quit procrastinating. Your reports aren't going to write themselves."
    # show jeanne casual smile at right
    # j "It's already been two days in a row. Let's take a break, please."

    # "Elise shut her laptop."

    # e "I could do with a cup of tea. I'm almost finished."
    # j "Are you kidding me?"
    # e "Regular and punctual studying does wonders."
    # j "Gimme that superpower."

    # "They took their laptops with them in precaution and closed the door tightly."
    # "The cafeteria was full of students cramming for their exams so they found a random staircase next to a skatepark outside."

    # "Grey. That was the taste of the coffee Jeanne felt on her tongue as she looked at the moody skies and the concrete walls surrounding her in silence. But, the taste changed as soon as she saw Elise texting. A newfound sweetness circled around her palette. She held back from teasing her friend, but she couldn't hold back her curiosity."
    
    # j "How's it going?"
    # e "It's going well."

    # "The last word of her sentence sounded a bit hesitant."

    # j "You've made more progress in two months than the whole last semester. If he answers your texts, that's already a good sign. He's been so busy lately."

    # "Elise finished her last sip of tea."
    
    # e "I've got to finish my group work too."
    # j "Doing everything by yourself?"
    # e "Like usual."
    # j "You should learn to rely on others."
    # e "Cannot do. Let's go."

    # "Elise sighed."

    # j "Five more minutes, please. My brain's going to dry out. I'm sure you have more stuff to share. We're also studying this afternoon. We've got plenty of time."
    # e "The faster I'm done with the assignments, the faster I'll be able to finish revising the contents of the written exams and relax."
    # j "“Apart from you, I don't know anybody who can relax during the exams period."

    # "Jeanne paused to think a second."

    # j "Ah! How about your choice for masters? Do you have an idea of what you want to apply for?"

    # "Elise said yes with her head like it was obvious."

    # e "Why are you asking me this question? We didn't even finish our first year of Bachelors."
    # j "I'm thinking of going on a gap year."
    # e "To do what?"
    # j "To think about what I want to do."
    # e "Well, think while studying."
    # "Jeanne's shoulders dropped at the idea of spending the rest of her day at the library while Elise looked more motivated than ever."
    # "Honors students were really a species on their own."

    # j "You always seem to have everything figured out."
    # e "I try my best to."
    # j "Your brightness is blinding me."
    # e "I'm sure you'd find your way if you put more efort into it."
    # j "I don't know about that. At least, when you fail without trying much, you can blame it on your lack of preparation."
    # e "Isn't it a waste to not see your full potential?"
    # j "People will expect more from you and you will expect more from yourself. An endless circle. Expectations are heavy."
    # e "And life is light."
    # j "Yeah. Do I say it that often?"

    # "Elise tied her hair into a bun, switching it to study mode."

    # e "You're just missing a trigger. A trigger to make that first step."

    #transition

    scene black with dissolve 
    
    scene bg bedroom with fade

    show jeanne casual smile at center
    "Spring rolled up with a new shine. Jeanne's smile couldn't get wider. It had been three weeks since she had completed her midterm finals, submitted her reports and performed her presentations."
    "She had been finally relieved from her student duty and was now committing fully to her sofa and bed."

    "However, today, she changed from her pajamas to a random tracksuit. Going out once in a while to somewhere other than the library and treating herself with a delicious meal would do her good." 
    "A look in the mirror was enough to understand how much she needed that outing. Her already white skin had become paler and her muscles had lost their vigor. Even her butt which she was proud of, had flattened from sitting on the chair and laying on the bed all day."
    
    scene bg street
    
    "On the road, she met her brother who was taking his daily walk."
    show jeanne casual smile at left
    show arthur smile at right
    
    a "Don't tell me you're going to meet friends"

    "He said with a shocked face."

    j "Not your business, ciao."

    a "Are you eating dinner at home?"

    "She said no."

    a "I'll give you some money. I should have change on me."

    "She refused."

    j "I've got the money I earned at my part-time job."

    "Her brother's eyes were watering."

    j "What the hell is wrong with you?"

    a "She's growing up so fast. Go ahead, free spirit."

    "She rolled her eyes as an interesting thought struck her."
    
    j "I saw that you bought fresh ingredients for dinner. Invite Elise, I'm sure she'd be happy to join you for a meal. And, she doesn't work tonight. Otherwise, she'd eat some crappy food. Later."

    hide jeanne with moveoutleft

    "He waved her goodbye as she quickened her pace."

    default choice5 = False

    menu:

        "Invite Elise.": 
            python:
                choice5 = True

            if affinity_with_arthur == 2:
                
                jump suite5_1_1 
         
        "Don't invite Elise.":

            "No, it could lead to misunderstandings."

    label suite5_1_1:

        if choice5 == True:
            "Arthur took out his phone and sent a small text."

            scene black with dissolve
            
            #transition
            
            "Elise had decided to properly wash her hair, but it was taking hours. It had gotten much longer. It reached her waist now. She was rinsing it thoroughly after using her new conditioner when her phone rang in the kitchen."
            "After enveloping her hair in a towel, and her body in another, she treaded carefully to not bump into her trash bin or her piles of study books."

            "“Jeanne is eating out. I planned food for two. Do you want to come over for dinner at eight?” Arthur had messaged."

            " It was only three short and clear sentences. Yet, Elise needed a minute to process the information. She jumped on her bed and dove her head in one of the giant cushions, her legs kicking in the air."   
            "Was that a home date? Good thing she didn't have a shift at the restaurant." 
            "What could she wear? Casual would be the sound option."
            "Elise rummaged in her wardrobe." 
            "Pants? Or a classic dress? What color palette would go well with the season? What color did he like? What was the temperature outside? Her two neurons were playing question-table-tennis at this stage." 
            "Time was ticking. She looked at the mess of knocked-down clothes, and sighed at the idea of folding them later. She put on random black matching underwear, a beige blouse long sleeve, a white shirt, and electric blue jeans. Blue always matched her eyes."
            "She dried off her hair and bolted off to the bus station and caught the bus in extremis."
            "Wiping the sweat off her forehead, a wide grin was placated on her face. She was so thrilled and stressed out at the same time that she couldn't stop her finger from nervously tapping on her leg."
            "Arthur appeared at the door in an red apron over a black shirt, black joggings."
            scene bg condo with fade

            
            show arthur smile at right
            show lise smile at left

            a "Do you drink?" 
            e "Sure."

            "He opened a bottle of wine and poured themselves two glasses."
            "Then, Elise realized she came empty-handed."

            e "Sorry. I forgot to bring something."
            a "No big deal."
            e "Next time, I'll bring over some drinks at least."
            a "Sure. As long it's nothing fancy. I'd feel bad otherwise."

            "He made her sit while he continued cooking. Humming an unfamiliar tune, his soft voice flowed around the kitchen."
            "No need to overthink it."
            "She took a deep breath and reset her mind."
            "The scent of freshly cut tomatoes, the dim lighting and the sound of his voice gently lulled her into peace. Her nervous finger lay down as her eyes followed his back."
            "Obviously, it wasn't a home date. Still, she could enjoy this moment, right?"

            a "Sorry, I was in my thoughts."

            "He laid two bowls on the table for the salad."

            a "The lasagnas will be ready in a few minutes. I'm not used to people arriving on time."

            "He took a sip of wine."

            a "How were your exams?"
            e "Nothing big. Hard work pays off."
            a "That's more than big."

            "Elise tented her fingers."

            default choice_6 = False

            menu:

                "Nod and stay silent": 

                    jump suite5_2_1 
                        

                "Ask Arthur about his life": 
                    python:
                        choice_6 = True
                    jump suite5_2_2

            label suite5_2_1:

                "They both looked at the red digits of the oven's timer and smiled."

            
            label suite5_2_2:
                if choice_6 == True:
                    python:
                        affinity_with_arthur += 1

                    e "And you?"
                    a "Can't say I didn't work hard, but would it be correct to say that it was hard work?"
                    e "I'm sure it was."
                    a "I didn't know you worked at the restaurant too."
                    e "I do some shifts here and there. Nothing too big. I started a while ago. Summer before starting college."
                    a "To make pocket money?"
                    e "Could say that. It's not as good as funding a successful startup, I have to say."
                    
                    "Arthur's left brow rose."

                    a "Waiting tables is harder."
                    e "Why do you say so?"
                    a "Because it is physically and mentally demanding. Difficult customers. Running around the whole night. The noise, the smell and the lights. Whereas, building a company with friends around a subject you enjoy is a different matter altogether."
                    e "It's tiring some days for sure."

                    "The corner of her eyes curved."

                    e "It is also rewarding some other days. Birthdays, for example. I love seeing families smile together around a great meal and a beautiful cake."
                    a "I see."

            "On cue, the oven and his mobile rang."
            "He served the steaming lasagnas winced."

            a "Sorry. Urgent call. Sorry, really. I hate people who're on their phones during meetings and dinners too."

            "He went into his room, leaving Elise with only her glass and her thoughts."
            "By the time he came back, the lasagnas had gone warm and her glass had gone empty."

            a "Sorry again."
            a "It was faster than I expected."
            e "The call?"
            a "The job interview results."

            "She stood up so fast, the room stood with her."

            e "What? Are you going to join a charity association?"
            a "Charity? I did mention that. But no, I'm going to Paris, to give a hand to a friend, Tom, the one you met at the restaurant."
            a "He's a bit older and has his own company which is currently expanding. He urgently needs new, trustworthy and competent collaborators. Of course, the job in itself is interesting and the offer too, but it means that I'll have to step down from my CEO position at my company."

            "She felt her composure break as she sat back down."

            #show elise sad

            menu:

                "Don't ask anything.": 

                    jump suite5_3_2

                "Ask him what he will be going.": 
                    
                    python:
                        affinity_with_arthur += 1
                    jump suite5_3_1 
                        

                

            label suite5_3_1:

                e "When are you going?"
                a "A week after my master's thesis presentations. In a month or so. Well, I don't think I'll miss London."

                "A piece of her heart fell off on her plate."

                a "Don't make that face."
            
            label suite5_3_2:
                
                "She bit her lip in silence."

            "Contradicting thoughts filled her head. She sat back down and nibbled at the lasagna. It was sadly well-made."

            e "Are you set on it?"
            a "I will need to discuss with my board next month, but yes, I guess. One of my colleagues will join too. She was getting tired of London, she was like 'Where are you going like that? Trying to get out of London first, uh?'"

            "Arthur chuckled."

            a "She's quite the competitive one."

            "Arthur gave her a glance."

            a "Hey, are you okay?" 
            e "Yes."

            "The news of him going to work abroad had shaken her."

            e "The lasagna was delicious."

            "Though the last spoons tasted bitter."

            a "A pleasure. Do you want dessert? I've baked a lemon cake."
            e "No, that's fine. I'll go home. It's late."

            "She bit her lips. Her tone came off a little rude."

            e "I think the exams tired me out."

            "She went to get her coat by reflex, but forgot that she didn't bring one."

            a "I'll drive you home. It should be quite chilly outside."

            "She avoided his eyes in a desperate attempt to contain her sudden surge of emotions."

            e "It's fine. It's fine."

            "Elise couldn't tell him it was about him leaving London. Although they had become much closer, she wasn't anybody to him. Even if she was, she would never want him to base his career choices on her personal feelings. It would be too selfish and unfair. Wouldn't it?"
            "His phone rang again."
            
            a "I'm sorry."

            e "I..."

            menu:

                "It's just that... I would have loved to spend more time with you.": 
                    
                    jump declaration
                        

                "Nothing.": 

                    jump silent


            label declaration:
                
                a "Me too."
                
                "He slightly smiled."

                a "Paris is not that far. I'll come around once in a while to visit anyways."

                python:
                    affinity_with_arthur += 1

                jump silent

            label silent: 

                "Elise stayed silent."

                a "I've gotta go. Sorry."

            "She opened the door."

            e "Don't apologize. It's fine. Work is work. I know what it is. I was going to go regardless."

            "Elise tried to smile, but her lips didn't move. She knew that if she didn't go now, she would regret it, they would regret it."

            "'Perhaps, I'm the one who's missing that trigger.'"

            if affinity_with_arthur < 4:

                jump suite5_1_2
    
    
            


    label suite5_1_2:
        if affinity_with_arthur < 4:

            scene black with dissolve
            #Chapter 5
            show text "End A : Angst" with Pause(8)
            return
        

    
        
    scene black with dissolve
    scene bg bedroom

    show jeanne casual smile at center
    "When Jeanne came back home the morning after sleeping at a friend’s place, she had a stifling feeling that something happened while she wasn’t here."
    "She inspected the flat, but noticed nothing suspiscious. No additional pairs of shoes or clothes. Clean as usual and quiet. Arthur was certainly sleeping."
    "She had said it as a joke, but Arthur could be very oblivious. Fortunately, it seemed that her brother had been reasonable and not dumb enough to really invite Elise over for a one-on-one dinner."
    "Her chair squeaked as she slumped on it. She put her arms on her desk and rested her chin on her hands as she played a video of her favorite idol."
    "These dark and deep eyes. Unshakeable. A diamond-pressured focus. This overwhelming passion."
    "This feeling, she wanted to feel the same."
    "If only she had more time to think about her life, to not waste another year in a Bachelor that didn’t spark anything in her. More time. That was it."
    "“It’s decided. I’m going to take a sabbatical year.”"
    "That was her first step."  

    scene black with dissolve
    #Chapter 5
    show text "Part 2" with Pause(8)
    



return
