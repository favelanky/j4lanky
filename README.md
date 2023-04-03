# Speed up your Sherlock judging

## How to use?

1. Clone this repo.
2. Install dependencies with `pip install -r requirements.txt`.
3. Clone judging repo into the `/submissions` directory or wherever you want.
4. Change SUBMISSIONS_DIR in `.env` to the directory with cloned submissions.
5. Write suggestions in the `judgments.txt` file.
6. Run `python3 main.py`.
7. The results will be in the used directory sorted by `judgments.txt` file.
8. Commit and push changes to your judging repo.

## How to write suggestions?

### Example

```
H-1: oracle manipulation
1
23-best

H-2: comments
22

M-1: replay attack
002

M-002: comments
008
10
56-best

3-M: something else
09 comments...


Invalid-submissions:
1 idk
2
03
4 recheck
006 violate rules
```

### Format

- Choose from `H-1:`, `1-m:`, `002-M:` more convenient for you to specify the severity and number of submissions. **Always use `-` and `:` in these lines.**
- Use `Invalid-submissions:` to specify invalid submissions.
- After the line with severity, all lines with numbers of submissions will be considered as suggestions for this severity. You can use **comments** on each line. They will be ignored.
- Use `best` to specify the best submission. Do not use this keyword otherwise.

**Note:** Everything will be properly formatted at the end.

## Rules

1. Read about [Judging](https://docs.sherlock.xyz/audits/judging) and [Rules](https://docs.sherlock.xyz/audits/judging/guide-to-judging-contests).

## Why I made this?

I wanted to make the judging process more comfortable and faster. I use a browser and a text editor to write suggestions. Now I do not need manually drag and drop files between folders.

## Creator

If you have any questions, feel free to write me on Discord favelanky#0282 or [Twitter](https://twitter.com/favelanky). Thanks for using my tool!
