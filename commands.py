class serverView(miru.View):
    @miru.button(emoji='⬇', style=hikari.ButtonStyle.PRIMARY)
    async def button_server(self, button: miru.Button, ctx: miru.Context):
        serverList = get_server()
        response = '```'
        response += '|All Online Servers:\n'
        response += '|------------------------------|\n'
        response += '| Server       |       Players |\n'
        for server in serverList.items():
            world_ID = server[0]
            player_count = server[1]
            if player_count >= 50:
                response += '| {0:12s} | {1:10d}/50 | [FULL]\n'.format(world_ID, player_count)
            else:
                response += '| {0:12s} | {1:10d}/50 |\n'.format(world_ID, player_count)
        response += '|------------------------------|\n'
        response += '|Full worlds need champion rank|\n'
        response += '```'
        await ctx.edit_response(response)


@bot.command
@lightbulb.command('wc', 'List of online servers')
@lightbulb.implements(lightbulb.SlashCommand)
async def server_list(ctx):
    view = serverView(timeout=60)
    serverList = get_server()
    index = 0
    show_servers = 10
    response = '```'
    response += '|Online Servers:\n'
    response += '|------------------------------|\n'
    response += '| Server       |       Players |\n'
    for server in serverList.items():
        if index <= show_servers:
            world_ID = server[0]
            player_count = server[1]
            if player_count >= 50:
                response += '| {0:12s} | {1:10d}/50 | [FULL]\n'.format(world_ID, player_count)
                index += 1
            else:
                response += '| {0:12s} | {1:10d}/50 |\n'.format(world_ID, player_count)
                index += 1
    response += '|------------------------------|\n'
    response += '|Click for Full list of servers|\n'
    response += '```'
    display = await ctx.respond(f'{response}', components=view.build())
    display = await display
    view.start(display)
    await view.wait()
