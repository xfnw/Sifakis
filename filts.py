
import asyncio

from irctokens import build, Line


async def line_read(self,line):
    # line tags command params source
    if line.command == "JOIN":
        await on_join(self,line)


async def on_join(self,line):
    reason = []
    user = self.users[line.source.split('!')[0].lower()]


    if not user.account:
        reason.append('NO_NS_ACCOUNT')
    else:
        account = user.account

        if self.name != 'freenode':
            reason += [f'NS_ACCOUNT ({ac})' for ac in ['lickthecheese'] if ac == account]
        
    host = line.source.split('@')[1]
    reason += [f'BAD_HOST ({host})' for ac in ['hot-chilli'] if ac in host]

    if len(reason) > 0:
        await self.linelog(f'{line.source} caught in {line.params[0]} because of {", ".join(reason)}')





