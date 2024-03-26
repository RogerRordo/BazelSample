package(default_visibility = ["//visibility:public"])

load("@python_deps//:requirements.bzl", "requirement")

py_library(
    name = "divide_utils",
    srcs = ["divide_utils.py"],
)

py_test(
    name = "divide_utils_test",
    srcs = ["divide_utils_test.py"],
    deps = [
        ":divide_utils",
    ],
)

py_binary(
    name = "example_main",
    srcs = ["example_main.py"],
    deps = [
        ":divide_utils",
        "//proto:py_example_proto",
        "@com_google_protobuf//:protobuf_python",
        requirement("click"),
    ],
)
