GUILDS = []
from basecord import Cog
from nextcord import Interaction
from nextcord import slash_command

class base(Cog):
    def __init__(self, bc):
        super().__init__(bc)
    
    def id_check(self, user, id):
        if user["id"] == id:
            return True
        return False

    @slash_command(name="ping", description="pong!", guild_ids=GUILDS)
    async def ping(self, inter: Interaction):
        await inter.response.send_message(f"pong! {str(self.bc.latency)[:4]}s latency")
        userdb = self.db.find("users", self.id_check, inter.user.id)
        if not userdb:
            userdb = {"id": inter.user.id, "usage": 0}
            self.db.push("users", userdb)
        self.db.pop("users", userdb)
        userdb["usage"] += 1
        self.db.push("users", userdb)
