import pytest


def test_user_str(base_user):
    """Test the custom user model string representation"""
    assert base_user.__str__() == f'{base_user.username}'


def test_user_short_name(base_user):
    """Test that the user models get_short_name method works"""
    short_name = f'{base_user.username}'
    assert base_user.get_short_name() == short_name


def test_user_full_name(base_user):
    """Test that the user models get_full_name method works"""
    full_name = f'{base_user.first_name} {base_user.last_name}'
    assert base_user.get_full_name() == full_name
