import os

from .model import BrowseModel
from .view import BrowseView


class BrowseController:
    def __init__(self):
        pass

    def run(self):
        i = 0
        model = BrowseModel()
        for src_dir, dst_dir in model.data.items():
            i += 1
            dir_linked = self.dirlink(
                f"'{os.getcwd()}{os.sep}{i:03} {src_dir}'",
                f"'E:{os.sep}Music{os.sep}{dst_dir}'"
            )

    @staticmethod
    def dirlink(src_dir, dst_dir):
        """Create a link to a directory using `mklink`
            Uses directory symbolic link method (/D)
        Args:
            src_dir (str): The directory to link to dest_dir
            dst_dir (str): The directory in which to create the link in
        Returns:
            (bool): True if directory link made successfully, False otherwise
        """
        # TODO: make a loop
        import subprocess
        cmds = [
            "mklink",
            "/D",
            src_dir,
            dst_dir
        ]
        print(" ".join(cmds).replace("'", '"'))
        # subprocess.run(cmds)
