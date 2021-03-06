﻿# Yelp-Data-Analysis
For DS3001 - Introduction to Data Science
Team 7 - Griffin Bishop, Michael Taylor, Alex O'Brien, Gio Aguila

Contained in the notebook-code-snippets folder are a few python files that are also in the notebook. These are separate because several of them use very large files (which we left out because they are so big). They also contain several json and .text files that are used in intermediate computations in the notebook questions.

# Case Study Problem
The problem we chose to solve is determining the sentiment of words. Yelp's data is uniquely suited to this because it is all labelled--each piece of text (review) is coupled with a rating from 1-5. We can use this labelled data to discover which words are associated with good and bad sentiments. This information would be valuable to businesses in this context because we would be able to detect if words related to the business often came up with bad sentiment. For example, if a sandwhich shop often had negative reviews about their turkey sandwiches, then we would be able to pick up one or both of these words, and we would be able to provide a recommendation to the company about improving their turkey, or their sandwiches, or their turkey sandwiches.

This solution is useful because the alternative is paying someone to go through the company's Yelp feed and reading the individual comments. This is resource consuming and not scalable. Our method provides a scalable, fast solution to this problem.
