import pytest
from wallet import Wallet, InsufficientAmount


# def test_default_initial_amount():
#     wallet = Wallet()
#     assert wallet.balance == 0
#
# def test_setting_initial_amount():
#     wallet = Wallet(100)
#     assert wallet.balance == 100
#
# def test_wallet_add_cash():
#     wallet = Wallet(10)
#     wallet.add_cash(90)
#     assert wallet.balance == 100
#
# def test_wallet_spend_cash():
#     wallet = Wallet(20)
#     wallet.spend_cash(10)
#     assert wallet.balance == 1
#
# def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
#     wallet = Wallet()
#     with pytest.raises(InsufficientAmount):
#         wallet.spend_cash(100)


###################################################################### Fixtures


# @pytest.fixture
# def empty_wallet():
#     '''Returns a Wallet instance with a zero balance'''
#     return Wallet()
#
# @pytest.fixture
# def wallet():
#     '''Returns a Wallet instance with a balance of 20'''
#     return Wallet(20)
#
# def test_default_initial_amount(empty_wallet):
#     assert empty_wallet.balance == 0
#
# def test_setting_initial_amount(wallet):
#     assert wallet.balance == 20
#
# def test_wallet_add_cash(wallet):
#     wallet.add_cash(80)
#     assert wallet.balance == 100
#
# def test_wallet_spend_cash(wallet):
#     wallet.spend_cash(10)
#     assert wallet.balance == 10
#
# def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
#     with pytest.raises(InsufficientAmount):
#         empty_wallet.spend_cash(100)

#################################################################### Parameterization


@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()


@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a balance of 20'''
    return Wallet(20)


def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0


def test_setting_initial_amount(wallet):
    assert wallet.balance == 20


def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance == 100


def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10


def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)


@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2.500, 17.500),
])
def test_transactions(empty_wallet, earned, spent, expected):
    empty_wallet.add_cash(earned)
    empty_wallet.spend_cash(spent)
    assert empty_wallet.balance == expected


@pytest.mark.parametrize("earned,spent", [
    (30, 40),
    (20, 100),
])
def test_transactions_insufficient_amounts(empty_wallet, earned, spent):
    empty_wallet.add_cash(earned)

    with pytest.raises(Exception):
        empty_wallet.spend_cash(spent)

