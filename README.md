### Task
- On the website https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites, there is a table called "Programming languages used in most popular websites."
- It is necessary to implement a parameterized test that checks if there are any rows in this table where the value in the column "Popularity (unique visitors per month)" is less than the parameter value passed to the test.
- If such rows exist in the table, the test should display an error message listing the error rows in the following format, for example:
"Yahoo (Frontend: JavaScript | Backend: PHP) has 750,000,000 unique visitors per month. (Expected more than 500,000)"
- The test should be executed for the following values: [10^7, 1.5 * 10^7, 5 * 10^7, 10^8, 5 * 10^8, 10^9, 1.5 * 10^9]
- When implementing the test, it should be considered that the data from this table may be needed in other tests as well. It would be a plus to implement storing the data from the table as data classes.

### Install
Pytest
```console
python -m pip install -r requirements.txt
```

### How to
To run this project run this command:

```console
pytest
```
