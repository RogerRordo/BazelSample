# Copyright 2024 the bazel_example project authors. All rights reserved.
# Authors: luozhuofeng@gmail.com (Zhuofeng Luo)
import logging

import click

from proto.example_pb2 import Foo
from py.divide_utils import integer_division


def setup_logging(logging_level=logging.INFO):
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter('%(asctime)s [%(filename)s:%(lineno)d] [%(levelname)s] %(message)s')
    )
    logger.addHandler(handler)
    logger.setLevel(logging_level)


@click.command()
@click.option(
    '--baz_a',
    type=int,
    default=3,
    help='This is baz_a.',
)
@click.option(
    '--baz_b',
    type=int,
    default=2,
    help='This is baz_b.',
)
def main(baz_a: int, baz_b: int):
    foo = Foo()
    foo.bar.baz_a = baz_a
    foo.bar.baz_b = baz_b
    logging.info('foo: {}'.format(foo))
    logging.info('integer_division(baz_a, baz_b): {}'.format(integer_division(baz_a, baz_b)))


if __name__ == '__main__':
    setup_logging(logging.INFO)
    main()
