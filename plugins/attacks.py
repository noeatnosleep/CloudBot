import asyncio
import codecs
import json
import os
import random
import re

from cloudbot import hook
from cloudbot.util import textgen


opt_out = ['#anxiety', '#math', '#sandersforpresident', '#drama', '#linuxmasterrace', '#bipolar']


def is_self(conn, target):
    """ Checks if a string is "****self" or contains conn.name. """
    if re.search("(^..?.?.?self|{})".format(re.escape(conn.nick)), target, re.I):
        return True
    else:
        return False


@hook.on_start()
def load_attacks(bot):
    """
    :type bot: cloudbot.bot.CloudBot
    """
    global larts, flirts, kills, slaps, north_korea, insults, strax, compliments, presents

    with codecs.open(os.path.join(bot.data_dir, "larts.txt"), encoding="utf-8") as f:
        larts = [line.strip() for line in f.readlines() if not line.startswith("//")]

    with codecs.open(os.path.join(bot.data_dir, "flirts.txt"), encoding="utf-8") as f:
        flirts = [line.strip() for line in f.readlines() if not line.startswith("//")]

    with codecs.open(os.path.join(bot.data_dir, "insults.txt"), encoding="utf-8") as f:
        insults = [line.strip() for line in f.readlines() if not line.startswith("//")]

    with codecs.open(os.path.join(bot.data_dir, "kills.json"), encoding="utf-8") as f:
        kills = json.load(f)

    with codecs.open(os.path.join(bot.data_dir, "slaps.json"), encoding="utf-8") as f:
        slaps = json.load(f)

    with codecs.open(os.path.join(bot.data_dir, "strax.json"), encoding="utf-8") as f:
        strax = json.load(f)

    with codecs.open(os.path.join(bot.data_dir, "compliments.json"), encoding="utf-8") as f:
        compliments = json.load(f)

    with codecs.open(os.path.join(bot.data_dir, "north_korea.txt"), encoding="utf-8") as f:
        north_korea = [line.strip() for line in f.readlines() if not line.startswith("//")]

    with codecs.open(os.path.join(bot.data_dir, "presents.json"), encoding="utf-8") as f:
        presents = json.load(f)


@asyncio.coroutine
@hook.command
<<<<<<< HEAD
def lart(text, conn, chan, nick, action):
=======
def lart(text, conn, nick, action, is_nick_valid):
>>>>>>> 4c53fc2bd502d2365ba5dc08b64f0d7821712acb
    """<user> - LARTs <user>"""
    target = text.strip()
    # do not activate command for channels that opt out.
    if chan in opt_out:
        return

    if not is_nick_valid(target):
        return "I can't lart that."

    if is_self(conn, target):
        # user is trying to make the bot attack itself!
        target = nick

    phrase = random.choice(larts)

    # act out the message
    action(phrase.format(user=target))


@asyncio.coroutine
@hook.command("flirt", "sexup", "jackmeoff")
<<<<<<< HEAD
def flirt(text, conn, nick, chan, message):
=======
def flirt(text, conn, nick, message, is_nick_valid):
>>>>>>> 4c53fc2bd502d2365ba5dc08b64f0d7821712acb
    """<user> - flirts with <user>"""
    target = text.strip()
    if chan in opt_out:
        return

    if not is_nick_valid(target):
        return "I can't flirt with that."

    if is_self(conn, target):
        # user is trying to make the bot attack itself!
        target = nick

    message('{}, {}'.format(target, random.choice(flirts)))


@asyncio.coroutine
@hook.command("kill", "end")
<<<<<<< HEAD
def kill(text, conn, nick, action, chan):
=======
def kill(text, conn, nick, action, is_nick_valid):
>>>>>>> 4c53fc2bd502d2365ba5dc08b64f0d7821712acb
    """<user> - kills <user>"""
    target = text.strip()
    if chan in opt_out:
        return

    if not is_nick_valid(target):
        return "I can't attack that."

    if is_self(conn, target):
        # user is trying to make the bot attack itself!
        target = nick

    generator = textgen.TextGenerator(kills["templates"], kills["parts"], variables={"user": target})

    # act out the message
    action(generator.generate_string())


@asyncio.coroutine
@hook.command
<<<<<<< HEAD
def slap(text, action, nick, chan, conn):
=======
def slap(text, action, nick, conn, is_nick_valid):
>>>>>>> 4c53fc2bd502d2365ba5dc08b64f0d7821712acb
    """<user> -- Makes the bot slap <user>."""
    target = text.strip()
    if chan in opt_out:
        return

    if not is_nick_valid(target):
        return "I can't slap that."

    if is_self(conn, target):
        # user is trying to make the bot attack itself!
        target = nick

    variables = {
        "user": target
    }
    generator = textgen.TextGenerator(slaps["templates"], slaps["parts"], variables=variables)

    # act out the message
    action(generator.generate_string())


@asyncio.coroutine
@hook.command
def compliment(text, action, nick, conn, is_nick_valid):
    """<user> -- Makes the bot compliment <user>."""
    target = text.strip()

    if not is_nick_valid(target):
        return "I can't compliment that."

    if is_self(conn, target):
        # user is trying to make the bot attack itself!
        target = nick

    variables = {
        "user": target
    }
    generator = textgen.TextGenerator(compliments["templates"], compliments["parts"], variables=variables)

    # act out the message
    action(generator.generate_string())


@hook.command(autohelp=False)
def strax(text, conn, message, nick, is_nick_valid):
    """Strax quote."""

    if text:
        target = text.strip()
        if not is_nick_valid(target):
            return "I can't do that."

        if is_self(conn, target):
            # user is trying to make the bot attack itself!
            target = nick
        variables = {
            "user": target
        }

        generator = textgen.TextGenerator(strax["target_template"], strax["parts"], variables=variables)
    else:
        generator = textgen.TextGenerator(strax["template"], strax["parts"])

    # Become Strax
    message(generator.generate_string())


@hook.command(autohelp=False)
def nk(chan, message):
    """outputs a random North Korea propoganda slogan"""
<<<<<<< HEAD
    if chan in opt_out:
        return
    index = random.randint(0,len(north_korea)-1)
=======
    index = random.randint(0, len(north_korea) - 1)
>>>>>>> 4c53fc2bd502d2365ba5dc08b64f0d7821712acb
    slogan = north_korea[index]
    message(slogan, chan)


@asyncio.coroutine
@hook.command()
<<<<<<< HEAD
def insult(text, conn, nick, chan, notice, message):
=======
def insult(text, conn, nick, notice, message, is_nick_valid):
>>>>>>> 4c53fc2bd502d2365ba5dc08b64f0d7821712acb
    """<user> - insults <user>
    :type text: str
    :type conn: cloudbot.client.Client
    :type nick: str
    """
    if chan in opt_out:
        return
    target = text.strip()

    if not is_nick_valid(target):
        notice("Invalid username!")
        return

    # if the user is trying to make the bot target itself, target them
    if is_self(conn, target):
        target = nick

    message("{}, {}".format(target, random.choice(insults)))


@asyncio.coroutine
@hook.command("present", "gift")
def present(text, conn, nick, action, is_nick_valid):
    """<user> - gives gift to <user>"""
    target = text.strip()

    if not is_nick_valid(target):
        return "I can't gift that."

    if is_self(conn, target):
        # user is trying to make the bot gift itself!
        target = nick

    variables = {
        "user": target
    }

    generator = textgen.TextGenerator(presents["templates"], presents["parts"], variables=variables)
    action(generator.generate_string())
