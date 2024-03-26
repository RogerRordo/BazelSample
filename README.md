# Bazel Example Repo

- Bazel 4.0.0
- Protobuf 21.4
- Python 3.8
  - Linter: Ruff
  - Formatter: Ruff

## Generate `*_pb2.pyi` files for code completion

```
./scripts/gen_pb.sh
```

## Update pip packages

Edit `third_party/requirements.txt`, then run

```
bazel run //third_party:python_requirements.update
```

## Run UTs

```
bazel test //py:divide_utils_test
bazel test //...
```

## Run `example_main`

```
bazel run //py:example_main -- --baz_a=5 --baz_b=2
```
