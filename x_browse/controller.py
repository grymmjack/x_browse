import os

from .utils import log, log_types

from .model import BrowseModel
from .view import BrowseView


class BrowseController:
    def __init__(self):
        pass

    def run(self):
        """Runs the controller
        Walks the contents of the model data and sets up the shortcuts and
        passes the heavy lifting to the dir_link func to do the work.

        Args:
            None

        Returns:
            (bool): True if controller runs successfully, False otherwise
        """
        i = 0
        model = BrowseModel()
        for src_dir, dst_dir in model.data.items():
            i += 1
            dir_linked = self.dir_link(
                f"{i:03} {src_dir}",
                f"E:{os.sep}Music{os.sep}{dst_dir}"
            )
            if not dir_linked:
                # Something didn't work
                # return False
                pass
        
        # Everything worked
        return True

    @staticmethod
    def dir_link(src_dir, dst_dir):
        """Create a link to a directory using `mklink`
            Uses directory symbolic link method (/D)
        Args:
            src_dir (str): The directory to link to dest_dir
            dst_dir (str): The directory in which to create the link in
        Returns:
            (bool): True if directory link made successfully, False otherwise
        """
        try:
            log(f"Creating symlink: {src_dir} [red]:right_arrow:[/] {dst_dir}", log_types.NOTICE)
            os.symlink(dst_dir, src_dir, target_is_directory=True)
        except:
            return False
        return True
