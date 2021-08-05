.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Paint Pot Refactoring and Procedural Abstraction
================================================

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
            generateSummary(EKmapping['3.05']);
            generateHovers();
			Tipped.create('.vocab', function(element) {
			var vocab = $(element).data('id');
			return vocabulary[vocab];
			}, {
            cache: false,
              position: 'topleft'
              });
    
        });
    </script>
    <h3 id="est-length">Time Estimate: 45 minutes</h3>
    

Introduction and Goals
-----------------------

.. raw:: html

    <p>
    <table><tbody
	<tr>
	    <td colspan=2>
			In this lesson we won’t add new functionality to the Paint Pot app. Instead, we will revise the code, leaving the app’s behavior unchanged. This process is called <span class="hover vocab yui-wk-div" data-id="refactoring">refactoring</span> and programmers do this to improve the quality of their code in various ways -- e.g., to simplify its design, make it easier to read, and easier to maintain. 
			<br/><br/>
			In this case we will introduce the concept of a <b><i>programmer-defined procedure</i></b> that will help reduce the complexity of our code and make it easier to read and maintain. This is an example of <span class="hover vocab yui-wk-div" data-id="procedural abstraction">procedural abstraction</span>, a very important concept and practice in programming. 
		</td>
	</tr>
	<tr>
		<td><img src="../_static/assets/img/GnuScreen.png"/></td>
		<td valign="top">
		<div><b>Learning Objectives:</b>&nbspI will learn to</div>
		  <ul>
		  <li>further navigate the App Inventor online programming platform</li>
		  <li>use a programmer-defined procedure and <span class="hover vocab yui-wk-div" data-id="refactoring">refactor</span> existing code</li>
		  <li>identify, fix, and test <span class="hover vocab yui-wk-div" data-id="computer bug">computer bugs</span></li>
		  </ul>
		  <div><b>Language Objectives:</b>&nbspI will be able to</div>
		  <ul>
		  <li>use target vocabulary, such as <span class="hover vocab yui-wk-div" data-id="refactoring">refactoring</span>, <span class="hover vocab yui-wk-div" data-id="procedural abstraction">procedural abstraction</span>, <span class="hover vocab yui-wk-div" data-id="debugging">debugging</span>, and <span class="hover vocab yui-wk-div" data-id="comment">comment</span> while describing app features and User Interface with the support of concept definitions and <a href="https://docs.google.com/presentation/d/1n-K4AQ_maHcXekzcfERQ9dxj91nqv9ytwJx4ZkAp8zw/copy" target="_blank" title="">vocabulary notes</a> from this lesson</li>
		</ul>
		</td>
	</tr>
    </tbody></table>
    

Learning Activities
--------------------

.. raw:: html

    <p><h3>Refactoring to Improve Code</h3>
    <p>
      Open App Inventor with the <a href="http://ai2.appinventor.mit.edu/?repo=templates.appinventor.mit.edu/trincoll/csp/unit3/templates/PaintPotRefactor/PaintPotRefactorTemplate.asc" target="_blank">Paint Pot Refactor template</a>  in a separate tab and follow 
      along with the video tutorial.   After the project opens, use the Save As option to rename 
      your project PaintPotWithProcedure.</p>
    
.. youtube:: bKbUcoAj6rw
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <p>(<a href="http://www.teachertube.com/video/mobile-csp-paint-pot-refactoring-438785" target="_blank" title="">Teacher Tube version</a>)<br/></p>
    
    <h3>Procedural Abstraction</h3>
    <p>In this lesson, we learned how to create <b>procedures</b> in App Inventor to refactor our code and reduce its complexity. <span class="hover vocab yui-wk-div" data-id="procedural abstraction">Procedural Abstraction</span>, the ability to name a block of code in a procedure and call it whenever needed, is a very important concept in programming. We are abstracting away from the details of that block of code and just using its name to do its job.  We only need to know what it does, not how it does it. </p>
    <p>
    <span class="hover vocab yui-wk-div" data-id="procedural abstraction">Procedural abstraction</span> allows <b>modularity</b> where a solution to a large problem can be found by creating procedures to solve each of the subproblems.  This modularity serves to organize our code by function and reduce its complexity. In addition, it helps with <span class="hover vocab yui-wk-div" data-id="debugging">debugging</span>, code readibility, and maintenance since changes to that block of code only need to happen in one place.  <span class="hover vocab yui-wk-div" data-id="procedural abstraction">Procedural abstraction</span> allows us to reuse code that is already written instead of rewriting the code and repeating it. 
    And it allows programmers to change the internals of the procedure (to make it faster, more efficient, use less storage, etc.) without needing to notify users of the change as long as what the procedure does is preserved.  In Unit 5 in Logo part 2, you will learn to make procedures even more powerful and more abstract by adding parameters to the procedure. </p>
    <p>In the College Board AP exam and Create Performance Task, you will be asked to identify and use procedural abstraction. The following AP pseudocode is used for procedures compared to App Inventor code:
      </p><table>
    <tbody>
    <tr><td style="width:33%;text-align:center">AP Text Pseudocode</td><td style="width:33%;text-align:center">AP Block Pseudocode</td><td style="width:33%;text-align:center">App Inventor Block</td></tr>
    <tr><td style="width:33%;">
    <pre>PROCEDURE name()
    {
     <em>instructions</em>
    }
    </pre>
    </td><td style="width:33%;text-align:center"><div class="yui-wk-div" id="APblocks">
    <bl class="dark">PROCEDURE name <br/>
    <bl>instructions</bl>
    </bl></div></td>
    <td style="width:33%;text-align:center"><img src="../_static/assets/img/procedure.png" width="70%"/></td></tr>
    </tbody></table>
    <h3>Documenting Code by Adding Comments</h3>
    <p>
      Programmers should document a program throughout its development. That is, a programmer should keep detailed documentation while they are developing a program. An important feature of most programming languages, including MIT App Inventor, 
      is the ability to add <span class="hover vocab yui-wk-div" data-id="comment">comments</span> internally to the code.   A <span class="hover vocab yui-wk-div" data-id="comment">comment</span>  is a non-executable block 
      of text that can be added to a program to provide clarification and documentation of the code.   
      Adding <span class="hover vocab yui-wk-div" data-id="comment">comments</span> to one’s code is a standard practice that programmers employ to help others 
      (and themselves) understand their code.
    </p>
    <p>In MIT App Inventor, each non-collapsed block comes with the capability of having a comment 
      added to it.   To access this capability you must <i><b>right-click on the block</b></i> and choose the 
      <b><i>Add Comment option</i></b>.  This will add a small comment-icon, a blue circle with a question mark,  
      to block (as shown here).
      <br/>
    <img src="../_static/assets/img/CommentRightClick.png" width="500"/>
    </p>
    <p>
      To add or edit the <span class="hover vocab yui-wk-div" data-id="comment">comment</span>, simply click on the comment-icon and type in your comment, as shown here:
    </p>
    <br/>
    <img src="../_static/assets/img/CommentDisplayDotsize.png" width="500"/>
    <p>In some programming languages, a form of external documentation may be used, especially if it is not possible to comment directly inside the program code. Some examples of external documentation include using a Google or text document for tracking development, a webpage, or a program index or glossary. MIT App Inventor's has external documentation on <a href="http://appinventor.mit.edu/explore/ai2/support/blocks" target="_blank" title="">Built-in Blocks</a> and on <a href="http://ai2.appinventor.mit.edu/reference/components/" target="_blank" title="">Components</a>. It may be helpful to reference these when building your own apps.</p>
    <p>
      A good commenting practice to follow is to provide <span class="hover vocab yui-wk-div" data-id="comment">comments</span> in the following situations:
      </p><ul>
    <li>To document every procedure that you define, as shown in this example here.</li>
    <li>To clarify a complex algorithm that isn’t clearly obvious.</li>
    <li>To acknowledge code segment(s) used in a program that were written by someone else or are from another source. In this case, the acknowledgement should include the origin source and/or the original author’s name.</li>
    <li>To acknowledge code segment(s) created collaboratively. </li>
    </ul>
    <h3>Debugging</h3>
    
    As your programs get larger, you will run across more <span class="hover vocab yui-wk-div" data-id="computer bug">bugs</span> (errors in your program) and you will have to spend more time <span class="hover vocab yui-wk-div" data-id="debugging">debugging</span> the programs to remove the <span class="hover vocab yui-wk-div" data-id="computer bug">bugs</span>. <span class="hover vocab yui-wk-div" data-id="computer bug">Debugging</span> takes a lot of time in text-based languages like Java because the programmer needs to type in everything exactly in the right case, with the right spelling, and with the right punctuation. App Inventor removes all syntax errors like this because the code is already written for you in the blocks. You do not need to type in any of the code. However, you can still make other errors that you will need to correct. For example, your code might not do what you want it to do. This is a runtime or semantic error.  
    
    Here are some <span class="hover vocab yui-wk-div" data-id="debugging">debugging</span> tips:
    <ul>
    <li>Pretend you are the computer and step through the program line by line and carefully record what happen to see if you can spot the error. This is called <b>tracing</b> the code.</li>
    <li>Put in a <a href="http://ai2.appinventor.mit.edu/reference/components/userinterface.html#Notifier" target="_blank">Notifier</a> block in the UI and then use <b>Notifier.ShowAlert</b> in the blocks to print out the values of different variables to see what they are as you are running the program. Or you could print out the values of variables in a label in your UI.</li>
    <li>Look for error messages that pop up in the blocks editor or on your screen and for red X's in the code that indicate you have errors there. Test your code on specific <b>test-cases</b> that might cause errors.</li>
    <li>Right click on a get block and choose <b>Do It</b> to see its value while it is running. Watch the video below on Do It and see <a href="http://ai2.appinventor.mit.edu/reference/other/testing.html" target="_blank">App Inventor Tips on Debugging</a>.</li>
    </ul>
    <iframe allow="autoplay; encrypted-media" allowfullscreen="" frameborder="0" height="400" src="https://www.youtube.com/embed/Z4ceHVE_L_8?rel=0" width="500"></iframe>
    

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

    Here is a table of the technical terms we've introduced in this lesson. Hover over the terms to review the definitions.
    
    <table align="center">
    <tbody><tr>
    <td><span class="hover vocab yui-wk-div" data-id="comment">comment</span>
    <br/><span class="hover vocab yui-wk-div" data-id="computer bug">computer bug</span>
    <br/><span class="hover vocab yui-wk-div" data-id="debugging">debugging</span>
    </td>
    <td>
    <span class="hover vocab yui-wk-div" data-id="procedural abstraction">procedural abstraction</span>
    <br/><span class="hover vocab yui-wk-div" data-id="refactoring">refactoring</span>
    </td>
    </tr>
    </tbody></table>
	<br/>
    
.. mchoice:: mcsp-3-5-1
    :random:
    :practice: T
    :answer_a: Restructuring a program to make it behave differently. 
    :feedback_a: This will be a challenging concept to learn, but we can all reach this goal. Refactoring does not involve changing a program's basic behavior.
    :answer_b: Changing the way the program behaves. 
    :feedback_b: This will be a challenging concept to learn, but we can all reach this goal. Refactoring does not involve changing a program's basic behavior. 
    :answer_c: Revising a program to remove bugs. 
    :feedback_c: This will be a challenging concept to learn, but we can all reach this goal. Removing bugs would be called <i>debugging</i>.
    :answer_d: Restructuring a program without changing its basic behavior.
    :feedback_d: Right.  A good reason to refactor is to provide a better organization to the code or make it more readable or make it more efficient. 
    :correct: d

    What does refactoring mean?


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    <br/>
    
    .. quizly:: mscp-3-5-2
    
        :quizname: quiz_proc_double
    
    
    .. quizly:: mscp-3-5-3
    
        :quizname: quiz_add_globals
    
    <br/><br/><br/>
    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/10znShyhWjz3gOotsHiiJclU68U6HrPL1UVHAbznUdW4/edit?usp=sharing" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vS0JWbjlAJyzwOppAGB4pWjTNF_3dFqDUsneHzgXI8-Mb12ngnTq7in6eWXjJrJe11XAq0ap0JGZ16D/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    <!--  &lt;p&gt;Create a page named &lt;i&gt;&lt;b&gt;Paint Pot Refactor&lt;/b&gt;&lt;/i&gt; under in your 
        portfolio and give brief answer to the following question:&lt;/p&gt;
      &lt;ol&gt;
        &lt;li&gt;This &lt;a target=&quot;_blank&quot; href=&quot;https://en.wikipedia.org/wiki/Code_refactoring&quot;&gt;Wikipedia article on refactoring&lt;/a&gt; 
          talks about &lt;i&gt;code smell&lt;/i&gt; as one motivation for engaging in refactoring.  What is code smell? Describe briefly 
          two examples of &#39;code smell&#39; and how refactoring would eliminate them.
        &lt;/li&gt;
        &lt;li&gt;Include a screenshot of your procedure in your app. What are the advantages of using procedural abstraction? Try to name at least 2 advantages.&lt;/li&gt;
      &lt;/ol&gt;-->
    </div>
    </div>