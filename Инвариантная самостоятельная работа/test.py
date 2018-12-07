import pytest
import main

def testing_fun1():
    assert main.FromJsonToTable('json.json') == 5, '1'