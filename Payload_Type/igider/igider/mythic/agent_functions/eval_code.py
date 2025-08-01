from mythic_container.MythicCommandBase import *
from mythic_container.MythicRPC import *


class EvalArguments(TaskArguments):
    def __init__(self, command_line, **kwargs):
        super().__init__(command_line, **kwargs)
        self.args = [
            CommandParameter(
                name="command",
                type=ParameterType.String,
                description="Command to evaluate in Python interpreter",
            )
        ]

    async def parse_arguments(self):
        if len(self.command_line) > 0:
            self.add_arg("command", self.command_line)
        
    async def parse_dictionary(self, dictionary_arguments):
        self.load_args_from_dictionary(dictionary_arguments)


class EvalCommand(CommandBase):
    cmd = "eval_code"
    needs_admin = False
    help_cmd = "eval_code python-code"
    description = "Evaluate python code in interpreter"
    version = 1
    attackmapping = []
    argument_class = EvalArguments
    attributes = CommandAttributes(
        supported_os=[SupportedOS.MacOS, SupportedOS.Windows, SupportedOS.Linux ],
    )

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        task.display_params = task.args.get_arg("command")
        return task

    async def process_response(self, task: PTTaskMessageAllData, response: any) -> PTTaskProcessResponseMessageResponse:
        resp = PTTaskProcessResponseMessageResponse(TaskID=task.Task.ID, Success=True)
        return resp
