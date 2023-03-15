import asyncio
import disnake
from disnake.ext import commands
from pyppeteer import launch
from pyppeteer_stealth import stealth


class PixelBot(commands.Bot):
    def __init__(self):
        intents = disnake.Intents.default().all()
        super().__init__(command_prefix=" ", intents=intents)
        @self.slash_command(name="putpixel",
                       description="Add a pixel to the canvas with the given coordinates and color index",
                       options=[
                           disnake.Option(
                               "x",
                               "The x-coordinate of the pixel",
                               type=disnake.OptionType.integer,
                               required=True
                           ),
                           disnake.Option(
                               "y",
                               "The y-coordinate of the pixel",
                               type=disnake.OptionType.integer,
                               required=True
                           ),
                           disnake.Option(
                               "colorindex",
                               "The index of the color to use",
                               type=disnake.OptionType.integer,
                               required=True
                           )
                       ])
        async def put_pixel(inter, x: int, y: int, colorindex: int):
            await inter.response.defer()
            headers = {
                "Content-Type": "application/json",
                "Authorization": "token",
                "Channel-ID": "822911019",
            }
            data = [x, y, colorindex]
            browser = await launch()
            page = await browser.newPage()
            await stealth(page)
            await page.goto("https://place.streamkit.com/putPixel", {"waitUntil": "networkidle0"})           
            await browser.close()
            await inter.response.send_message()
            pass
            # Will finish when I will find out how to send pixels

            
if __name__ == "__main__":
    bot = PixelBot()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.start("TOKEN OKAY"))
