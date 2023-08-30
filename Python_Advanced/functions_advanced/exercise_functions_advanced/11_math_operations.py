from collections import deque


def math_operations(*args, **kwargs):
    nums = deque(args)

    while nums:
        kwargs["a"] += nums.popleft()
        if not nums:
            break

        kwargs["s"] -= nums.popleft()
        if not nums:
            break

        divisor = nums.popleft()
        if divisor != 0:
            kwargs["d"] /= divisor
        if not nums:
            break

        kwargs["m"] *= nums.popleft()
    return kwargs

# from collections import deque
#
#
# def math_operations(*args, **kwargs):
#     numbers = deque(args)
#     while numbers:
#         if numbers:
#             kwargs['a'] += numbers.popleft()
#         if numbers:
#             kwargs['s'] -= numbers.popleft()
#         if numbers:
#             divisor = numbers.popleft()
#             if divisor > 0:
#                 kwargs['d'] /= divisor
#         if numbers:
#             kwargs['m'] *= numbers.popleft()
#
#     return '\n'.join([f"{k}: {v:.1f}" for k, v in sorted(kwargs.items(), key=lambda kvp: (-kvp[1], kvp[0]))])
#