from mythic_container.MythicCommandBase import *
from mythic_container.MythicRPC import *


class PsArguments(TaskArguments):
    def __init__(self, command_line, **kwargs):
        super().__init__(command_line, **kwargs)
        self.args = []

    async def parse_arguments(self):
        pass


class PsCommand(CommandBase):
    cmd = "ps"
    needs_admin = False
    help_cmd = "ps"
    description = "Get limited process listing"
    version = 2
    attackmapping = ["T1106"]
    supported_ui_features = ["process_browser:list"]
    argument_class = PsArguments
    browser_script = BrowserScript(script_name="ps",for_new_ui=True)
    attributes = CommandAttributes(
        supported_python_versions=["Python 3.8" ],
        supported_os=[ SupportedOS.Windows],
    )

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        task.display_params = "Getting limited process listing"
        return task

    async def process_response(self, task: PTTaskMessageAllData, response: any) -> PTTaskProcessResponseMessageResponse:
        resp = PTTaskProcessResponseMessageResponse(TaskID=task.Task.ID, Success=True)
        return resp
