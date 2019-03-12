{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# How many negative numbers are there?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(a[a < 0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "# How many positive numbers are there?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(a[a > 0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "# How many even positive numbers are there?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3,)"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pos = a[a > 0]\n",
    "even = pos[pos % 2 == 0]\n",
    "even.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# If you were to add 3 to each data point,\n",
    "# how many positive numbers would there be?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b = a + 3\n",
    "c = b > 0\n",
    "sum(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# If you squared each number, \n",
    "# what would the new mean and standard deviation be?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 4 10 12 23 -2 -1  0  0  0 -6  3 -7]\n",
      "3.0\n",
      "8.06225774829855\n"
     ]
    }
   ],
   "source": [
    "# a\n",
    "print(a)\n",
    "print(np.average(a))\n",
    "print(np.std(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 16 100 144 529   4   1   0   0   0  36   9  49]\n",
      "74.0\n",
      "144.0243035046516\n"
     ]
    }
   ],
   "source": [
    "# a square\n",
    "b = a**2\n",
    "print(b)\n",
    "print(np.average(b))\n",
    "print(np.std(b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# A common statistical operation on a dataset is centering. \n",
    "# This means to adjust the data such that the center of the data is at 0. \n",
    "# This is done by subtracting the mean from each data point. \n",
    "# Center the data set."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 4, 10, 12, 23, -2, -1,  0,  0,  0, -6,  3, -7])"
      ]
     },
     "execution_count": 125,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([  1.,   7.,   9.,  20.,  -5.,  -4.,  -3.,  -3.,  -3.,  -9.,   0.,\n",
       "       -10.])"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "avg = np.average(a)\n",
    "centered = a - avg\n",
    "centered"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculate the z-score for each data point. \n",
    "# Recall that the z-score is given by:\n",
    "# Z = x − μ / σ"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0.12403473,  0.86824314,  1.11631261,  2.48069469, -0.62017367,\n",
       "       -0.49613894, -0.3721042 , -0.3721042 , -0.3721042 , -1.11631261,\n",
       "        0.        , -1.24034735])"
      ]
     },
     "execution_count": 130,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "avg = np.average(a)\n",
    "std = np.std(a)\n",
    "\n",
    "z_score = (a - avg) / std\n",
    "z_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "metadata": {},
   "outputs": [],
   "source": [
    "#  #8 setup 1\n",
    "a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "55"
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sum_of_a = sum(a)\n",
    "sum_of_a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 141,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "min_of_a = min(a)\n",
    "min_of_a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 142,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "max_of_a = max(a)\n",
    "max_of_a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5.5"
      ]
     },
     "execution_count": 143,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mean_of_a = np.average(a)\n",
    "mean_of_a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying \n",
    "# all the numbers in the above list together"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3628800"
      ]
     },
     "execution_count": 145,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "product_of_a = np.product(a)\n",
    "product_of_a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 6 - Make a variable named squares_of_a. \n",
    "# It should hold each number in a squared like [1, 4, 9, 16, 25...]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([  1,   4,   9,  16,  25,  36,  49,  64,  81, 100])"
      ]
     },
     "execution_count": 146,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "squares_of_a = np.square(a)\n",
    "squares_of_a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 3, 5, 7, 9]"
      ]
     },
     "execution_count": 164,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "odds_in_a = []\n",
    "for num in a:\n",
    "    if num % 2 == 1:\n",
    "        odds_in_a.append(num)\n",
    "\n",
    "odds_in_a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2, 4, 6, 8, 10]"
      ]
     },
     "execution_count": 165,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "even_in_a = []\n",
    "for num in a:\n",
    "    if num % 2 == 0:\n",
    "        even_in_a.append(num)\n",
    "\n",
    "even_in_a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#  set up 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "metadata": {},
   "outputs": [],
   "source": [
    "b = [\n",
    "    [3, 4, 5],\n",
    "    [6, 7, 8]\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 168,
   "metadata": {},
   "outputs": [],
   "source": [
    "# # Exercise 1 - refactor the following to use numpy. \n",
    "# Use sum_of_b as the variable.\n",
    "# **Hint, you'll first need to make sure that the \"b\" variable is a numpy array**\n",
    "\n",
    "# sum_of_b = 0\n",
    "# for row in b:\n",
    "#     sum_of_b += sum(row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 183,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "33"
      ]
     },
     "execution_count": 183,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np_b = np.array(b)\n",
    "sum_of_b = np.sum(b)\n",
    "sum_of_b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 176,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 2 - refactor the following to use numpy. \n",
    "# min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 175,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "min_of_b = np.min(b)\n",
    "min_of_b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.\n",
    "# max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 177,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "max_of_b = np.max(b)\n",
    "max_of_b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 4 - refactor the following using numpy to find the mean of b\n",
    "# mean_of_b = (sum(b[0]) + sum(b[1])) / (len([b[0]]) + len(b[1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5.5"
      ]
     },
     "execution_count": 178,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mean_of_b = np.average(b)\n",
    "mean_of_b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.\n",
    "# product_of_b = 1\n",
    "# for row in b:\n",
    "#     for number in row:\n",
    "#         product_of_b *= number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20160"
      ]
     },
     "execution_count": 179,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "product_of_b = np.product(b)\n",
    "product_of_b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 6 - refactor the following to use numpy to find the list of squares \n",
    "# squares_of_b = []\n",
    "# for row in b:\n",
    "#     for number in row:\n",
    "#         squares_of_b.append(number**2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 9, 16, 25],\n",
       "       [36, 49, 64]])"
      ]
     },
     "execution_count": 180,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "squares_of_b = np.square(b)\n",
    "squares_of_b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 7 - refactor using numpy to determine the odds_in_b\n",
    "# odds_in_b = []\n",
    "# for row in b:\n",
    "#     for number in row:\n",
    "#         if(number % 2 != 0):\n",
    "#             odds_in_b.append(number)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 185,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([3, 5, 7])"
      ]
     },
     "execution_count": 185,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "odds_in_b = np_b[np_b % 2 == 1]\n",
    "odds_in_b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 8 - refactor the following to use numpy to filter only the even numbers\n",
    "# evens_in_b = []\n",
    "# for row in b:\n",
    "#     for number in row:\n",
    "#         if(number % 2 == 0):\n",
    "#             evens_in_b.append(number)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 186,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([4, 6, 8])"
      ]
     },
     "execution_count": 186,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evens_in_b = np_b[np_b % 2 == 0]\n",
    "evens_in_b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 9 - print out the shape of the array b."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2, 3)"
      ]
     },
     "execution_count": 192,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np_b.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 10 - transpose the array b."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 195,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[3, 6],\n",
       "       [4, 7],\n",
       "       [5, 8]])"
      ]
     },
     "execution_count": 195,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.transpose(np_b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 204,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[3, 4, 5, 6, 7, 8]])"
      ]
     },
     "execution_count": 204,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.reshape(np_b,(1,6))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 202,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[3],\n",
       "       [4],\n",
       "       [5],\n",
       "       [6],\n",
       "       [7],\n",
       "       [8]])"
      ]
     },
     "execution_count": 202,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.reshape(np_b,(6,1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 208,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3],\n",
       "       [4, 5, 6],\n",
       "       [7, 8, 9]])"
      ]
     },
     "execution_count": 208,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Setup 3\n",
    "\n",
    "c = [\n",
    "    [1, 2, 3],\n",
    "    [4, 5, 6],\n",
    "    [7, 8, 9]\n",
    "]\n",
    "\n",
    "c = np.array(c)\n",
    "c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 1 - Find the min, max, sum, and product of c.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 210,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "9\n",
      "45\n",
      "362880\n"
     ]
    }
   ],
   "source": [
    "print(np.min(c))\n",
    "print(np.max(c))\n",
    "print(np.sum(c))\n",
    "print(np.product(c))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 2 - Determine the standard deviation of c.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 213,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.581988897471611"
      ]
     },
     "execution_count": 213,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "std_c = np.std(c)\n",
    "std_c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 3 - Determine the variance of c.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 214,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6.666666666666667"
      ]
     },
     "execution_count": 214,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "var_c = np.var(c)\n",
    "var_c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 4 - Print out the shape of the array c\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 216,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3, 3)"
      ]
     },
     "execution_count": 216,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 5 - Transpose c and print out transposed result.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 218,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 4, 7],\n",
       "       [2, 5, 8],\n",
       "       [3, 6, 9]])"
      ]
     },
     "execution_count": 218,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_c = np.transpose(c)\n",
    "x_c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 221,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 6 - Multiply c by the c-Transposed and print the result."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 220,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1,  8, 21],\n",
       "       [ 8, 25, 48],\n",
       "       [21, 48, 81]])"
      ]
     },
     "execution_count": 220,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "prod_c = c * x_c\n",
    "prod_c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 206,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 224,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "261"
      ]
     },
     "execution_count": 224,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sum1 = sum(prod_c)\n",
    "sum2 = sum(sum1)\n",
    "sum2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 229,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "131681894400"
      ]
     },
     "execution_count": 229,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "big_c = np.product(prod_c)\n",
    "big_c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 237,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 90,  30,  45,   0, 120, 180],\n",
       "       [ 45, -90, -30, 270,  90,   0],\n",
       "       [ 60,  45, -45,  90, -45, 180]])"
      ]
     },
     "execution_count": 237,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Setup 4\n",
    "\n",
    "d = [\n",
    "    [90, 30, 45, 0, 120, 180],\n",
    "    [45, -90, -30, 270, 90, 0],\n",
    "    [60, 45, -45, 90, -45, 180]\n",
    "]\n",
    "\n",
    "d = np.array(d)\n",
    "d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 1 - Find the sine of all the numbers in d\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 238,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0.89399666, -0.98803162,  0.85090352,  0.        ,  0.58061118,\n",
       "        -0.80115264],\n",
       "       [ 0.85090352, -0.89399666,  0.98803162, -0.17604595,  0.89399666,\n",
       "         0.        ],\n",
       "       [-0.30481062,  0.85090352, -0.85090352,  0.89399666, -0.85090352,\n",
       "        -0.80115264]])"
      ]
     },
     "execution_count": 238,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sin_d = np.sin(d)\n",
    "sin_d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 2 - Find the cosine of all the numbers in d\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 239,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-0.44807362,  0.15425145,  0.52532199,  1.        ,  0.81418097,\n",
       "        -0.59846007],\n",
       "       [ 0.52532199, -0.44807362,  0.15425145,  0.98438195, -0.44807362,\n",
       "         1.        ],\n",
       "       [-0.95241298,  0.52532199,  0.52532199, -0.44807362,  0.52532199,\n",
       "        -0.59846007]])"
      ]
     },
     "execution_count": 239,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cos_d = np.cos(d)\n",
    "cos_d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 3 - Find the tangent of all the numbers in d\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 240,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-1.99520041, -6.4053312 ,  1.61977519,  0.        ,  0.71312301,\n",
       "         1.33869021],\n",
       "       [ 1.61977519,  1.99520041,  6.4053312 , -0.17883906, -1.99520041,\n",
       "         0.        ],\n",
       "       [ 0.32004039,  1.61977519, -1.61977519, -1.99520041, -1.61977519,\n",
       "         1.33869021]])"
      ]
     },
     "execution_count": 240,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tan_d = np.tan(d)\n",
    "tan_d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 4 - Find all the negative numbers in d\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 244,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-90, -30, -45, -45])"
      ]
     },
     "execution_count": 244,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "neg_d = d[d < 0]\n",
    "neg_d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 5 - Find all the positive numbers in d\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 245,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 90,  30,  45, 120, 180,  45, 270,  90,  60,  45,  90, 180])"
      ]
     },
     "execution_count": 245,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pos_d = d[d > 0]\n",
    "pos_d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 6 - Return an array of only the unique numbers in d.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 247,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-90, -45, -30,   0,  30,  45,  60,  90, 120, 180, 270])"
      ]
     },
     "execution_count": 247,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "uniq_d = np.unique(d)\n",
    "uniq_d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 7 - Determine how many unique numbers there are in d.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 249,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(11,)"
      ]
     },
     "execution_count": 249,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "uniq_d.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 235,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 8 - Print out the shape of d.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 250,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3, 6)"
      ]
     },
     "execution_count": 250,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 9 - Transpose and then print out the shape of d.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 251,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 90,  45,  60],\n",
       "       [ 30, -90,  45],\n",
       "       [ 45, -30, -45],\n",
       "       [  0, 270,  90],\n",
       "       [120,  90, -45],\n",
       "       [180,   0, 180]])"
      ]
     },
     "execution_count": 251,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.transpose(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 10 - Reshape d into an array of 9 x 2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 252,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 90,  30],\n",
       "       [ 45,   0],\n",
       "       [120, 180],\n",
       "       [ 45, -90],\n",
       "       [-30, 270],\n",
       "       [ 90,   0],\n",
       "       [ 60,  45],\n",
       "       [-45,  90],\n",
       "       [-45, 180]])"
      ]
     },
     "execution_count": 252,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d.reshape(9,2)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
