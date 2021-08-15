.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Quiz App Projects Loops with Lists
==================================

.. raw:: html

    <!-- Custom Scripts -->
    <script src="../_static/assets/lib/lessons/tipped.js" type="text/javascript"></script>
    <script src="../_static/assets/lib/lessons/Framework2020.js" type="text/javascript"></script>
    <link href="../_static/assets/lib/lessons/tipped.css" rel="stylesheet" type="text/css"></link>
    <link href="../_static/assets/lib/lessons/lessons.css" rel="stylesheet" type="text/css"></link>
    <link href="../_static/assets/css/custom.css" rel="stylesheet" type="test/css"></link>
    <script src="../_static/assets/lib/lessons/vocabulary.js" type="text/javascript"></script>
    <style>    td { text-align: left; padding: 5px;}</style>


.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
        $(document).ready(function() {
            generateSummary(EKmapping['5.06']);
            generateHovers();
    
        });
    </script>
    <!-- for apml questions -->
    <link href="assets/css/apmlblockStyles.css" rel="stylesheet" type="text/css"/>
    <h3 id="est-length">Time Estimate: 90 minutes</h3>
    

Introduction and Goals
-----------------------

.. raw:: html

    <p>
    <table>
    <tbody>
	<tr>
		<td valign="top" colspan=2>In this lesson, you will complete several small programming projects that add enhancements to the Quiz App.  You are encouraged to discuss your ideas for how to solve these problems with the instructor and with your partner  and other students. Hints and suggestions are provided.	</td>
	</tr>
    <tr>
    <td>
		<!--  &lt;img src=&quot;assets/img/6-3-QuizAppProjectsUI.png&quot; width=&quot;100%&quot;&gt; -->
		<iframe allowfullscreen="" frameborder="0" height="325" src="https://www.youtube.com/embed/1Mb_Hr8nqEU" width="275"></iframe>
    </td>
	<td valign="top">
		<div><b>Learning Objectives:</b>&nbspI will learn to</div>
		<ul>
		<li>count right and wrong answers using a list to keep track of which questions have already been answered</li>
		<li>use loops with lists and standard algorithms to enhance my app</li>
		<li>manipulate lists in pseudocode using the insert, append, and length procedures</li>
		<li>design and implement my own custom quiz app features</li>
		</ul>
		<div><b>Language Objectives:</b>&nbspI will be able to</div>
		<ul>
		<li>use target vocabulary, such as insert, append, and length while improving app features and User Interface with the support of concept definitions and <a href="https://docs.google.com/presentation/d/1n-K4AQ_maHcXekzcfERQ9dxj91nqv9ytwJx4ZkAp8zw/copy" target="_blank" title="">vocabulary notes</a> from this lesson</li>
		</ul>
	</td>
    </tr>
    </tbody>
    </table>
    

Learning Activities
--------------------

.. raw:: html

    <h3>Loops with Lists:</h3>
    <p>
    <a href="https://docs.google.com/presentation/d/1puzK5D_unNI65CMvxNwqPHW6DkDuPq-reuISHST5bMQ/edit?usp=sharing" target="_blank">Presentation slides on Loops with Lists</a></p>
    
.. youtube:: zEZ3F9SgfPE
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    <p>Here is a quick review of comparing AP pseudocode and App Inventor blocks for loops with list: <br/>
    </p>
    
    <img src="../_static/assets/img/AP_Loops.png" />
    
    <!-- Old Table Format
    <table width="90%">
    <tbody>
    <tr><td width="20%">AP Text Pseudocode</td><td width="45%">AP Block Pseudocode</td><td width="35%">App Inventor Block</td></tr>
    <tr> <td>
    <pre>FOR EACH item IN list 
    {
      DISPLAY( item )
    }
    </pre>
    </td>
    <td><div class="yui-wk-div" id="APblocks"><bl class="dark">FOR EACH item IN list 
      <br/>   <bl>DISPLAY <bl> item</bl></bl>
    </bl>
    </div>
    </td> <td><img src="../_static/assets/img/6-3-QuizAppProjectForEachLoop.png" width="400px"/> </td>
    </tr>
    <tr>
    <td>
    <pre>i ←  1 
    REPEAT n TIMES
    {
        DISPLAY( list[i] )
        i ←  i + 1 
    }
     </pre>
    </td>
    <td><div class="yui-wk-div" id="APblocks"><bl>i ← 1 </bl> <br/>
    <bl class="dark">REPEAT n TiMES 
      <br/>   <bl>DISPLAY <bl>list<bl>i</bl></bl></bl>
    <br/>   <bl>i ← <bl>i + 1</bl></bl>
    </bl>
    </div>
    </td> <td><img src="../_static/assets/img/6-3-QuizAppProjectsForLoop.png" width="450px"/> </td>
    </tr>
    <tr><td>questionsList[index]</td><td><div class="yui-wk-div" id="APblocks"><bl>questionsList<bl>index</bl></bl></div></td><td><img src="../_static/assets/img/6-2-QuizAppSelectFromList.png" width="300px"/></td></tr></tbody></table>
    
    -->
    
    Basic operations on lists include:
    <ul>
    <li>Accessing an element by index: list[i] where i is an index from 1 to the length of the list.</li>
    <li>Saving an element of a list into a variable like x:   x ← list[i] 
      </li>
    <li>Assigning a value to an element of a list: 
        <ul>
    <li>list[i] ← x assigns the value of x to list[i].</li>
    <li>list[i] ← list[j] assigns the value of list[j] to list[i].</li>
    </ul>
    </li></ul>
    Some other list operations in AP-style questions are:
    <ul>
    <li>INSERT(list, i, value) : inserts value into the list at index i, moving down all other items at and after i in the list.</li>
    <li>APPEND(list, value): adds value to the end of the list.</li>
    <li>REMOVE(list, i): removes the item at index i and moves up all items after the ith item.</li>
    <li> LENGTH(list): evaluates to the number of elements currently in the given list. 
    </li></ul>
    <h3>Programming and Creative Projects</h3>
    <p>
      For this lesson you can start up 
      <a href="http://ai2.appinventor.mit.edu" target="_blank">App Inventor</a> and open the project 
      you created in the previous lesson.  <!-- Or, if you prefer, you can open App Inventor with the &lt;a target=&quot;_blank&quot; href=&quot;http://ai2.appinventor.mit.edu/?repo=templates.appinventor.mit.edu/trincoll/csp/unit6/templates/QuizApp/QuizAppProjectsTemplate.asc&quot;&gt;Quiz App Projects Template&lt;/a&gt;.--> After opening your Quiz project, rename it <i>QuizProjects2</i>, for  
      Quiz Version 2 -- or something similar to that.  Then complete the  programming exercises described below. 
    </p>
    <p></p>
    <ol>
    <li style="margin-bottom: 5px;"><b>If/else Scoring Algorithm:</b> Modify your app to keep score of how many questions are answered correctly or 
        incorrectly. Be sure to restrict it so that the quiz taker can only receive credit 
        for answering each question once (i.e., if there are three questions, the quiz taker 
        can only be credited with three correct answers).
        Use this <a href="https://docs.google.com/document/d/1g3vEjfz1jBxCAoddWHA2D_CxpY7PPk6Qkw1H90Imxy8/edit?usp=sharing" target="_blank">short handout</a> to guide you with this project.
        
      </li>
    <li style="margin-bottom: 5px;"><b>Loop Algorithm for Searching:</b> Add a keyword search capability to your app.  For example, if the user types in NASA and clicks on the search button, you should find the question or answer with the word NASA in it and show that question.  This will be a linear search through the parallel question and answer lists using a loop. Use this <a href="https://docs.google.com/document/d/1IuSbMQM_NlNplN2pzNRNTD7LduyxAScvmzKz5En1u18/edit?usp=sharing" target="_blank">short handout</a> to guide you with this project.
      </li>
    <li><b>Your Own Quiz App:</b> Use the Quiz App as a template to 
        create a quiz on a topic of your own choosing. Besides changing the questions, 
        answers, and pictures, add at least one enhancement to the app. Be creative! 
      </li>
    </ol>
    

Summary
--------

.. raw:: html

    <p>
    In this lesson, you learned how to:
      <div class="yui-wk-div" id="summarylist">
    </div>
    

Self-Check
-----------

.. raw:: html

    <p>
    <p>You can practice more algorithms with loops and lists below. It is useful to know standard algorithms that use loops like searching for an item in a list, finding the minimum or maximum value in a list, computing the sum or average of a list of values, etc. Using existing algorithms as building blocks for constructing new algorithms has benefits such as reducing development time, reducing testing, and simplifying the identification of errors.</p>
    
    
.. quizly:: mscp-5-6-6
    
    
    :quizname: quiz_scrambled_sum_a_list
    
    <br/>
    
.. mchoice:: mcsp-5-6-1
    :random:
    :practice: T
    :answer_a: Displays 0 which is the minimum (lowest) value in the list.
    :feedback_a: No, 0 is not greater than 1.
    :answer_b: Displays 1 which is the first item in the list.
    :feedback_b: No, 1 is replaced the third time through the loop.
    :answer_c: Displays -1 which is the value of x.
    :feedback_c: No, the items in the list replace x's -1 value.
    :answer_d: Displays 4 which is the maximum (largest) value in the list.
    :feedback_d: That's correct!
    :correct: d

    .. raw:: html
    
    	<p>What does the following code do?</p>
    	<img src="../_static/assets/img/AP_5-6-1.png" width="40%" />

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

    
.. mchoice:: mcsp-5-6-2
    :random:
    :practice: T
    :answer_a: IF (item &gt; 99)  <br>  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; x ← item 
    :feedback_a: No, that would only display 99.
    :answer_b: IF (item &gt; x)  <br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;   x ← item 
    :feedback_b: No, that would find the max item in the list.
    :answer_c: IF (item &lt; 99)  <br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;   x ← item 
    :feedback_c: No, that would display the last item in the list.
    :answer_d: IF (item &lt; x)  <br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;   x ← item 
    :feedback_d: That's correct!
    :correct: d

    .. raw:: html
    
    	<p>Which code below could be placed in the following loop to print out the item in a list that has the lowest (minimum) value?</p>
    	<pre>
    	list ← [1, 0, 4, 2]
    	x ← 99
    	FOR EACH item IN list
    	{      
    		&lt;MISSING CODE&gt;
    	}
    	DISPLAY(x)
    	</pre>


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

    
.. mchoice:: mcsp-5-6-3
    :random:
    :practice: T
    :answer_a: [0, 3, 4, 5]
    :feedback_a: APPEND(list,value) puts the value at the end of the list, while INSERT(list, i, value) puts the value at position i in the list and REMOVE(list,i) removes the ith element.
    :answer_b: [0, 3, 5, 4]
    :feedback_b: APPEND(list,value) puts the value at the end of the list, while INSERT(list, i, value) puts the value at position i in the list and REMOVE(list,i) removes the ith element.
    :answer_c: [1, 3, 5, 4]
    :feedback_c: 
    :answer_d: [1, 2, 3, 4]
    :feedback_d: APPEND(list,value) puts the value at the end of the list, while INSERT(list, i, value) puts the value at position i in the list and REMOVE(list,i) removes the ith element.
    :correct: c

    .. raw:: html
    
    	<p>What are the values in the list after executing the following code:</p>
    	<pre>
    	list ← [ 0, 3, 5 ]
    	APPEND( list, 4 )
    	INSERT( list, 2, 1 )
    	REMOVE( list, 1 )
    	</pre>


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

    <h3>Sample AP CSP Exam Questions</h3>
    
.. mchoice:: mcsp-5-6-4
    :random:
    :practice: T
    :answer_a: &nbsp;<br />IF (IsFound (afternoonList, child))<blockquote>{<br>&nbsp;APPEND (lunchList, child)<br>}</blockquote>
    :feedback_a: 
    :answer_b: &nbsp;<br />IF (IsFound (lunchList, child))<blockquote>{<br>&nbsp;APPEND (afternoonList, child)<br>}</blockquote>
    :feedback_b: 
    :answer_c: &nbsp;<br />IF (IsFound (morningList, child))<blockquote>{<br>&nbsp;APPEND (lunchList, child)<br>}</blockquote>
    :feedback_c: 
    :answer_d: &nbsp;<br />IF ((IsFound (morningList, child)) OR&nbsp;<br><span style="line-height: 1.22;"><span class="Apple-tab-span" style="white-space:pre">    </span>&nbsp; &nbsp;(IsFound (afternoonList, child)))</span><blockquote>{<br>&nbsp;APPEND (lunchList, child)<br>}</blockquote>
    :feedback_d: 
    :correct: a

    .. raw:: html
    
    	<p>A summer camp offers a morning session and an afternoon session.</p>
    	<p>The list <i>morningList</i> contains the names of all children attending the morning session, and the list <i>afternoonList</i> contains the names of all children attending the afternoon session.</p>
    	<p>Only children who attend both sessions eat lunch at the camp. The camp director wants to create <i>lunchList</i>, which will contain the names of children attending both sessions.</p>
    	<p>The following code segment is intended to create <i>lunchList</i>, which is initially empty. It uses the procedure <i>IsFound (list, name)</i>, which returns <i>true</i> if <i>name</i> is found in <i>list</i> and returns <i>false</i> otherwise.</p>
    	<pre>
    	FOR EACH child IN morningList
    	{  
    		&lt;MISSING CODE&gt;
    	}
    	</pre>
    	<br />
    	<p>Which of the following could replace &lt;MISSING CODE&gt; so that the code segment works as intended?</p>


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

    
.. mchoice:: mcsp-5-6-5
    :random:
    :practice: T
    :answer_a:  <br />gradeList[i] ← min (gradeList[i] + 5, 100)
    :feedback_a: 
    :answer_b:  <br />gradeList[i] ← max (gradeList[i] + 5, 100)
    :feedback_b: 
    :answer_c:  <br />gradeList[i] ← gradeList[i] + 5<br />IF (gradeList[i] &gt; 100)<br />{<br />&Tab;gradeList[i] ← gradeList[i] - 5<br />}<br />
    :feedback_c: 
    :answer_d:   <br />gradeList[i] ← gradeList[i] + 5<br />IF (gradeList[i] &gt; 100)<br />{<br />&Tab;gradeList[i] ← 100<br />}<br />
    :feedback_d: 
    :correct: a,d

    .. raw:: html
    
    	<p>A teacher uses the following program to adjust student grades on an assignment by adding 5 points to each student’s original grade. However, if adding 5 points to a student’s original grade causes the grade to exceed 100 points, the student will receive the maximum possible score of 100 points. The students’ original grades are stored in the list <i>gradeList</i>, which is indexed from 1 to <i>n</i>.</p>
    	<pre>
    	i ← 1
    	REPEAT n TIMES
    	{  
    		&lt;MISSING CODE&gt;
    		i ← i + 1
    	}
    	</pre>
    	<p>The teacher has the following procedures available.</p>
    	<img src="../_static/assets/img/Q30Table.png" />
    	<p>Which of the following code segments can replace &lt;MISSING CODE&gt; so that the program works as intended?</p>
    	<p>Select <u>two</u> answers.</p>

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1x3VzmXOmHZXLrQxXO_dHGpGm4AtrvtF5rhuBd_CflFI/edit?usp=sharing" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vS3UDewHm9gq9ws9u5ngDZfYhH08Ry-Nqcim2q6gF58WGQKtN66aZYdGxGwuEA_5uL1FpNEVReVdZBr/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    <!--  &lt;p&gt;Create a page named &lt;b&gt;&lt;i&gt;Quiz App Projects&lt;/i&gt;&lt;/b&gt; under the &lt;i&gt;Creative Projects&amp;nbsp;&lt;/i&gt;category 
        of your portfolio and answer the following questions.
      &lt;/p&gt; 
      &lt;ol&gt;   
        &lt;li&gt; Describe your solution for the first project that added scoring. Why was an extra list necessary? Provide a screenshot of your Answer Button Click event that uses a complex algorithm with the lists.
        &lt;/li&gt;
        &lt;li&gt; Describe your solution for the second project that added a Search button. Provide a screenshot of the search button click code that uses a complex algorithm with loops and lists. Why was a loop necessary?
        &lt;/li&gt;
        &lt;li&gt;Write AP text-style pseudocode for a linear search that searches through a &lt;em&gt;list&lt;/em&gt; to find an item &lt;em&gt;x&lt;/em&gt;. It should display &lt;em&gt;found&lt;/em&gt; if the x is equal to an item in the list.
         &lt;/li&gt;&lt;li&gt;Give brief descriptions of the enhancements you added to your app for the third project, a quiz topic of your own choosing.  Provide screenshots of important blocks and describe how you used them to solve certain programming problems.
        &lt;/li&gt;
         
        
      &lt;/ol&gt;-->
    </div>
    </div>