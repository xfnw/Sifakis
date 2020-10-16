#!/usr/bin/env python3


logchan = "#xfnwtest"


import asyncio, importlib

from irctokens import build, Line
from ircrobots import Bot as BaseBot
from ircrobots import Server as BaseServer
from ircrobots import ConnectionParams, SASLUserPass, SASLSCRAM

import filts, auth

SERVERS = [
    ("freenode", "chat.freenode.net"),
    ("tilde","irc.tilde.chat"),
]

class Server(BaseServer):
    async def line_read(self, line: Line):
        print(f"{self.name} < {line.format()}")
        if line.command == "001":
            self.lc = "#" *(self.name == "freenode") + logchan
            print(f"connected to {self.name}")
            await self.send(build("JOIN", [self.lc]))
        if line.command == "PRIVMSG":
            if 'batch' in line.tags and line.tags['batch'] == '1':
                return
            if line.params[1] == '!reload':
                importlib.reload(filts)
                await self.linelog('reloaded')#sifakis
            if line.params[1][0:9] == "Sifakis: " and line.tags and 'account' in line.tags and line.tags['account'] == 'lickthecheese':
                await self.send_raw(line.params[1][9:])
        if line.command == "INVITE":
            await self.send(build("JOIN",[line.params[1]]))
        
        asyncio.create_task(filts.line_read(self,line))
    async def line_send(self, line: Line):
        print(f"{self.name} > {line.format()}")
    async def linelog(self,string):
        await self.send(build("NOTICE",[self.lc,string]))



class Bot(BaseBot):
    def create_server(self, name: str):
        return Server(self, name)

async def main():
    bot = Bot()
    for name, host in SERVERS:
        sasl_params = SASLUserPass("Sifakis", auth.password)
        params = ConnectionParams("Sifakis", host, 6697, True, sasl = sasl_params)
        await bot.add_server(name, params)

    await bot.run()

if __name__ == "__main__":
    asyncio.run(main())
