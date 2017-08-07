# WD_python

[Selenium Python Page Objects](http://selenium-python.readthedocs.io/page-objects.html)

Introduction to page objects design pattern. A page object represents an area in the web application user interface that your test is interacting.

Benefits of using page object pattern:

* Creating reusable code that can be shared across multiple test cases

* Reducing the amount of duplicated code

* If the user interface changes, the fix needs changes in only one place


## COVERAGE

Usage of coverage module

```
Directory of C:\Users\Anna\PycharmProjects\WebDriver_PageObject

08/01/2017  06:52 PM    <DIR>          .
08/01/2017  06:52 PM    <DIR>          ..
08/06/2017  08:38 PM    <DIR>          .idea
08/01/2017  06:52 PM    <DIR>          lib
08/01/2017  06:52 PM               854 TestLogin.py
08/01/2017  02:50 PM             2,289 TestLogin_HRM.py
               2 File(s)          3,143 bytes
               4 Dir(s)  179,580,342,272 bytes free

C:\Users\Anna\PycharmProjects\WebDriver_PageObject>coverage run TestLogin.py
.
----------------------------------------------------------------------
Ran 1 test in 36.359s

OK

C:\Users\Anna\PycharmProjects\WebDriver_PageObject>coverage report -m
Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
TestLogin.py         23      0   100%
lib\__init__.py       0      0   100%
lib\element.py       11      7    36%   7-10, 13-17
lib\locators.py      13      0   100%
lib\page.py          58      7    88%   26-34
lib\utils.py         25      6    76%   18-19, 28-32
-----------------------------------------------
TOTAL               130     20    85%

C:\Users\Anna\PycharmProjects\WebDriver_PageObject>coverage html

```
Resulf of running comand *coverage html*

![coverage html](https://github.com/annaVVV/WD_python/blob/master/Coverage.jpg)

