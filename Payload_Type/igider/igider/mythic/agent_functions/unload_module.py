from mythic_container.MythicCommandBase import *
from mythic_container.MythicRPC import *

class UnloadModuleArguments(TaskArguments):
    def __init__(self, command_line, **kwargs):
        super().__init__(command_line, **kwargs)
        self.args = [
            CommandParameter(
                name="module_name",
                type=ParameterType.String,
                description="Name of module to load, e.g. cryptography"
            )
        ]

    async def parse_arguments(self):
        if len(self.command_line) > 0:
            if self.command_line[0] == "{":
                self.load_args_from_json_string(self.command_line)
            else:
                self.add_arg("module_name", self.command_line)
        else:
            raise ValueError("Missing arguments")


class UnloadModuleCommand(CommandBase):
    cmd = "unload_module"
    needs_admin = False
    help_cmd = "unload_module [module]"
    description = (
        "Unload an in-memory Python module from the agent"
    )
    version = 1
    attackmapping = []
    argument_class = UnloadModuleArguments
    attributes = CommandAttributes(
        supported_python_versions=["Python 3.8"],
        supported_os=[SupportedOS.MacOS, SupportedOS.Windows, SupportedOS.Linux ],
    )


    async def create_tasking(self, task: MythicTask) -> MythicTask:        
        task.display_params = f"Unloading {task.args.get_arg('module_name')} module"
        return task

    async def process_response(self, task: PTTaskMessageAllData, response: any) -> PTTaskProcessResponseMessageResponse:
        resp = PTTaskProcessResponseMessageResponse(TaskID=task.Task.ID, Success=True)
        return resp
