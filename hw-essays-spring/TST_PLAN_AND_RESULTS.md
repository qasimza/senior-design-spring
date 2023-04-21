# Test Plan and Results

## Description of Overall Test Plan
Tune-Me is a web-based application that allows users to generate playlists based on the parameters provided by them. The testing approach involves individually testing each component of the project as well as the integration of each of these components at various interfaces. While the recommendation system is a part of the web-application, the two are separated for simplicity. The recommendation system tests may not be exhaustive since the multitude of possible queries is virtually infinite. Instead, broader categories of tests are identified (based on most likely use cases) to ensure the proper working of the system. Test results will be logged for debugging and record purposes.

## Test Case Descriptions and Results

Following tests were conducted to validate project outcomes. n > 5.

**WA1.1	Web Application Test 1**
WA1.2	Ensure that the login/logout authentication works correctly.  
WA1.3	Test that the login page redirects to home page if attempting to login with pre-exiting credentials entered correctly. Test with incorrect credentials to ensure user is redirected back to login page. 
WA1.4	Input: Correct Credentials (1), Incorrect Credentials (2) 
WA1.5	Output: Home Page (1), Redirected to Login Page with error message (2)
WA1.6	Both
WA1.7	Black-Box
WA1.8	Functional
WA1.9	Integration
WA1.10	Result : Login Page Produces correct results for each.
	
**WA2.1	Web Application Test 2**
WA2.2	Ensure that the registration works correctly.  
WA2.3	Test the registration page to ensure that the user is able to create a new profile (unless the user id/email already exists - display appropriate message). Display message to indicate successful creation of profile. Once the profile is created, the user should be able to login from the login page thereafter. 
WA2.4	Input: Non existing user id credentials (1), Existing user id (2), Credentials from(1) in login page
WA2.5	Output: Success message (1), Failure Message(2), Home page (3)  
WA2.6	Both
WA2.7	Black-Box
WA2.8	Functional
WA2.9	Integration
WA2.10	Result: Registration page works seamlessly.
	
**WA3.1	Web Application Test 3**
WA2.2	Ensure that the home page works correctly.
WA2.3	Test each button on home page to ensure it redirects to the correct page with correct user session values. 
WA2.4	Input: Click each of the buttons on the home page.
WA2.5	Output: Correct pages are redirected to and rendered based on user session values.
WA2.6	Normal
WA2.7	Black-Box
WA2.8	Functional
WA2.9	Integration
WA2.10	Result: Home page works seamlessly and maintains credentials needed. 
	
**WA4.1	Web Application Test 4**
WA4.2	Ensure that the search page works correctly.
WA4.3	Input randomized values for each search option. Ensure that query is registered correctly and responds with correct matching values for the query. Ensure that user is redirected to results page once the search query is submitted. 
WA4.4	Input: Randomized search queries. (Test each search option individually, combination of options, all) 
WA4.5	Output: Results page with suggested songs. 
WA4.6	Both
WA4.7	Black-Box
WA4.8	Functional
WA4.9	Integration
WA4.10	Result: Results page rendered with matching suggestions (accuracy of results measured in RS tests) 
	
**WA5.1	Web Application Test 5**
WA5.2	Ensure that the results page works correctly.
WA5.3	Ensure that buttons from the results page redirect to correct pages.
WA5.4	Input: Click each of the buttons on the home page.
WA5.5	Output: Correct pages are redirected to and rendered based on user session values.
WA5.6	Normal
WA5.7	Black-Box
WA5.8	Functional
WA5.9	Integration
WA5.10	Result: Results page works seamlessly. 
	
**WA6.1	Web Application Test 6**
WA6.2	Ensure that the user profile is updated correctly. 
WA6.3	Go to user profile page, change values, submit, logout. Login and see if the changes are registered. 
WA6.4	Input: New values for user profile
WA6.5	Output: Registered changes on login page.
WA6.6	Normal
WA6.7	Black-Box
WA6.8	Functional
WA6.9	Integration
WA6.10	Result: Changes are logged correctly.
	
**RS.1.1	Recommendation System Test 1**
RS.1.2	Ensure that the top n songs (based on similarity score) are output when only Song is provided in query
RS.1.3	Use test set data to run a regression of test cases with different songs. Ensure top matching values are output for each or an error message is returned if query cannot be matched. Record the number of matches for each query and the median similarity (based on median similarity score, 0 if no matches).  RS passes test if on average 10 or more results are produced with a median similarity score of 70%
RS.1.4	Input: Song Name
RS.1.5	Output: Overall average number of results and average similarity score.
RS.1.6	Normal 
RS.1.7	White-box
RS.1.8	Functional
RS.1.9	Unit
RS.1.10	Result: System produces desired output.
	
**RS.2.1	Recommendation System Test 2**
RS.2.2	Ensure that the top n songs are output when only one of the following - Artist, Genre, or Year - is provided in query
RS.2.3	For each of the following - Artist, Genre, or Year, input values from the tests sets. Record the number of matches for each query and the median similarity (based on median similarity score, 0 if no matches).  RS passes test if on average 10 or more results are produced with a median similarity score of 70%
RS.2.4	Input: Artist, Genre, Year values one at a time from respective test sets.
RS.2.5	Output: Overall average number of results and average similarity score.
RS.2.6	Boundary
RS.2.7	White box
RS.2.8	Functional
RS.2.9	Unit
RS.2.10	Result: System produces desired output.
	
**RS.3.1	Recommendation System Test 3**
RS.3.2	Ensure that the top n songs are output when Genre and Year is provided in query.
RS.3.3	Input values from the test sets. Record the number of matches for each query and the median similarity (based on median similarity score, 0 if no matches).  RS passes test if on average 10 or more results are produced with a median similarity score of 70%
RS.3.4	Input: Randomized Genre - Year pairs one at a time from test set. 
RS.3.5	Output: Overall average number of results and average similarity score.
RS.3.6	Normal 
RS.3.7	White box
RS.3.8	Functional
RS.3.9	Unit
RS.3.10	Result: System produces desired output.
	
**RS.4.1	Recommendation System Test 4**
RS.4.2	Ensure that the top n songs are output when Artist and Genre is provided in query
RS.4.3	Input values from the test sets. Record the number of matches for each query and the median similarity (based on median similarity score, 0 if no matches).  RS passes test if on average 10 or more results are produced and results have a median similarity score of 70%.
RS.4.4	Input: Randomized Genre(s) - Artist pairs one at a time from test set. 
RS.4.5	Output: Overall average number of results and average similarity score.
RS.4.6	Normal 
RS.4.7	White box
RS.4.8	Functional
RS.4.9	Unit
RS.4.10	Result: System produces desired output.
	
**RS.5.1	Recommendation System Test 5**
RS.5.2	Ensure that the top n songs are output when Artist and Year is provided in query
RS.5.3	Input values from the test sets. Record the number of matches for each query and the median similarity (based on median similarity score, 0 if no matches).  RS passes test if on average 10 or more results are produced or results have a median similarity score of 70%.
RS.5.4	Input: Randomized Artist - Year pairs one at a time from test set. 
RS.5.5	Output: Overall average number of results and average similarity score.
RS.5.6	Normal 
RS.5.7	White box
RS.5.8	Functional
RS.5.9	Unit
RS.5.10	Result: System produces desired output.
	
**RS.6.1	Recommendation System Test 6**
RS.6.2	Ensure that the top n songs are output when Song and Artist/Genre/Year (Song Aritst/Genre/Year and Artist/Genre/Year are different) is provided in query
RS.6.3	Input values from the test sets. Record the number of matches for each query and the median similarity (based on median similarity score, 0 if no matches).  RS passes test if on average 10 or more results are produced or results have a median similarity score of 70%.
RS.6.4	Input: Randomized Artist - Genre(s)-Year pairs one at a time from test set. 
RS.6.5	Output: Overall average number of results and average similarity score.
RS.6.6	Normal
RS.6.7	White box
RS.6.8	Functional
RS.6.9	Unit
RS.6.10	Result: System produces desired output.
	
**RS.7.1	Recommendation System Test 7**
RS.7.2	Ensure that the Advanced Search Parameter values are reflected in the output.
RS.7.3	Input values from the test sets. Record the number of matches for each query and the median similarity (based on median similarity score, 0 if no matches).  RS passes test if on average 10 or more results are produced or results have a median similarity score of 70%.
RS.7.4	Input: Randomized Queries with Advanced parameter value pairs one at a time from test set. 
RS.7.5	Output: Overall average number of results and average similarity score.
RS.7.6	Normal
RS.7.7	White box
RS.7.8	Functional
RS.7.9	Unit
RS.7.10	Result: System produces desired output.

**T.1.1	Timing Test 1**
T.1.2	Ensure that the matches are returned in a reasonable amount of time (10 seconds) 
T.1.3	Run randomized queries from all test sets. Record time taken for searching. Ensure system produces results in less < 10 seconds 95 % of the time.
T.1.4	Input: Randomized queries from tests sets.
T.1.5	Output: Boolean Value indicating whether at least 95% of queries took less than 10 seconds 
T.1.6	Both
T.1.7	Black box
T.1.8	Performance
T.1.9	Unit
T.1.10	Result: System produces desired output.
