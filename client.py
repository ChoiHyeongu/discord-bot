#-*- coding:utf-8 -*-
import discord
import asyncio
import action
import command as Command
import config as Config
import constant as Constant

class Client(discord.Client):
    action = action.Action()

    # 준비가 되면 로그를 찍음
    async def on_ready(self):
        print('Logged on as', self.user)

    # Message가 입력됐을 때
    async def on_message(self, message):
        if self.check_author_is_user(message.author):
           return

        else:
            send_message = self.check_command(message)

        await message.channel.send(send_message)

    # Author과 봇이 같은지 확인
    def check_author_is_user(self, author):
        return author == self.user
            
    # 커맨드 확인하기
    def check_command(self, message):
        if message.content.startswith(Config.PREFIX_CHAR):
            return self.action.match_action(message.content) 
        elif message.content == Command.AGGRO.value:
            return self.action.aggro()