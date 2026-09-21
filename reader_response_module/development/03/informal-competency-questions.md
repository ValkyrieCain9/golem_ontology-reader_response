# Iteration 3 - Informal Competency Questions

## Question 1

### Identifier
CQ_3.1

### Question
What is the type and subject of a review on Goodreads?

### Expected Outcome
A list of the discourse attributes of a Goodreads review

### Result Sample
* `review_1` is a `Discourse_Act`
* `review_1` has type `evaluation`
* `review_1` has subject `The Infinite and Divine`

### Based on
Example 1

***

## Question 2

### Identifier 
CQ_3.2

### Question
Which are the different discourse acts, their theme and degree, which make up an evaluation act on GoodReads?

### Expected outcome
A list of discourse acts, their theme and degree, which are part of a review on GoodReads with an evaluation act type

### Result Sample
* `review_1` is a `Discourse_Act`
* `review_1` has type `evaluation`
* `clause_1` is a `Discourse_Act`
* `clause_1` is part of `review_1`
* `clause_1` has type `evaluation`
* `clause_1` has theme `individual_experience`
* `clause_1` has degree `negative`

### Based on 
Example 1

***

## Question 3

### Identifier
CQ_3.3

### Question
What type of users are involved in a discourse chain on AO3?

### Expected Outcome
A list of users, their roles, and their accociated discourse acts

### Result Sample
* `user_1` has role `author`
* `user_1` created `Forever Girl`
* `user_2` has role `reader`
* `user_2` created `comment_1`
* `comment_1` is a `Discourse_Act`
* `comment_1` has type `Appreciation`
* `comment_1` has subject `Forever Girl`

### Based on
Example 2

***

## Question 4

### Identifier
CQ_3.4

### Question
What are the discourse relations that make up a thread on Reddit?

### Expected Outcome
A list of comments as discourse acts, with their relevant discourse attributes which form part of a thread structured into parts

### Result Sample
* `comment_1` responds to `Post`
* `comment_1` is a `Discourse_Act`
* `comment_1` has type `Statement`
* `comment_1` is part of `top-level_comment_thread`
* `comment_2` responds to `comment_1`
* `comment_2` has type `Suggestion`
* `comment_2` part of `nested_thread`
* `nested_thread` has parent `comment_1`

### Based on
Example 3
