.. raw:: html 

   <div class="logo-header"  id="student-logo"  > <img class="align-center" src="../_static/Mobile_CSP_Logo_White_transparent.png" width="250px"/> </div>

Coin Flip Experiment (optional)
===============================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
      $(document).ready(function() {
        generateSummary(EKmapping['4.06']);
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
        "model":"A model is an abstraction that provides a simplified representation of some complex object or phenomenon.",
        "PRNG":"A pseudo random number generator (PRNG) is an algorithm that generates a sequence of numbers that seems random but is actually completely predictable.",
        "fair coin":"A fair coin is one that when flipped would come up heads 50% of the time over a large number of coin flips.",
        "hypothesis":"A hypothesis is an explanation that can be tested by experimentation.",
      };      */
    </script>
    <h3 id="est-length">Time Estimate: 45 minutes</h3>
    

Introduction and Goals
-----------------------

.. raw:: html

    <p>
    <table><tbody>
	<tr>
		<td colspan=2>
			<b><i>Coin Flip Experiment</i></b>.  
			In this lesson you will use a slightly modified version of the app that you built in the preceding lesson, the <i>Coin Flip Simulation</i> tutorial.</p>
			<p>The <i>CoinFlipExperiment</i> app will let you conduct an experiment aimed at determining how good App Inventor’s pseudorandom number 
			generator (<span class="hover vocab yui-wk-div" data-id='PRNG'>PRNG</span>) is.  The app will let you quickly "flip a coin" many times and display the results.</p>
			<p>In this lesson you will run the app several times, record and tally the results, 
			and calculate the percentage of heads. The expectation is that as you flip a coin more times, the percentage of heads should approach 50%.</p>
		</td>
	</tr>
	<tr>
		<td valign="top">
			<iframe allowfullscreen="" frameborder="0" height="285" src="https://www.youtube.com/embed/XoAoL6dGdCE" width="300"></iframe>
			<!-- 
			  (&lt;a target=&quot;_blank&quot; href=&quot;http://www.teachertube.com/video/358491&quot;&gt;Teacher Tube version&lt;/a&gt;)
			-->
		</td>
		<td valign="top">
			<div><b>Learning Objectives:</b>&nbspI will learn to</div>
			<ul>
			<li>use software to conduct an experiment</li>
			<li>make and test a <span class="hover vocab yui-wk-div" data-id='hypothesis'>hypothesis</span> about App Inventor's ability to generate random numbers</li>
			</ul>
			<div><b>Language Objectives:</b>&nbspI will be able to</div>
			<ul>
			<li>represent data in a table, explore the results of a simulation, and test my <span class="hover vocab yui-wk-div" data-id="hypothesis">hypothesis</span>
			<li>use target vocabulary, such as <span class="hover vocab yui-wk-div" data-id="PRNG">PRNG</span>, <span class="hover vocab yui-wk-div" data-id="fair coin">fair coin</span>, and <span class="hover vocab yui-wk-div" data-id="hypothesis">hypothesis</span> while using an app to examine a <span class="hover vocab yui-wk-div" data-id="model">model</span>, with the support of concept definitions and <a href="https://docs.google.com/presentation/d/1YsJJ7IwEEpQGLqSizFhIFJVIw5TfDc5LqDtCSD-o42E/copy" target="_blank" title="">vocabulary notes</a> from this lesson</li>
			</ul>
		</td>
	</tr>
    </tbody></table>
    

Learning Activities
--------------------

.. raw:: html

    <ul align="center" style="list-style: none; margin: 0; padding: 0; background: lightgrey">
	<li style="display: inline"><a href="https://docs.google.com/document/d/123rmkHfSoBGoPazKLNw9mBh69_WXJJKchNHbgsa0ID0" target="_blank" title="">text-version</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="https://docs.google.com/document/d/1L458KOn6izBLdrWSwkALekLqBocSe9ijJT9WCvBcbRc/copy" target="_blank">POGIL worksheet</a></li>
	</ul> 
	
	<p><h3>Background</h3>
    <p>Here are some things you should know  about how computers and computer languages (App Inventor) implement randomness:</p>
    <ul>
    <li>Randomness is used in lots of programs, especially games (Android Mash) and simulations (Coin Flip, 4-bit Computer Simulator).</li>
    <li>Creating a truly random process is hard to do.  And creating a truly random process in a computer is no exception.</li>
    <li>Because creating true randomness is hard, computers use algorithms known as <span class="hover vocab yui-wk-div" data-id="PRNG">pseudo random number 
        generators (PRNGs)</span> to simulate randomness.  This is much easier to do than generating truly random numbers. If 
      you are curious about how <span class="hover vocab yui-wk-div" data-id="PRNG">PRNG</span>s work, the 
        next lesson goes into the details.</li>
    <li><span class="hover vocab yui-wk-div" data-id="PRNG">PRNG</span>s generate a sequence of "random seeming" numbers.</li>
    <li><span class="hover vocab yui-wk-div" data-id="PRNG">PRNG</span>s are <span class="hover vocab yui-wk-div" data-id="model">models</span> of true randomness.  As such, they can be 'good' or 'bad' depending on how well they <i><b>approximate</b></i> true randomness. Much research by mathematicians and computer scientists goes into creating good <span class="hover vocab yui-wk-div" data-id="PRNG">PRNG</span>s.</li>
    <li>App Inventor uses a standard and well established <span class="hover vocab yui-wk-div" data-id='PRNG'>PRNG</span>, which should do a good job of modeling randomness.</li>
    </ul>
    <h3>The Experiment</h3>
    <p>Our CoinFlip app simulates flipping a coin.  If you had a <span class="hover vocab yui-wk-div" data-id='fair coin'>fair coin</span>
    and you flipped it many, many times -- maybe a million times -- then if it were truly
    fair, you would expect it to come up "Heads" half the time.  That's why we say for
    any coin flip, it has a 50:50 chance of coming up heads.
    
    </p><p>App Inventor's <i><b>random integer block</b></i> uses its <span class="hover vocab yui-wk-div" data-id='PRNG'>PRNG</span> to
    generate a random sequence of integers.  In our app, the sequence is between 1
    and 2 inclusive.  So, if the <span class="hover vocab yui-wk-div" data-id='PRNG'>PRNG</span> is good, it should generate a 1 half the time and
    a 2 half the time.  And this, in turn, should let our Coin Flip app be a good <span class="hover vocab yui-wk-div" data-id='model'>model</span>
    of flipping a coin.
    <br/><img alt="App Inventor's random integer block" src="http://appinventor.mit.edu/explore/sites/all/files/UserGuide/blocks/math/randomint.png"/>
    </p>
    <h3>Hypothesis</h3>
    <p>Our <span class="hover vocab yui-wk-div" data-id='hypothesis'>hypothesis</span> is that App Inventor’s random integer block is a 
    good approximation  of the process of randomly generating a 1 half the time and a 
    2 half the time.
    </p>
    <p>If you were testing that a particular coin was “fair”, you would flip it lots of times 
    and record the number of heads and tails.  Their ratio should come out 50:50.  
      But you have to do <i>a lot</i> of flips.
    </p>
    <p>So, to test our <span class="hover vocab yui-wk-div" data-id='hypothesis'>hypothesis</span> about App Inventor’s random integer block, we 
    have to perform a simulated “coin flip” lots of times.  To help with this, we will 
    use the <i>Coin Flip Experiment</i> app, which will let us repeatedly “flip” a coin. 
    The app uses an algorithm that uses the random integer block.  If the random 
    integer block is a good approximation of randomness, we would expect that 
    when it is used to <span class="hover vocab yui-wk-div" data-id='model'>model</span> the process of flipping a coin, it would make the odds 
    of getting a “Heads” or “Tails” 50:50. 
    </p>
    <p>For our <span class="hover vocab yui-wk-div" data-id='hypothesis'>hypothesis</span> to be true, the ratio between “Heads” and “Tails” in the app 
    should approximate 50:50 as the number of trials gets large.  The more trials 
    we perform, the closer our ratio should be to 50:50.   
    </p>
    <p>If the ratio does approach 50:50, that would validate our <span class="hover vocab yui-wk-div" data-id='hypothesis'>hypothesis</span>.  
    If it does not, that would prove that our <span class="hover vocab yui-wk-div" data-id='hypothesis'>hypothesis</span> is invalid.  
    </p>
    <h3>Download and Install the App</h3>
    
    If you have an Android mobile device, use the AI Companion app (or a barcode scanner app like <a href="https://play.google.com/store/apps/details?id=com.google.zxing.client.android&amp;hl=en" target="_blank">ZXing Barcode Scanner</a>)  to scan this QR code to download and install the app directly 
    to your mobile device.  If you have an iOS device or are using the emulator, you will not be able to directly download and install an app, so download the 
    <a href="http://ai2.appinventor.mit.edu/?repo=templates.appinventor.mit.edu/trincoll/csp/unit4/templates/CoinFlipExperiment/CoinFlipExperimentV1.asc">source .aia file</a> and import it into App Inventor and use the Connect/AI Companion to try it on your iOS device or Connect/Emulator. (Note: If you are having problems installing the app, you can use this <a href="http://www.shodor.org/interactivate/activities/Coin/" target="_blank" title="Coin Toss Simulator">Coin Toss Simulator</a> website. If your Internet connection is not very good, you could also install the app ahead of time or at home so that it's available even without Internet.)<br/>
    <img height="300px" src="../_static/assets/img/CoinFlipExperimentV1_2019QRCode.png"/>
    <h3>Reading the Source Code</h3>
    
    Here is the source code for the app that is performing the experiment.  
    As you can see, it is only slightly different from the version you created 
    in the tutorial.  The difference is an if statement after inputting N from 
    the text box.  The statement checks that N is a number (not the empty string) 
    and that it’s no greater than 100,000.  <br/>
    <img src="../_static/assets/img/CoinflipExperimentBlocks.png" width="600"/>
    <br/>
    <div class="pogil yui-wk-div">
    <h3>POGIL Activity for the Classroom (30 minutes)</h3> 
      Break into POGIL teams of 4.  Each team member should download the coin flip app and
      run it on his or her device.  Record your answers <a href="https://docs.google.com/document/d/1L458KOn6izBLdrWSwkALekLqBocSe9ijJT9WCvBcbRc/edit" target="_blank">using this worksheet</a>. (File-Make a Copy to have a version you can edit.) In addition, team members should take the following roles.
        <table>
    <tbody><tr><th>Role</th><th>Responsibility</th></tr>
    <tr>
    <td>Facilitator</td>
    <td>Records the teams data -- i.e., the number of flips and the number of heads
              for each run of the app. Tallies the results and calculates the percentage
              of heads and tails.</td>
    </tr>
    <tr>
    <td>Spokesperson</td>
    <td>Reports the teams results.</td>
    </tr>
    <tr>
    <td>Quality Control</td>
    <td>Validates the Facilitator's data -- are the results of each run recorded 
              correctly. Are the tallies and calculations correct?</td>
    </tr>
    <tr>
    <td>Process Analyst</td>
    <td>Keeps track of the teams progress and assesses its performance.</td>
    </tr>
    </tbody></table>
    <h3>Experimental Procedure</h3>
    <p>Our <span class="hover vocab yui-wk-div" data-id='hypothesis'>hypothesis</span> for this experiment: <i><b>App Inventor's <span class="hover vocab yui-wk-div" data-id='PRNG'>PRNG</span> provides a good <span class="hover vocab yui-wk-div" data-id='model'>model</span> of randomness</b></i>.</p>
    <p>Perform the following steps.</p>
    <ol><li style="margin-bottom: 5px;">Repeatedly run the app on each device and record the number of heads and tails received in each trial.  
        Do at least 20 runs (<b>trials</b>) among the team. The maximum number of "flips" per trial is 100.
        Your team should have at least 2000 "flips".
        </li>
    <li style="margin-bottom: 5px;">Tally your results and calculate the percentage of heads for each trial.  In addition, calculate
          the cumulative number and percentage of heads after each trial. For example, after the 5th trial of 100
        flips, your table will show the number and percentage of heads for 500 flips.</li>
    <li style="margin-bottom: 5px;">(<b>Portfolio</b>) Record your teams results for each trial in a neatly organized table.  That is, if you did 20 trials
          of 100 coin flips each, your table should have 20 rows of results, with the percentage for 
          each trial along with the cumulative numbers. Here's an example:
          <blockquote style="font-size: 1.0em;" >
    <table><tbody><tr><th>Trial</th><th>Flips</th><th>Heads</th><th>% Heads</th><th>Total Flips</th><th>Total Heads</th><th>Total % Heads</th></tr>
    <tr><td>1</td><td>10000</td><td>4950</td><td>49.5</td><td>10000</td><td>4950</td><td>49.5%</td></tr>
    <tr><td>2</td><td>10000</td><td>5040</td><td>50.4</td><td>20000</td><td>9990</td><td>49.95%</td></tr>
    </tbody></table>
    </blockquote>
          Here is a Google <a href="https://docs.google.com/spreadsheets/d/1pmbjF_A6Kc1-X3a5nTdsf8YNYuAOwuEt7jotG0V_XQc" target="_blank">spreadsheet</a>
          that you can use to record your data.  Just enter your data in columns B and C.  The rest of the columns will be calculated
          automatically. 
        </li>
    <li style="margin-bottom: 5px;">(<b>Portfolio</b>) According to your results, does App Inventor's <span class="hover vocab yui-wk-div" data-id='PRNG'>PRNG</span> provide a good <span class="hover vocab yui-wk-div" data-id='model'>model</span> of randomness?
        </li>
    <li>(<b>Portfolio</b>) A friend claims that flipping a coin 100 times and 
          finding that it comes up heads only 45% of the time shows that the coin is biased. How
          should you reply?
        </li>
    </ol>
    <!-- &lt;a target=&quot;_blank&quot; href=&quot;https://docs.google.com/spreadsheets/d/1_2gAzhHdXZfIZDV-8ZKoDsTWeAXnqbrFFxY9TfhRvUg&quot;&gt;Experimental results spreadsheet&lt;/a&gt;  -->
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
    <p>Hopefully this lesson has made you curious about how <span class="hover vocab yui-wk-div" data-id="PRNG">PRNGs</span> work.  If so, you should check out <a href="https://runestone.academy/runestone/books/published/mobilecsp/Unit4-Animation-Simulation-Modeling/Pseudo-Random-Numbers.html" target="_blank" title="">this lesson</a>, which shows how to use some simple mathematics to create a <span class="hover vocab yui-wk-div" data-id="PRNG">PRNG</span>.</p>

Self-Check
-----------

.. raw:: html

    <p>
    
    
    Here is a table of the technical terms introduced in this lesson. Hover over the terms to review the definitions.
    <table align="center">
    <tbody>
    <tr>
    <td><span class="hover vocab yui-wk-div" data-id="model">model</span>
    <br/><span class="hover vocab yui-wk-div" data-id="PRNG">PRNG</span>
    <br/><span class="hover vocab yui-wk-div" data-id="fair coin">fair coin</span>
    <br/><span class="hover vocab yui-wk-div" data-id="hypothesis">hypothesis</span>
    </td>
    </tr>
    </tbody>
    </table>    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1eFQL9FGxU_Zdv-ATW7N_2McwraXtF1Bm9yGcHXXp0vE/copy" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vQzjr01cqLqLou_Bab8bSh_LHMuFYW0glMpTmC7b295YODGrv_npqOMZIXFQD13Bb7O_K1sNdSWC6av/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    <!--&lt;p&gt;Create a page named &lt;b&gt;&lt;i&gt;App Inventor&#39;s PRNG&lt;/i&gt;&lt;/b&gt; under the
    &lt;i&gt;Reflections&lt;/i&gt; category of your portfolio and answer the following questions.
    &lt;/p&gt;
    
    &lt;ol&gt;
        &lt;li&gt;(&lt;b&gt;POGIL&lt;/b&gt;) Record your team&#39;s results for each run in a neatly organized table.  That is, if you did 20 runs
          of 100 coin flips each, your table should have 20 rows of results, with percentages for each row and totals at the bottom.
        &lt;/li&gt;
        &lt;li&gt;(&lt;b&gt;POGIL&lt;/b&gt;) According to your results, does App Inventor&#39;s PRNG provide a good model of randomness?
        &lt;/li&gt;
        &lt;li&gt;(&lt;b&gt;POGIL&lt;/b&gt;) A friend claims that flipping a coin 100 times and 
          finding that it comes up heads only 45% of the time shows that the coin is biased. How
          should you reply?
        &lt;/li&gt;
    &lt;!-- &lt;li&gt;Do you notice any kind of trend as the number of trials (coin flips) increases?  
    Discuss what you expected to happen and what you observed?
    &lt;/li&gt;
    
    &lt;li&gt;What does this experiment tell you about App Inventor’s <span class="hover vocab yui-wk-div" data-id="PRNG">PRNG</span>?  Is it ‘good’?
    &lt;/li&gt;
    
    &lt;li&gt;How many trials should be performed in order to draw a conclusion one way 
    or the other about our <span class="hover vocab yui-wk-div" data-id="hypothesis">hypothesis</span>?
    &lt;/li&gt;
    
    
    &lt;li&gt;Because we are using a coin flip app, this experiment really tests only that
      App Inventor&#39;s &lt;i&gt;random integer&lt;/i&gt; block generates a 1 around half the time.
      Is this a sufficient test for App Inventor&#39;s PRNG?  What other experiments might
      you do to increase your confidence in App Inventor’s PRNG?
    &lt;/li&gt;
    
    &lt;/ol&gt;-->
    </div>
    </div>