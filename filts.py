
M = 60
H = 60*M
D = 24 * H

import asyncio

from irctokens import build, Line


async def line_read(self,line):
    # line tags command params source
    if line.command == "PING" or line.command == "001":
        self.jointh = []
        self.tomode=["#chaos","-cunt"]
    if line.command == "482":
        await self.send(build("cs",["owner","#chaos"]))
    if line.command == "JOIN":
        await on_join(self,line)
    if line.command == "MODE":
        await on_mode(self,line)
    if line.command == "KICK":
        await on_kick(self,line)

async def on_kick(self,line):
    if (
            line.params[0] == '#chaos' and
            line.params[1] == self.nickname
            ):
        await self.send(build("cs",["invite",line.params[0]]))


async def awpop(obj,item):
    await asyncio.sleep(1*M)
    obj.pop(item)

async def on_join(self,line):
    nick = line.source.split('!')[0].lower()
    #if nick in self.jointh:
    #    return
    #else:
    #    asyncio.create_task(awpop(self.jointh,len(self.jointh)))
    #    self.jointh.append(nick)

async def checkUser(self,nick):
    reason = []
    user = self.users[nick]

    reason += [f'BAD_NICK ({nick}) (malicious robot)' for ac in ['war','space'] if ac in nick]
    reason += [f'NS_ACCOUNT ({ac}) (Kied)' for ac in ['kiedtl','yeenkuus','kiedtl_bots'] if ac == user.account]

    reason += [f'BAD_REALNAME ({user.realname}) (Kied)' for ac in ['kiedtl','spacehare'] if ac in user.realname]

    reason += [f'BAD_USERNAME ({user.username}) (Kied)' for ac in ['kiedtl','spacehare'] if ac in user.username]
    reason += [f'BAD_HOSTNAME ({user.hostname}) (Open Proxy)' for ac in ['chilli','harris.team'] if ac in user.hostname]

    if len(reason) > 0:
        #self.tomode = nick
        return nick
        #await self.send(build("MODE",["#chaos","-qocunt",nick,nick]))
        #await self.linelog(f'{nick} caught because of {", ".join(reason)}')
    else:
        return False

async def on_mode(self,line):
    if self.nickname in line.source:
        return
    if line.params in [["#chaos","+q",self.nickname],["#chaos","+qo",self.nickname,self.nickname]]:
        await self.send(build("MODE",self.tomode))
        return
    unmo = []
    for i in self.channels['#chaos'].users: #set(line.params[2:]):
        nick = i.lower()
        if line.params[0] in self.channels and nick in self.channels[line.params[0]].users:
            us = await checkUser(self,nick)
            if us:
                unmo.append(us)
    if len(unmo) > 0:
        self.tomode=["#chaos","+q-cunt"+"q"*len(unmo)+"o"*len(unmo),"xfnw"]+unmo+unmo
        await self.send(build("MODE",self.tomode))
            


