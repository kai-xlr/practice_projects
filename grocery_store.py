#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: grocery_store.py
Author: kai-xlr
Date: 2025-03-25
Description: Simple port of grocery_store.c
"""

Quantity = 23
Price = 1.49
Review = 82.5
ReviewDisplay = int(Review // 1)
Location = "F"

print(f"An apple costs: ${Price}, there are {Quantity} in inventory found in section: {Location} and your customers gave it an average review of {ReviewDisplay}%!")