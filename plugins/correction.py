import re

from cloudbot import hook

from cloudbot.util.formatting import ireplace

correction_re = re.compile(r"^[sS]/(.*/.*(?:/[igx]{,4})?)\S*$")

# define channels that want this plugin disabled.

opt_out = []

def shorten_msg(msg):
    out = (msg[:500]) if len(msg) > 500 else msg
    return out
@hook.regex(correction_re)
def correction(match, conn, nick, chan, message):
    """
    :type match: re.__Match
    :type conn: cloudbot.client.Client
    :type chan: str
    """
    if chan in opt_out:
        return
    groups = [b.replace("\/", "/") for b in re.split(r"(?<!\\)/", match.groups()[0])]
    find = groups[0]
    replace = groups[1]
    if find == replace:
        return "really dude? you want me to replace {} with {}?".format(find, replace)
    
    if not find.strip(): # Replacing empty or entirely whitespace strings is spammy
        return "really dude? you want me to replace nothing with {}?".format(replace)

    for item in conn.history[chan].__reversed__():
        name, timestamp, msg = item
        if correction_re.match(msg):
            # don't correct corrections, it gets really confusing
            continue

        if find.lower() in msg.lower():
            if "\x01ACTION" in msg:
                msg = msg.replace("\x01ACTION", "").replace("\x01", "")
                mod_msg = shorten_msg(ireplace(msg, find, "\x02" + replace + "\x02"))
                message("Correction, * {} {}".format(name, mod_msg))
            else:
                mod_msg = shorten_msg(ireplace(msg, find, "\x02" + replace + "\x02"))
                message("Correction, <{}> {}".format(name, mod_msg))

            msg = shorten_msg(ireplace(msg, find, replace))
            if nick.lower() == name.lower():
                conn.history[chan].append((name, timestamp, msg))
            return
        else:
            continue
    # return("No matches for \"\x02{}\x02\" in recent messages from \x02{}\x02. You can only correct your own messages.".format(find, nick))
