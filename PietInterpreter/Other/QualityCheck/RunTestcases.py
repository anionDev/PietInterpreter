import sys
from pathlib import Path
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure


def run_testcases():
    TasksForCommonProjectStructure().standardized_tasks_run_testcases_for_python_codeunit(str(Path(__file__).absolute()), True, 1, "QualityCheck", sys.argv)


if __name__ == "__main__":
    run_testcases()
