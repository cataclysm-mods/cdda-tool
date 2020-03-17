from .command import Command


class AboutCommand(Command):
    name = "about"
    description = "Shows information about cdda-tool."

    def handle(self):
        self.line(
            """<info>CDDA Tool</info>
<comment>cdda-tool is a tool for interacting with JSON data consumed by the game Cataclysm: Dark Days Ahead.
See <fg=blue>https://github.com/cdda-mods/cdda-tool</> for more information.</comment>"""
        )
