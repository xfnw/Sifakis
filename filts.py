
import asyncio

from irctokens import build, Line


async def line_read(self,line):
    # line tags command params source
    if line.command == "PING" or line.command == "001":
        self.jointh = []
    if line.command == "JOIN":
        await on_join(self,line)


async def on_join(self,line):
    nick = line.source.split('!')[0].lower()
    if nick in self.jointh:
        return
    else:
        self.jointh.append(nick)
    reason = []
    user = self.users[nick]

    reason += [f'NS_ACCOUNT ({ac}) (yeen yeen yeen)' for ac in ['yeenis'] if ac == user.account]
    
    reason += [f'BAD_REALNAME ({user.realname}) (gore spammer?)' for ac in ['kendo'] if ac in user.realname]

    host = line.source.split('@')[1]
    reason += [f'BAD_HOST ({host}) (chilli xmpp bridge)' for ac in ['hot-chilli'] if ac in host]

    if len(reason) > 0:
        await self.linelog(f'{line.source} caught in {line.params[0]} because of {", ".join(reason)}')





