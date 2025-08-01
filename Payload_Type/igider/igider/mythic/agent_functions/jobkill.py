from mythic_container.MythicCommandBase import *
from mythic_container.MythicRPC import *


class JobKillArguments(TaskArguments):
    def __init__(self, command_line, **kwargs):
        super().__init__(command_line, **kwargs)
        self.args = [
            CommandParameter(
                name="target_task_id",
                type=ParameterType.String,
                description="Stop a long-running job",
            )
        ]

    async def parse_arguments(self):
        if len(self.command_line) > 0:
            if self.command_line[0] == "{":
                self.load_args_from_json_string(self.command_line)
            else:
                self.add_arg("target_task_id", self.command_line)
        else:
            raise ValueError("Missing arguments")

class JobKillCommand(CommandBase):
    cmd = "jobkill"
    needs_admin = False
    help_cmd = "jobkill {task_id}"
    description = "Sends a stop signal to a long-running job"
    version = 1
    attackmapping = []
    argument_class = JobKillArguments
    attributes = CommandAttributes(
        supported_os=[SupportedOS.MacOS, SupportedOS.Windows, SupportedOS.Linux ],
    )

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        task.display_params = "Sending stop signal for task with id: " + task.args.get_arg("target_task_id")
        return task

    async def process_response(self, task: PTTaskMessageAllData, response: any) -> PTTaskProcessResponseMessageResponse:
        resp = PTTaskProcessResponseMessageResponse(TaskID=task.Task.ID, Success=True)
        return resp
