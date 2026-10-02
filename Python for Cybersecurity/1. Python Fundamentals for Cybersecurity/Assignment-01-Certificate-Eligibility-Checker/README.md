# Assignment 01 — Cybersecurity Awareness Certificate Eligibility Checker

First Python assignment of Module 2 — moving from Linux commands into actually writing code. This one's a simple eligibility checker: a training institute wants to hand out a Cybersecurity Awareness Certificate, but only to people who meet a minimum score and age requirement.

## The task

> A cybersecurity training institute issues a Cybersecurity Awareness Certificate only to candidates who meet the required criteria. Write a program that checks eligibility.

The rule I went with: a candidate is eligible if their score is **60 or above** and their age is **18 or above**. Both conditions have to be true — missing either one means no certificate.

## The code

```python
# 1. Get input from the user and convert to numbers
Score = int(input("Enter your score: "))
Age = int(input("Enter your age: "))

# 2. Check eligibility (your fixed logic)
if Score >= 60 and Age >= 18:
    print("Eligible for Certificate")
else:
    print("Not Eligible for Certificate")
```

## Walking through it

- **`int(input(...))`** — `input()` always gives back a string, even if the user types a number. Wrapping it in `int()` converts that string into an actual number so it can be compared with `>=` later. Skip the `int()` and Python would try to compare a string to a number and throw an error.
- **`and`** — both conditions need to be true at once. If someone scored 90 but is only 16, they still shouldn't get the certificate — that's exactly what `and` enforces here, instead of `or` which would let either condition alone pass them.
- **if / else** — pretty much the simplest form of a decision in code: one path if the condition holds, the other if it doesn't.

## Things I'd want to add later

This works for the basic case, but it's not really production-ready yet:

- No validation if someone types letters instead of numbers — right now that would just crash with an error
- No handling for negative numbers or unrealistic ages
- Score boundary could use a comment explaining *why* 60 was chosen as the cutoff (it was just the task's example number here)

## What I took away from this

- `input()` returning a string by default is one of those small things that trips people up early on — forgetting to convert it is a really common beginner mistake.
- Chaining a condition with `and` instead of writing nested if-statements keeps the logic a lot more readable for a case like this.
- Even a tiny script like this maps directly to a real use case — automated eligibility checks are everywhere (exam results, loan approvals, access control), and this is the same basic pattern underneath all of them.

## Wrapping up

Short one, but it's the right kind of "short" to start Module 2 with — getting comfortable with input handling, type conversion, and basic conditional logic before building anything more complex in Python.
