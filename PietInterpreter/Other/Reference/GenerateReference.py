import sys
from pathlib import Path
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure


def generate_reference():
    TasksForCommonProjectStructure().standardized_tasks_generate_reference_by_docfx(str(Path(__file__).absolute()), 1, "QualityCheck", sys.argv)


if __name__ == "__main__":
    generate_reference()
