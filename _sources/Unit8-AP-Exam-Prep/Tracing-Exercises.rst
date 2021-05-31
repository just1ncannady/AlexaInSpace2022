.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Tracing Pseudocode Exercises
============================

.. raw:: html

	<!-- Copy these 6 lines to the top of the lesson's HTML code.  -->
	<script type="text/javascript" src="https://code.jquery.com/jquery-1.11.3.min.js"></script>
	<script type="text/javascript" src="assets/lib/lessons/tipped.js"></script>
	<script type="text/javascript" src="assets/lib/Framework2020.js"></script>
	<link rel="stylesheet" href="//code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
	<link rel="stylesheet" type="text/css" href="assets/lib/lessons/tipped.css">
	<link rel="stylesheet" type="text/css" href="assets/lib/lessons/lessons.css">
	<script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
	<script type="text/javascript" src="assets/lib/vocabulary.js"></script>
	
	<script>
	$(document).ready(function() {
		generateSummary(EKmapping['8.03']);
	   	generateHovers();
	
	});
	</script>
	
	
	<h3 id="est-length">Time Estimate: 45 minutes</h3>
	
	
	<p><b>Tracing</b> is a technique used to simulate a dry run through the code or pseudocode line by line by hand  as if you are the computer executing the code. Tracing can be used for debugging or proving that your program runs correctly or for figuring out what the code actually does.  <b>Trace tables</b> can be used  to track the values of variables as they change throughout a program. To trace through code, write down a variable in each column of the trace table and keep track of its value throughout the program. Some trace tables also keep track of the output and the line number you are currently tracing.
	 
	 </p><p>For example, here is a simple algorithm that adds x to the total every time through the loop which is executed 3 times. 
	</p><pre>x ← 2
	total ← 0
	REPEAT 3 TIMES 
	{
	 total ← total + x
	}
	DISPLAY(total)
	</pre>
	Try tracing through the code and see if your results match the trace table below:
	<table border="">
	 <tbody><tr><th><u>x</u></th><th><u>total</u></th><th><u>Output</u></th></tr>
	 <tr><td>2</td><td>0</td></tr>
	 <tr><td></td><td>2</td></tr>
	 <tr><td></td><td>4</td></tr>
	 <tr><td></td><td>6</td><td>6</td></tr>
	</tbody></table>
	<br>
	
	<div class="pogil yui-wk-div">
	 <h3>POGIL Activity for the Classroom </h3> 
	 <p>Break into POGIL teams of 4 and assign each team member one of the following roles. Record your answers <a href="https://docs.google.com/document/d/1YG1aKf7XP2gMxEhKSxQ8w6zqZNlYd1QRILuOT1Uqq8Q/edit" target="_blank">using this worksheet</a>. (File-Make a Copy to have a version you can edit.)</p>
	   <table>
	     <tbody><tr><th>Role</th><th>Responsibility</th></tr>
	     <tr>
	       <td>Facilitator</td>
	       <td>Reads the questions aloud, keeps track of time and makes sure everyone contributes appropriately.</td>
	     </tr>
	     <tr>
	       <td>Spokesperson</td>
	       <td>Talks to the instructor and other teams. </td>
	     </tr>  
	     <tr>
	       <td>Quality Control</td>
	       <td>Records all answers &amp; questions, and provides team reflection to team and instructor.</td>
	     </tr>
	     <tr>
	       <td>Process Analyst</td>
	       <td>Considers how the team could work and learn more effectively.</td>
	     </tr>
	 </tbody></table>
	 
Writing and Tracing Pseudocode:  Critical Thinking Questions
------------------------------------------------------------

.. raw:: html
	 
	
	 <p>Suppose we have a list of numbers -- e.g.,  5,  10, -2,  -3, 7,  8,  12
	 Here's an algorithm that uses sequence, selection, and iteration (repetition) to add all 
	 the <b><i>even numbers</i></b> in the list and print out their sum.
	 
	 Notice how indentation and curly brackets are used to clarify the different parts of the algorithm.</p>
	 <pre> 
	1  total ← 0      (Set total to 0)
	2  FOR EACH number IN list  
	3  {
	4     IF (EVEN(number)) 
	5     {
	6        total ← total + number    (Set total to the current total + number)
	7     }
	8  }
	9  DISPLAY(total)
	 </pre>
	
	 This algorithm contains  examples of all three types of 
	 control structures, sequence, selection, and repetition.  The lines are numbered for convenience.
	 <ol>
	   <li>Which line(s) of the algorithm contain a repetition control structure? Remember a control structure
	     can consist of multiple statements.
	   </li>
	   <li>Which line(s) of the algorithm contain a selection control structure?       
	   </li>
	   <li>(<b>Portfolio</b>) If you ran this algorithm on the list of numbers, 5,  10, -2,  -3, 7,  8,  12, what would it print? When tracing through an algorithm, write down the variables (total and number) and pretend you are the computer executing each line of code and change the values of the variables on your paper as needed.</li>
	   <li>(<b>Portfolio</b>) Suppose you had a list of positive numbers such as 
	     5, 10, 12, 13, 6, 7, 1, 3, 2, 1.  And suppose  for each of the numbers in the list 
	     you added the number to a running total if it is even and subtracted it if it is odd, starting the total at 0. 
	     What result would you get for this list of numbers?
	   </li>
	   <li>(<b>Portfolio</b>) Write a pseudocode algorithm that implements the algorithm you 
	     used to calculate this total. Make sure that you use AP CSP text-style pseudocode.
	   </li>
	 </ol>
	 
	</div>
	<br>
	
Summary
-------

.. raw:: html

	<p>In this lesson, you learned how to:</p>
	 <div id="summarylist">
	 </div>
	
Self-Check
----------
.. raw:: html
	
	<p></p>
	<question quid="5177138009341952" qu_type="null" weight="1" instanceid="HaCKFNvEk9Mj"></question><br>
	<question quid="5332167583334400" qu_type="sa" weight="1" instanceid="Fn5Ljgo8DadW"></question><br>
	<quizly quizname="quiz_convert_list_to_string" preamble="Create a procedure called  <b>convertListToString</b> below that uses loops with lists. Make sure that all of your code is in the procedure, including initializing text to &amp;ldquo;&amp;rdquo;" \"."="" hasanswerbox="false" isrepeatable="false" hints="true" width="100%" instanceid="69MfN6vXmbKL">
	</quizly><br>
	<quizly quizname="quiz_count_nonzeros_in_list_procedure" preamble="Create a procedure called  <b>countNonzerosInList</b> below that uses loops with lists. Make sure that all of your code is in the procedure, including initializing count to 0." hasanswerbox="false" isrepeatable="false" hints="true" width="100%" instanceid="CMcsWiDTnGiA">
	</quizly><br>
	
	
	
Sample AP CSP Exam Question
---------------------------

.. raw:: html

	<p></p>
	<question quid="5981474378481664" weight="1" instanceid="xMVDHWtEhCzE"></question>
	
	
	<div id="portfolio" class="yui-wk-div">

Reflection: For Your Portfolio
------------------------------

.. raw:: html
	
	<p>
	 Create a page named&nbsp;<i><b>Tracing Pseudocode</b></i> in your portfolio and answer the following questions:</p>
	
	<ol>
	  <li>(<b>POGIL</b>) If you ran the algorithm in the POGIL on the list of numbers, 5,  10, -2,  -3, 7,  8,  12, what would it print? </li>
	 <li>(<b>POGIL</b>) Suppose you had a list of positive numbers such as 
	     5, 10, 12, 13, 6, 7, 1, 3, 2, 1.  And suppose  for each of the numbers in the list 
	     you added the number to a running total if it is even and subtracted it if it is odd.  
	     What result would you get for this list of numbers?
	 </li>
	 <li>(<b>POGIL</b>) Write a pseudocode algorithm that implements the algorithm you 
	     used to calculate this total. Make sure that you use AP CSP text-style pseudocode.
	 </li>
	
	
	
	</ol>
	</div>
