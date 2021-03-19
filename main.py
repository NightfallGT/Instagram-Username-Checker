import asyncio
import aiohttp
from typing import List
from os import system

def open_file() -> List[str]:
    with open('usernames.txt', 'r', encoding='UTF-8') as f:
        file_contents = [line.strip('\n') for line in f]

    return file_contents

def write_file(arg: str) -> None:
    with open('hits.txt', 'a', encoding='UTF-8') as f:
        f.write(f'{arg}\n')

class Checker:
    HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
    def __init__(self, usernames: List[str]):
        self.to_check = usernames
        #self.count = 0

    async def _check(self, session: aiohttp.ClientSession, username: str) -> None:     
        async with session.get('https://www.instagram.com/%s' % username) as response:
            try:
                r = await response.text()

                if response.status == 404:
                    print('%s[AVAILABLE] https://www.instagram.com/%s%s' % ('\u001b[32;1m', username, '\u001b[0m'))
                    write_file(username)

                elif response.status == 200 and 'Login • Instagram' in r:
                    print('[!] Failed to check username. Try again later', username)
                    # if self.count == 50:
                    #     print(r)
                else:
                    print('%s[UNAVAILABLE] https://www.instagram.com/%s%s' % ('\u001b[31;1m', username, '\u001b[0m'))

                #self.count += 1
                #print(r)
                #print(response.status)
            except Exception as e:
                print('[ERROR] ' + e)                    
                    
    async def start(self):
        tasks = []
        async with aiohttp.ClientSession(headers=self.HEADERS) as session:
            for i in self.to_check:
                print('[*] Appending.. :', i)
                tasks.append(asyncio.create_task(self._check(session, i)))
            system('cls')
            print('Loading.. This may take awhile.')
            task = await asyncio.gather(*tasks)
            return task

if __name__ == '__main__':
    system('title Instagram Username Checker by NightfallGT')
    system('cls')
    username_list = open_file() 
    checker = Checker(username_list)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(checker.start())
