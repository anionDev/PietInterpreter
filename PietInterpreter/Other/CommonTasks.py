import sys
import os
from pathlib import Path
from ScriptCollection.GeneralUtilities import GeneralUtilities
from ScriptCollection.ScriptCollectionCore import ScriptCollectionCore
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure


def common_tasks():
    file = str(Path(__file__).absolute())
    folder_of_current_file = os.path.dirname(file)
    sc = ScriptCollectionCore()
    cmd_args = sys.argv
    t = TasksForCommonProjectStructure()
    codeunitname = os.path.basename(GeneralUtilities.resolve_relative_path("..", os.path.dirname(file)))
    verbosity = t.get_verbosity_from_commandline_arguments(cmd_args, 1)
    targetenvironmenttype = t.get_targetenvironmenttype_from_commandline_arguments(cmd_args, "QualityCheck")
    additional_arguments_file = t.get_additionalargumentsfile_from_commandline_arguments(cmd_args, None)
    codeunit_version = sc.get_semver_version_from_gitversion(GeneralUtilities.resolve_relative_path(
        "../..", os.path.dirname(file)))  # Should always be the same as the project-version
    sc.replace_version_in_ini_file(GeneralUtilities.resolve_relative_path("../setup.cfg", folder_of_current_file), codeunit_version)
    sc.replace_version_in_python_file(GeneralUtilities.resolve_relative_path(f"../{codeunitname}/{codeunitname}Core.py", folder_of_current_file), codeunit_version)
    t.standardized_tasks_do_common_tasks(file, codeunit_version, verbosity, targetenvironmenttype, True, additional_arguments_file, False, cmd_args)


if __name__ == "__main__":
    common_tasks()
