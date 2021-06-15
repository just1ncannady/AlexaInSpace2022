.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

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
    <li><b><span class="hover vocab yui-wk-div" data-id='Sequential computing'>Sequential computing</span></b> is a computational model in which operations are performed in order, one at a time on one processor or computer. </li>
    <li><b><span class="hover vocab yui-wk-div" data-id='Parallel computing'>Parallel computing</span></b> is a computational model where a problem or program is broken into multiple smaller <span class="hover vocab yui-wk-div" data-id='sequential computing'>sequential computing</span> operations some of which are performed simultaneously in parallel. This is usually on one computer with multiple processors, but it could also use multiple computers.</li>
    <li><b><span class="hover vocab yui-wk-div" data-id='Distributed computing'>Distributed computing</span></b> is a computational model in which multiple networked computers are used to run a program. An algorithm can be both parallel and distributed. </li>
    </ul>
    <img src="../_static/assets/img/parallel.png" width="60%"/>
    

Learning Activities
--------------------

.. raw:: html

    <div class="pogil yui-wk-div">
    <h3>Searching POGIL Activity</h3>
    
    Each group of 4 should be given a deck of cards (or use <a href="http://PlayingCards.io" target="_blank" title="">PlayingCards.io</a>) Have one team member time the following tasks:
    <ol><li><b>Sequential Algorithm:</b> Have 1 team member search through the deck of cards one card at a time for the Queen of Hearts (using a linear search) while the rest of the team times them. How long did it take?  If you find the card right away, put the Queen of Hearts near the bottom of the deck, and time the search for it again to record the worst case longest time it takes to find a card sequentially.
    </li>
    <li><b>Parallel Algorithm:</b> Start the timer. Divide the group’s deck of cards into 4 roughly equal stacks of cards and give each team member one stack. And have each team member search through their stack of cards one card at a time in parallel looking for the Queen of Hearts. Yell out "found it" when someone in the group finds it and stop the clock. How long did it take? </li>
    <li><b><span class="hover vocab yui-wk-div" data-id='Speedup'>Speedup</span>:</b> We can compute the <span class="hover vocab yui-wk-div" data-id='speedup'>speedup</span> of a parallel solution by dividing the time it took to do the task sequentially by the time it took to complete the task in parallel. What is the <span class="hover vocab yui-wk-div" data-id='speedup'>speedup</span> of your search algorithm?</li>
    </ol>
    <p>   </p>
    </div>
    
    We can compare the efficiency of sequential vs. parallel solutions by comparing the time it takes them to perform the same task. A sequential solution takes as long as the sum of all of its steps. In the card activity, in the worst case, you would need to look through 52 cards with the sequential algorithm to find a particular card. A <span class="hover vocab yui-wk-div" data-id='parallel computing'>parallel computing</span> solution takes as long as its sequential tasks (for example, splitting up the deck of cards into 4 stacks) plus the longest of its parallel tasks (for example, finding the card in parallel). In the parallel algorithm card activity, the 52 cards were divided into 4 stacks, and the 4 team members each looked through around 13 cards in the worst case to find the card in parallel. 
      <p>The <b><span class="hover vocab yui-wk-div" data-id='speedup'>speedup</span></b> of a parallel solution is measured in the time it took to complete the task sequentially divided by the time it took to complete the task when done in parallel. The <span class="hover vocab yui-wk-div" data-id='speedup'>speedup</span> for the card activity could be close to 4 times as fast with the parallel algorithm. 
    
    
    </p><h3>Benefits and Challenges in Parallel Computing </h3>
    
    Solutions that use <span class="hover vocab yui-wk-div" data-id='parallel computing'>parallel computing</span> can scale up which means that they can get faster as we add more processors. However, there is a limit to this speed up. <span class="hover vocab yui-wk-div" data-id='Parallel computing'>Parallel computing</span> consists of a parallel portion and a sequential portion. The sequential portion is usually before and after the parallel part to divide the workload and combine the results. The time taken is the sum of the time taken in the sequential and parallel parts.  This means the efficiency of the solution is limited by the sequential portion, at some point, adding parallel portions will no longer meaningfully increase efficiency.
    
    <div class="pogil yui-wk-div">
    <h3>Sorting POGIL Activity</h3>
      
    
    Each group of 4 should be given a deck of cards. Have one team member time the following tasks:
      <ol>
    <li><b>Parallel Sorting with 2 processors: </b>One team member should start the timer. Divide the group’s deck of cards into 2 roughly equal stacks of cards and give 2 team members each stack. Have each of the 2 team members sort their stack of cards in parallel. When they are done, have another team member merge together the 2 stacks into 1 sorted deck of cards. Stop the timer. How long did it take?</li>
    <li><b>Parallel Algorithm with 4 processors: </b>Mix up the cards. Start the timer. Divide the group’s deck of cards into 4 roughly equal stacks of cards and give each team member one stack. Have each team member sort their stack. Then have one team member merge together the 4 sorted stacks to make 1 sorted stack. Stop the timer. How long did it take? </li>
    <li><b><span class="hover vocab yui-wk-div" data-id='Speedup'>Speedup</span>:</b> Was it faster to use 4 processors instead of 2? How was the <span class="hover vocab yui-wk-div" data-id='speedup'>speedup</span> affected by the sequential part of the algorithm which was the merge? </li>
    <li><b>Reflection:</b> What are the benefits and challenges of <span class="hover vocab yui-wk-div" data-id='parallel computing'>parallel computing</span>?
        </li>
    </ol>
    <p>   </p>
    </div>
    <h3>Distributed Computing </h3>
    <p>
    In <span class="hover vocab yui-wk-div" data-id='Distributed Computing'>Distributed Computing</span>, multiple networked computers are used to solve a problem. <span class="hover vocab yui-wk-div" data-id='Distributed computing'>Distributed computing</span> allows problems to be solved that could not be solved on a single computer because of the required long processing time or large storage needs. And it allows much larger problems to be solved quicker than they could be solved using a single computer.
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
    
    <br/><blockquote>
    <table align="left">
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
    </blockquote>
    <p> </p>
    <br/>
.. mchoice:: mcsp-5-9-1
    :random:
    :practice: T
    :answer_a: (A) 60 seconds
    :feedback_a: Since there are only 2 processors available, one of them must do 2 tasks. Combining any 2 of the X, Y, and Z tasks will add up to more than 70 seconds.
    :answer_b: (B) 70 seconds
    :feedback_b: Since there are only 2 processors available, one of them must do 2 tasks. Combining any 2 of the X, Y, and Z tasks will add up to more than 70 seconds.<br>
    :answer_c: (C) 80 seconds
    :feedback_c: If you did process X on processor 1 at the same time as doing process Y and then Z on processor 2, processor 1 would be done in 60 seconds and processor 2 would be done in 80 sections (50+30).&nbsp;
    :answer_d: (D) 90 seconds
    :feedback_d: This would be true if you did process X and Y on processor 1 (60+30 = 90 seconds) but there is a shorter execution time available if you combined processes in another way.
    :correct: c

    AP 2021 Sample Question: A certain computer has two identical processors that are able to run in parallel.Each processor can run only one process at a time, and each process must beexecuted on a single processor. The following table indicates the amount of timeit takes to execute each of three processes on a single processor. Assume thatnone of the processes are dependent on any of the other processes.ProcessExecution Time on Either ProcessorX 60 secondsY 30 secondsZ 50 secondsWhich of the following best approximates the minimum possible time to execute all three processes when the two processors are run in parallel? 


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
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1xcGKkrASyllF7oos2dAMkZeH7-lJDk5qqg-keTFybTw/edit?usp=sharing" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vTIgibTnlTOKs3MsB50DPwM0n_ghaNmwm1nkNSBFpvYI9saxRK57iV7T_CRIgNCyvt0bdrflGqvLUXO/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    </div>
    </img></div>