.. image:: ../../_static/MobileCSPLogo.png
    :width: 250
    :align: center
    
I Have a Dream Tutorial
========================

.. raw:: html

    <!-- Might not need - jquery should be built in  
    <script src="../code.jquery.com/jquery-1.11.3.min.js" type="text/javascript"></script>
    <link href="../code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css" rel="stylesheet"/>
    <script src="../code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
   -->
   <!-- downloaded custom script files -->
    <script src="../../_static/assets/lib/lessons/tipped.js" type="text/javascript"></script>
    <script src="../../_static/assets/lib/Framework2020.js" type="text/javascript"></script>
    <link href="../../_static/assets/lib/lessons/tipped.css" rel="stylesheet" type="text/css"/>
    <link href="../../_static/assets/lib/lessons/lessons.css" rel="stylesheet" type="text/css"/>
    <script src="../../_static/assets/lib/vocabulary.js" type="text/javascript"></script>

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
      /*
      var vocabulary = { 
        "Input" : "Input  is data sent to a computer for processing by a program and can be tactile, audible, visual, or text",
        "Output" : "Output is the data sent back from the program to the device and can be tactile, audible, visual, or text.",
        "User Interface" : "The part of computer application through which a user interacts with a program.",
        "UI Components" : "Parts of the user interface such as Buttons, Labels, etc.",
        "User Events" : "Actions by the user such as button clicks.",
        "Event-driven Programming" : "In event-driven programming, the program is activated by events such as button clicks.",
        "Event Handler" : "A block of code that reacts to an event like a button click.",
        "IDE" : "An IDE is software that provides comprehensive tools for programming such as UI design, code editing, and a way to interpret and run the program."

      };*/
    </script>

    <h3 id="est-length">Time Estimate: 45 minutes</h3>

    <!-- added style -->
    <style>    td { text-align: left; padding: 5px; } </style>
    <table><tbody>
      <tr><td><iframe allowfullscreen="" frameborder="0" height="420" src="https://www.youtube.com/embed/pQ0zjP-VC2E" width="315"></iframe>
      <br/>(<a href="http://www.teachertube.com/video/358482" target="_blank">Teacher Tube version</a>)</td>
    <td>
      <p><b><i>I Have a Dream!</i></b> is an educational &quot;soundboard&quot; app that plays the famous speech of Martin Luther King. This is a great example of a socially-useful app which provides multimedia education on African-American history and the civil rights movement.</p>
      <p><b>Objectives:</b> In this lesson you will learn to:</p>
      <ul>
        <li>follow an instructor-led walkthrough to create the <i>I Have a Dream</i> app on a mobile device;
        </li><li>navigate the App Inventor programming platform;
        </li><li>develop your understanding of what an App Inventor program is;
        </li><li>develop your understanding of event handlers.
        </li>
      </ul>
        </td></tr>
      </tbody></table>

Tutorial
---------

.. raw:: html

    <!-- <h2>Tutorial</h2> -->

    <p>To get started, <a href="http://ai2.appinventor.mit.edu/?repo=templates.appinventor.mit.edu/trincoll/csp/tutorials/aias/IHaveADreamStarter.asc" target="_blank">
    open the I Have a Dream Starter project with the embedded tutorial in App Inventor</a> and login with your Google account into App Inventor.
      <!-- &lt;a target=&quot;_blank&quot; href=&quot;http://ai2.appinventor.mit.edu/?repo=templates.appinventor.mit.edu/trincoll/csp/unit2/templates/IHaveADreamStarter/IHaveADreamStarter.asc&quot;&gt;
    open the I Have a Dream Starter project in App Inventor&lt;/a&gt; -->
     Follow along with your teacher or the following video tutorial. You can also use the embedded tutorial in the template or the <a href="https://drive.google.com/open?id=1Bg64PZclbPwhFg8Qg2GZJw5hVC08tDIFBhs5bBbyves" target="_blank">text-version of this tutorial</a> or the <a href="https://drive.google.com/open?id=1x9KDcEIyXwC7_h-bRJQCe-sIuXpQTGSRUnONxMs-MLA" target="_blank">short handout</a>. NOTE: The video below asks you to open a starter app, but if you
      use the link above the IHaveADreamStarter app will already be loaded and you can start following the video at time 1:12. </p>


.. youtube:: KDepcRIfnNs
    :width: 650
    :height: 415
    :align: center

.. raw:: html

    <!-- Replaced video tag 
    <p id="QBSRy5iS9gEk">
        <script src="../modules/core_tags/_static/js/youtube_video.js"></script>
        <script>gcbTagYoutubeEnqueueVideo("KDepcRIfnNs", "QBSRy5iS9gEk");</script>
    </p> -->

    <!-- does not resize
    &lt;iframe width=&quot;700&quot; height=&quot;400&quot; src=&quot;https://www.youtube-nocookie.com/embed/KDepcRIfnNs?start=72&quot; frameborder=&quot;0&quot; allow=&quot;accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture&quot; allowfullscreen=&quot;&quot;&gt;&lt;/iframe&gt; -->

    <p>(<a href="http://www.teachertube.com/video/mobile-csp-i-have-a-dream-tutorial-437861" target="_blank" title="">Teacher Tube version</a>)</p>

    <!-- Replace <h2>'s with RST subsections <h2>Input/Output</h2> -->

Input/Output
------------

.. raw:: html

    <p><img src="../../_static/assets/img/phoneIO.png" style="float:left;margin:2px" width="250px"/> 

    Our mobile devices and computers are built to interact with us. The mobile apps that you create will also communicate with users by getting <b>input</b> from the users and displaying <b>output</b> to the users. Input  is data sent to a computer for processing by a program, and output is the data sent back from the program to the device.  Program output is usually based on a program’s input or prior state (e.g., internal values or variables). Input and output can come in many forms, such as <b>tactile</b> (for example touching a button or the device vibrating), <b>audible</b> (a sound), <b>visual</b> (an image), or <b>text</b>. Try listing all the forms of input and output in the I Have a Dream app!  </p>

    <p>Designing a good <b>user interface</b> (UI) for a program is very important! User Experience (UX) designers are very much in demand. Most programs and apps these days are <b>event-driven programming</b>, which means they display the UI and wait for a <b>user event</b>, for example for the user to touch a button as input.  In event-driven programming, program statements are executed when triggered rather than through the sequential flow of control.
    Events are triggered when a key is pressed, a mouse is clicked, a program is started by another application, etc., and they supply input data to a program and trigger different blocks of code in the program that influence its behavior.  A program needs to work for a variety of inputs and situations!</p>

     <!--   <h2 id="summary">Summary</h2> -->
     
Summary
--------

.. raw:: html

    In this lesson, you learned how to:
      <div id="summarylist">
      </div>

    <h2 id="self-check" style="clear:both">Self-Check</h2>
    <b>Vocabulary:</b><br/>
    <table align="center">
    <tbody><tr>
      <td>
        <span class="hover vocab yui-wk-div" data-id="Input">Input</span>
        <br/><span class="hover vocab yui-wk-div" data-id="Output">Output</span><br/>
            <span class="hover vocab yui-wk-div" data-id="User Interface">User Interface (UI)</span>
        <br/><span class="hover vocab yui-wk-div" data-id="UI Components">UI Components</span>

      </td>
      <td>

      <span class="hover vocab yui-wk-div" data-id="User Events">User Events</span>
      <br/>
        <span class="hover vocab yui-wk-div" data-id="Event-driven Programming">Event-driven Programming</span>
        <br/><span class="hover vocab yui-wk-div" data-id="Event Handler">Event Handler</span>
       <br/><span class="hover vocab yui-wk-div" data-id="IDE">Integrated Development Environment (IDE)</span>
      </td>
      </tr>
    </tbody></table>




    <p>Complete the following self-check exercises. Please note that you should login if you want your answers saved and scored. In addition, some of these exercises will not work in Internet Explorer or Edge browsers. We recommend using Chrome.</p>
    
    <!-- Replaced one question with RST -->
    
.. mchoice:: mcsp-2-2-1

   What type of input does the I have a Dream app expect?
   
   - tactile
   
     + Correct!
   
   - audible
   
     - Incorrect
   
   - visual
   
     - Incorrect
   
   - text
   
     - Incorrect
   

.. raw:: html

          <div class="qt-check-answer">
            <button class="gcb-button qt-check-answer-button">

               Check Answer 
            </button>
          </div>


        <div class="qt-feedback qt-hidden" role="alert">
        </div>
      </div>

    </div></div><div><div class="gcb-border-box">
      <link href="../modules/assessment_tags/resources/questions.css" rel="stylesheet" type="text/css"/>
      <script>
        questionData['i33Fd4m7xDzN'] = JSON.parse(window.atob("eyJkZWZhdWx0RmVlZGJhY2siOiAiIiwgIndlaWdodCI6IDEuMCwgInNob3dBbnN3ZXJXaGVuSW5jb3JyZWN0IjogZmFsc2UsICJjaG9pY2VzIjogW3sidGV4dCI6ICJ0YWN0aWxlIiwgInNjb3JlIjogMC4wLCAiZmVlZGJhY2siOiAiIn0sIHsidGV4dCI6ICJhdWRpYmxlIiwgInNjb3JlIjogMS4wLCAiZmVlZGJhY2siOiAiIn0sIHsidGV4dCI6ICJ2aXN1YWwiLCAic2NvcmUiOiAwLjAsICJmZWVkYmFjayI6ICIifSwgeyJ0ZXh0IjogInRleHQiLCAic2NvcmUiOiAwLjAsICJmZWVkYmFjayI6ICIifV0sICJwZXJtdXRlQ2hvaWNlcyI6IGZhbHNlLCAicXVpZCI6ICI1MzAwMDQyNTIwODU0NTI4IiwgImFsbE9yTm90aGluZ0dyYWRpbmciOiBmYWxzZX0="));
        var assessmentTagMessages = {};


        assessmentTagMessages.correct = "Correct. ";

        assessmentTagMessages.incorrect = "Incorrect. ";

        assessmentTagMessages.partiallyCorrect = "Partially Correct. ";


        assessmentTagMessages.correctAnswer = " Yes, the answer is correct. ";

        assessmentTagMessages.incorrectAnswer = " No, the answer is incorrect. ";

        assessmentTagMessages.partiallyCorrectAnswer = " The answer is partially correct. ";


        assessmentTagMessages.correctAnswerHeading = "The correct answer is:";

        assessmentTagMessages.targetedFeedbackHeading = "Targeted Feedback:";

        assessmentTagMessages.feedbackHeading = "Feedback:";


        assessmentTagMessages.yourScoreIs = " Your score is: ";
      </script>
      <script src="../modules/assessment_tags/resources/grading_lib.js"></script>
      <script src="../modules/assessment_tags/resources/grading.js"></script>
      <noscript>
        &lt;div class=&#39;qt-warning&#39;&gt;

           JavaScript should be enabled to grade this question. 
        &lt;/div&gt;
      </noscript>




      <div class="qt-mc-question qt-standalone" id="i33Fd4m7xDzN">
        <div class="qt-points">
          <em>


              1 point

          </em>
        </div>

        <div class="qt-question">What type of output does the I have a Dream app generate?</div>
        <div class="qt-choices">

            <div>
              <input data-index="0" id="i33Fd4m7xDzN.0" name="i33Fd4m7xDzN" type="radio"/>
              <label for="i33Fd4m7xDzN.0">
                tactile
              </label>
            </div>

            <div>
              <input data-index="1" id="i33Fd4m7xDzN.1" name="i33Fd4m7xDzN" type="radio"/>
              <label for="i33Fd4m7xDzN.1">
                audible
              </label>
            </div>

            <div>
              <input data-index="2" id="i33Fd4m7xDzN.2" name="i33Fd4m7xDzN" type="radio"/>
              <label for="i33Fd4m7xDzN.2">
                visual
              </label>
            </div>

            <div>
              <input data-index="3" id="i33Fd4m7xDzN.3" name="i33Fd4m7xDzN" type="radio"/>
              <label for="i33Fd4m7xDzN.3">
                text
              </label>
            </div>

        </div>


          <div class="qt-check-answer">
            <button class="gcb-button qt-check-answer-button">

               Check Answer 
            </button>
          </div>


        <div class="qt-feedback qt-hidden" role="alert">
        </div>
      </div>

    </div></div><div><div class="gcb-border-box">
      <link href="../modules/assessment_tags/resources/questions.css" rel="stylesheet" type="text/css"/>
      <script>
        questionData['jbEsdK1NvFeJ'] = JSON.parse(window.atob("eyJkZWZhdWx0RmVlZGJhY2siOiAiIiwgIndlaWdodCI6IDEuMCwgInNob3dBbnN3ZXJXaGVuSW5jb3JyZWN0IjogZmFsc2UsICJjaG9pY2VzIjogW3sidGV4dCI6ICJBIGNsb3VkIGFwcGxpY2F0aW9uIiwgInNjb3JlIjogMC4yNSwgImZlZWRiYWNrIjogIlllcy4gQXBwIEludmVudG9yIGlzIGFuIGFwcGxpY2F0aW9uIHRoYXQgcnVucyBvbiB0aGUgd29ybGQgd2lkZSB3ZWIgKFdXVykgYW5kIGlzIGFjY2Vzc2VkIHRocm91Z2ggYSBXZWIgYnJvd3Nlci4gIn0sIHsidGV4dCI6ICJBbiBJbnRlZ3JhdGVkIERldmVsb3BtZW50IEVudmlyb25tZW50IChJREUpIiwgInNjb3JlIjogMC4yNSwgImZlZWRiYWNrIjogIlllcy4gIEFwcCBJbnZlbnRvciBpcyBhbmQgSURFLiBBcyBzdWNoLCBpdCBpcyBhIGNvbGxlY3Rpb24gb2Ygc29mdHdhcmUgdG9vbHMgZm9yIGRlc2lnbmluZywgZGV2ZWxvcGluZywgZGVidWdnaW5nLCBhbmQgdGVzdGluZyBtb2JpbGUgYXBwcy4gIn0sIHsidGV4dCI6ICJBIHNvZnR3YXJlIHN5c3RlbSBmb3IgZGV2ZWxvcGluZyBtb2JpbGUgYXBwcy4iLCAic2NvcmUiOiAwLjI1LCAiZmVlZGJhY2siOiAiWWVzLCBBcHAgSW52ZW50b3IgaXMgdXNlZCBmb3IgYnVpbGRpbmcgbW9iaWxlIGFwcHMuIn0sIHsidGV4dCI6ICJBIHByb2dyYW1taW5nIGxhbmd1YWdlIiwgInNjb3JlIjogMC4yNSwgImZlZWRiYWNrIjogIlllcy4gIEFwcCBJbnZlbnRvciBpcyBhbiBleGFtcGxlIG9mIGEgdmlzdWFsIHByb2dyYW1taW5nIGxhbmd1YWdlLiAifV0sICJwZXJtdXRlQ2hvaWNlcyI6IGZhbHNlLCAicXVpZCI6ICI1MDkxNzc4NTMxMTY0MTYwIiwgImFsbE9yTm90aGluZ0dyYWRpbmciOiBmYWxzZX0="));
        var assessmentTagMessages = {};


        assessmentTagMessages.correct = "Correct. ";

        assessmentTagMessages.incorrect = "Incorrect. ";

        assessmentTagMessages.partiallyCorrect = "Partially Correct. ";


        assessmentTagMessages.correctAnswer = " Yes, the answer is correct. ";

        assessmentTagMessages.incorrectAnswer = " No, the answer is incorrect. ";

        assessmentTagMessages.partiallyCorrectAnswer = " The answer is partially correct. ";


        assessmentTagMessages.correctAnswerHeading = "The correct answer is:";

        assessmentTagMessages.targetedFeedbackHeading = "Targeted Feedback:";

        assessmentTagMessages.feedbackHeading = "Feedback:";


        assessmentTagMessages.yourScoreIs = " Your score is: ";
      </script>
      <script src="../modules/assessment_tags/resources/grading_lib.js"></script>
      <script src="../modules/assessment_tags/resources/grading.js"></script>
      <noscript>
        &lt;div class=&#39;qt-warning&#39;&gt;

           JavaScript should be enabled to grade this question. 
        &lt;/div&gt;
      </noscript>




      <div class="qt-mc-question qt-standalone" id="jbEsdK1NvFeJ">
        <div class="qt-points">
          <em>


              1 point

          </em>
        </div>

        <div class="qt-question">App Inventor is an example of which of the following (Choose all that apply)</div>
        <div class="qt-choices">

            <div>
              <input data-index="0" id="jbEsdK1NvFeJ.0" name="jbEsdK1NvFeJ" type="checkbox"/>
              <label for="jbEsdK1NvFeJ.0">
                A cloud application
              </label>
            </div>

            <div>
              <input data-index="1" id="jbEsdK1NvFeJ.1" name="jbEsdK1NvFeJ" type="checkbox"/>
              <label for="jbEsdK1NvFeJ.1">
                An Integrated Development Environment (IDE)
              </label>
            </div>

            <div>
              <input data-index="2" id="jbEsdK1NvFeJ.2" name="jbEsdK1NvFeJ" type="checkbox"/>
              <label for="jbEsdK1NvFeJ.2">
                A software system for developing mobile apps.
              </label>
            </div>

            <div>
              <input data-index="3" id="jbEsdK1NvFeJ.3" name="jbEsdK1NvFeJ" type="checkbox"/>
              <label for="jbEsdK1NvFeJ.3">
                A programming language
              </label>
            </div>

        </div>


          <div class="qt-check-answer">
            <button class="gcb-button qt-check-answer-button">

               Check Answer 
            </button>
          </div>


        <div class="qt-feedback qt-hidden" role="alert">
        </div>
      </div>

    </div></div>
    <div><div class="gcb-border-box">
      <link href="../modules/assessment_tags/resources/questions.css" rel="stylesheet" type="text/css"/>
      <script>
        questionData['yOkVTqWogdaF'] = JSON.parse(window.atob("eyJkZWZhdWx0RmVlZGJhY2siOiAiIiwgIndlaWdodCI6IDEuMCwgInNob3dBbnN3ZXJXaGVuSW5jb3JyZWN0IjogZmFsc2UsICJjaG9pY2VzIjogW3sidGV4dCI6ICJBIGJ1dHRvbiB0aGF0IGFwcGVhcnMgb24gdGhlIHNjcmVlbi4gIiwgInNjb3JlIjogMC4yNSwgImZlZWRiYWNrIjogIiJ9LCB7InRleHQiOiAiQW4gYXVkaWJsZSBjbGljayB0aGF0IGhhcHBlbnMgd2hlbiB0aGUgdXNlciB0YXBzIHRoZSBidXR0b24uICIsICJzY29yZSI6IDAuMjUsICJmZWVkYmFjayI6ICIifSwgeyJ0ZXh0IjogIiBBbiBlcnJvciBtZXNzYWdlIHRoYXQgYXBwZWFycyB3aGVuIHNvbWV0aGluZyBnb2VzIHdyb25nLiIsICJzY29yZSI6IDAuMjUsICJmZWVkYmFjayI6ICIifSwgeyJ0ZXh0IjogIlRoZSBhcHAncyBtZW1vcnkgdXNhZ2UuICIsICJzY29yZSI6IC0xLjAsICJmZWVkYmFjayI6ICJMZXQgbWUgYWRkIG5ldyBpbmZvcm1hdGlvbiB0byBoZWxwIHlvdSBzb2x2ZSB0aGlzIGluZm9ybWF0aW9uLiBBbiBhcHAgZG9lcyBzdG9yZSBpbmZvcm1hdGlvbiBpbiBjb21wb25lbnQgcHJvcGVydGllcyBhbmQgdmFyaWFibGVzLCBidXQgdGhpcyBkYXRhIGlzIGhpZGRlbiBhbmQgbm90IHBhcnQgb2YgdGhlIFVJICh1bmxlc3MgeW91IGRpc3BsYXkgdGhlIGluZm9ybWF0aW9uIGV4cGxpY2l0bHkpLiJ9LCB7InRleHQiOiAiVGhlIGNvbG9yIG9mIHRoZSBhcHAncyBiYWNrZ3JvdW5kIHNjcmVlbi4iLCAic2NvcmUiOiAwLjI1LCAiZmVlZGJhY2siOiAiIn1dLCAicGVybXV0ZUNob2ljZXMiOiBmYWxzZSwgInF1aWQiOiAiNTczMzkzNTk1ODk4MjY1NiIsICJhbGxPck5vdGhpbmdHcmFkaW5nIjogZmFsc2V9"));
        var assessmentTagMessages = {};


        assessmentTagMessages.correct = "Correct. ";

        assessmentTagMessages.incorrect = "Incorrect. ";

        assessmentTagMessages.partiallyCorrect = "Partially Correct. ";


        assessmentTagMessages.correctAnswer = " Yes, the answer is correct. ";

        assessmentTagMessages.incorrectAnswer = " No, the answer is incorrect. ";

        assessmentTagMessages.partiallyCorrectAnswer = " The answer is partially correct. ";


        assessmentTagMessages.correctAnswerHeading = "The correct answer is:";

        assessmentTagMessages.targetedFeedbackHeading = "Targeted Feedback:";

        assessmentTagMessages.feedbackHeading = "Feedback:";


        assessmentTagMessages.yourScoreIs = " Your score is: ";
      </script>
      <script src="../modules/assessment_tags/resources/grading_lib.js"></script>
      <script src="../modules/assessment_tags/resources/grading.js"></script>
      <noscript>
        &lt;div class=&#39;qt-warning&#39;&gt;

           JavaScript should be enabled to grade this question. 
        &lt;/div&gt;
      </noscript>




      <div class="qt-mc-question qt-standalone" id="yOkVTqWogdaF">
        <div class="qt-points">
          <em>


              1 point

          </em>
        </div>

        <div class="qt-question">Which of the following elements would be considered part of the user interface (UI) for an app? 
    <br/>
    Choose all that apply. </div>
        <div class="qt-choices">

            <div>
              <input data-index="0" id="yOkVTqWogdaF.0" name="yOkVTqWogdaF" type="checkbox"/>
              <label for="yOkVTqWogdaF.0">
                A button that appears on the screen. 
              </label>
            </div>

            <div>
              <input data-index="1" id="yOkVTqWogdaF.1" name="yOkVTqWogdaF" type="checkbox"/>
              <label for="yOkVTqWogdaF.1">
                An audible click that happens when the user taps the button. 
              </label>
            </div>

            <div>
              <input data-index="2" id="yOkVTqWogdaF.2" name="yOkVTqWogdaF" type="checkbox"/>
              <label for="yOkVTqWogdaF.2">
                 An error message that appears when something goes wrong.
              </label>
            </div>

            <div>
              <input data-index="3" id="yOkVTqWogdaF.3" name="yOkVTqWogdaF" type="checkbox"/>
              <label for="yOkVTqWogdaF.3">
                The app&#39;s memory usage. 
              </label>
            </div>

            <div>
              <input data-index="4" id="yOkVTqWogdaF.4" name="yOkVTqWogdaF" type="checkbox"/>
              <label for="yOkVTqWogdaF.4">
                The color of the app&#39;s background screen.
              </label>
            </div>

        </div>


          <div class="qt-check-answer">
            <button class="gcb-button qt-check-answer-button">

               Check Answer 
            </button>
          </div>


        <div class="qt-feedback qt-hidden" role="alert">
        </div>
      </div>

    </div></div>
    <div><div class="gcb-border-box">
      <link href="../modules/assessment_tags/resources/questions.css" rel="stylesheet" type="text/css"/>
      <script>
        questionData['pERZIYiMxcKV'] = JSON.parse(window.atob("eyJkZWZhdWx0RmVlZGJhY2siOiAiIiwgIndlaWdodCI6IDEuMCwgInNob3dBbnN3ZXJXaGVuSW5jb3JyZWN0IjogZmFsc2UsICJjaG9pY2VzIjogW3sidGV4dCI6ICJUaGUgVXNlciBJbnRlcmZhY2UgZHJhd2VyIiwgInNjb3JlIjogMC4wLCAiZmVlZGJhY2siOiAiT0ssIHNvIHlvdSBkaWRuXHUyMDE5dCBnZXQgaXQgcmlnaHQgdGhpcyB0aW1lLiBMZXRcdTIwMTlzIGxvb2sgYXQgdGhpcyBhcyBhbiBvcHBvcnR1bml0eSB0byBsZWFybi4gVHJ5IHJldmlld2luZyB0aGlzIGluZm9ybWF0aW9uLiBUaGUgdXNlciBpbnRlcmZhY2UgZHJhd2VyIGNvbnRhaW5zIHZpc3VhbCBjb21wb25lbnRzIGxpa2UgYnV0dG9ucywgbGFiZWxzLCBhbmQgdGV4dCBib3hlcy4ifSwgeyJ0ZXh0IjogIlRoZSBNZWRpYSBkcmF3ZXIiLCAic2NvcmUiOiAxLjAsICJmZWVkYmFjayI6ICJUaGUgTWVkaWEgZHJhd2VyIGhhcyBjb21wb25lbnRzIGZvciBwbGF5aW5nIHNvdW5kcyBhbmQgdmlkZW8sIHJlY29yZGluZyB2aWRlbywgdGV4dC10by1zcGVlY2gsIGFuZCByZWNvZ25pemluZyBzcGVlY2guIn0sIHsidGV4dCI6ICJUaGUgRHJhd2luZyBhbmQgQW5pbWF0aW9uIGRyYXdlciIsICJzY29yZSI6IDAuMCwgImZlZWRiYWNrIjogIk9LLCBzbyB5b3UgZGlkblx1MjAxOXQgZ2V0IGl0IHJpZ2h0IHRoaXMgdGltZS4gTGV0XHUyMDE5cyBsb29rIGF0IHRoaXMgYXMgYW4gb3Bwb3J0dW5pdHkgdG8gbGVhcm4uIFRyeSByZXZpZXdpbmcgdGhpcyBpbmZvcm1hdGlvbi4gVGhlIGRyYXdpbmcgYW5kIGFuaW1hdGlvbiBkcmF3ZXIgaGFzIHRoZSBDYW52YXMgY29tcG9uZW50IGFsb25nIHdpdGggdGhlIEltYWdlU3ByaXRlIGFuZCBCYWxsIGNvbXBvbmVudHMgdGhhdCBsaXZlIGluIGNhbnZhc2VzLiJ9LCB7InRleHQiOiAiVGhlIFNvY2lhbCBEcmF3ZXIiLCAic2NvcmUiOiAwLjAsICJmZWVkYmFjayI6ICJPSywgc28geW91IGRpZG5cdTIwMTl0IGdldCBpdCByaWdodCB0aGlzIHRpbWUuIExldFx1MjAxOXMgbG9vayBhdCB0aGlzIGFzIGFuIG9wcG9ydHVuaXR5IHRvIGxlYXJuLiBUcnkgcmV2aWV3aW5nIHRoaXMgaW5mb3JtYXRpb24uIFRoZSBzb2NpYWwgZHJhd2VyIGhhcyBjb21wb25lbnRzIGZvciBjb250YWN0cywgdGV4dGluZywgYW5kIHBob25lIGNhbGxzLiJ9XSwgInBlcm11dGVDaG9pY2VzIjogZmFsc2UsICJxdWlkIjogIjU2OTM0MTcyMzc1MTIxOTIiLCAiYWxsT3JOb3RoaW5nR3JhZGluZyI6IGZhbHNlfQ=="));
        var assessmentTagMessages = {};


        assessmentTagMessages.correct = "Correct. ";

        assessmentTagMessages.incorrect = "Incorrect. ";

        assessmentTagMessages.partiallyCorrect = "Partially Correct. ";


        assessmentTagMessages.correctAnswer = " Yes, the answer is correct. ";

        assessmentTagMessages.incorrectAnswer = " No, the answer is incorrect. ";

        assessmentTagMessages.partiallyCorrectAnswer = " The answer is partially correct. ";


        assessmentTagMessages.correctAnswerHeading = "The correct answer is:";

        assessmentTagMessages.targetedFeedbackHeading = "Targeted Feedback:";

        assessmentTagMessages.feedbackHeading = "Feedback:";


        assessmentTagMessages.yourScoreIs = " Your score is: ";
      </script>
      <script src="../modules/assessment_tags/resources/grading_lib.js"></script>
      <script src="../modules/assessment_tags/resources/grading.js"></script>
      <noscript>
        &lt;div class=&#39;qt-warning&#39;&gt;

           JavaScript should be enabled to grade this question. 
        &lt;/div&gt;
      </noscript>




      <div class="qt-mc-question qt-standalone" id="pERZIYiMxcKV">
        <div class="qt-points">
          <em>


              1 point

          </em>
        </div>

        <div class="qt-question">Which Palette drawer (folder) contains the Player component? </div>
        <div class="qt-choices">

            <div>
              <input data-index="0" id="pERZIYiMxcKV.0" name="pERZIYiMxcKV" type="radio"/>
              <label for="pERZIYiMxcKV.0">
                The User Interface drawer
              </label>
            </div>

            <div>
              <input data-index="1" id="pERZIYiMxcKV.1" name="pERZIYiMxcKV" type="radio"/>
              <label for="pERZIYiMxcKV.1">
                The Media drawer
              </label>
            </div>

            <div>
              <input data-index="2" id="pERZIYiMxcKV.2" name="pERZIYiMxcKV" type="radio"/>
              <label for="pERZIYiMxcKV.2">
                The Drawing and Animation drawer
              </label>
            </div>

            <div>
              <input data-index="3" id="pERZIYiMxcKV.3" name="pERZIYiMxcKV" type="radio"/>
              <label for="pERZIYiMxcKV.3">
                The Social Drawer
              </label>
            </div>

        </div>


          <div class="qt-check-answer">
            <button class="gcb-button qt-check-answer-button">

               Check Answer 
            </button>
          </div>


        <div class="qt-feedback qt-hidden" role="alert">
        </div>
      </div>

    </div></div>
    <div><div class="gcb-border-box">
      <link href="../modules/assessment_tags/resources/questions.css" rel="stylesheet" type="text/css"/>
      <script>
        questionData['1ttlsfX8NBTz'] = JSON.parse(window.atob("eyJkZWZhdWx0RmVlZGJhY2siOiAiIiwgIndlaWdodCI6IDEuMCwgInNob3dBbnN3ZXJXaGVuSW5jb3JyZWN0IjogZmFsc2UsICJjaG9pY2VzIjogW3sidGV4dCI6ICJCdXR0b24iLCAic2NvcmUiOiAwLjMzLCAiZmVlZGJhY2siOiAiIn0sIHsidGV4dCI6ICJMYWJlbCIsICJzY29yZSI6IDAuMzMsICJmZWVkYmFjayI6ICIifSwgeyJ0ZXh0IjogIlBsYXllci5Jc1BsYXlpbmciLCAic2NvcmUiOiAtMS4wLCAiZmVlZGJhY2siOiAiVGhpcyBpcyBjaGFsbGVuZ2luZywgYnV0IHJld2FyZGluZyEgVGhpcyBpcyBhIHByb3BlcnR5IG9mIGEgY29tcG9uZW50LCBub3QgYSBjb21wb25lbnQifSwgeyJ0ZXh0IjogIlBsYXllciIsICJzY29yZSI6IDAuMzQsICJmZWVkYmFjayI6ICIifSwgeyJ0ZXh0IjogIkJ1dHRvbi5JbWFnZSIsICJzY29yZSI6IC0xLjAsICJmZWVkYmFjayI6ICJUaGlzIGlzIGNoYWxsZW5naW5nLCBidXQgcmV3YXJkaW5nISBUaGlzIGlzIGEgcHJvcGVydHkgb2YgYSBjb21wb25lbnQsIG5vdCBhIGNvbXBvbmVudCJ9XSwgInBlcm11dGVDaG9pY2VzIjogZmFsc2UsICJxdWlkIjogIjU3NjY0NjYwNDEyODI1NjAiLCAiYWxsT3JOb3RoaW5nR3JhZGluZyI6IGZhbHNlfQ=="));
        var assessmentTagMessages = {};


        assessmentTagMessages.correct = "Correct. ";

        assessmentTagMessages.incorrect = "Incorrect. ";

        assessmentTagMessages.partiallyCorrect = "Partially Correct. ";


        assessmentTagMessages.correctAnswer = " Yes, the answer is correct. ";

        assessmentTagMessages.incorrectAnswer = " No, the answer is incorrect. ";

        assessmentTagMessages.partiallyCorrectAnswer = " The answer is partially correct. ";


        assessmentTagMessages.correctAnswerHeading = "The correct answer is:";

        assessmentTagMessages.targetedFeedbackHeading = "Targeted Feedback:";

        assessmentTagMessages.feedbackHeading = "Feedback:";


        assessmentTagMessages.yourScoreIs = " Your score is: ";
      </script>
      <script src="../modules/assessment_tags/resources/grading_lib.js"></script>
      <script src="../modules/assessment_tags/resources/grading.js"></script>
      <noscript>
        &lt;div class=&#39;qt-warning&#39;&gt;

           JavaScript should be enabled to grade this question. 
        &lt;/div&gt;
      </noscript>




      <div class="qt-mc-question qt-standalone" id="1ttlsfX8NBTz">
        <div class="qt-points">
          <em>


              1 point

          </em>
        </div>

        <div class="qt-question">Which of the following are components?</div>
        <div class="qt-choices">

            <div>
              <input data-index="0" id="1ttlsfX8NBTz.0" name="1ttlsfX8NBTz" type="checkbox"/>
              <label for="1ttlsfX8NBTz.0">
                Button
              </label>
            </div>

            <div>
              <input data-index="1" id="1ttlsfX8NBTz.1" name="1ttlsfX8NBTz" type="checkbox"/>
              <label for="1ttlsfX8NBTz.1">
                Label
              </label>
            </div>

            <div>
              <input data-index="2" id="1ttlsfX8NBTz.2" name="1ttlsfX8NBTz" type="checkbox"/>
              <label for="1ttlsfX8NBTz.2">
                Player.IsPlaying
              </label>
            </div>

            <div>
              <input data-index="3" id="1ttlsfX8NBTz.3" name="1ttlsfX8NBTz" type="checkbox"/>
              <label for="1ttlsfX8NBTz.3">
                Player
              </label>
            </div>

            <div>
              <input data-index="4" id="1ttlsfX8NBTz.4" name="1ttlsfX8NBTz" type="checkbox"/>
              <label for="1ttlsfX8NBTz.4">
                Button.Image
              </label>
            </div>

        </div>


          <div class="qt-check-answer">
            <button class="gcb-button qt-check-answer-button">

               Check Answer 
            </button>
          </div>


        <div class="qt-feedback qt-hidden" role="alert">
        </div>
      </div>

    </div></div>
    <div><div class="gcb-border-box">
      <link href="../modules/assessment_tags/resources/questions.css" rel="stylesheet" type="text/css"/>
      <script>
        questionData['qKJyEkTbBD6m'] = JSON.parse(window.atob("eyJkZWZhdWx0RmVlZGJhY2siOiAiIiwgIndlaWdodCI6IDEuMCwgInNob3dBbnN3ZXJXaGVuSW5jb3JyZWN0IjogZmFsc2UsICJjaG9pY2VzIjogW3sidGV4dCI6ICJUaGUgdXNlciB0YXBzIG9uIHRoZSBzY3JlZW4uIiwgInNjb3JlIjogMC4yNSwgImZlZWRiYWNrIjogIlRoaXMgaXMgdGhlIEJ1dHRvbi5DbGljayBldmVudCJ9LCB7InRleHQiOiAiVGhlIHBob25lIHJlY2VpdmVzIGEgdGV4dCBtZXNzYWdlLiIsICJzY29yZSI6IDAuMjUsICJmZWVkYmFjayI6ICJUaGlzIGlzIGEgVGV4dGluZy5NZXNzYWdlUmVjZWl2ZWQgZXZlbnQifSwgeyJ0ZXh0IjogIlRoZSBwaG9uZSdzIGxvY2F0aW9uIGNoYW5nZXMuIiwgInNjb3JlIjogMC4yNSwgImZlZWRiYWNrIjogIlRoaXMgaXMgYSBMb2NhdGlvblNlbnNvci5Mb2NhdGlvbkNoYW5nZWQgZXZlbnQifSwgeyJ0ZXh0IjogIlRoZSBhcHAgcGxheXMgYSBzb3VuZCBjbGlwIiwgInNjb3JlIjogLTEuMCwgImZlZWRiYWNrIjogIlRoaXMgaXMgY2hhbGxlbmdpbmcsIGJ1dCByZXdhcmRpbmchIFRoZSBhcHAgY2FuIHBsYXkgYSBzb3VuZCBjbGlwIGluIHJlc3BvbnNlIHRvIGFuIGV2ZW50IGJ1dCB0aGUgcGxheWluZyBvZiB0aGUgc291bmQgaXMgbm90IGNvbnNpZGVyZWQgYW4gZXZlbnQgaXRzZWxmLiJ9LCB7InRleHQiOiAiVGhlIHBob25lJ3MgaW50ZXJuYWwgY2xvY2sgdGlja3MiLCAic2NvcmUiOiAwLjI1LCAiZmVlZGJhY2siOiAiVGhpcyBpcyBhIENsb2NrLlRpbWVyIGV2ZW50In1dLCAicGVybXV0ZUNob2ljZXMiOiBmYWxzZSwgInF1aWQiOiAiNTYzNDM4NzIwNjk5NTk2OCIsICJhbGxPck5vdGhpbmdHcmFkaW5nIjogZmFsc2V9"));
        var assessmentTagMessages = {};


        assessmentTagMessages.correct = "Correct. ";

        assessmentTagMessages.incorrect = "Incorrect. ";

        assessmentTagMessages.partiallyCorrect = "Partially Correct. ";


        assessmentTagMessages.correctAnswer = " Yes, the answer is correct. ";

        assessmentTagMessages.incorrectAnswer = " No, the answer is incorrect. ";

        assessmentTagMessages.partiallyCorrectAnswer = " The answer is partially correct. ";


        assessmentTagMessages.correctAnswerHeading = "The correct answer is:";

        assessmentTagMessages.targetedFeedbackHeading = "Targeted Feedback:";

        assessmentTagMessages.feedbackHeading = "Feedback:";


        assessmentTagMessages.yourScoreIs = " Your score is: ";
      </script>
      <script src="../modules/assessment_tags/resources/grading_lib.js"></script>
      <script src="../modules/assessment_tags/resources/grading.js"></script>
      <noscript>
        &lt;div class=&#39;qt-warning&#39;&gt;

           JavaScript should be enabled to grade this question. 
        &lt;/div&gt;
      </noscript>




      <div class="qt-mc-question qt-standalone" id="qKJyEkTbBD6m">
        <div class="qt-points">
          <em>


              1 point

          </em>
        </div>

        <div class="qt-question">Which of the following would be considered an event on your smart phone? 
    <br/>
    Choose all that apply. </div>
        <div class="qt-choices">

            <div>
              <input data-index="0" id="qKJyEkTbBD6m.0" name="qKJyEkTbBD6m" type="checkbox"/>
              <label for="qKJyEkTbBD6m.0">
                The user taps on the screen.
              </label>
            </div>

            <div>
              <input data-index="1" id="qKJyEkTbBD6m.1" name="qKJyEkTbBD6m" type="checkbox"/>
              <label for="qKJyEkTbBD6m.1">
                The phone receives a text message.
              </label>
            </div>

            <div>
              <input data-index="2" id="qKJyEkTbBD6m.2" name="qKJyEkTbBD6m" type="checkbox"/>
              <label for="qKJyEkTbBD6m.2">
                The phone&#39;s location changes.
              </label>
            </div>

            <div>
              <input data-index="3" id="qKJyEkTbBD6m.3" name="qKJyEkTbBD6m" type="checkbox"/>
              <label for="qKJyEkTbBD6m.3">
                The app plays a sound clip
              </label>
            </div>

            <div>
              <input data-index="4" id="qKJyEkTbBD6m.4" name="qKJyEkTbBD6m" type="checkbox"/>
              <label for="qKJyEkTbBD6m.4">
                The phone&#39;s internal clock ticks
              </label>
            </div>

        </div>


          <div class="qt-check-answer">
            <button class="gcb-button qt-check-answer-button">

               Check Answer 
            </button>
          </div>


        <div class="qt-feedback qt-hidden" role="alert">
        </div>
      </div>

    </div></div>
    
    <!-- Quizly -->
    
    <div><script>if (!window.quizlies) {window.quizlies={};}var quiz = {};quiz.name="quiz_pause_the_player";quiz.id="LXgF4NO50hNM";window.quizlies["quiz_pause_the_player"]= quiz;</script><script>function updateQuizlyProgressIcon(id, score) {   var qname = window.quizlies.quizname;  var iframes = document.getElementsByTagName('iframe');  var iconholder = '';  var innerHtml = '';  if (score >= 1)     innerHtml = '<img alt="Completed" class="gcb-progress-icon" src="../../_static/assets/img/completed.png" title="Completed">';  else    innerHtml = '<img alt="In_progress" class="gcb-progress-icon" src="../../_static/assets/img/in_progress.png" title="In progress">';  for (var i=0; i < iframes.length; i++) {     var iframe = iframes[i];    if (iframe.src.indexOf(qname) != -1) {       iconholder = iframe.previousSibling.previousSibling;      break;    }  }  if (iconholder != '')     iconholder.innerHTML = innerHtml;}</script><script> function checkAnswer(){ var quizName = window.quizlies["quizname"];var instanceid = window.quizlies[quizName].id;var result = window.quizlies[quizName].result;var workspace = window.quizlies[quizName].workspace;var score = (result) ? 1 : 0;console.log("RAM (quizly.py):  That solution was " + result);if (gcbCanRecordStudentEvents) {console.log("RAM (quizly.py): POSTing to server");console.log("RAM (quizly.py): instanceid=" + instanceid);var auditDict = {'instanceid': instanceid,'answer': result,'score': score,'type': "SaQuestion",'workspace': workspace,};gcbAudit(gcbCanRecordStudentEvents, auditDict, "tag-assessment", true);}  updateQuizlyProgressIcon(instanceid, score);}</script><div style="border: 1px solid black; margin: 5px; padding: 5px;"><div class="gcb-progress-icon-holder gcb-pull-right" id="icon-holder-quiz_pause_the_player"><img src="../../_static/assets/img/not_started.png"/></div><div class="qt-points"><em>1 point  </em></div>
    <iframe height="595" src="../../_static/assets/lib/quizly/gcb-index60c4.html?backpack=hidden&amp;selector=hidden&amp;quizname=quiz_pause_the_player&amp;hints=true&amp;repeatable=false" style="border: 0px; margin: 1px; padding: 1px;" width="100%"></iframe></div></div>
    <div><script>if (!window.quizlies) {window.quizlies={};}var quiz = {};quiz.name="quiz_button_click_stop_player";quiz.id="BtQ8hSoGkeml";window.quizlies["quiz_button_click_stop_player"]= quiz;</script><script>function updateQuizlyProgressIcon(id, score) {   var qname = window.quizlies.quizname;  var iframes = document.getElementsByTagName('iframe');  var iconholder = '';  var innerHtml = '';  if (score >= 1)     innerHtml = '<img alt="Completed" class="gcb-progress-icon" src="../../_static/assets/img/completed.png" title="Completed">';  else    innerHtml = '<img alt="In_progress" class="gcb-progress-icon" src="../../_static/assets/img/in_progress.png" title="In progress">';  for (var i=0; i < iframes.length; i++) {     var iframe = iframes[i];    if (iframe.src.indexOf(qname) != -1) {       iconholder = iframe.previousSibling.previousSibling;      break;    }  }  if (iconholder != '')     iconholder.innerHTML = innerHtml;}</script><script> function checkAnswer(){ var quizName = window.quizlies["quizname"];var instanceid = window.quizlies[quizName].id;var result = window.quizlies[quizName].result;var workspace = window.quizlies[quizName].workspace;var score = (result) ? 1 : 0;console.log("RAM (quizly.py):  That solution was " + result);if (gcbCanRecordStudentEvents) {console.log("RAM (quizly.py): POSTing to server");console.log("RAM (quizly.py): instanceid=" + instanceid);var auditDict = {'instanceid': instanceid,'answer': result,'score': score,'type': "SaQuestion",'workspace': workspace,};gcbAudit(gcbCanRecordStudentEvents, auditDict, "tag-assessment", true);}  updateQuizlyProgressIcon(instanceid, score);}</script>
    <div style="border: 1px solid black; margin: 5px; padding: 5px;"><div class="gcb-progress-icon-holder gcb-pull-right" id="icon-holder-quiz_button_click_stop_player"><img src="../../_static/assets/img/not_started.png"/></div><div class="qt-points"><em>1 point  </em></div>
    <iframe height="595" src="../../_static/assets/lib/quizly/gcb-index535c.html?backpack=hidden&amp;selector=hidden&amp;quizname=quiz_button_click_stop_player&amp;hints=true&amp;repeatable=false" style="border: 0px; margin: 1px; padding: 1px;" width="100%"></iframe></div></div>

    <div class="yui-wk-div" id="portfolio">


Reflection: For Your Portfolio
--------------------------------

.. raw:: html


    <!-- 
    <h2>Reflection: For Your Portfolio</h2> -->
    
      <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1B90zQGsq4YFEUC5LZQ0MOo7t4vZoNA7WxsoBls66ft0/edit?usp=sharing" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
      <p>If you are using a Google Sites portfolio, see the videos on the <a href="https://sites.google.com/site/mobilecspportfoliohelp/home/portfolio-help" target="_blank">portfolio help page</a> on how to embed your google document in your web page.</p>

       <!-- added width, margin-left -->
      <iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vQK2N8f05DkZyvrk6AQdJQBXffYaEfsNxYpEFAhJp7GE2cleEs-sbeQ5OSXVMVEhsMZLd2CPw6AKBHs/pub" style="height:30em; width:100%; margin-left: 100px"></iframe>

    </div>

