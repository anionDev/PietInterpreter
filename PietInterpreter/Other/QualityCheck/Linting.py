import sys
from pathlib import Path
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure


def linting():
    TasksForCommonProjectStructure().standardized_tasks_linting_for_python_codeunit(str(Path(__file__).absolute()), 1,  "QualityCheck", sys.argv)


if __name__ == "__main__":
    linting()
