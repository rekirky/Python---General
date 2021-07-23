@bot.event
async def on_message(msg):
    if msg.author.bot: 
        return 
    username = msg.author.name
    general_channel = bot.get_channel(867594154937679872) 
    int (formatted_time)
    formatted_time =  msg.created_at.strftime("%H:%M")
    if msg.content.startswith('/present' ) and formatted_time > datetime.datetime.strptime("11:30", "%H:%M") < datetime.datetime.strptime("10:30", "%H:%M"):
        await msg.channel.send(f"{username} You said present at the correct time!") and await msg.general_channel.send(f"{username} said present at {formatted_time}")
    else:
        await msg.channel.send(f"wrong time")