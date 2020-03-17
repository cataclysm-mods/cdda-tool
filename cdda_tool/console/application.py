from cleo import Application as BaseApplication

from cdda_tool import __version__

from .commands.about import AboutCommand


class Application(BaseApplication):
    def __init__(self):
        super(Application, self).__init__("cdda-tool", __version__)

        for command in self.get_default_commands():
            self.add(command)

    def get_default_commands(self):
        commands = [
            AboutCommand(),
        ]

        return commands


if __name__ == "__main__":
    Application().run()
