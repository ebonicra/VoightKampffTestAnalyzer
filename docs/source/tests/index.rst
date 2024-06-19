Tests
=====


Purpose
-------

This directory contains all test files and test cases for the Voight-Kampff project.


Tools and Frameworks
---------------------

In our project, we use the pytest framework for writing and running tests. We also utilize the unittest library for writing unit tests.


Example Test Files
------------------

Example test file unit_tests/test_calculations.py:

.. code-block:: python

    def test_addition():
        assert add(1, 2) == 3

    def test_subtraction():
        assert subtract(5, 3) == 2

These elements will help users understand how your tests are organized and what they test.

Running Tests
-------------

To run the tests, navigate to the root directory of the project in your terminal and execute the following command:

.. code-block:: bash

    pytest