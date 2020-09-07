# Adaptative Gamification Api

An api to generate embedding code of adaptative gamification mechanics (as well as common mechanics), which is easily used in your web project. All data involved with the mechanics is managed through this application, so developers shouldn't care about managing gamification data, while they offer a gamified experience. This is a project from Barcelona University, namely NanoMOOC UB project, so for any use of it, contact with nanomoocsub@gmail.com

## Features ##

Currently the api generates incrustable code for the following gamification mechanics:

- Development Tools (Disruptor)
- Challenges (Disruptor)
- Easter Eggs (Free spirit)
- Unlockables (Free spirit)
- Badges (Achiever)
- Levels (Achiever)
- Points (Player)
- Leaderboards (Player)
- Lotteries (Player)
- Social Networks (Socializer)
- Social Statuses (Socializer)
- Sharing (Philantropist) :: IN PROGRESS
- Gifts (Philantropist) :: IN PROGRESS
- Adaptative Mechanic via gamer profiles (Adaptative)
- Adaptative Mechanic via gamer profiles and interaction statistics (Adaptative)

## Installation ##

The api doesn't need any special installation: Just ensure to install in your virtualenv all requirements (requirements.txt) or use the default venv in this repo (probably not working by dependences with the current development machine).

## Usage ##

Use django's runserver to run the application:

```bash
python manage.py runserver
```

