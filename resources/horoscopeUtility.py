"""Utility functions to figure out zodiac sign and zodiac_sign"""
from collections import Counter


def get_horoscope(day: int, month: int) -> list:
    """ Function to get zodiac_sign and zodiac based on birthdate"""

    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        zodiac_sign = "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        zodiac_sign = "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        zodiac_sign = "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        zodiac_sign = "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        zodiac_sign = "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        zodiac_sign = "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        zodiac_sign = "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        zodiac_sign = "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        zodiac_sign = "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        zodiac_sign = "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        zodiac_sign = "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        zodiac_sign = "Pisces"
    else:
        zodiac_sign = "Invalid date"

    if zodiac_sign != "Invalid date":
        horoscopes[zodiac_sign]['count'] += 1
        return [zodiac_sign, horoscopes[zodiac_sign]]
    return [zodiac_sign, {}]


def get_top_three():
    """
    Get top 3 horoscopes
    :return: list of tuples with sign name and count of the top 3 zodiac signs
    """
    zodiac_name_and_count_dict = {}
    for zodiac_name, zodiac_info in horoscopes.items():
        zodiac_name_and_count_dict[zodiac_name] = zodiac_info['count']

    k = Counter(zodiac_name_and_count_dict)
    top_3_zodiac = k.most_common(3)
    return top_3_zodiac


horoscopes = {
    "Aquarius": {"zodiac_sign": "/resources/horoscopes/aquarius_img.png",
                 "horoscope": "Making connections with interesting people is going to be your full-time job today, "
                              "but since when did you mind being social? Keeping busy will keep you happy, "
                              "so get out there and get to talking. Go online. Check your social media feeds and "
                              "spend some time touching base with folks you haven't talked to in a while. Send some "
                              "funny messages and see what happens. There's bound to be some fresh news or gossip, "
                              "and aren't you just dying to know what it is? Find out.",
                 "count": 0},
    "Aries": {"zodiac_sign": "/resources/horoscopes/aries_img.png",
              "horoscope": "With every step you take today, you are approaching a major turning point, so you've got "
                           "to be primed and ready to act when you see a great opportunity heading your way. Changes "
                           "can happen at any time in your life if you are ready and waiting for them. It might not "
                           "be comfortable for you to act quickly at first, but eventually you will get into the "
                           "excitement and enjoy the unpredictability of it all. You'll never feel more in charge of "
                           "your life than you do today.",
              "count": 0},
    "Cancer": {"zodiac_sign": "/resources/horoscopes/cancer_img.png",
               "horoscope": "It's not selfish to want to be by yourself. It's actually healthy! If being a social "
                            "butterfly is simply not high on your priority list now, don't be ashamed of it. Get "
                            "comfy on the couch and watch one of your favorite movies tonight. Order in some food and "
                            "just relax. Some friends may not understand this inward phase you're going through, "
                            "but they will accept it. They'll have to! You need to be honest with your needs. People "
                            "appreciate it.",
               "count": 0},
    "Capricorn": {"zodiac_sign": "/resources/horoscopes/capricorn_img.png",
                  "horoscope": "Pretending someone is what they are not is a dangerous game. You can't be idealistic "
                               "about what someone is really about. Take off your rose-colored glasses today and see "
                               "the person for who they truly are. What other people have been saying hasn't been to "
                               "your liking, but it may be true. Look at the entire person and see all of their "
                               "imperfections. Who knows? You might even like them more than you did before. Seeing "
                               "all sides of people may be a rude awakening from a dream state, but you have to wake "
                               "up at some point.",
                  "count": 0},
    "Gemini": {"zodiac_sign": "/resources/horoscopes/gemini_img.png",
               "horoscope": "There is nothing wrong with adding some fun to a business situation. As long as you stay "
                            "professional, why is it wrong to smile and laugh? You can't take everything so seriously "
                            "all of the time. It's not healthy! So try out a few silly jokes. Not only will you make "
                            "everyone relax a bit, but you will encourage other people to add their personality to "
                            "the conversation. It will help everyone connect on a deeper level and help you all get a "
                            "lot more done.",
               "count": 0},
    "Leo": {"zodiac_sign": "/resources/horoscopes/leo_img.png",
            "horoscope": "Clear your schedule and set aside your expectations. This is going to be a fickle kind of "
                         "day, and you need to be as flexible as possible. It's a day to toss out the rule book and "
                         "just let things go along their merry way. You won't be disappointed. But if you struggle "
                         "against the tide of the day and stubbornly try to stick to what you had planned, "
                         "you'll experience a lot of frustration. Become more passive, and you will learn an awful "
                         "lot about the world around you.",
            "count": 0},
    "Libra": {"zodiac_sign": "/resources/horoscopes/libra_img.png",
              "horoscope": "Your imagination, creativity, and intuition can be combined today to give you almost "
                           "superhuman powers, so use them with abandon to get an edge. Is everyone around you "
                           "scratching their heads at the big mystery that's been plaguing them? Cook up a theory "
                           "about what's been going on, and chances are you will be right on the money. This is a "
                           "wonderful time for you if you are in any kind of leadership position. People will know "
                           "that what you say goes because what you say is usually right.",
              "count": 0},
    "Pisces": {"zodiac_sign": "/resources/horoscopes/pisces_img.png",
               "horoscope": "Are you starting to feel like a doormat in one of your relationships, like they're "
                            "walking all over you and you aren't getting half of the credit you deserve? Today, "
                            "get off the ground and get out of this person's life for a while. Show them that they "
                            "need you a lot more than you need them. They will be back asking for your help soon, "
                            "but by then you will have formulated the terms you expect and be able to set the "
                            "boundaries that make you comfortable. You need to demand equal footing.",
               "count": 0},
    "Sagittarius": {"zodiac_sign": "/resources/horoscopes/sag_img.png",
                    "horoscope": "Get out in the world today. Set your alarm clock an hour early and give yourself "
                                 "some time to walk around the block, stop for breakfast, or just read the news while "
                                 "you nurse a cup of coffee. If you've been feeling moody and slow, this more gentle "
                                 "introduction to your day will help you unlock some of the energy that you need to "
                                 "stay motivated. And if you can get someone to join you on this calm, early morning "
                                 "adventure, that's even better.",
                    "count": 0},
    "Scorpio": {"zodiac_sign": "/resources/horoscopes/scorpio_img.png",
                "horoscope": "It's all about endurance today, and you'll be able to do anything for any length of "
                             "time, including sitting through that boring meeting without falling asleep, "
                             "surviving that awful blind date with effortless charm, and waiting in a long line "
                             "without grumbling. You have some serious strength and patience deep down inside, "
                             "which will come to your rescue today. Entertaining yourself has never been so easy. "
                             "You'll always be in your happy place no matter where you are.",
                "count": 0},
    "Taurus": {"zodiac_sign": "/resources/horoscopes/taurus_img.png",
               "horoscope": "Your fiery enthusiasm for what you believe in is powerful. You can always make things "
                            "happen with your emotional conviction, but today, rein in that power and keep it to "
                            "yourself. Controversial conversations could be filled with traps. If you jump into "
                            "things headfirst, you may end up getting burned, or at least putting your foot in your "
                            "mouth. Experiment by taking an impersonal point of view. Don't let your listening skills "
                            "be hampered by your passion.",
               "count": 0},
    "Virgo": {"zodiac_sign": "/resources/horoscopes/virgo_img.png",
              "horoscope": "All of your plans are going to go well today. And if any obstacles do appear, they will be "
                           "the kind that fizzle out on their own soon enough. The only way you can fall into a bad "
                           "mood today is if you let your mind wander to problems that you can't fix. Dwell on things "
                           "beyond your control, and you could start feeling blue. Instead, let yourself be happy. "
                           "Keep your mind on all the good news in your life right now. There is plenty of it.",
              "count": 0},
}
