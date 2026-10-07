# Assignment 02 — Sum of Numbers from 1 to n

Second Python assignment — a classic beginner exercise, using a `for` loop and `range()` to add up a sequence of numbers.

## The task

> Write a program to calculate the sum of event counts from 1 to n.

(I'm reading "event counts" as just meaning "numbers" here — the code below sums every number from 1 up to whatever `n` the user enters.)

## The code

```python
# Get the value of n from the user
n = int(input("Enter a number: "))

total = 0
for i in range(1, n + 1):
    total += i

print(total)
```

## Walking through it

- **`n = int(input(...))`** — same pattern as Assignment 1, converting the text input into an actual number so it can be used in `range()`.
- **`total = 0`** — a running total, started at zero before the loop begins.
- **`for i in range(1, n + 1):`** — `range(1, n+1)` counts from 1 up to and including `n`. It's easy to forget the `+1` here, since `range(1, n)` would stop one short and leave out `n` itself.
- **`total += i`** — shorthand for `total = total + i`. Each pass through the loop adds the current number onto the running total.
- **`print(total)`** — once the loop finishes, prints the final sum.

For `n = 10`, this adds up `1 + 2 + 3 + ... + 10` and prints `55`.

## A note on the task wording

The comment in the task says "sum of **even** counts," but what the code actually does is sum *every* number from 1 to n — not just the even ones. If the goal really was "only even numbers," the fix would be small — either add a check inside the loop (`if i % 2 == 0:`) before adding to `total`, or step through only even numbers directly with `range(2, n + 1, 2)`. I'm keeping the code as it was written rather than silently changing what it does, but it's worth being upfront that there's a mismatch between the task description and what this version actually calculates.

## What I took away from this

- `range(1, n + 1)` vs `range(1, n)` is a classic off-by-one trap — worth double-checking any time a loop needs to *include* the upper bound.
- `total += i` is the standard pattern for accumulating a running total inside a loop — I'll be using this a lot going forward.
- Reading the task description carefully matters just as much as writing the code — this one was a good reminder to check that what the code *does* actually matches what was *asked for*.

## Wrapping up

Simple loop exercise, but a good one to actually sit with — `for` + `range()` + a running total is a pattern that shows up constantly, whether it's summing numbers, counting matches in a list, or processing log entries later on.
