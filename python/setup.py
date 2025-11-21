from setuptools import setup, find_packages

setup(
    name="task-tracker",
    version="0.1.0",
    description="A simple task tracker application made in python for roadmap.sh",
    author="Davi Vitorino",
    package_dir={"":"src"},
    packages=find_packages(where="src"),
    python_requires=">=3.12.2",
    py_modules=["main", "taskTrackerFuncs"],
    entry_points={
        "console_scripts": [
            "task-tracker=main:main"
        ],
    },
    data_files=[
        ("", ["./src/tasks.json"]),
    ],
)