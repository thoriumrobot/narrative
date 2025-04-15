import random
from langchain_ollama import OllamaLLM

# 1. Placeholder lists for Alice (Wound) and Botanical (Medicine) readings
# Fill these with your actual 90 Wound readings and 66 Medicine readings.
alice_readings = [
    "All in the Golden Afternoon. Time to create. An imaginative idea. Inspiration takes hold. Talent and ability. The muse touches down in your life - get ready!",
    "All in the Golden Afternoon Reversed. Feeling Dull, uninspired, mundane. Believing you lack creativity. Dissatisfaction with your work. Negative self-talk.",
    "I Wonder What Will Happen Next? A longing for excitement. Wonder at what is meant to take place next. Someone who is comfortable but vaguely dissatisfied. Be ready for a challenge and new experiences.",
    "I Wonder What Will Happen Next? Reversed. Attachment to habit. Locked into stultifying sameness. Comfort over adventure. A lack of curiosity. Satisfaction remaining within the same world, in a repetitive cycle.",
    "Follow the White Rabbit. A wondrous opportunity is going to break through your ordinary reality and give you the chance to change your world and your perception, forever.",
    "Follow the White Rabbit Reversed. Opportunity after opportunity, chance after chance to have adventures, but not feeling ready. Thinking you must think on it, take more timeor even that the opportunity will come by again. Hesitation is costing you a more exciting, dynamic and enchanted life.",
    "Becoming Braver. You have been tested. The development of strength and resilience through the courageous meeting of challenges. The demonstration of great character. The acknowledgement of how much you have learned. The ability to cope with so many little things, due to a great ordeal endured with grace, dignity and humor. Testing times show true character.",
    "Becoming Braver Reversed. Feeling there is no point to your trials. An inability to see you are courageous and learning all the time. Doubting you have the endurance to cope with the challenges being faced. Believing you are weak and unable to tackle the smallest of adversities. Feeling you will fall apart when troubled times come. Afraid of adventure, daunted by tests.",
    "Choices. Choosing which way to go. A moment of decision. Uncertain of what is best or what to do next. Feeling like each door is closed. Wanting to reach the next stage of life but not seeing a single way through.",
    "Choices Reversed. Giving up too soon. Feeling daunted by challenges or stuck in an in-between place. An unwillingness to alter habits in order to transform. Reluctance to move forward. A lack of curiosity.",
    "Investigate. An important decision requires you to enquire, inform yourself and think through it thoroughly. Find out as much as you can and look at the fine print!",
    "Investigate Reversed. Rushing ahead without checking. Being reckless and even arrogantly thinking you know best. Refusing to learn from experience. Being overly trusting that this time it will be okay. Doing what you are told, without using your own wits and intelligence.",
    "Do Not Drink Poison. Avoid toxic situations, people or relationships. Do not partake in what you know is not best for you. Ending harmful relationships, changingtoxic habits or improving your nutrition and health regime. A clean out from your home and pantry of substances, foods, even fabrics that can poison your personal environment. Changing unhealthy harmful thoughts and beliefs about yourself and refusing to speak ill of others. Choosing to encourage support and lead through kindness and strength.",
    "Do Not Drink Poison Reversed. Suffering unnecessarily. Holding on to relationships that hurt you. Lacking the energy to change habits which harm you. A denial that poisonous things can hurt you. Denial about certain substances. Potential for addiction to food or substances. Obsessive and harmful behaviors which need to be changed, but which you may refuse to recognise.",
    "Curiouser and Curiouser. New and unfamiliar places and surroundings. A general lack of familiarity. A fascinating turn of events. Growth amidst strange customs and people. Changing as a person. New interests and talents are being discovered.",
    "Curiouser and Curiouser Reversed. A lack of interest in finding out about different places, cultures or people. A desire to stick to the familiar. Believing you have grown enough and need not extend yourself any further. Becoming static, habitual and apathetic.",
    "Follow Your Own Good Advice. Harsh self-judgement for a mistake or an error made. Unmet personal expectation causing inconsolable sadness. A reminder to detach, find clarity and follow your personal internal guidance system which has some very practical solutions!",
    "Follow Your Own Good Advice Reversed. A refusal to listen to yourself Making the same mistake over and over. Feeling that if you become emotional others will step in to rescue you. Thinking that all is doom and gloom. Becoming bogged down emotionally, unable to think clearly.",
    "Changed in the Night. Sudden, unexpected change. A shock. Unexpected news. Adjusting to a new situation. Finding out more about who you are. Inexperience and uncertainty. An identity crisis due to changed circumstances.",
    "Changed in the Night Reversed. Feeling you are not growing as a person or that you have stayed the same for a very long time. You may be looking at introducing some new and exciting challenges into your life to help you grow and discover more about all the wonderful selves you have within you.",
    "Lead the Way. It is time to step into a leadership role. Others are looking to you to solve a problem or show them how to work through an emotional situation. Help others by showing them what needs to be done, not by telling them what to do. Calm your emotions, ground and centre yourself so you can be of greater service to others. You cannot help others overcome emotional distress until you have learned how to calm your own feelings. Be steadfast, strong, and encourage others by your own calm example.",
    "Lead the Way Reversed. Refusing to take charge. Letting your emotions overwhelm you. Wanting to tell others what to do, but being afraid to, in case you get it wrong. Feeling you are too emotional to take charge. Avoiding responsibility. Fear of failing others and of letting yourself down. Discouraging others from relying on you.",
    "All Must Have Prizes. Trying to keep everyone happy. Treating everyone as equals and rewarding those who have not worked hard. Playing nice, wanting to please. An inability to choose who or what is best for you. Trying to be fair, but avoiding difficult decisions is not fair on yourself Maintaining illusions, to avoid disappointing others.",
    "All Must Have Prizes Reversed. Clearly knowing what is best for you. Refusing to praise or to give energy away where it is not warranted. Easily choosing between what is better for you and what would not serve you. Being more concerned with honesty and truth than with keeping everyone happy.",
    "Clock Time. A time of stress and added workload. Increased responsibility, feeling it is too late to pursue your dreams. Feeling pushed to complete too many tasks. An inability to say no. Insufficient support. The urge to rush. This could be a time of dynamic opportunity - but you must take charge of your own workload and do what must be done. It is time for one last push!",
    "Clock Time Reversed. Refusing to meet a deadline. Procrastination and avoidance. Feeling overwhelmed with responsibility. Giving up on dreams. Making no progress. Being too slow. Staying still when movement is needed.",
    "Messages for a Rabbit. Animal communication. A proximity to animals. Enjoying the company of animals. An interest in animal behaviour and symbology. Feeling drawn to animals more so than humans. Intuitively understanding their needs. Rewards of friendship, closeness and trust.",
    "Messages for a Rabbit Reversed. Feeling bewildered by animals. Making assumptions about animal behaviours. Feeling you know about them, but missing the messages they are sending you. Missing a beloved pet or the closeness you once had. Feeling more drawn to people. Being sentimental about animals, rather than truly understanding their actual needs and desires.",
    "A Moment's Regret. Second-guessing your decisions. Berating yourself for the choices you have made. Feeling regretful and missing what was. Nostalgia 一 living in the past. A focus on what is going wrong or what could still go wrong?",
    "A Moment's Regret Reversed.  Forging ahead without reflection. An inability to marry the past, the present, and the future. No thinking back. A lack of attachment to what once was. The refusal to remember. Seeing nostalgia as sentimental and foolish. A focus on the future and lack of appreciation for what was good about the past.",
    "Growing Up. Understanding that the years bring their lessons to you. Embrace becoming an elder. Watching time make its marks upon you and embracing the signs of ageing. Understanding the wisdom that can come with age. Being young at heart, yet yearning for encounters that will help you evolve, grow and experience the fullness of life.",
    "Growing Up Reversed. Hanging on to youth at all costs. Denying the existence of change as we grow older. Being stuck in a habit of our youth. Wishing to be young again. Feeling you have learned very little, although you are growing older. Seeing maturation only as a process of deterioration. Concern about your fate as you grow older.",
    "No Need to Fear. You may be afraid out of habit, not out of reason. Feeling intimidated, but without need. Remember how many reasons you have to feel confident! Go forward with courage! You are more powerful than you are feeling. Others cannot harm you, as you are so strong.",
    "No Need to Fear Reversed. Timidity despite all that is available to you. A refusal to behave in an empowered way. Being craven, fearful or giving way to others because you believe them to be more powerful than you. Allowing others to treat you poorly because you believe they are better than you. Unwarranted lack of confidence.",
    "Who in the World Are You? A fascination with getting to know yourself again. Growing into a new self Defying assumptions about who you are. Exploration of the self questioning who you have been told you are. Changing at a very deep level. The readiness to evolve and experiment to come to greater self-knowledge.",
    "Who in the World Are You? Reversed. Believing you know just who you are. Certain of identity. Refusing to question yourself Believing you are fixed and unchanging. Going along with the main current of who you are supposed to be. Feeling comfortable with who you believe yourself to be, but ultimately limiting your potential because of this.",
    "Keep Your Temper. Being pushed. Running out of patience. Feeling like the people about you are not cooperative. Evasive companions and bothersome circumstances. The need to keep your temper cool and in check. Remind yourself you will go far further when you harness your power, and use it at the right time 一 which is, by the way, not right now!",
    "Keep Your Temper Reversed. Unleashing. Saying whatever you wish. Lashing out. Expressing anger and frustration. Heated conversations. An unwillingness to remain calm. Believing aggression will create a breakthrough. Feeling entitled to express emotions without a thought for consequences.",
    "The Right Way. Wanting to get through to the other side of a situation. A desire to walk through a gateway or a life transition, to become an 'insider' rather than remaining on the periphery. Wanting to have an impact, to be included, to be a part of the activities and have an influence on the world. A willingness to learn, step by step.",
    "The Right Way Reversed. Leaving it all up to fate. Waiting, rather than acting. Philosophising, rather than doing. Being dreamy, rather than practical.",
    "Set Your Course. Know where you wish to go in this life. Set goals, write a wish list of accomplishments. Realising that to bring your dreams into reality, you need to know what it is you want to do, be, or create. The refusal to be flotsam any longer. Strike out in the best direction for you.",
    "Set Your Course Reversed. Unable to set a course, drifting. Saying you are going with the flow, but allowing others to send you this way and that. Asking for guidance without knowing where it is you wish to go. Refusing to plan or prepare, and then feeling confused as to why you seem to be stuck or thrown this way and that.",
    "We're All Mad Here. Beginning to realise that everyone is interesting, a little bit different and full of secrets, good and bad. Understanding that hiding what makes you your very own self is not only exhausting, but it is robbing the world of your unique wonder. Discovering that you are a little mad - and so, in truth, is everyone else. Embrace your eccentricities and your own peculiar genius.",
    "We're All Mad Here Reversed. Telling yourself you are normal, over and over, won't make you so. You may be grounded, wholesome, earthy, realistic, pragmatic, but you are still a little mad! There is no need to deny it so strongly 一 or to point out the madness of everyone else. Come to know your own brand of madness and youll be so much more at peace and able to enjoy the amazing life you have been blessed enough to experience.",
    "Use Your Time Well. Someone could be wasting your time by asking questions they have no interest in answering. People not listening or repeatedly asking for assistance, but not heeding advice. Someone wishes to take up a great deal of your time in order to feel more important, listened to, and cared about. Set your boundaries.",
    "Use Your Time Well Reversed. Being available to one and all. Exhausting yourself by answering questions that are not asked with the right intentions. Squandering your precious time. Lack of appreciation for your time. Being prepared to martyr yourself to help others. Feeling helpless, like the victim of time. Spending time on unsolvable problems. Having little impact due to your time being wasted. Feeling pointlessly harassed.",
    "Wake Up. A rude awakening. Being asked to deliver before you feel you are ready. Being present and fully engaged with what is happening around you. Making a contribution. Being assertive, despite your gentle nature. Insisting on being able to tell your story. Making your moment count. Sharing with others who are ready to listen.",
    "Wake Up Reversed. Missing your moment. Holding yourself back. Sleeping through opportunities. Not seeing the chances about you. Hiding from your destiny. Pulling back at the last moment. Taking refuge in a dream world rather than stepping forward and seeing what you can create in the real world. Believing that no-one would listen to you anyway. Staying quiet to avoid disappointment.",
    "It's Always Teatime. A change in schedules, repetition, cycles, patterns and loops. Situations being repeated, being trapped by schedules that need to be changed. A wonderful time to challenge the order in which things are done. Reworking traditions so they are more aligned with the way you see the world.",
    "It's Always Teatime Reversed. Wanting to keep to routine and to the schedule. An inability to be spontaneous and break free of what has been decided.",
    "Painting the Roses Red. Working for or being in a relationship with someone who is harsh on those who make mistakes. Feeling forced to cover up errors to avoid punishment. Fear of mistakes being discovered. Hiding the evidence as the consequences are much harsher than the mistake. Feeling that what you need to do to stay safe is no longer reasonable.",
    "Painting the Roses Red Reversed. Refusing to hide mistakes or errors. Taking on a punishment that is too harsh. Refusing to change something that is perfect just as it is. Encouraging others to stand together. No longer fearing an oppressive societal expectation or a tyrannical person.",
    "Nonsense! Courageously standing up for yourself when someone is behaving in a way that is silly and unfair. Refusing to be cowed. Pointing out a persons bad behaviour. Not backing down on the truth. Looking someone in the eye, being very brave, strong and no longer intimidated. Surprising yourself with your power.",
    "Nonsense! Reversed. Backing down at the moment of truth. Running from a confrontation. Allowing someone to intimidate you. An inability to find the courage within. Fear of punishment. Loss of voice. Believing you cannot be brave without being aggressive.",
    "Find the Lesson. Upheaval. Quarrelsome people. Disputes, anta­gonism and confusion. Uncertainty about the purpose of a situation. Feeling frustrated and ready to complain. Let it go to the Universe, ask the Universe for clarity and trust that time will bring an understanding of the lessons this uncomfortable adventure is teaching you.",
    "Find the Lesson Reversed. The reversal of this card amplifies the confusion you may be feeling. A challenging time that feels very unfair. There is a reason - it may be too hard to even begin to contemplate that there could be a higher purpose to this situation right now. Give yourself a little bit of space and be patient with yourself Dont struggle to find the reason. Just find a way to make it through what is happening.",
    "Law is not Justice. Someone may have the authority to impose the law, but the law, or the rule is ready to be questioned. Following the law, even though it is unjust. Condemnation without knowing the full story. Being judged by people who do not know you or have a biased view. You may be judging people you do not understand. Be sure to have a fuller picture, and avoid condemnation and judgement. Be discerning but be sure to be fair and just.",
    "Law is not Justice Reversed. Believing the law is right, under any circumstances. Accepting the judgement of a powerful person without question. Allowing yourself to be influenced without knowing the story. A deep bias, which is colouring your vision. A flawed filter through which you, or another, may be seeing the world. Take the time to think independently.",
    "Believe. Meeting people who are very unlike people you have met before. Mystic events and peculiar experiences. Interacting with different cultures, customs and belief systems. Mystical encounters with elemental beings who interact with you 一 finding they are just as real as you! Discovering new places, environments, even climates that are different to any you have experienced before. Something unusual, that is most decidedly as real as you are.",
    "Believe Reversed. Refusing to accept differences. Feeling that your spiritual encounters or mystical visions are unreal, untrue or fantasy. Disliking being in unfamiliar places or spaces. Finding people too different for you to really connect or engage with. A refusal or difficulty believing in the existence of elemental beings.",
    "Belong to Your Own Dream. Finding you have been following a plan and a path that is not truly your own. Deciding to take steps to live in a way that is authentic and truly your own. Rebelling. Wishing to live in your own world. No longer making decisions, staying with people or in jobs that are not part of your dream. Not being directed or governed by the desires and dreams of others. Deciding to make some big changes toward following the path that is your souls true dream for its evolution this lifetime.",
    "Belong to Your Own Dream Reversed. Content going along with what others feel is right for you. Not thinking through what is best for you. Not getting in touch with your own soul nor going with your dreams. Coasting along and fitting into roles for the sake of ease. Going with the flow, but at the expense of what would be more nourishing and magickal for you. Denying your soul calling.",
    "I Want to Be a Queen. Raising your status. You are taking charge of your life, making decisions for yourself and setting rules and boundaries that work for you. Declaring your independence. Becoming powerful and influential. Wanting to embrace your potential.",
    "I Want to Be a Queen Reversed. Fear of your power. A preference for being told what to do rather than deciding what is best for you. Acquiescing to another s will. Seeing power as a corrupting influence. Shrinking away from potential. Fear of failure. Over-compromising.",
    "Impossible Things. A struggle to accept what seems unlikely. Devote regular time to improving a situation. Becoming better at something you care about or changing something for the better. Meditate on a miracle and believe in impossible things!",
    "Impossible Things Reversed. Stubbornly refusing to believe that any kind of action can change things for the better. Denying that action brings results. Feeling that something is too far out of your reach or that miracles are for other people.",
    "Never Jam Today. Words are plentiful, but deeds are few. Thinking that the past and the future are better than the present. Being attracted by promises of good times and abundance that may never be kept. Boasting of plenty, but never enjoying it in the moment. Manipulation and withholding. Demand results in the present and work toward satisfying your desires yourself Dont buy what they are selling!",
    "Never Jam Today Reversed. Being easily manipulated because you believe what people say, rather than what they do. Living off promises and hopes. Wondering if someone will ever deliver the payoff they have promised you. Fantasising about tomorrow, dreaming of yesterday.",
    "Shine Bright Like a Candle. Your divine light is strong. You are radiant. Endurance, resilience, making it through a trying time. Hopeful future. Wondering about life and death. Contemplating the purpose of your existence. Connections with the afterlife.",
    "Shine Bright Like a Candle Reversed. No interest in life beyond the immediate and material. Questioning whether there is existence beyond this lifetime. The refusal to wonder about the next stages of your life or what will happen next. Sureness that nothing at all will change.",
    "Nature Communication. You are being asked not to make assumptions. Be open to possibilities that seem to be outside rational expectation. Attempts to communicate with beings from other realms - within nature, spiritual planes or even just humans it is thought there is no chance of speaking to or being understood by. Be open and express the desire for communication. Be more lateral and less literal about the ways communication can take place. Be a being worth communicating with - this will go far!",
    "Nature Communication Reversed. Stubbornness. Refusing to approach language from a different perspective. Assuming signs and communication must fit in with your own. Assuming things about other beings, without really tuning in. Refusing to expand your capacity for understanding.",
    "You Are Rare and Free. A struggle to find places where people accept you or where you feel you fit in. You must learn to embrace all that makes you different and become the very best you that you can possibly be. You will never be defined, so refuse to comply. Explore the frontiers of the human spirit and know how precious and rare you are.",
    "You Are Rare and Free Reversed. Conforming may seem like the answer, as may disguising all that makes you different. Vbu may be attempting to be like others and allowing yourself to be told who you ought to be. Consider being your own best friend and celebrating your differences!",
    "Uncertainty. Good advice from an unexpected quarter. If you try, practice and are willing to make mistakes along the way, you will become far more powerful, and reach the place you are longing to be.",
    "Uncertainty Reversed.  Fear of following advice and learning through experience. Wishing things were easier or more predictable. The belief that becoming who you wish to be ought to be simpler. Wanting another to do the hard work or solve your problems for you. Wanting support, but being unwilling to apply discipline or too scared to make the mistakes from which you will learn.",
    "Keeping Up. A time of very hard work. Getting ahead. Determination and resolve to push through into the next stage. Hie urge to improve your status and be rewarded. Moving quickly, with strength and stamina. A great deal to process and integrate.",
    "Keeping Up Reversed. Sluggish approaches will not be rewarded. Feeling it is impossible to change the way things are. Feeling entrapped by the effort required to change your current circumstances.",
    "Forget Who You Are. You are discovering what can happen when you rely less on conditioning, memory and civilisation, and more on heart, receptivity and nature. New friendships, connections, gentleness and joy will be yours.",
    "Forget Who You Are Reversed. Believing everything you have been told you are. Defining self through labels, cultural programming, rules and laws. Missing out on beautiful, heart-opening opportunities to connect due to conformity and rigid beliefs.",
    "Mortality. Appreciation of existence. Relishing being alive. Making the most of every moment. Accepting mortality in ourselves and in others. Living in the present. Feeling joy at being alive.",
    "Mortality Reversed. The belief that this life has less value than other possible lives. Vesting time, procrastinating or stagnating. Waiting for a 'heaven.' Believing life is more a curse than a blessing... a burden to be carried. Refusing to believe in your own mortality. Denial of deaths presence within life. Living as though life is forever.",
    "Manage to Be Glad. Tour happiness is in your own hands 一 it is something, which can be managed, nurtured and grown. Acknowledgement that life can be very difficult and challenging, but you are being asked to grow the happiness you long for, out of your magickal will and desire to feel joy once again.",
    "Manage to Be Glad Reversed. A belief that happiness is easier for others who seem more fortunate and have been given blessings you have missed out on. Believing that happiness is an act of fate rather than a disciplined way of thinking and behaving. Feeling happiness is out of reach. Focusing on the sadness, rather than the bliss that can be created.",
    "You Can't Go Back to Yesterday. You are more than your past. You have evolved and changed. Sharing your history is only to share who you once were. You are no longer the same person.",
    "You Can't Go Back to Yesterday Reversed. Living in the past. Speaking of past events. Musing over what once was. Nostalgia. Believing you are the same as you once were. Living through stories rather than experiences. Memory overrides the present. No anticipation of the future.",
    "Such a Curious Dream. A time when work must be done. Eat well and prepare good meals. Make magick in your everyday activities and ordinary moments. A return from an extraordinary experience, adventure, travel or holiday. When the time is right, you will encounter Wonderland once again.",
    "Such a Curious Dream Reversed. Venting to hold on to an experience and not return to the everyday. Wishing to live in Wdnderland rather than experiencing it and bringing its magick into your everyday world. Becoming ungrounded and disconnected. Feeling drawn to fantasy. Being susceptible to illusions."
]

botanical_readings = [
    "Angel's Trumpet. What message are you not hearing that is urging you to transform? Look at the devils holding their ears as they cannot stand her holy sound. What devils or attachments do you need to cast out from your life, allowing you to evolve? Look to the graveyard. To what are you dying, and to what are you being reborn? Let go and trust the process as you really have no choice. How can the ancestors help you? Who in your lineage is willing to help you speak your trth or offer a message to you?",
    "Angel's Trumpet Reversed. Resisting the message. We are not ready to let go and need more time. Do not avoid the messages you are receiving about change. Embrace them to prepare yourself for the coming change. Cast out that which no longer serves and embrace your own spiritual beauty.",
    "Belladonna. A gateway opens into a new realm, a new breakthough, though she also acts as guardian of the gateway, asking if you are truly ready to step through to the other side and leave what attachments no longer serve, cutting their cords. Each step towards her, towards the gate, is a deepening of your commitment to your spirit. She holds the sickle in one hand and the forked stang in the other. She is attended by two angels of death, one on each side, holding her foliage over the gateway. The branches of Belladonna are a crooked path, and each flower embodies the enchantment of the stars in the darkness.",
    "Belladonna Reversed. What spell are you under? What has enchanted you or distracted you? What might be toxic to you, but you haven't realized it yet? What messages from the spirit world are right there, but being ignored by you?",
    "Bleeding Heart. Reflect on unhealed wounds. Where do you hold on to grief or pain? What unhealthy attachments bind you? What needs to be released to move on with your life? Notice how that plant spirit turns her back, turning away from the past to let it go. Bleeding Heart tells you to seek catharsis, often through tears, as the drop is also evocative of tears cleansing the heart. Don't be afraid to cry to heal. Each of the heart-shaped flowers needs to crack and split open to bloom, to release the teardrop in order to heal.",
    "Bleeding Heart Reversed. You are stubbornly refusing to release unhealthy attachments and old wounds. You have build identities around your wounded self and fear who or what you will be if you let them go. You are holding back tears and pretending things are good when they are not. Be honest with yourself.",
    "Calla Lily. A balance of desire and spiritual attainment is found. It can indicate a time of personal empowerment, or a relationship going well on all levels, indicating a match physically and spiritually. You might find yourself taking on the qualities of enchantment with a partner, or in turn, being enchanted y another. Things are pleasurable, peaceful and connected.",
    "Calla Lily Reversed. Something is ending, and you are not at peace. You need to learn how to transition to make the necessary change without a lot of drama. Accept what is ending, and grieve, but allow something new to rise. Difficulty or conflict in relationships, where one aspect of the relationship, spiritual or physical, is being nurtured, while the other is not. It is time to seek balance.",
    "Camellia. Appreciate what you have-your home, belongings, health and happiness. Gratitude for what you have and a reminder that gratitude combined with humility is the key to going forward. The flower spirit is enveloped in the luxury of her petals. Enjoy the world and your life. Enjoy your family and friends. Listen to your intuition from a place of beauty and security. Do not fear scarcity.",
    "Camellia Reversed. A need to self-soothe and self-comfort or accept the comfort offered to you. Settle yourself and see things from a clearer perspective. If you are feeling confused or unsafe, calmly evaluate what you can do to get into a better situation and do it.",
    "Cannabis. Be aware. Be sensitive. Connect and commune. Feel connected and play. Now is a time for letting down rigid differences and enjoying the world. Find your bliss in simple everyday things, and be aware of the vast levels of life all around you, seen and unseen, physical and spiritual.",
    "Cannabis Reversed. Feeling lost or adrift and needing some structure to balance an excess of dissolution. Find our own center amidst the streams of life and establish our sense of self without slipping into fear.",
    "Dandelion. A time and place for you to shine and play, and while doing so, be successful at what is at hand. This plant spirit can indicate success and good fortune in business and goals coming to fruition, all with a light-hearted and fun attitude for you. Enjoy your success and keep it going. Where is your eye drawn-root, leaf, flower, seed? The solar attributes are the most flower-like. The root helps you to get to the root of the matter and shows that you need grounding or purification. The leaf is cleansing and nutritive, indicating support. The flying seeds are of dreams and travel.",
    "Dandelion Reversed. You are holding on to anger or poison and need to purge. What is preventing you from moving forward and shining? What toxicity are you holding onto internally, any why? Learn to release it.",
    "Dragon Tree. You are called to draw forth your natural power and take action as necessary. Express your will. Take flight. It is time to be active and make things happen in inner or outer worlds, but you cannot remain idle. While the Dragon Tree can have an aggressive nature, you are not necessarily called to be aggressive, but confident and strong. The Dragon Tree tells you not to be passive, but to take an active role in shaping your life.",
    "Dragon Tree Reversed. Your power is going inward. Is this your desire? If yes, then focus on your inner experience and inner changes. But if you are called to take action in your life, you are challenged to express that power outward to make beneficial changes.",
    "Fly Agaric. An opportunity to make contact with a deeper level of awareness, catalyzing your creativity and healing. You must be willing to risk being perceived as foolish or crazy, and also take time to listen in order to learn. Reconnect with craftiness, speed and fertility, transformation or love and good fortune.",
    "Fly Agaric Reversed. A gateway to the darker unconscious. While it can heal you deeply, it will not be easy. The healing will require you to face fears about yourself and the world, and you will need a willingness to let go of poisons that are familiar, but which will ultimately harm you.",
    "Hellebore. We need time alone, to be unseen and unheard to reflect upon our life and path. The spirit is gazing off in her own direction, unconcerned about us, doing her own work. We might need to set boundaries more aggressively, as other could impede and pressure us to support their needs. When we are alone and unseen, we will bloom.",
    "Hellebore Reversed. Not wanting to be alone or feeling alone in the darkness. Rather than choosing to be alone, the choice was made for us by others or circumstances beyond our control.",
    "Hemlock. By paying attention to dreams or nightmares, you have an opportunity to get unstuck and move through anything that's stopping you. The inner voice and intuitive message create the key for you to bypass anything that keeps you stuck and get going on your evolution without delay. The noxious root stares directly at us, and we cannot avert our gaze. Face the situation head on.",
    "Hemlock Reversed. Stuck in the current situation. You might feel that another had positioned you to be blocked, but we know that on some level, we have to take responsibility for the thoughts, feelings and actions that have gotten us into this paralysis. Seek answers in dreams and meditations, but be prepared to confront realities you would rather deny.",
    "Henbane. You are called to see things differently, looking at the whole arc of the past, present and future in a complete picture. You might find yourself gaining access to reserves of deeper power, inspiration or insight. Aptitudes within you will be awakened.",
    "Henbane Reversed. Blocked inspiration. You are missing a part of the picture and need a fuller scope to see clearly. Ask questions.",
    "Holly. The Holly King looks coldly at you, attired in his winter regalia. You need protection from outside forces. Look for clues on how to approach your protection in a just and balanced manner.",
    "Holly Reversed. You need protection from self-harm. How are you directing angry and aggressive feelings, and how are they hurting you?",
    "Ivy. Reach up and out while rooted. How can you grow without losing your roots? What must you bind to protect you, or bring closer to unite with it? Possible indication of good luck and abundance while others around you are struggling.",
    "Ivy Reversed. Are you feeling uprooted and ungrounded? Is it hard to go on? Find the roots to grow once again. Don't give up. Thrive. Develop the strength and resilience to to go on.",
    "Lavender. Pause, calm and center ourselves for the task before us. Approach it with a clear mind and tranquil heart. We may feel we are working day and night, but use the cycles of work and rest to restore balance in your life.",
    "Lavender Reversed. We may be acting too calm, too peaceful, not seeing things as they are, but as we want them to be. Get clarity to see the situation truly, and then approach the work calmly, but realistically.",
    "Love Lies Bleeding. We are in the process of healing or supporting another in the healing process. We might be experiencing grief, pain or despair, but our isolation or pain is temporary as long as we continue onward in our process.",
    "Love Lies Bleeding Reversed. We are rejecting the help and support offered to move through our suffering. Why are we in love with our suffering? How can we move on to the next situation, putting our suffering into perspective?",
    "Mandrake. Seek mystery in hidden and dark places, embracing who we really are. Ask yourself how you are using your gifts. We have the power to bless, curse and offer protection.",
    "Mandrake Reversed. We might be delirious and using our power irresponsibly.",
    "Moonflower. Develop your creative power by breaking patterns and rhythms and finding your own way. You will attract allies if you follow your own way.",
    "Moonflower Reversed. Make peace with the ephemeral. All life changes, dies and is reborn. Open your heart and take deep breaths to find peace. See the world clearly and enjoy pleasures while we have them. Tomorrow, they might not be there.",
    "Oak. Oak indicates strength, protection or good fortune in the current undertaking. The situation looks good for success, and you will have the support to go forward. Within the branches of the oak is the cardinal, the bird of rejuvenation, hope and energy. Climbing the trunk is the squirrel, the animal of preparation and hard work. The Oak King stares at you directly, armored and ready to face any challenge head on.",
    "Oak Reversed. Consider withdrawing from responsibilities or projects that are too much of a burden before you break. This is not a time to be inflexible, but to compromise and know your limits. Let someone else shoulder the burden for a time.",
    "Poppy. Pay attention to your dreams to find your creative voice. Let go of assumptions about what you can and cannot do. Enter into your creative self, and return with treasures.",
    "Poppy Reversed. Warning to rest and regenerate. We are nearing exhaustion if not already there. We need time out from expectations to simply be. Let go for a time to renew your sense of joy.",
    "Rose. Seek love, beauty and harmony. As above, so below rises crowned in divine knowledge. Feel your heartbeat and sense creation spreading above, below and around it. Find beauty in yourself and in all creation. Look for opportunities for true, divine love in your present situation. You need to open yourself.",
    "Rose Reversed. Where are you unbalanced and lacking harmony? Are you closed to love or blind to beauty? Even the most devastating prodigies are shaped in beauty. This does not diminish their pain or harm, but helps us move past them and take the right action. You might be speaking too much. Keep things sub-rosa.",
    "Rue. We need protection and blessing even if things appear to be going well. Forces are working against us. Bring in more light and take precaution so no harm might befall us or our loved ones. Vervain represents protection blessings, healing, love and peace. The key of mysteries represents the gates we believe are locked to us. The waxing crescent Moon indicates slow and steady growth of good thinhg. The dagger represents protection and truth. The rooster head symbolizes vigilance and guardianship.",
    "Rue Reversed. Our defenses and protections have failed. Redouble your efforts or ask for help.",
    "Sorcerer's Violet. Reaching, striving and opening up while remaining grounded, centered and true to our past. Explore, but don't forget where you come from. Take reasonable precautions and be aware of subtle forces around you.",
    "Sorcerer's Violet Reversed. We need to protect ourselves from harm by laying low and paying attention or we really need to reflect on the harder lessons of the past before making our next move. Lessons of past loves might apply to the current situation.",
    "Sunflower. Beneficial omen indicating a time of joy, good cheer, health, wealth and success. The beautiful, balanced growth of the spiral symbolizes nature aligning with the infinite.",
    "Sunflower Reversed. Your good cheer is not gone, but covered by clouds. What will make you shine? Sometimes you just have to wait and let the clouds pass. At other times, you might have to take action, looking to see how either low self-esteem or arrogance might be blocking your happiness. Unhealed aspects of relationships with the father.",
    "Thistle. Stand in your nobility and assert your power. Stand tall for justice. Exhibit quiet strength and deal with the situation with confidence and security. When two hearts are united in one cause, they are crowned and multiply in strength and power.",
    "Thistle Reversed. Someone or something is pushing against your boundaries. Danger is coming and it's time to be perpared. Even if the danger is not yet visible, prepare to defend yourself in battle.",
    "Thorn Apple. Messages from the worlds above and below. Remember dreams. Potential romantic opportunities.",
    "Thorn Apple Reversed. Deception or influence against our better judgment. Subtle deceptions or our own delusions.",
    "Vine. Things are going well. Health, wealth and happiness are already present or coming your way. Slow down and enjoy the pleasures of the world while you have them. Possible turnaround after a period of difficulty and misfortune or successful period of creative interpretation and personal growth.",
    "Vine Reversed. Relax and loosed up from our sense of control and attachment. We are dominating, nervous and tense. Relax and open up to receive the abundance of blessings around us. We might also be entering a fallow time when there is hope for regeneration, but we must now prepare for the coming of winter. We might feel stuck, but inspiration will return.",
    "Willow. The leaping frog is a totem of transformation. The dragonfly signifies the shattering of illusions. The bees symbolize industry. The urn is the awareness of life and death.We need to be flexible by bending, changing and adapting to curcustances. Take steps to ease our pain and suffering. Do not become adamant in perspectives and feelings.",
    "Willow Reversed. Go within and reconnect with the unconscious.",
    "Wolfsbane. Courage in the face of challenge. Vitality and power to accomplish whatever is needed and go past it, further and deeper. Victory from the primal self.",
    "Wolfsbane Reversed. Terror. An uncontrollable desire to run away from confrontation or escape by becoming someone or something else. What are you running from? What fear are you being forced to confront? Learn courage, for it is only by facing fear that the next step will become apparent, not by avoiding it.",
    "Wormwood. We need to purge and protext ourselves from toxic forces, ranging from minor pests to poisonous serpents. Strengthen boundaries and speak out when they are crossed. With vitality reserved for ourselves instead of parasitic forces, connections to inspiration have been renewed. What song are w called to compose or sing? Follow your passion and don't let anything get in your way.",
    "Wormwood Reversed. Seek inspiration and insight in madness and poetry, looking between the gates of life and death to see things differently. Express insights through word, song and art. You may be reveling in toxic behaviors or relationships, or be enchanted by your obsessions.",
    "Yarrow. Time to consider who or what is allowed into your life. If you close down and limit yourself, consider opening to new people, situations and spiritual allies. If you are too open, pull back and ficus on deepening existing relationships. If you can offer aid to someone in need, now is the time.",
    "Yarrow Reversed. A violation of boundaries. A need to seal up wounds and re-establish shields. In recent interactions, when were lines crossed, contributing to a loss of your energy?",
    "Yew. Regeneration. Do not be afraid to push yourself past the breaking point.",
    "Yew Reversed. You are in crisis with spiritual or physics illness and you don't know what to do. Shed unnecessary burdens without being afraid of breaking, tghen grow and heal. You have the power to regenerate, but you can't hold on to the past. Move on.",
    "Garden. Reception of information and manifestation as an act of creation. What seeds do you tend in your spirit? Transformation, gentleness, breaking illusions and the greak work. Anchoring intentions, manifest willpower.",
    "Garden Reversed. What isn't clearly planted in your life? What has been uprooted? What is unbalanced? Which powers misaligned? Replant your garden."
]

thoth_readings = [
    "Fool. Movement, Energy, Innocence, Potential.",
    "Magus. Willpower, Activity, Impulse, Self-direction, Manifestation.",
    "Priestess. Internal change, Connecting with inner self, Seeing beyond illusion.",
    "Empress. Fertility, Life, Vitality, Connection with nature, Connection with the Universal Spirit.",
    "Emperor. Control, Order and organization, Discipline, Power, Rational thought, Will over nature.",
    "Hierophant. Rules, Regulations, Traditions, Education, Spiritual teacher.",
    "Lovers. Choices, Commitment, Harmony, Devotion, Being with another.",
    "Chariot. Success. Victory over past obstructions, Movement towards goals, Conquering.",
    "Lust. Vitality, Passion, Lust for life, Harmony with animalistic nature, Intensity.",
    "Hermit. Retreat, Self-reflection, Hidden wisdom, Insight, Soul-searching.",
    "Fortune. Cycles, Constant change, Fate, Acceptance, Movement with change.",
    "Adjustment. Objectivity, Honesty, Fairness, Knowledge, Clarity, Karma.",
    "Hanged Man. Patience, Waiting, Stillness, Change in perspective, Pause.",
    "Death. Death and rebirth, Beginnings and endings, Transformation, End of Cycle, Darkest fears.",
    "Art. Alchemy, Fusion, To combine and create.",
    "Devil. Independence, Spiritual freedom, Shadow self.",
    "Tower. Broken structures, Breaking foundations, Reckoning, Destruction, Loss of serenity.",
    "Star. Hope, Trust, Faith, Optimism, Inspiration, Following dreams.",
    "Moon. Feeling lost, Loss of clarity, Deception, Secrets, Hidden Truths.",
    "Sun. Abundance, Success, Generosity, Illumination, Truth.",
    "Aeon. Awakening, Rebirth, Renewal, Liberation, Revelation.",
    "Universe. Completion, Resolution, Mastery, Fulfillment, Accomplishment, End of journey.",
    "Ace of Wands. Will to create, Inspiration, Enthusiasm, Potential of creation.",
    "II of Wands: Dominion. Planning, Direction, Progress, Discovery, Expansion.",
    "III of Wands: Virtue. Constructive use of energy, Openness, Honesty.",
    "IV of Wands: Completion. Phase completed, Satisfaction, Stability.",
    "V of Wands: Strife. Personality clash, Competition, Inner conflict.",
    "VI of Wands: Victory. Victory of conflict, Public recognition, Confidence for other endeavors.",
    "VII of Wands: Valor. Bravery in adversity, Standing ground, Fighting for beliefs.",
    "VIII of Wands: Swiftness. Sudden movement, Progress, Rapid completion, Going with the flow.",
    "IX of Wands: Strength. Endurance, New trust in self, Determination, Discipline, Overcoming obstancles.",
    "X of Wands: Oppression. Blockages, Suppression, Frustration, Lost faith.",
    "Princess of Wands. Courage, Excitement, Free spirit, Love of life.",
    "Prince of Wands. Speed, Activity, Impulsiveness, Generosity.",
    "Queen of Wands. Trandformation, Independence, Honor, Passion.",
    "Knight of Wands. Inspiration, Power, Will, Expansion.",
    "Ace of Chalices. Unconditional love, New feelings, New friendship or relationship, Camaraderie.",
    "II of Chalices: Love. Close friendships and partnerships, Working in unity, Equality, Balance.",
    "III of Chalices: Abundance. Happiness in groups, Joyful social life, Sharing happiness with friends, Pleasure.",
    "IV of Chalices: Luxury. Familiarity, Boredom, Lack of motivation, Taking life for granted, Lack of risk.",
    "V of Chalices: Disappointment. Disappointment, Suffering, Pain, Grief, Self-pity, Disillusionment, Fear of risk.",
    "VI of Chalices: Pleasure. Healing, Rtion, Pleasure after hardship, Moving away from old wounds.",
    "VII of Chalices: Debauchery. Intoxication, Indulgence, Addictive emotions, Loss of control, Escapism.",
    "VIII of Chalices: Indolence. Lack of center, Numbness, Feeling dissatisfied, No lasting value, Wandering without cause.",
    "IX of Chalices: Happiness. Luck, Wishes fulfilled, Optimism, Trust in the universe, Compassion.",
    "X of Chalices: Satiety. Contentment, Emotional satisfaction, Gratitude, Feeling blessed, Generosity.",
    "Princess of Chalices. Fantasy, Self-exploration, Intuition, Kindness.",
    "Prince of Chalices. Outer serenity, Secrets, Volatility, Turbulence.",
    "Queen of Chalices. Imagination, Sensitivity, Depth, Emotional maturity.",
    "Knight of Chalices. Grace, Compassion, Vanity, Moodiness.",
    "Ace of Swords. Insight, Clarity, Breakthrough, Cutting to the heart of the matter, Sudden inspiration.",
    "II of Swords: Peace. Compromise, Equal and opposite forces, Balanced mind and heart, Stalling, Passivity.",
    "III of Swords: Sorrow. Pain, Suffering, Bitter truths, Separation, Breaking illusions.",
    "IV of Swords: Truce. Reflection, Temporary rest, Recharging, Recovery, Avoiding stress.",
    "V of Swords: Defeat. Fear, Negativity, Self-sabotage, Realizing limitations, Fear of failure.",
    "VI of Swords: Science. Research, Search for truth, Deeper thinking, Trial and error, Problem solving.",
    "VII of Swords: Futility. Doubts, Low self-esteem, Feeling helpless, Feeling exhausted, Loss of focus.",
    "VIII of Swords: Interference. Restless mind, Over-analysis, Uncontrolled thoughts, Fruitless thinking.",
    "IX of Swords: Cruelty. Aggression, Lack of compassion, Inflicting pain, Shame, Guilt.",
    "X of Swords: Ruin. Hopelessness, Ruin, Loss, Destruction, Catastrophe.",
    "Princess of Swords. Harsh words, Aggression, Bluntness, Manifestation.",
    "Prince of Swords. Idealism, Overactive mind, Mastery of words, Scattered energy.",
    "Queen of Swords. Wisdom, Open-mindedness, Perception, Fairness.",
    "Knight of Swords. Science, Intellect, Logic, Theory.",
    "Ace of Disks. Opportunity, Financial luck, Potential for abundance, Spirit connected to matter.",
    "II of Disks: Change. Flexibility, Adaptation, Trusting the process, Constant flux and change.",
    "III of Disks: Work. Achievement at work, Concentrated effort, Ambition, Work-life imbalance.",
    "IV of Disks: Power. Material security, Solid foundations, Stability, Wise investments, Conservatism.",
    "V of Disks: Worry. Material or physical challenges, Hard times, Threat to security.",
    "VI of Disks: Success. Generosity, Understanding true value of things.",
    "VII of Disks: Failure. Material loss, Crushed hope, False success, Failed investments.",
    "VIII of Disks: Prudence. Patience, Waiting for your chance, Considering details, Being careful, Hard work.",
    "IX of Disks: Gain. Wealth, Material comfort, General contentedness.",
    "X of Disks: Wealth. Security, Riches, Applying resources in meaningful ways.",
    "Princess of Disks. Reliability, Achievement, Hard work, Endurance.",
    "Prince of Disks. Determination, Planned action, Inventiveness, Stubbornness.",
    "Queen of Disks. Stability, Sensuality, Kindness, Practicality.",
    "Knight of Disks. Patience, Diligence, Focus, Instinct."
]


# 2. The 8 effects of trauma
effects = [
    "1. Sensitivity",
    "2. Inattention",
    "3. Obsession",
    "4. Depression",
    "5. Anger",
    "6. Panic",
    "7. Guilt",
    "8. Dissociation"
]

def generate_divination():
    """
    Returns a dictionary of 8 trauma effects, each with a randomly
    drawn Wound (from Alice readings) and Medicine (from Botanical readings),
    ensuring no index is repeated in the same reading.
    """
    # Select 8 unique indices from the Alice readings
    wound_indices = random.sample(range(len(alice_readings)), len(effects))
    # Select 8 unique indices from the Botanical readings
    medicine_indices = random.sample(range(len(botanical_readings)), len(effects))
    # Select 8 unique indices from the Thoth readings
    thoth_indices = random.sample(range(len(thoth_readings)), len(effects))

    readings = {}
    for i, effect in enumerate(effects):
        wound = alice_readings[wound_indices[i]]
        medicine = botanical_readings[medicine_indices[i]]
        thoth = thoth_readings[thoth_indices[i]]
        readings[effect] = {
            "Wound": wound,
            "Medicine": medicine
            "Context": thoth
        }
    return readings

def reading_to_string(reading):
    """
    Helper function to create a friendly string representation
    of the reading dictionary.
    """
    lines = []
    for effect, cards in reading.items():
        lines.append(f"{effect}\n  Wound: {cards['Wound']}\n  Medicine: {cards['Medicine']}\n  Context: {cards['Context']}\n")
    return "\n".join(lines)

# 3. The function to generate interpersonal events from an offline LLM
def generate_interpersonal_events(character1, character2):
    # Initialize the LLaMA 3.1 8B model (make sure you have this model available offline)
    llm = OllamaLLM(model="llama3.1:8b")

    # Convert dict-based readings into strings
    char1_str = reading_to_string(character1)
    char2_str = reading_to_string(character2)

    # Construct the prompt
    prompt = f"""
Objective: Generate three interpersonal events that advance the narrative.

Character traits format: For each of the 8 effects of trauma, the nature of the wound and the "medicine", i.e. the character arc that would serve as treatment, are indicated.

Character 1:
{char1_str}

---

Character 2:
{char2_str}

Describe the characters. Please provide three possible interpersonal events that could occur between these characters, each propelling the story forward. The events should be interpreted by each character differently because of their divergent traumas. Avoid therapy settings.
    """
    
    print(prompt)

    # Generate and return the response
    response = llm.invoke(prompt)
    return response

# 4. Generate two separate readings, then generate events
if __name__ == "__main__":
    # First character’s reading
    character1 = generate_divination()
    # Second character’s reading
    character2 = generate_divination()

    # Generate the interpersonal events
    events = generate_interpersonal_events(character1, character2)
    print(events)
