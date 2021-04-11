import requests        
import discord


joel_msg = ["Hey! There's nothing wrong with a little bit of drippin'",  
        "When you get a raging boner, and you're like: I want a fuck alot of shit dude", 
        "I left a little sauce for you baby",
        "I have a Sublime t-shirt and I've actually been to a Sublime concert",
        "This is where the basement dwellers reside",
        "Baba Bababooey!",
        "There's nothin' wrong with some sister loving dawg",
        "You better tell the 5 year olds that Joel got 'em for 5 dollars a pack.",
        "Can you feel it? That's my cock swaggin'.",
        "I'll tell you this:\nI got, like, probably 150 packs not even opened. I've only opened 9 of them.",
        "There's nothing wrong with some sister loving dawg",
        "I want to bang your mom. Seriously, what does she look like?",
        "I was fucking dead bodies over in Ireland dawg",
        "You're just mad because I have itchy cock right now, dawg",
        "I've played 21 years of Battlefield. Yes, I am on edge.",
        "Pokimane wishes she could fuck my cards.",
        "I will fuck the shit out of your family.",
        "Hey. You're just mad dude. I just fucked you dude",
        "Shut up you fucking downy! Shut the fuck up goat shack! ",
        "If Snorlax had a Fifi, shit dude. Smash dawg.",
        "Does you mama got some mommy milkers? I want to suck it out of the tit.",
        "Let me weigh you up. You don't even weigh as much as me dude",
        "I'm gonna rub both your dicks on spore island and we're gonna have a threesome",
        "I'm a bring this to your mom's work, make a sandwich, and cum in it",
        "Don't make me have put on my thong and fucking big brain and do head to matches",
        "You're just mad dude that I'd pick up your mom with this voice dawg.",
        "I'm gonna look good and cum while I'm doing it: in my mouth",
        "Whoo! I might start twerking. I don't care. I go commando, dude. I let that fucking shit hang out",
        "This is the basement! We get down, we yell, we have nut sweat, we have ass sweat! The boys are in the basement! The real gamers got fucking 50 feet with their big dicks and fucking stamina dude!",
        "You know xChocoBars? I'm gonna blackmail her ass.",
        "You're just mad that I have itchy cock right now!",
        "Do not ruin this moment because we're going fishing.",
        "Shut up you fuckin' horse tooth!",
        "Your mom is a fucking nanny goat! I just fucked her dude! That was the best pussy I ever had and you came out.",
        "You're just mad because I fucked your nanny goat dude.",
        "They made a GIF of me eating Little Caesers. I wonder who did that? It's perfect dude.\nhttps://media3.giphy.com/media/Hodzpdb7J7VRULgY5z/giphy.gif",
        "I'm gonna plug this in, right? And I'm gonna fuck you up. ",
        "You're just mad, dude. I'm banging your mom bro. How is she doing?",
        "Your just mad dude that I'd pick up your mom with this voice dawg",
        "You know xChocoBars? She been DM-ing me on facebook, dawg. She be sending me pictures of her inner thong and shit"
        ]
yt = ['https://youtu.be/camj6yZc-gc',
        'https://youtu.be/uZJo7hwkQp8',
        'https://youtu.be/wYBqoRh-YtI',
        'https://youtu.be/VVXvz9IP3hg',
        'https://youtu.be/XtRp56GNYMI',
        'https://youtu.be/O8mOhjErleY',
        'https://youtu.be/L6aGSRGe7b8'
        ]
gifs = ['https://media3.giphy.com/media/X8Q5XyiNKTOxsPA42g/giphy.gif',
        'https://media4.giphy.com/media/ZnoTEV2kXyIYCCGcas/giphy.gif',
        'https://media2.giphy.com/media/0Mtrvd5lWfbBmRS8Px/giphy.gif',
        'https://media0.giphy.com/media/AkKSPM4H1DTwtDjAyK/giphy.gif',
        'https://media0.giphy.com/media/Ev0YtsRwUFiRxpMehq/giphy.gif',
        'https://media1.giphy.com/media/dh35ZPS55DqPUAriT6/giphy.gif',
        'https://media3.giphy.com/media/Qj7SpiN0E0nduXFup6/giphy.gif',
        'https://media3.giphy.com/media/wDnQ0tCRgXjD5a0DbU/giphy.gif',
        'https://media3.giphy.com/media/VhsUwUnvhQGxzOvcJ0/giphy.gif',
        'https://media4.giphy.com/media/BNfjIW3lAyXkzW0Kd8/giphy.gif',
        'https://media3.giphy.com/media/VEwPG2qvdv8JSSSDUc/giphy.gif',
        'https://media3.giphy.com/media/Z5vyY6gy0e9CEy1dkQ/giphy.gif',
        'https://media3.giphy.com/media/cPz1a3Y4X9e1MOZvEc/giphy.gif',
        'https://media0.giphy.com/media/njPGBL2yE5BG80mH3q/giphy.gif',
        'https://media3.giphy.com/media/bSksLcnqDPw8Qu4A0I/giphy.gif',
        'https://media0.giphy.com/media/T32vAPTrkivk5cQ6le/giphy.gif',
        'https://media4.giphy.com/media/jKaT1v0aYWrIJOM1A1/giphy.gif',
        'https://media1.giphy.com/media/e2x5ADkuVPPXKKj3ZE/giphy.gif',
        'https://media1.giphy.com/media/EbwhMeSSL2gz9j5shg/giphy.gif',
        'https://media2.giphy.com/media/h7mfRXaLnRPaZmGTjp/giphy.gif',
        "https://media2.giphy.com/media/LBMHGbpAc4CH4waAMG/giphy.gif",
        "https://media2.giphy.com/media/WYsARJ82IjboYlQSYN/giphy.gif"
        ]

def fakePerson():
    person = requests.get("https://pipl.ir/v1/getPerson")
    # fake person data
    edu = person.json()['person']['education']['certificate'] +" - "+ person.json()['person']['education']['university']
    email = person.json()['person']['online_info']['email']
    ip = person.json()['person']['online_info']['ip_address']
    age = person.json()['person']['personal']['age']
    blood = person.json()['person']['personal']['blood']
    cellphone = person.json()['person']['personal']['cellphone']
    city = person.json()['person']['personal']['city']
    country = person.json()['person']['personal']['country']
    eyeColor = person.json()['person']['personal']['eye_color']
    lastname=person.json()['person']['personal']['last_name']
    firstname=person.json()['person']['personal']['name']
    religion = person.json()['person']['personal']['religion']
    height=person.json()['person']['personal']['height']
    weight=person.json()['person']['personal']['weight']
    gender=person.json()['person']['personal']['gender']
    position=person.json()['person']['work']['position']
    salary =person.json()['person']['work']['salary']
    # embed
    embed = discord.Embed(title="Person: "+firstname+" "+lastname, color=discord.Color.blue())
    embed.add_field(name="Education:", value=edu)
    embed.add_field(name="Gender:", value=gender)
    embed.add_field(name="Age:", value=str(age))
    embed.add_field(name="Blood Type:", value=blood)
    embed.add_field(name="Eye Color:", value=eyeColor)
    embed.add_field(name="Height(m):", value=str(height))
    embed.add_field(name="Weight(kg):", value=str(weight))
    embed.add_field(name="Phone:", value=cellphone)
    embed.add_field(name="Location:", value=(city+", "+country))
    embed.add_field(name="Position:", value=position)
    embed.add_field(name="Salary:", value=salary)
    embed.add_field(name="Religion:", value=religion)
    embed.add_field(name="IP Address:", value=ip)

    return embed

