package(default_visibility = ["//visibility:public"])

load("@rules_python//python:pip.bzl", "compile_pip_requirements")

compile_pip_requirements(
    name = "python_requirements",
    extra_args = ["--allow-unsafe"],
    requirements_in = ":requirements.txt",
    requirements_txt = ":requirements_lock.txt",
    tags = ["manual"],
)

exports_files([
    "requirements.txt",
    "requirements_lock.txt",
])
