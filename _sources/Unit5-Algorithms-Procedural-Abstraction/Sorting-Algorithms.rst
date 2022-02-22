.. raw:: html 

   <div class="logo-header"  id="student-logo"  > <img class="align-center" src="../_static/Mobile_CSP_Logo_White_transparent.png" width="250px"/> </div>

Sorting Algorithms
==================

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
            generateSummary(EKmapping['5.04']);
            generateHovers();
    
        });
    </script>
    <h3 id="est-length">Time Estimate: 45 minutes</h3>
    

Introduction and Goals
-----------------------

.. raw:: html

    <p>
    <p>This lesson will focus on different sorting algorithms and we will use a deck of 
    cards in some of the examples.   If you have a deck of cards handy, it may 
    help you understand the algorithms better. Alternatively, you can use <a href="http://PlayingCards.io" target="_blank" title="">PlayingCards.io</a>.</p><p>Sorting is a very important area of study in computer science. As we saw in the previous
    lesson on <i>Search</i>, it is much more efficient to search a collection if its elements
    are in order.  <i>Sorting</i> is the process of putting objects in order. Sorting
    algorithms have been studied extensively by computer scientists.</p>
    
	<div><b>Learning Objectives:</b>&nbspI will learn to</div>
	<ul>
	<li>apply sorting algorithms to given data sets</li>
	<li>identify the strengths and weaknesses of the bubble sort, merge sort, and bucket sort algorithms</li>
	<li>describe the difference between comparison sorts such as bubble sort and merge sort, and non-comparison sorts such as bucket sort.</li>
	</ul>
	<div><b>Language Objectives:</b>&nbspI will be able to</div>
	<ul>
	<li>use target vocabulary, such as bubble sort, merge sort, bucket sort, and radix sort, while considering algorithms for sorting data sets, with the support of concept definitions and <a href="https://docs.google.com/presentation/d/1-IY5fs_ygKlgwUGBD9nX_tx_tFerN7pEeQvdgQIwrdw/copy" target="_blank" title="">vocabulary notes</a> from this lesson</li>
	</ul>

Learning Activities
--------------------

.. raw:: html

    <ul align="center" style="list-style: none; margin: 0; padding: 0; background: lightgrey">
	<li style="display: inline"><a href="https://youtu.be/aQ9f0rXhuQ4" target="_blank" title="">YouTube Video Bubble Sort</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="https://youtu.be/CWjOwaqeYpA" target="_blank">YouTube Video Merge Sort</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="https://youtu.be/je0bBZxfmMM" target="_blank">YouTube Video Bucket Sort</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="http://playingcards.io/" target="_blank" title="">PlayingCards.io</a></li>
	</ul> 
	
	<h3>Bubble Sort</h3>
	<p>One of simplest sorting algorithms is the <i>bubble sort</i>.  Here's a video
    that demonstrates a version of the bubble sort on a collection of 13 playing cards.  
    As you watch it, see if you can discover the algorithm.
    
    
.. youtube:: aQ9f0rXhuQ4
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    </p>
    <p>
      Bubble sort is an example of a <i><b>comparison sort</b></i>.  It repeatedly
      compares two cards, placing the smaller one on the left pile.   As you can see, bubble sort 
      makes several <i>passes</i> through the cards?
    </p>
    <p>
      The bubble sort is so-called because on each <i>pass</i> through the data, 
      the highest value "bubbles" to the top.  For example, in the video, after the first pass,
      the <i>Ace</i> is placed on the sorted pile. On the second pass, a <i>Queen</i> is
      placed on the sorted pile.  And so on.
    </p>
	
	<p><h3>Pseudocode for Bubble Sort</h3>
    <p>Here is a <i>pseudocode</i> description of the bubble sort as seen in the video:
    
    </p><pre><font color="blue"><b>To Bubble Sort a deck of N cards:</b></font>
    Place the unsorted deck, face down, in the right hand pile.
    <b>Repeat</b> N times
        Put the top card of the right pile in your hand.
        <b>Repeat</b> until there are no more cards in the right pile.
            <b>If</b> the card in your hand &gt; the top card on the right pile
                Place top card on the left pile.
            <b>Else</b>
                Place the hand card on the left pile.
        When the pass is finished, put the card left in your hand on the sorted pile.
        Move the left pile to the right pile.
    </pre>
    
.. fillintheblank:: mcsp-5-4-1
    :casei:

    In the bubble sort demo, 13 cards are being sorted.  How many passes does this version of the algorithm require to sort the cards? |blank|

    - :13: Right.  For a deck of 13 cards, this version of bubble sorts makes 13 passes through the deck.   On the last pass, there was only 1 card left in the unsorted deck, but we can still consider that a pass. There are different versions of bubble sort, some of which would say that N-1 passes are made through the deck to sort N cards.
      :x: For a deck of 13 cards, this version of bubble sorts makes 13 passes through the deck if we count placing the last card on the sorted pile as a pass. There are different versions of bubble sort, some of which would say that N-1 passes are made through the deck to sort N cards.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    <h3>Activity</h3>Using a physical deck of cards or <a href="http://playingcards.io/" target="_blank" title="">PlayingCards.io</a>, try to use the bubble sort algorithm to sort a
    small part of the deck – six or seven cards.
    
    <h3>Merge Sort</h3>
    <p><i><b>Merge sort</b></i> is another comparison sorting algorithm,
    so called because it merges the cards into ever larger piles of cards.  
    See if you can follow the algorithm.
    
    
.. youtube:: CWjOwaqeYpA
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    </p><p>As you can see, merge sort starts with the cards in piles of 1 card each.
    Then on each pass, it merges them into piles of 2 cards, then 4 cards, then 8 cards,
    and so on,  until all the cards are merged into one sorted pile.   You probably also 
    noticed that it was quite a bit faster than bubble sort.
    
    </p><h3>Pseudocode of Mergesort</h3>
    
    Here is a pseudocode description of merge sort as seen in the video:
    
    <p></p><pre><font color="blue">
    <b>To Merge Sort a deck of N cards:</b></font>
    Divide the cards into N piles containing one card each.
    <b>Repeat</b> until there is 1 pile containing all <i>N</i> cards:
        Merge adjacent piles into new piles that are twice as big.
    </pre>
    <p>As you can see, <i>Merge sort</i>, like binary search, is another example of 
     a <b>divide and conquer</b> approach to solving the problem,
    so-called, because it breaks the big problem into smaller problems and works on the
    smaller problems.  In this case, the deck is divided into piles of 1 card each before
    merging the piles.
    
    </p><h3>Activity</h3>Using a physical deck of cards or <a href="http://playingcards.io/" target="_blank" title="">PlayingCards.io</a>, try sorting it using merge sort.  If you try the
    algorithm on 16 cards, you will always have the same number of cards in each pile. 
    
    <h3>Bucket Sort: A Non Comparison Sort</h3>
    <p>Not all sorts are <i>comparison</i> sorts.   One example of a non-comparison sort, 
    is the <i><b>bucket sort</b></i>, which uses some feature of the values being sorted
    to place them into distinct buckets.  The buckets are then combined together.   
    
    </p><p>In this video, the buckets are the values of the cards -- i.e., 2, 3, Jack, Ace, and so on.
    
    
.. youtube:: je0bBZxfmMM
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    <br/>
    <br/>
    </p><p>As you see, bucket sort does not compare one card with another.  Rather,
    it uses the card's value to place it into the appropriate bucket.  Once all the cards
    are in their buckets, they are collected together in order.  This
    sort is the fastest of the three examples we've considered. 
    
    </p><h3>Pseudocode for Bucket Sort</h3>
    <p>In order for bucket sort to work, you would have to be able to perform some  calculation 
    that would convert the item being sorted into a number that can be used to identify 
    its bucket. For example,  we could use
    the following scheme to give numbers to our playing cards:
    
    </p><table>
    <tbody><tr><th>Card</th><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td>
    <td>9</td><td>10</td><td>Jack</td><td>Queen</td><td>King</td><td>Ace</td></tr>
    <tr><th>Bucket</th><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td>
    <td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td></tr>
    </tbody></table>
    <p>We have simply given numerical values (called <i>ranks</i>) to each of the face cards. 
     Now if we have 13 buckets, numbered 2 through 14, then we could use the following 
    algorithm to bucket sort them:
    
    </p><p></p><pre><font color="blue">
    <b>To Bucket Sort a deck of N cards:</b></font>
    1. For each card in the deck, put it into the bucket indicated by its rank.
    2. Starting with the lowest numbered bucket, collect all the cards together.
    </pre>
    <h3>Activity</h3>
    <p>That's it.  Pretty simple, eh? Using a physical deck of cards or <a href="http://playingcards.io/" target="_blank" title="">PlayingCards.io</a>, try it with the full 52-card
    deck.  After step 1, bucket number 2 should contain all the 2s in the deck.  Bucket 
    number 14 should contain all the Aces. If you collect all the cards together in buckets 2, then
    3, then 4, and so on, the deck will be completely sorted.
    
    </p>
    <h3>Radix Sort</h3>
    <p>Bucket sort is actually an example of a more general 
    non-comparison sort called <i><b>radix</b></i>.  The word <i>radix</i> is another 
    word for <i>base</i> and the original idea behind 
    radix sorting is to sort numbers by their digits.  
    
    </p><p>For example, suppose we want to sort
    the following list of base 10 2-digit numbers.  For convenience we will use leading 0s for 
    numbers between 1 and 9:
    
    </p><pre>25 26 01 31 24 22 17 16 07 09
    </pre>
    <p>We begin by putting them in buckets based on their <i>least significant digit</i> –
    their rightmost digit.
    
    </p><table>
    <tbody><tr><td>Buckets</td><td>0s</td><td>1s</td><td>2s</td><td>3s</td><td>4s</td><td>5s</td><td>6s</td><td>7s</td>
    <td>8s</td><td>9s</td></tr>
    <tr><td>Values</td><td> </td><td>01</td><td>22</td><td> </td><td>24</td><td>25</td><td>26</td>
    <td>17</td><td> </td><td>09</td></tr>
    <tr><td> </td><td> </td><td>31</td><td> </td><td> </td><td> </td><td> </td><td>16</td>
    <td>07</td><td> </td><td> </td></tr>
    </tbody></table>
    <p>Now if we take the numbers out of the buckets from left to right and from top to bottom in each bucket we get
    the following list:
    
    </p><pre>01 31 22 24 25 26 16 17 07 09
    </pre>
    <p>Now let's put them into buckets by their left-most digit: 
    
    </p><table>
    <tbody><tr><td>Buckets</td><td>0s</td><td>1s</td><td>2s</td><td>3s</td><td>4s</td><td>5s</td><td>6s</td><td>7s</td>
    <td>8s</td><td>9s</td></tr>
    <tr><td>Values</td><td>01</td><td>16</td><td>22</td><td>31</td><td> </td><td> </td><td> </td>
    <td> </td><td> </td><td> </td></tr>
    <tr><td> </td><td>07</td><td>17</td><td>24</td><td> </td><td> </td><td> </td><td> </td>
    <td> </td><td> </td><td> </td></tr>
    <tr><td> </td><td>09</td><td> </td><td>25</td><td> </td><td> </td><td> </td><td> </td>
    <td> </td><td> </td><td> </td></tr>
    <tr><td> </td><td> </td><td> </td><td>26</td><td> </td><td> </td><td> </td><td> </td>
    <td> </td><td> </td><td> </td></tr>
    </tbody></table>
    
    If we now take the numbers out of the buckets from left to right and from top to bottom we get the following sorted list:
    <pre>01  07 09 16 17 22 24 25 26 31
    </pre>
    <p>As you can probably see, we can sort numbers of any size by re-using the buckets as 
    we sort them through successive passes starting with their rightmost digit and working to 
    their leftmost digit.
    
    </p><p>
    
    Here's a really cool example of radix sort on the playground.  In this example, the kids are sorting 
    3 digit numbers using 9 buckets.  First the sort by the ones digit. Then regroup in order.  
    Then by the tens digit.  Then regroup in order. And then by the hundreds digit. 
    Then regroup, at which point the numbers are sorted.   
    (Notice there's no bucket for '0' in this example.  So none of their numbers contain a 0.)<br/>
    
.. youtube:: ibtN8rY7V5k
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    </p>
    <h3>Recap</h3>
    <p>To review all of the sort algorithms explained above, try taking a look through some animations of each sort. Go to <a href="http://www.sorting-algorithms.com/" target="_blank" title="">Sorting Algorithms Visualizations</a> or on <a href="https://visualgo.net/sorting" target="_blank">Visualgo</a>.</p>
    

Summary
--------

.. raw:: html

    <p>
    In this lesson, you learned how to:
      <div id="summarylist">
    </div>
    
Still Curious?
---------------

.. raw:: html

    <p>
    <ul>
    <li>This discussion of <a href="http://en.wikipedia.org/wiki/Merge_sort">Merge Sort</a>
    includes a nice animation.
    </li><li>An accessible analysis of <a href="http://en.wikipedia.org/wiki/Radix_sort">Radix Sort</a>.
    </li><li>Even President Obama knows about bubble sort:
    <br/>
.. youtube:: k4RRi_ntQc8
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    </li>
    </ul>

Self-Check
-----------

.. raw:: html

    <p>
    
.. mchoice:: mcsp-5-4-2
    :random:
    :practice: T
    :answer_a: Arranging a deck of cards from the lowest to the highest value cards. 
    :feedback_a: True. Bubble sort would be appropriate for sorting cards by their face value
    :answer_b: Looking up a name in the phone book.
    :feedback_b: Let me add new information to help you solve this...a bubble sort would not be appropriate for looking up a name in the phone book. That's a search problem.
    :answer_c: Sorting a stack of paper money into denominations -- i.e., $1, $5, $10 etc. 
    :feedback_c: True. Bubble sort would be appropriate for sorting paper money by their denominations since we know that $1 come before $5 and $5 come before $10, etc.
    :answer_d: Sorting a basket of laundry into socks, shirts, shorts, and sheets. 
    :feedback_d: Let me add new information to help you solve this...a bubble sort would not be appropriate for sorting the laundry, unless you, imposed some rule that socks come before shirts which come before sheets, and so on.
    :answer_e: Arranging books on a bookshelf by author's last name. 
    :feedback_e: True. Bubble sort would be appropriate for arranging books by author's last name since arranging by last name means sorting them in alphabetical order by last name.
    :correct: a,c,e

    For which of the problems would the bubble sort algorithm provide an appropriate solution. Choose all that apply. 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-5-4-3
    :random:
    :practice: T
    :answer_a: 16
    :feedback_a: This will be a challenging concept to learn, but we can all reach this goal. 16 is not the highest number in the list and therefore will not 'bubble up' to the right of the list.
    :answer_b: 17
    :feedback_b: That's right! The largest value, 17, would 'bubble up' to the right of the list during the first pass. 
    :answer_c: 9
    :feedback_c: This will be a challenging concept to learn, but we can all reach this goal. 9 is not the highest number in the list and therefore will not 'bubble up' to the right of the list.
    :answer_d: -1
    :feedback_d: This will be a challenging concept to learn, but we can all reach this goal. Since you are sorting in ascending order, the highest value in the list should appear on the right of the list after the first pass.
    :answer_e: 5
    :feedback_e: This will be a challenging concept to learn, but we can all reach this goal. 5 is not the highest number in the list and therefore will not 'bubble up' to the right of the list.
    :correct: b

    Suppose you are sorting the following list of numbers in ascending order using bubble sort: [16, 5, -1, 4, 12, 17, 3, 10, 5, 9]. After the first pass through the numbers, what value would appear on the right of the list? 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-5-4-4
    :random:
    :practice: T
    :answer_a: apple
    :feedback_a: If it were easy, you wouldn’t be learning anything! Sorting the list into alphabetical order means the word that comes last alphabetically would 'bubble up' to the right of the list.
    :answer_b: squash
    :feedback_b: If it were easy, you wouldn’t be learning anything!
    :answer_c: tomato
    :feedback_c: That's right! The largest value, tomato, would 'bubble up' to the right of the list during the first pass. 
    :answer_d: pumpkin
    :feedback_d: If it were easy, you wouldn’t be learning anything!
    :answer_e: papaya
    :feedback_e: If it were easy, you wouldn’t be learning anything!
    :correct: c

    Suppose you are sorting the following list of words into alphabetical order using bubble sort: [apple, orange, banana, papaya, lemon, pumpkin, squash, tomato]. After the first pass through the list, what word would appear on the right of the list? 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-5-4-5
    :random:
    :practice: T
    :answer_a: [apple, banana, lemon, tomato, orange, squash, papaya, pumpkin] 
    :feedback_a: Try asking a classmate for advice—s/he may be able to explain/suggest some ideas or recommend some strategies.
    :answer_b: [apple, banana, lemon, squash, tomato, orange, papaya, pumpkin] 
    :feedback_b: Try asking a classmate for advice—s/he may be able to explain/suggest some ideas or recommend some strategies.
    :answer_c: [apple, banana, lemon, orange, papaya, pumpkin, tomato, squash] 
    :feedback_c: Try asking a classmate for advice—s/he may be able to explain/suggest some ideas or recommend some strategies.
    :answer_d: [apple, banana, lemon, orange, papaya, pumpkin, squash, tomato] 
    :feedback_d: That's right! The two largest values, squash and tomato, would 'bubble up' to the right of the list after two passes. 
    :answer_e: [apple, banana, lemon, orange, papaya, squash, tomato, pumpkin] 
    :feedback_e: Try asking a classmate for advice—s/he may be able to explain/suggest some ideas or recommend some strategies.
    :correct: d

    Suppose you are sorting the following list of words in alphabetical order using bubble sort: [apple, banana, lemon, tomato, orange, squash, papaya, pumpkin]. Which of the following gives the correct order of the list after two passes through the list? 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>
    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1mu1KSZfleHLa1FS8aswV3XPamxrcQzqquG57o2iad-E/copy" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vQa6jCuERGNzpL3PvPNmC_NInIGL--vTlZhyfVcOdme1bghblRPty-sz6G_UkuUCkVCrsKesUSFwcxj/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    <!--Create a page named &lt;i&gt;&lt;b&gt;Sort Algorithms&lt;/b&gt;&lt;/i&gt; under the &lt;i&gt;Reflections&lt;/i&gt; 
    category of your portfolio and answer the following questions:
    
    &lt;ol&gt;
       &lt;li&gt;Bubble and Merge Sort are referred to as comparison sorts because the values of the two pieces of data are compared during each step. Why are the radix and bucket sort not comparison sorts?&lt;/li&gt;
       &lt;li&gt;Which sort do you think would be the fastest if you had to sort more than one deck of cards (i.e. as the amount of data to be sorted increases)? Why?&lt;/li&gt;
    &lt;/ol&gt;-->
    </div>
    </div>