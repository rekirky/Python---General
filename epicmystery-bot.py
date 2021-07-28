#Create a welcome image using PIL

@bot.event
async def on_member_join(member):
    guild = bot.get_guild(752763308964315167)
    channel = guild.get_channel(789465897076523068)
    welcome = Image.open(Path(__file__).parent / 'welcome.png').convert("RGB")
    asset = member.avatar_url_as(size = 2048)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize ((1280, 1280))

    pfp.save('pfp_saved.png')

    pfp_saved = Image.open('pfp_saved.png').convert("RGBA")

    def make_circular(im):
        mask = Image.new('L', im.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + im.size, fill=255)

        out = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
        out.putalpha(mask)
        return out

    if __name__ == '__main__':
        with Image.open("pfp_saved.png") as im:
            im = im.convert('RGBA')
            circular_im = make_circular(im)
            circular_im.save('pfp_round.png')

        pfp_round = Image.open('pfp_round.png').convert("RGBA")
        welcome.paste(pfp_round, (1350,500))
        welcome.save("welcome_user.png")

        img = Image.open("welcome_user.png").convert('RGB')

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arialbd.ttf", 200)
        font2= ImageFont.truetype("arialbd.ttf", 175)
        str1=('Welcome to ΞPIC MYSTΞRY YT')
        str2=('Very EPIC to have you in our Server!!')

        draw.text((700, 130 + 2), str1, font = font, fill = (50,50,50))
        draw.text((700, 130), str1, font = font, fill = (255,255,255))

        draw.text((500, 1900 + 2), str2, font = font2, fill = (50,50,50))
        draw.text((500, 1900), str2, font = font2, fill = (255,255,255))

        img.save("welcome_user2.png")
        await channel.send(file= discord.File('welcome_user2.png'))