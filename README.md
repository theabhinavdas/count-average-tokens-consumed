# count average tokens consumed

1. put your .csv exports from humanloop or wherever into the `log_dumps` directory
2. ensure the `tokens` colum contains the total tokens consumed data
3. `pip install -r requirements.txt`
4. `python main.py`

## output looks something like:

Filename                                                                                            Average Tokens
========================================================================================================================
some-file-check-something-last-3-years-2024-07-24-20-52-14.csv                                          3757.65
other-file-check-something-else-2024-07-25-03-02-02.csv                                                 2562.98
