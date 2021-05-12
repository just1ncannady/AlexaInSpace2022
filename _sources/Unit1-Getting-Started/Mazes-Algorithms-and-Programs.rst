.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Mazes Algorithms and Programs
=============================

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
        generateSummary(EKmapping['2.02']);
        generateHovers();
        Tipped.create('.vocab', function(element) {
        var vocab = $(element).data('id');
        return vocabulary[vocab];
          }, {
            cache: false,
              position: 'topleft'
        });
      });
      
      var vocabulary = { 
        "algorithm": "An algorithm is a precise sequence of instructions for processes that can be implemented in a programming language and executed by a computer.",
        "control structure": "A control structure is one or more programming language statements that control the flow of a computer program.",
        "sequence": "The sequence control structure is simple a sequence of one or more statements in a computer program",
        "selection": "In a selection structure, a question is asked, and depending on the answer, the program takes one of two courses of action, after which the program moves on to the next event.",
        "repetition":  "A repetition structure, or loop, is used when a program needs to repeatedly process one or more instructions until some condition is met, at which time the loop ends.",
        "iteration": "Iteration is another term for repetition",
      };
    
    </script>
    <h3 id="est-length">Time Estimate: 45 minutes</h3>

Introduction and Goals
-----------------------

.. raw:: html

    <p>
    <h3>Let's do some programming</h3>
    <p>MIT App Inventor  is based on a blocks platform named 
    <a href="https://blockly-demo.appspot.com/static/apps/index.html" target="_blank">Blockly</a>.  This demo
      is from <a href="http://code.org" target="_blank">Code.org</a>'s Hour of Code activity -- maybe you've 
      seen it before?   It will help you get a sense of the type of programming you will be doing in this course.  
      It lets you write small Blockly programs (called <i>scripts</i>) to solve Maze puzzles.  Can you solve all
      20 problems? 
    
    </p><h4>Click on the maze to get started!</h4>
    <a href="http://learn.code.org/hoc/1" target="_blank"><img src="../_static/assets/img/codeorgmaze.png"/></a>
    <h3>Algorithms and Programs</h3>
    <p>As you learned in that activity, an <a href="http://en.wikipedia.org/wiki/Algorithm" target="_blank">algorithm</a> 
      is a sequence of precise instructions that solves some problem or performs some computation.   
      A <i>program</i> is an algorithm that is written in a programming language that runs on a computer and is often referred to as <i>software</i>.  A program can be described by what it does and how the program statements accomplish its function.
      Each of the levels in the previous activity contained <i>code segments</i> which are collections of program statements that are part of a program. 
    
    </p><p>The scripts you created in the Maze demo contain all the essential <i><b>control
    structures</b></i> that programmers use to design algorithms:
    </p><ul>
    <li><b>Sequence</b>.  An algorithm is a sequence of precise statements (blocks).
    </li><li><b>Selection (if/else)</b>. An algorithm can select between two alternative
    paths based on some condition.
    </li><li><b>Repetition or Iteration (repeat)</b>. An algorithm can repeat a sequence of statements.
    </li></ul>
    <h3>Algorithms are Everywhere</h3> 
    
    Now that you've been introduced to the term <i>algorithm</i> and have an initial idea of what it means, you're 
    going to discover algorithms everywhere. As you've grown up, you've learned all sorts of
    algorithms to solve everyday problems.  For example, certainly we all know how to tie our shoelaces. But can you 
    tie your shoelace in 2 seconds?   You could if you follow this algorithm:
    
    
    
    
    
    <br/><br/>
.. youtube:: _aAeI7p-Tkc
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

    <p>Here's an interesting fact:  Computer scientists have 
    <a href="http://en.wikipedia.org/wiki/Structured_program_theorem" target="_blank">proved</a> that sequence, 
    selection, and repetition are sufficient to 
    build any algorithm that can be thought of.  In other words, any algorithm 
    can be expressed using only sequence, selection, and repetition. 
    
    </p><h3>Food for Thought</h3>
    <p>Computer scientists write algorithms to solve problems. 
    And we know now that sequence, selection, and repetition are sufficient to 
    express any algorithm we can think of.  
    
    </p><p>Are there algorithms we <i>can't</i> think of?  Or, to put that another
    way, are there problems that can't be solved by an algorithm?   What do you
    think?
    
    </p><p>That's one of the interesting questions we will take up in this course. In a few weeks, you'll know the answer.
    </p>
    

Summary
--------

.. raw:: html

    <p>
    In this lesson, you learned how to:
      <div id="summarylist">
    </div>
    <h3>Technical Terminology</h3>
    Here is a table of the technical terms that were introduced in this lesson and that will be used throughout the course. 
    You will see tables such as this in many of the lessons.  If you hover over the term, its definition or description will
    pop up.
    
    <table align="center">
    <tbody><tr>
    <td><span class="hover vocab yui-wk-div" data-id="algorithm">algorithm</span>
    <br/><span class="hover vocab yui-wk-div" data-id="control structure">control structure</span>
    <br/><span class="hover vocab yui-wk-div" data-id="sequence">sequence</span>
    </td>
    <td>
    <span class="hover vocab yui-wk-div" data-id="selection">selection</span>
    <br/><span class="hover vocab yui-wk-div" data-id="repetition">repetition</span>
    <br/><span class="hover vocab yui-wk-div" data-id="iteration">iteration</span>
    </td>
    </tr>
    </tbody></table>
    </div>