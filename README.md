# 20newsgroups-kafka-mongo


Below is a sorting system for old text messages divided into 2 groups - interesting and not interesting.
The system will save the messages in MongoDB and return the data according to the appropriate request (details below)

The data collection we will use is 20newsgroups, which is a well-known text collection in the data world.
It can be pulled from the sklearn package.
Briefly explore the sklearn explanation page regarding the different categories

### Agenda

To build a pub-sub system that handles the 20Newsgroups dataset.
PUB extracts messages from the dataset and publishes them to subscribers according to 2 topics:
interesting
not_interesting

SUBS store messages in MongoDB, each in a separate collection according to the topic, and each provides a GET function to return new information since the last time (which was sent in a GET request).

### Main components

1. **Publisher - PUB** - FastAPI service

GET endpoint that triggers the publishing process.

For each GET received, 20 messages will be retrieved from the dataset (one from each news source) according to the 2 categories we gave.

Messages will be sent to subscribers by topic (according to the topics)

2. **Subscribers - SUBS** - two separate FastAPI services

Each subscribes to one topic (according to the details above).

Each receives messages from the PUB, adds a timestamp as an additional field, and saves in a separate collection for each topic.

GET endpoint that returns all messages saved in the database (including the timestamp) for a specific service. (Check if more than one GET is needed)

3. **MongoDB** - a unified database, with a collection for each topic.

### Additional implementations

1. The message in the SUB include a **timestamp** of the time of receipt.
2. **Dockerfile** for each service.
3. System test with **curl / Postman / Python script:**

PUB's GET sends messages (according to what is written in the main components - PUB).

SUBS stores and returns messages in GET according to the TOPIC.


### Results:

***Messages:***

```
publisher                   | [2025-08-25 16:23:54,256] INFO in producer: Sent message to topic: interesting
publisher                   | [2025-08-25 16:23:54,256] INFO in producer: Sent message to topic: not_interesting
publisher                   | INFO:     162.159.141.50:22740 - "GET /publish HTTP/1.1" 200 OK
subscriber_not_interesting  | [2025-08-25 16:23:54,279] INFO in consumer_not_interesting: Saved message with timestamp.
subscriber_interesting      | [2025-08-25 16:23:54,280] INFO in consumer_interesting: Saved message with timestamp.
subscriber_not_interesting  | [2025-08-25 16:23:54,279] INFO in consumer_not_interesting: Saved message with timestamp.
subscriber_interesting      | [2025-08-25 16:23:54,280] INFO in consumer_interesting: Saved message with timestamp.
subscriber_not_interesting  | [2025-08-25 16:23:54,285] INFO in consumer_not_interesting: Saved message with timestamp.
subscriber_not_interesting  | [2025-08-25 16:23:54,286] INFO in consumer_not_interesting: Saved message with timestamp.


subscriber_not_interesting  | [2025-08-25 16:23:54,285] INFO in consumer_not_interesting: Saved message with timestamp.
subscriber_interesting      | [2025-08-25 16:23:54,286] INFO in consumer_interesting: Saved message with timestamp.
```


```
# http://localhost:8000/publish

{
  "status": "published",
  "count": 40
}

# curl http://localhost:8001/messages

{
  "messages": [
    {
      "text": "From: ahatcher@athena.cs.uga.edu (Allan Hatcher)\nSubject: Re: Traffic morons\nOrganization: University of Georgia, Athens\nLines: 37\n\nIn article \u003CStafford-200493102833@stafford.winona.msus.edu\u003E Stafford@Vax2.Winona.MSUS.Edu (John Stafford) writes:\n\u003EIn article \u003C10326.97.uupcb@compdyn.questor.org\u003E,\n\u003Eryan_cousineau@compdyn.questor.org (Ryan Cousineau) wrote:\n\u003E\u003E \n\u003E\u003E NMM\u003EFrom: nielsmm@imv.aau.dk (Niels Mikkel Michelsen)\n\u003E\u003E NMM\u003ESubject: How to act in front of traffic jerks\n\u003E\u003E \n\u003E\u003E NMM\u003EThe other day, it was raining cats and dogs, therefor I was going only to\n\u003E\u003E NMM\u003Ethe speed limit, on nothing more, on my bike. This guy in his BMW was\n\u003E\u003E NMM\u003Edriving 1-2 meters behind me for 7-800 meters and at the next red light I\n\u003E\u003E NMM\u003Ecalmly put the bike on its leg, walked back to this car, he rolled down the\n\u003E\u003E NMM\u003Ewindow, and I told him he was a total idiot (and the reason why).\n\u003E\u003E \n\u003E\u003E NMM\u003EDid I do the right thing?\n\u003E\n\u003E\timho, you did the wrong thing.  You could have been shot\n\u003E or he could have run over your bike or just beat the shit\n\u003E out of you.  Consider that the person is foolish enough\n\u003E to drive like a fool and may very well _act_ like one, too.\n\u003E\n\u003E Just get the heck away from the idiot.\n\u003E\n\u003E IF the driver does something clearly illegal, you _can_\n\u003E file a citizens arrest and drag that person into court.\n\u003E It's a hassle for you but a major hassle for the perp.\n\u003E\n\u003E====================================================\n\u003EJohn Stafford   Minnesota State University @ Winona\nYou can't make a Citizens arrest on anything but a felony.\n.\n  \n\n\n\u003E\n\u003E                    All standard disclaimers apply.\n\n\n",
      "timestamp": "2025-08-25T16:11:24.835192+00:00"
    },
...

# curl http://localhost:8002/messages
{
  "messages": [
    {
      "text": "From: mpaul@unl.edu (marxhausen paul)\nSubject: Re: Mary's assumption\nOrganization: University of Nebraska--Lincoln\nLines: 31\n\nI hate to sound flippant, having shot off my mouth badly on the net\nbefore, but I'm afraid that much of this material only adds to my\nfeeling that \"the assumption of Mary\" would be better phrased \"our\nassumptions _about_ Mary.\"  In all the time I've been reading about\nMary on this group, I can not recall reading much about Mary that\ndid not sound like wishful veneration with scant, if any, Scriptural\nfoundation.  \n\nI find in the New Testament a very real portrait of Christ's parents\nas compellingly human persons; to be honored and admired for their\nhumility and submission to God's working, beyond doubt.  But the almalga-\nmation of theories and dogma that has accreted around them gives me\nan image of alien and inhuman creatures, untouched by sin or human\ndesire.  Only Christ himself was so truly sanctified, and even He knew\ntemptation, albeit without submitting to it.\n\nI also don't see the _necessity_ of saying the Holy Parents were some-\nhow sanctified beyond normal humanity: it sounds like our own inability\nto grasp the immensity of God's grace in being incarnated through an or-\ndinary human being.  \n\nI won't start yelling about how people are \"worshipping\" Mary, etc.,\nsince folks have told me otherwise about that, but I do think we\nlose part of the wonder of God's Incarnation in Christ when we make\nhis parents out to be sinless, sexless, deathless, otherworldly beings.\n  \n--\npaul marxhausen .... ....... ............. ............ ............ .......... \n .. . .  . . . university of nebraska - lincoln .  . . .. . .  .. . . . . . . .\n .     .    .  .   .     .   .  .    .   .  .   .    .   .  grace .   .    .  . \n   .         .       .      .        .        .      .        .   happens .     \n",
      "timestamp": "2025-08-25T16:11:24.834945+00:00"
    },
...
```


***Logging:***

```
publisher                   | [2025-08-25 16:23:54,256] INFO in producer: Sent message to topic: interesting
publisher                   | [2025-08-25 16:23:54,256] INFO in producer: Sent message to topic: not_interesting
publisher                   | INFO:     162.159.141.50:22740 - "GET /publish HTTP/1.1" 200 OK
subscriber_not_interesting  | [2025-08-25 16:23:54,279] INFO in consumer_not_interesting: Saved message with timestamp.
subscriber_interesting      | [2025-08-25 16:23:54,280] INFO in consumer_interesting: Saved message with timestamp.
subscriber_not_interesting  | [2025-08-25 16:23:54,279] INFO in consumer_not_interesting: Saved message with timestamp.
subscriber_interesting      | [2025-08-25 16:23:54,280] INFO in consumer_interesting: Saved message with timestamp.
subscriber_not_interesting  | [2025-08-25 16:23:54,285] INFO in consumer_not_interesting: Saved message with timestamp.
subscriber_not_interesting  | [2025-08-25 16:23:54,286] INFO in consumer_not_interesting: Saved message with timestamp.


subscriber_not_interesting  | [2025-08-25 16:23:54,285] INFO in consumer_not_interesting: Saved message with timestamp.
subscriber_interesting      | [2025-08-25 16:23:54,286] INFO in consumer_interesting: Saved message with timestamp.
```
