"""Helpers for account handling."""


def work_out_account_figure(values):
    """Mean of the numbers in values, ignoring None; 0.0 when there are none."""
    nums = [v for v in values if v is not None]
    if not nums:
        return 0.0
    return sum(nums) / len(nums)


def label_account(value):
    return f"account:{value}"
