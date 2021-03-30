import torch
import random
import logging
import argparse
import numpy as np

logger = logging.getLogger(__name__)


def set_args() -> argparse:
    parser = argparse.ArgumentParser()

    # model hyperparameters
    parser.add_argument('--img_emb_dim', type=int, default=128)
    parser.add_argument('--img_hid_dim', type=int, default=384)
    parser.add_argument('--dropout', type=int, default=0.1)
    parser.add_argument('--max_len', type=int, default=512)
    parser.add_argument('--batch_size', type=int, default=16)
    parser.add_argument('--epochs', type=int, default=100)
    parser.add_argument('--seed', type=int, default=1234)
    parser.add_argument('--lr', type=float, default=0.00001)
    parser.add_argument('--warmup_step', type=float, default=0.1)

    # type of processing
    parser.add_argument('--train_', type=str, default='True')
    parser.add_argument('--test_', type=str, default='True')
    parser.add_argument('--eval', type=str, default='True')
    parser.add_argument('--only_text_input', type=str, default='False')

    # fp16
    parser.add_argument('--opt_level', type=str, default='O1')
    parser.add_argument('--fp16', type=str, default='False')

    # Data loader parser
    parser.add_argument('--train_data', type=str, default='train.tsv')
    parser.add_argument('--test_data', type=str, default='test.tsv')
    parser.add_argument('--valid_data', type=str, default='val.tsv')

    parser.add_argument('--path_to_data', type=str, default='./data/DramaQA_v2.1/AnotherMissOh/')
    parser.add_argument('--path_to_image', type=str, default='./data/DramaQA_v2.1/AnotherMissOh/AnotherMissOh_images/AnotherMissOh')
    parser.add_argument('--path_to_save', type=str, default='./output')
    parser.add_argument('--path_to_saved_model', type=str, default='./output/.pt')

    parser.add_argument('--device', type=str, default=torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu'))

    args = parser.parse_args()
    return args


def set_logger() -> logger:
    _logger = logging.getLogger()
    formatter = logging.Formatter(
        '[%(levelname)s] %(asctime)s [ %(message)s ] | file::%(filename)s | line::%(lineno)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    _logger.addHandler(stream_handler)
    _logger.setLevel(logging.DEBUG)
    return _logger


def set_seed(args):
    logger.info('Setting Seed')
    seed = args.seed
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    logger.info('Setting Seed Complete')


def print_args(args):
    logger.info('Args configuration')
    for idx, (key, value) in enumerate(args.__dict__.items()):
        if idx == 0 : print("argparse{\n", "\t", key, ":", value)
        elif idx == len(args.__dict__) - 1 : print("\t", key, ":", value, "\n}")
        else : print("\t", key, ":", value)