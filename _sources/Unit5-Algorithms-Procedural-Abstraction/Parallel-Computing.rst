.. raw:: html 

   <div class="logo-header"  id="student-logo"  > <img class="align-center" src="../_static/Mobile_CSP_Logo_White_transparent.png" width="250px"/> </div>

Parallel Computing
======================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
      $(document).ready(function() {
        generateSummary(EKmapping['5.09']);
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
    <h3>Parallel Computing</h3>
     
    
    For hard problems that take a long time to solve, we can sometimes speed up the algorithm by using multiple processors or computers. We can split the workload and compute the parts of the solution in parallel.  
    <ul>
    <li><span class="hover vocab yui-wk-div" data-id='sequential computing'>Sequential computing</span> is a computational model in which operations are performed in order, one at a time on one processor or computer. </li>
    <li><span class="hover vocab yui-wk-div" data-id='parallel computing'>Parallel computing</span> is a computational model where a problem or program is broken into multiple smaller <span class="hover vocab yui-wk-div" data-id='sequential computing'>sequential computing</span> operations some of which are performed simultaneously in parallel. This is usually on one computer with multiple processors, but it could also use multiple computers.</li>
    <li><span class="hover vocab yui-wk-div" data-id='distributed computing'>Distributed computing</span> is a computational model in which multiple networked computers are used to run a program. An algorithm can be both parallel and distributed. </li>
    </ul>
    <img src="../_static/assets/img/parallel.png" width="60%"/>
	<br/>
	<div><b>Learning Objectives:</b>&nbspI will learn to</div>
	<ul>
	<li>compare <span class="hover vocab yui-wk-div" data-id='sequential computing'>sequential</span> and <span class="hover vocab yui-wk-div" data-id='parallel computing'>parallel</span> computing solutions</li>
	<li>determine the efficiencies of <span class="hover vocab yui-wk-div" data-id='sequential computing'>sequential</span> and <span class="hover vocab yui-wk-div" data-id='parallel computing'>parallel</span> computing solutions</li>
	</ul>
	<div><b>Language Objectives:</b>&nbspI will be able to</div>
	<ul>
	<li>use target vocabulary, such as <span class="hover vocab yui-wk-div" data-id="distributed computing">distributed computing</span> and <span class="hover vocab yui-wk-div" data-id="speedup">speedup</span> while describing the benefits and challenges of <span class="hover vocab yui-wk-div" data-id='parallel computing'>parallel computing</span> with the support of concept definitions and <a href="https://docs.google.com/presentation/d/1-IY5fs_ygKlgwUGBD9nX_tx_tFerN7pEeQvdgQIwrdw/copy" target="_blank" title="">vocabulary notes</a> from this lesson</li>
	</ul>


Learning Activities
--------------------

.. raw:: html

    <ul align="center" style="list-style: none; margin: 0; padding: 0; background: lightgrey">
	<li style="display: inline"><a href="https://docs.google.com/document/d/1ZJUHpudn7dl_gP0kuyE0mXysOX7zky9w-xF6j_3QebY" target="_blank" title="">text-version</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="https://youtu.be/bjYS0UKA4dE" target="_blank">YouTube video</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="http://playingcards.io/" target="_blank" title="">Playingcards.io</a></li>
	</ul> 
	
	<br/>
	<div class="pogil yui-wk-div">
    <h3>Searching POGIL Activity</h3>
    
    Each group of four should be given a deck of cards (or use <a href="http://PlayingCards.io" target="_blank" title="">PlayingCards.io</a>) Have one team member time the following tasks:
    <ol><li style="margin-bottom: 5px;"><b>Sequential Algorithm:</b> Have one team member search through the deck of cards one card at a time for the Queen of Hearts (using a linear search) while the rest of the team times them. How long did it take?  If you find the card right away, put the Queen of Hearts near the bottom of the deck, and time the search for it again to record the worst case longest time it takes to find a card sequentially.
    </li>
    <li style="margin-bottom: 5px;"><b>Parallel Algorithm:</b> Start the timer. Divide the group’s deck of cards into four roughly equal stacks of cards and give each team member one stack. And have each team member search through their stack of cards one card at a time in parallel looking for the Queen of Hearts. Yell out "found it" when someone in the group finds it and stop the clock. How long did it take? </li>
    <li><b>Speedup:</b> We can compute the <span class="hover vocab yui-wk-div" data-id='speedup'>speedup</span> of a parallel solution by dividing the time it took to do the task sequentially by the time it took to complete the task in parallel. What is the <span class="hover vocab yui-wk-div" data-id='speedup'>speedup</span> of your search algorithm?</li>
    </ol>
    </div>
    
    <p>We can compare the efficiency of <span class="hover vocab yui-wk-div" data-id='sequential computing'>sequential</span> vs. <span class="hover vocab yui-wk-div" data-id='parallel computing'>parallel</span> solutions by comparing the time it takes them to perform the same task. <span class="hover vocab yui-wk-div" data-id='sequential computing'>A sequential</span> solution takes as long as the sum of all of its steps. In the card activity, in the worst case, you would need to look through 52 cards with the <span class="hover vocab yui-wk-div" data-id='sequential computing'>sequential algorithm</span> to find a particular card. A <span class="hover vocab yui-wk-div" data-id='parallel computing'>parallel computing</span> solution takes as long as its sequential tasks (for example, splitting up the deck of cards into 4 stacks) plus the longest of its parallel tasks (for example, finding the card in parallel). In the <span class="hover vocab yui-wk-div" data-id='parallel computing'>parallel algorithm</span> card activity, the 52 cards were divided into 4 stacks, and the 4 team members each looked through around 13 cards in the worst case to find the card in parallel.</p> 
    <p>The <span class="hover vocab yui-wk-div" data-id='speedup'>speedup</span> of a parallel solution is measured in the time it took to complete the task sequentially divided by the time it took to complete the task when done in parallel. The <span class="hover vocab yui-wk-div" data-id='speedup'>speedup</span> for the card activity could be close to four times as fast with the parallel algorithm. 
        
    </p><h3>Benefits and Challenges in Parallel Computing </h3>
    
    Solutions that use <span class="hover vocab yui-wk-div" data-id='parallel computing'>parallel computing</span> can scale up which means that they can get faster as we add more processors. However, there is a limit to this speed up. <span class="hover vocab yui-wk-div" data-id='parallel computing'>Parallel computing</span> consists of a parallel portion and a sequential portion. The sequential portion is usually before and after the parallel part to divide the workload and combine the results. The time taken is the sum of the time taken in the sequential and parallel parts.  This means the efficiency of the solution is limited by the sequential portion, at some point, adding parallel portions will no longer meaningfully increase efficiency.
    
    <div class="pogil yui-wk-div">
    <h3>Sorting POGIL Activity</h3>
      
    
    Each group of four should be given a deck of cards. Have one team member time the following tasks.
      <ol>
    <li style="margin-bottom: 5px;"><b>Parallel Sorting with 2 processors: </b>One team member should start the timer. Divide the group’s deck of cards into two roughly equal stacks of cards and give two team members each stack. Have each of the two team members sort their stack of cards in parallel. When they are done, have another team member merge together the two stacks into one sorted deck of cards. Stop the timer. How long did it take?</li>
    <li style="margin-bottom: 5px;"><b>Parallel Algorithm with 4 processors: </b>Mix up the cards. Start the timer. Divide the group’s deck of cards into four roughly equal stacks of cards and give each team member one stack. Have each team member sort their stack. Then have one team member merge together the four sorted stacks to make one sorted stack. Stop the timer. How long did it take? </li>
    <li style="margin-bottom: 5px;"><b>Speedup:</b> Was it faster to use four processors instead of two? How was the <span class="hover vocab yui-wk-div" data-id='speedup'>speedup</span> affected by the sequential part of the algorithm which was the merge? </li>
    <li><b>Reflection:</b> What are the benefits and challenges of <span class="hover vocab yui-wk-div" data-id='parallel computing'>parallel computing</span>?
        </li>
    </ol>
    <p>   </p>
    </div>
    <h3>Distributed Computing </h3>
    <p>
    In <span class="hover vocab yui-wk-div" data-id='distributed computing'>Distributed Computing</span>, multiple networked computers are used to solve a problem. <span class="hover vocab yui-wk-div" data-id='Distributed computing'>Distributed computing</span> allows problems to be solved that could not be solved on a single computer because of the required long processing time or large storage needs. And it allows much larger problems to be solved quicker than they could be solved using a single computer.
    </p>
    <img src="../_static/assets/img/distributed.png" width="70%">
    <p>
    Watch the following  <a href="https://www.youtube.com/watch?v=bjYS0UKA4dE" target="_blank">video</a> for <span class="hover vocab yui-wk-div" data-id='distributed computing'>distributed computing</span> in practice at <a href="https://foldingathome.org/" target="_blank">Folding@Home</a>  where you can donate distributed computer time to solve real world problems. They also have a new <a href="https://github.com/FoldingAtHome/coronavirus" target="_blank">initiative to help with COVID-19 research</a>.
    </p>
    
.. youtube:: bjYS0UKA4dE
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    <br/>
    

Summary
--------

.. raw:: html

    <p>
    In this lesson, you learned how to:
      <div class="yui-wk-div" id="summarylist">
    </div>
    <p> </p>
    

Self-Check
-----------

.. raw:: html

    <p>
    Here is a table of some of the technical terms discussed in this
    lesson. Hover over the terms to review the definitions.
    
    <br/>
    <table align="center">
    <tbody>
    <tr>
    <td>
    <span class="hover vocab yui-wk-div" data-id="sequential computing">sequential computing</span>
    <br/><span class="hover vocab yui-wk-div" data-id="parallel computing">parallel computing</span>
    </td>
    <td><span class="hover vocab yui-wk-div" data-id="distributed computing">distributed computing</span>
    <br/><span class="hover vocab yui-wk-div" data-id="speedup">speedup</span>
    </td>
    </tr>
    </tbody>
    </table>
    <br/>
    
.. mchoice:: mcsp-5-9-1
    :random:
    :practice: T
    :answer_a:  60 seconds
    :feedback_a: Since there are only 2 processors available, one of them must do 2 tasks. Combining any 2 of the X, Y, and Z tasks will add up to more than 70 seconds.
    :answer_b:  70 seconds
    :feedback_b: Since there are only 2 processors available, one of them must do 2 tasks. Combining any 2 of the X, Y, and Z tasks will add up to more than 70 seconds.<br>
    :answer_c:  80 seconds
    :feedback_c: If you did process X on processor 1 at the same time as doing process Y and then Z on processor 2, processor 1 would be done in 60 seconds and processor 2 would be done in 80 sections (50+30).&nbsp;
    :answer_d:  90 seconds
    :feedback_d: This would be true if you did process X and Y on processor 1 (60+30 = 90 seconds) but there is a shorter execution time available if you combined processes in another way.
    :correct: c

    .. raw:: html
	    
	    <p><b>AP 2021 Sample Question</b>: A certain computer has two identical processors that are able to run in parallel. Each processor can run only one process at a time, and each process must be executed on a single processor. The following table indicates the amount of time it takes to execute each of three processes on a single processor. Assume that none of the processes are dependent on any of the other processes.</p>
	    <table border="1"><tbody>
	    <tr>
	    	<th>Process</th>
	    	<th>Execution Time on Either Processor</th>
	    </tr>
	    <tr>
	    	<td>X</td>
	    	<td>60 seconds</td>
	    </tr>
	        <tr>
	    	<td>Y</td>
	    	<td>30 seconds</td>
	    </tr>
	    <tr>
	    	<td>Z</td>
	    	<td>50 seconds</td>
	    </tr>
	    </tbody>
	    </table>
	    <br />	
		<p>Which of the following best approximates the minimum possible time to execute all three processes when the two processors are run in parallel?</p> 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

.. mchoice:: mcsp-5-9-2
    :random:
    :practice: T
    :answer_a: 1
    :feedback_a: The “speedup” of a parallel solution is measured in the time it took to complete the task sequentially divided by the time it took to complete the task when done in parallel.<br>
    :answer_b: 1.6
    :feedback_b: speedup = 160 seconds sequential time / 100 seconds parallel time = 1.6
    :answer_c: 2
    :feedback_c: The “speedup” of a parallel solution is measured in the time it took to complete the task sequentially divided by the time it took to complete the task when done in parallel.
    :answer_d: .06
    :feedback_d: Try dividing sequential time / parallel time
    :correct: b

    Consider an algorithm to solve a problem that takes 160 seconds to run on 1 processor. This algorithm can be divided among two processors to solve the same problem in 100 seconds. What is the speedup for this parallel algorithm? 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1xcGKkrASyllF7oos2dAMkZeH7-lJDk5qqg-keTFybTw/copy" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vTIgibTnlTOKs3MsB50DPwM0n_ghaNmwm1nkNSBFpvYI9saxRK57iV7T_CRIgNCyvt0bdrflGqvLUXO/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    </div>
    </img></div>