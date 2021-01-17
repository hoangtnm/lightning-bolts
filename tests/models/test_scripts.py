from unittest import mock

import pytest
import torch

from tests import DATASETS_PATH


@pytest.mark.parametrize(
    'cli_args', [
        f'--dataset mnist --data_dir {DATASETS_PATH} --max_epochs 1'
        ' --batch_size 2 --limit_train_batches 2 --limit_val_batches 2',
        f'--dataset cifar10 --data_dir {DATASETS_PATH} --max_epochs 1'
        ' --batch_size 2 --limit_train_batches 2 --limit_val_batches 2',
    ]
)
def test_cli_run_basic_gan(cli_args):
    from pl_bolts.models.gans.basic.basic_gan_module import cli_main

    with mock.patch("argparse._sys.argv", ["any.py"] + cli_args.strip().split()):
        cli_main()


@pytest.mark.parametrize(
    "cli_args",
    [
        f"--dataset mnist --scale_factor 4 --data_dir {DATASETS_PATH} --max_epochs 1"
        " --batch_size 2 --limit_train_batches 2 --limit_val_batches 2"
    ],
)
def test_cli_run_srgan(cli_args):
    from pl_bolts.models.gans.srgan.srgan_module import cli_main

    with mock.patch("argparse._sys.argv", ["any.py"] + cli_args.strip().split()):
        cli_main()


@pytest.mark.parametrize(
    "cli_args",
    [
        f"--dataset mnist --data_dir {DATASETS_PATH} --max_epochs 1"
        " --batch_size 2 --limit_train_batches 2 --limit_val_batches 2"
    ],
)
def test_cli_run_srresnet(cli_args):
    from pl_bolts.models.gans.srgan.srresnet_module import cli_main

    with mock.patch("argparse._sys.argv", ["any.py"] + cli_args.strip().split()):
        cli_main()


# TODO: this test is hanging (runs for more then 10min) so we need to use GPU or optimize it...
@pytest.mark.skipif(not torch.cuda.is_available(), reason="test requires GPU machine")
@pytest.mark.parametrize(
    'cli_args', [
        f'--data_dir {DATASETS_PATH} --max_epochs 1  --limit_train_batches 2'
        ' --limit_val_batches 2 --batch_size 2 --encoder resnet18',
    ]
)
def test_cli_run_cpc(cli_args):
    from pl_bolts.models.self_supervised.cpc.cpc_module import cli_main

    cli_args = cli_args.split(' ') if cli_args else []
    with mock.patch("argparse._sys.argv", ["any.py"] + cli_args):
        cli_main()


@pytest.mark.parametrize('cli_args', [f'--data_dir {DATASETS_PATH} --max_epochs 1 --max_steps 2'])
def test_cli_run_mnist(cli_args):
    """Test running CLI for an example with default params."""
    from pl_bolts.models.mnist_module import cli_main

    cli_args = cli_args.split(' ') if cli_args else []
    with mock.patch("argparse._sys.argv", ["any.py"] + cli_args):
        cli_main()


@pytest.mark.parametrize(
    'cli_args', [
        f'--dataset cifar10 --data_dir {DATASETS_PATH} --max_epochs 1 --batch_size 2 --fast_dev_run 1',
    ]
)
def test_cli_run_basic_ae(cli_args):
    """Test running CLI for an example with default params."""
    from pl_bolts.models.autoencoders.basic_ae.basic_ae_module import cli_main

    cli_args = cli_args.split(' ') if cli_args else []
    with mock.patch("argparse._sys.argv", ["any.py"] + cli_args):
        cli_main()


@pytest.mark.parametrize(
    'cli_args', [
        f'--dataset cifar10 --data_dir {DATASETS_PATH} --max_epochs 1 --batch_size 2 --fast_dev_run 1',
    ]
)
def test_cli_run_basic_vae(cli_args):
    """Test running CLI for an example with default params."""
    from pl_bolts.models.autoencoders.basic_vae.basic_vae_module import cli_main

    cli_args = cli_args.split(' ') if cli_args else []
    with mock.patch("argparse._sys.argv", ["any.py"] + cli_args):
        cli_main()


@pytest.mark.parametrize('cli_args', ['--max_epochs 1 --max_steps 2'])
def test_cli_run_lin_regression(cli_args):
    """Test running CLI for an example with default params."""
    from pl_bolts.models.regression.linear_regression import cli_main

    cli_args = cli_args.split(' ') if cli_args else []
    with mock.patch("argparse._sys.argv", ["any.py"] + cli_args):
        cli_main()


@pytest.mark.parametrize('cli_args', ['--max_epochs 1 --max_steps 2'])
def test_cli_run_log_regression(cli_args):
    """Test running CLI for an example with default params."""
    from pl_bolts.models.regression.logistic_regression import cli_main

    cli_args = cli_args.split(' ') if cli_args else []
    with mock.patch("argparse._sys.argv", ["any.py"] + cli_args):
        cli_main()


# TODO: this test is hanging (runs for more then 10min) so we need to use GPU or optimize it...
@pytest.mark.skipif(not torch.cuda.is_available(), reason="test requires GPU machine")
@pytest.mark.parametrize('cli_args', [f'--data_dir {DATASETS_PATH} --max_epochs 1 --max_steps 2'])
def test_cli_run_vision_image_gpt(cli_args):
    """Test running CLI for an example with default params."""
    from pl_bolts.models.vision.image_gpt.igpt_module import cli_main

    cli_args = cli_args.split(' ') if cli_args else []
    with mock.patch("argparse._sys.argv", ["any.py"] + cli_args):
        cli_main()
