.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Abstraction Inside the CPU optional
===================================

.. raw:: html

    <div class="MCSP-lesson-content">
    <script>
    $(document).ready(function() {
        generateSummary(EKmapping['4.09']);
        generateHovers();
        Tipped.create('.vocab', function(element) {
        var vocab = $(element).data('id');
        return vocabulary[vocab];
          }, {
            cache: false,
              position: 'topleft'
              });
      });
    
     /* var vocabulary = { 
        "RAM":"RAM (Random Access Memory) stores the computer's programs and data temporarily while power is on.",
        "CPU":"CPU (Central Processing Unit) is that part of the computer's hardware that interprets and runs the computer program.",
        "ALU":"ALU (Arithmetic Logic Unit) is that part of the CPU that performs all logic and arithmetic operations.", 
        "machine langauge": "A machine language is a programming language that is directly readable by the computer’s CPU. It consists entirely of 0s and 1s.",
        "fetch-execute cycle":"The fetch-execute cycle is the basic process performed by the CPU.  On each cycle the CPU fetches the next instruction from RAM, interprets it and executes it.",
        "instruction register":"The instruction register is a special memory location in the CPU that stores the current instruction that is being executed.",
        "instruction counter":"The instruction counter is a special register in the CPU that keeps track of the next instruction to be fetched.",
        "accumulator":"The accumulator is a special register in the CPU where data is put in order to peform arithmetic and logic operations.",
        "assembly language":"An assembly language is low-level language that uses symbolic names, rather than binary sequences of 0s and 1s, to represent the machine language instructions.",
        "overflow error": "An overflow error is an error that occurs when the computer attempts to handle a number that is outside of the defined range of values can be represented."
      };    */    
    </script>
    <h3 id="est-length"><b>Time Estimate: 45 minutes</b></h3>

Introduction and Goals
-----------------------

.. raw:: html

    <p><h3>Abstraction In Hardware and Software</h3>
    <p><strong><em>Abstraction</em></strong> is an important concept in CS -- and justifiably so. 
      In fact, the history of computing can be seen as an advance from very primitive abstractions to very 
      high-level abstractions.
    </p>
    <p>Our App Inventor language is a great example of a very high-level abstraction.   Consider the <em>Camera</em> component. App
      Inventor lets you take a photo by using a single <i>Camera.TakePicture</i> block in your app.  But think about all of the very low-level
      operations that have to take place to focus the camera, gather and convert light rays into pixels and then into bits and then into 
      an image file on your device.  The App Inventor block hides all of that complexity. 
	<p>
		<div><b>Learning Objectives:</b>&nbspI will learn to</div>
		<ul>
		<li>describe how abstractions in the <span class="hover vocab yui-wk-div" data-id="CPU">CPU</span> hide complexity and make a computer easier to use </li>
		<li>explain in detail how the <span class="hover vocab yui-wk-div" data-id="CPU">CPU</span> executes the instrucitons of a program</li>
		</ul>
		<div><b>Language Objectives:</b>&nbspI will be able to</div>
		<ul>
		<li>use target vocabulary, such as <span class="hover vocab yui-wk-div" data-id="machine language">machine language</span>, <span class="hover vocab yui-wk-div" data-id="fetch-execute cycle">fetch-execute cycle</span>, and <span class="hover vocab yui-wk-div" data-id="overflow error">overflow error</span> while describing abstractions within the <span class="hover vocab yui-wk-div" data-id="overflow error">CPU</span>, with the support of concept definitions and <a href="https://docs.google.com/presentation/d/1n-K4AQ_maHcXekzcfERQ9dxj91nqv9ytwJx4ZkAp8zw/copy" target="_blank" title="">vocabulary notes</a> from this lesson</li>
		</ul>

	</p>
    

Learning Activities
--------------------

.. raw:: html
      
    </p><h3>Before There Was Software</h3>
    <!-- &lt;p&gt;&lt;img src=&quot;assets/img/WomenEniac.png&quot; alt=&quot;Women programming ENIAC&quot; width=&quot;187&quot; align=&quot;left&quot; hspace=&quot;20px&quot; vspace=&quot;20px&quot; height=&quot;136&quot;&gt;  -->
    <p>  
      To help us get a sense of this march through ever higher levels of abstraction, we're going to imagine
      ourselves back in the very first days of computing -- to the days before there was such a thing as <em>software</em>, 
      when "programming" was a matter of manually inserting instructions and data into the computer, pressing 
      the "run" switch and hoping for the best.  There were no operating systems and blocks editors back then -- 
      those abstractions came much later.
    </p>
    <p>In the early days of computing, before there was software, virtually all programmers were women. Women
      'computers', as they were called, wrote the first programs on the 
      <a href="https://en.wikipedia.org/wiki/ENIAC" target="_blank" title="">ENIAC</a>, 
      the first digital computer.  But the story of the ENIAC programmers had not been told until just
      recently. Watch the trailer of a new movie. After watching, discuss with your classmates whether or not programmers used the same or different skills compared to what you're learning in this course.</p>
    <!--  &lt;iframe align=&quot;center&quot; src=&quot;https://player.vimeo.com/video/107667129&quot; width=&quot;640&quot; height=&quot;360&quot; frameborder=&quot;0&quot; 
            webkitallowfullscreen mozallowfullscreen allowfullscreen&gt;&lt;/iframe&gt; -->
    <p>
    <a href="https://vimeo.com/107667129" target="_blank">Watch the ENIAC Trailer - Created with Studio G for Google I/O</a> from <a href="https://vimeo.com/user9500462" target="_blank">Kathy Kleiman</a> on Vimeo.</p>
    <a href="https://vimeo.com/107667129" target="_blank"><img alt="Women programming ENIAC" class="yui-img" src="https://upload.wikimedia.org/wikipedia/commons/a/aa/Reprogramming_ENIAC.png" style="max-width: 100%"/></a>
    <h3>4-Bit Computer Simulator</h3>
    <p>The ENIAC weighed 30 tons. But in the hardware of the day it could store only 20 10-digit numbers in its
      <span class="hover vocab yui-wk-div" data-id='accumulator'>accumulators</span> or memory registers. Programs had to be written by hand on paper and once the algorithm
      was figured out, it would often take days to get the program into the ENIAC by manipulating its switches
      and cables. Later on, punched cards like the following were used to input programs or a simple addition calculation.<br/><img src="../_static/assets/img/punchedCard.jpg" width="300px"/><br/></p>
    <img align="right" alt="Gen 0 4-bit" class="yui-img" hspace="20px" src="../_static/assets/img/Gen0.png" title="Gen 0 4-bit" vspace="20px" width="250"/>
    <p>In this lesson, we will use a <a href="https://mobile-csp.org/webapps/computer/gen0.html" target="_blank" title=""> 4-bit Computer Simulator</a> that
      has only 16 8-bit memory locations, so it's not that much 'smaller' than ENIAC. 
      And like the ENIAC, it has little or no software.  This will give you a hands-on sense of what programming was 
      like before we had high-level languages and sophisticated programming platforms.  It's also important to realize
      that the 4-bit Simulator is an accurate model of how today's computers work -- before your App Inventor
      programs can be run on your smart phones, they have to be translated into machine language, where they
      are interpreted by the <span class="hover vocab yui-wk-div" data-id='CPU'>CPU</span>.
    </p>
    <p>The videos and exercises below introduce the <strong><em>4-bit computer simulator</em></strong>. 
    </p>
    <ul>
    <li><b>Generation 0: Programming the raw machine</b>. Just like the ENIAC women did, machine
        language programs have to be put directly into the computer's memory.</li>
    <li><b>Generation 1: Using an Editor and a Loader</b>. Our first software abstractions will be an 
        <em>editor</em>, 
        which will let us type out the machine instructions, and a <em>loader</em>, which will load the instructions 
        into memory for us.</li>
    <li><b>Generation 2. Using an <span class="hover vocab yui-wk-div" data-id='assembly language'>Assembly Language</span></b>. Instead of having to deal with 0s and 1s, our 
        <span class="hover vocab yui-wk-div" data-id='assembly language'>assembly language</span> will give us a higher-level abstraction by letting us deal with 
        symbolic names for instructions and data. </li>
    </ul>
    <p>The simulator models a simple <span class="hover vocab yui-wk-div" data-id='CPU'>CPU</span> <span class="hover vocab yui-wk-div" data-id='fetch-execute cycle'>Fetch/Execute Cycle</span> like below but where the instructions are 1) Fetched from <span class="hover vocab yui-wk-div" data-id='RAM'>RAM</span>, 2) Decoded in the <span class="hover vocab yui-wk-div" data-id='CPU'>CPU</span> 3) Any needed data is fetched from <span class="hover vocab yui-wk-div" data-id='RAM'>RAM</span> and 4) the operation is Executed in the <span class="hover vocab yui-wk-div" data-id='CPU'>CPU</span>.
      <br/><img class="yui-img" src="../_static/assets/img/FetchExecuteCycle.png" width="450px"/>
    <!-- 
    &lt;h2&gt;Ready for a Challenge?&lt;/h2&gt;
    &lt;p&gt;Among other things, this activity is going to require us to use &lt;strong&gt;&lt;em&gt;binary numbers,&lt;/em&gt;&lt;/strong&gt;, which are 
      used for both the machine&#39;s instructions and its data. Also, as you will see, programming in machine language 
      (and <span class="hover vocab yui-wk-div" data-id='assembly language'>assembly language</span>) can be very tedious. It will require great attention to detail
    &lt;/p&gt;
    
    &lt;p&gt;But, if you work through the exercises, the payoff will be well worth it. Not only will you get a better sense 
      of what abstraction is all about. You&#39;ll also get an inside look at what&#39;s going on inside the computer 
      when you are creating and running your apps. Although our 4-bit computer is a very simple 
      model of a real computer, its parts and its functionality provide a reasonable representation of 
      basic computer hardware and software.&lt;/p&gt;
    -->
    </p><p>For each of the simulators below, watch the video and then in groups or pairs, do the self-check exercises after each video.
    </p>
    <p></p><h3>Generation 0: The Raw Machine</h3>
    <p>The video that follows takes us on a tour of the 4-bit computer. Perhaps the easiest way to follow along on 
      the tour is to open the simulator itself in an adjacent tab and <strong><em>pause the video</em></strong> at spots 
      to explore the simulator itself. Here's a 
      <a href="https://mobile-csp.org/webapps/computer/gen0.html" target="_blank" title="">link to the simulator</a> 
      that will open in a separate tab.
    </p>
    <!-- Broken link &lt;gcb-youtube videoid=&quot;sMiCrOpnSdg&quot; instanceid=&quot;fqA3rx45NzH5&quot;&gt;&lt;/gcb-youtube&gt;
    replaced with Ralph&#39;s youtube -->
    
.. youtube:: -70EG8Me1vU
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

    <p>
    
.. mchoice:: mcsp-4-9-1
    :random:
    :practice: T
    :answer_a: The decimal value 3.
    :feedback_a: Yes, when stored in a memory location, 0011 could represent the decimal value 3.  So this is part of the correct answer.
    :answer_b: The machine instruction for ADDing a number to the accumulator
    :feedback_b: Yes, if it occurred in the Instruction Register (IREG) or as part of a machine language program, 0011 would represent the machine language ADD instruction. So this is part of the correct answer. 
    :answer_c: A memory location in the computer's RAM.
    :feedback_c: Yes, memory locations in the 4-bit simulator have addresses that range from 0000 to 1111, so 0011 could be the address of a memory location.  So this is part of the correct answer. 
    :answer_d: The decimal value 17. 
    :feedback_d: If 0011 represents a number, then it would have to be a value between 0 and 15.  The value 17 cannot be represented in 4 bits. So this is not part of the correct answer.  
    :correct: a,b,c

    .. raw:: html
    	
    	<h4>What is 0011?</h4>
    	<p>In the 4-bit computer we can find several occurrences of the 4-bit string, <b>0011</b>. What does this string of bits represent?</p>
    	<p>Choose all answers that apply.</p>


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-4-9-2
    :random:
    :practice: T
    :answer_a: <br />Load the value at 1000 into the Accumulator<br />Add the value in 1001 to the Accumulator<br />Print the value in location 1010<br />Stop  	
    :feedback_a: This algorithm wouldn't work. The sum hasn't been put into location 1010 before printing it. 
    :answer_b: <br />Load the value at 1000 into the Accumulator<br />Add the value in 1000 to the Accumulator<br />Store the Accumulator at location 1010<br />Print the value in location 1010<br />Stop	
    :feedback_b: This algorithm wouldn't work. It would add 1 + 1 and print 2.
    :answer_c: <br />Load the value at 1000 into the Accumulator<br />Add the value in 1001 to the Accumulator<br />Store the Accumulator at location 1010<br />Print the value in location 1010<br />Stop	
    :feedback_c: Yes, that is the correct algorithm. As you can see from the algorithm, in order to add two numbers, the numbers had to be moved into the Accumulator, a special register in the computer's Arithmetic Logic Unit (ALU) where all logic and arithmetic operations are performed. Even though the details are hidden from us now by the sophisticated   software we use, today's computers still work the same way. When you add two numbers in App Inventor, software has to translate your program code into machine language instructions that load the numbers   into the ALU registers before performing the addition and storing the numbers back to RAM. </p>
    :answer_d: <br />Load the value at 1000 into the Accumulator<br />Add the value in 1001 to the Accumulator<br />Store the Accumulator at location 1010<br />Stop	
    :feedback_d: This algorithm wouldn't work. It has no print statement. 
    :correct: c

    .. raw:: html
    
    	<h4>What's the Algorithm?</h4>
    	<p><a href="https://mobile-csp.org/webapps/computer/gen0.html">Generation 0</a> of the 4-bit computer comes pre-loaded with a program that adds 1 and 2 and outputs their sum, 3. The value 1 in decimal is stored in location 1000. And the value 2 is stored in location 1001. Which of the following pseudocode algorithms correctly describes that program's machine language algorithm?</p>


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-4-9-3
    :random:
    :practice: T
    :answer_a: 0
    :feedback_a: Yes, the correct answer is 0. This would be an example of an <b>overflow error</b>. But it would not crash the machine.
    :answer_b: 255
    :feedback_b: No. You would get 255 if you added 0 to 255. 
    :answer_c: 256
    :feedback_c: No. The value 256 cannot be represented at all in 8 bits. In 8 bits you can represent 256 different values, ranging from 00000000 to 11111111, decimal 0 to decimal 255. 
    :answer_d: No value. The machine would crash.
    :feedback_d: No. Adding 1 to 255 in 8 bits causes an overflow error, but it would not crash the machine. 
    :correct: a

    .. raw:: html
    
    	<h4>What's the Output?</h4>
    	<p>Our 4-bit computer uses 8-bit bytes to represent its data. An 8-bit byte can store values ranging from 0 to 255 -- i.e., 00000000 to 11111111.  What do you suppose would happen if you added 1 to 11111111?</p>
    	<p>To help answer this question, you might want to use the <a href="https://mobile-csp.org/webapps/computer/gen0.html">4-bit simulator</a> to write a little machine language program to see what happens. By default, the 4-bit computer adds the values in locations 1000 and 1001 and prints the sum. So here is how you would set up the machine to add 11111111 and 00000001:</p>
    	<ul>
    		<li>Put the value 11111111 (decimal 255) in memory location 1000.</li>
    		<li>Put the value 00000001 (decimal 1) in memory location 1001.
    		<li>Run the program and observe the output.</li>
    	</ul>
    	
    	<p>What decimal value do you get when you add binary 1 to binary 11111111?</p>


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    <p>As you saw in the last self-check exercise, it is easy to see an <span class="hover vocab yui-wk-div" data-id='overflow error'>overflow error</span> when the 4-bit computer attempts to handle a number that is larger than the memory it has available. Even modern computers can occasionally have an <span class="hover vocab yui-wk-div" data-id='overflow error'>overflow error</span> when the computer attempts to handle a very large number that is outside of the defined range of values can be represented.</p><p>
    </p>

	<h3>Generation 1: Machine Language Programming</h3>

    <p>
    <p>
    <a href="https://mobile-csp.org/webapps/computer/gen1.html" target="_blank" title="">Generation 1</a>  
      of the 4-bit computer comes with some <b><i>system software</i></b>, software that today
      would be considered part of the computer's operating system. It provides an 
      <i><b>editor</b></i>, which is software that lets you compose a machine language 
      program, and a <i><b>loader</b></i>, software that will load the program into memory. This was similar to using  punched cards to load in a program into a computer in the 1950s-1970s.
    </p>
    <p>
      It also represents the first step toward a <b><i>higher-level abstraction</i></b> by 
      freeing us from having to directly input values into the machine's
      memory.  Instead, we can just type the program in the editor and the software
      will figure out how to load it into memory. 
    </p>
    <p>
      The following video will show you how this works.
    </p>
    
.. youtube:: _7-44rIkc24
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

    <p>
    
.. fillintheblank:: mcsp-4-9-4

    .. raw:: html
    
    	<h4>What's the Output?</h4>
    	<p>As you saw in the <a href="https://www.youtube.com/watch?v=qFMH6fI_oFQ">demo video</a>, the 4-bit editor requires you to organize your program as follows:</p>
    	<pre>
    	Data initialization statements
    	Machine language instructions
    	</pre>
    	<p>Type the following machine language program into the editor --   just the 0s and 1s part, not the pseudocode comments,   which begin after the --.</p>
    	<br />
    	<table border="1"><tbody>
    	<tr>
    		<td>1000:00001111</td>
    		<td width="8px"></td>
    		<td>-- Initialize memory location 1000 to 00001111</td>
    	</tr>
    	<tr>
    		<td>1001:00001000</td>
    		<td width="8px"></td>
    		<td>-- Initialize memory location 1001 to 00001000</td>
    	</tr>
    	<tr>
    		<td>00011000</td>
    		<td width="8px"></td>
    		<td>-- Loads value at memory location 1000 into ACC</td>
    	</tr>
    	<tr>
    		<td>01011001</td>
    		<td width="8px"></td>
    		<td>-- Multiplies value at memory location 1001 to ACC</td>
    	</tr>
    	<tr>
    		<td>00101010</td>
    		<td width="8px"></td>
    		<td>-- Stores value in ACC to location 1010</td>
    	</tr>
    	<tr>
    		<td>10001010</td>
    		<td width="8px"></td>
    		<td>-- Prints the value currently in location 1010</td>
    	</tr>
    	<tr>
    		<td>00000000</td>
    		<td width="8px"></td>
    		<td>-- Stops the program</td>
    	</tr>
    	</tbody></table>
    	<br /><br />
    	<p>Then click the "Load" button to load it into memory and then run   the program.  What value does it output?</p>

    - :120: The correct answer is 120. The program multiplies the numbers 15 x 8, which equals 120. 
      :x: Don't forget the colon in the data initialization statements. 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

	<h3>Generation 2: Assembly Language Programming</h3>

    <p>
    <p>
    <a href="https://mobile-csp.org/webapps/computer/gen2.html" target="_blank" title="">Generation 2</a> 
      of the 4-bit computer introduces some additional software in the form of an <span class="hover vocab yui-wk-div" data-id='assembly language'>assembly language</span>.  
      Assembly languages were the first step in the direction of raising the level of abstraction used in writing 
      and debugging programs.  It's not a big step beyond machine language.  But it does succeed in hiding some 
      of the machine's underlying complexity, including the need to remember binary opcodes, memory addresses and 
      data values.
    </p>
    
      The following video will show you how this works.<br/>  
.. youtube:: L5TamiB3Bf0
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

    

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
    <p>Here are a couple of additional assembly language problems:
      </p><ul>
    <li>Write an assembly language program that computes the square function for any valur x -- i.e., <i>f(x) = x<sup>2</sup></i>. HINT:  
          You'll need to use the <i>INP</i> operation to input the value for <i>x</i>.  Once you have your program working,
          use it to help answer this question:  Given that the 4-bit computer
          can only represent the numbers between 0 and 255, what's the largest value for <i>x</i> for which your program will work?
        </li>
    <li>Write an assembly language program that computes the value <i>f(a,b) = a<sup>2</sup> + b</i>.  HINT: Be economical. 
          This program will barely fit into the 4-bit computer's memory. 
        </li>
    </ul>
    <p>The <a href="http://eniacprogrammers.org/see-the-film/" target="_blank">story of the ENIAC programmers</a> 
      is now told in a short documentary film that is freely available for viewing. If you 
      want to watch it individually it is 20 minutes long (and may cost $5 to stream it). 
    </p>
    
    
Self-Check
-----------

.. raw:: html

    <p>Here is a table of the technical terms introduced in this lesson. Hover over the terms to review the definitions.</p>
    <table align="center">
    <tbody>
    <tr>
    <td><span class="hover vocab yui-wk-div" data-id="RAM">RAM</span>
    <br/><span class="hover vocab yui-wk-div" data-id="CPU">CPU</span>
    <br/><span class="hover vocab yui-wk-div" data-id="ALU">ALU</span>
    <br/><span class="hover vocab yui-wk-div" data-id="machine langauge">machine language</span>
    <br/><span class="hover vocab yui-wk-div" data-id="fetch-execute cycle">fetch-execute cycle</span>
    </td>
    <td><span class="hover vocab yui-wk-div" data-id="instruction register">instruction register</span>
    <br/><span class="hover vocab yui-wk-div" data-id="instruction counter">instruction counter</span>
    <br/><span class="hover vocab yui-wk-div" data-id="accumulator">accumulator</span>
    <br/><span class="hover vocab yui-wk-div" data-id="assembly language">assembly language</span>
    <br/><span class="hover vocab yui-wk-div" data-id="overflow error">overflow error</span>
    </td>
    </tr>
    </tbody>
    </table>
    
.. fillintheblank:: mcsp-4-9-5
    :casei:

    .. raw:: html
    	
    	<h4>What's the Output?</h4>
    	<p>As you saw in the <a href="https://www.youtube.com/watch?v=-3URMbryRrM">demo video</a>, <a href="https://mobile-csp.org/webapps/computer/gen2.html">Generation 2</a> of the 4-bit computer lets you use an assembly language to program the  machine. Here's an example:</p>
    	<pre>
    	VAR A 10
    	VAR B 0
    	LDA A
    	MUL A
    	STA B
    	PRN B
    	NOP
    	</pre>
    	<br />
    	<p>Type that program into the Editor and then assemble, load, and run it. What output do you get?</p>

    - :100: The correct answer is 100.  The program multiplies 10 x 10.  
      :x: Make sure you type in the program exactly as given. The opcodes and variable names are <i><b>case sensitive</b></i>.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>
    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1RkiX9q2eGBUqN2EACD0cwpf7ODSHJc1y9wpLNZKjIuU/edit?usp=sharing" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vQIjox6utw5m-GJFxbvAAwtBh94A7Zdr2YoOOMnFdA4QGTbcGHhpAV4hAVWC_7zyqTmly4SmjIKQBh5/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    <!--  &lt;p&gt;Create a page named &lt;i&gt;&lt;b&gt;Abstraction: Inside the CPU&lt;/b&gt;&lt;/i&gt; under the &lt;i&gt;Reflections&lt;/i&gt; category of your portfolio and answer the following questions:&lt;/p&gt;
      &lt;ol&gt;
        &lt;li&gt;Which generation of the 4-bit simulators above is the most abstract? Why?&lt;/li&gt;
        &lt;li&gt;Explain the purpose or function of the RAM and the CPU.&lt;/li&gt;
        &lt;li&gt;Describe in your own words the difference between the fetch and execute steps.&lt;/li&gt;
        &lt;li&gt;Summarize the differences between assembly language and machine language programming.&lt;/li&gt;
      &lt;/ol&gt;-->
    </div>
    </div>