.. image:: ../../_static/MobileCSPLogo.png
    :width: 250
    :align: center
    
I Have a Dream Tutorial
========================

.. raw:: html

    
   <!--  custom script files -->
    <script src="../../_static/assets/lib/lessons/tipped.js" type="text/javascript"></script>
    <script src="../../_static/assets/lib/lessons/Framework2020.js" type="text/javascript"></script>
    <link href="../../_static/assets/lib/lessons/tipped.css" rel="stylesheet" type="text/css"/>
    <link href="../../_static/assets/lib/lessons/lessons.css" rel="stylesheet" type="text/css"/>
    <script src="../../_static/assets/lib/lessons/vocabulary.js" type="text/javascript"></script>

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
   :random:
   :practice: T

   What type of input does the I have a Dream app expect?
   
   - tactile
   
     + Correct!
   
   - audible
   
     - Incorrect
   
   - visual
   
     - Incorrect
   
   - text
   
     - Incorrect
   
.. mchoice:: mcsp-2-2-2
   :random:
   :practice: T

   What type of output does the I have a Dream app generate?
   
   - tactile
   
     - Incorrect
   
   - audible
   
     + Correct
   
   - visual
   
     - Incorrect
   
   - text
   
     - Incorrect
   
.. mchoice:: mcsp-2-2-3
   :random:
   :practice: T
   
   App Inventor is an example of which of the following (Choose all that apply)

   - A cloud application

     + Yes. App Inventor is an application that runs on the world wide web (WWW) and is accessed through a Web browser.

   - An Integrated Development Environment (IDE)

     + Yes. App Inventor is and IDE. As such, it is a collection of software tools for designing, developing, debugging, and testing mobile apps.

   - A software system for developing mobile apps

     + Yes, App Inventor is an IDE. It enables you to develop and run apps.

   - A programming language

     + That's right. App Inventor is used for developing mobile apps. 

.. mchoice:: mcsp-2-2-4
   :random:
   :practice: T

   Which of the following elements would be considered part of the user interface (UI) for an app? (Choose all that apply.)

   - A button that appears on the screen.

     + Yes, a button is a visible part of the UI.

   - An audible click that happens when the user taps the button.

     + Yes, audible sounds are part of the UI.

   - An error message that appears when something goes wrong.

     + Yes, an error message counts as part of the UI.

   - The color of the app's background screen.

     + Yes, colors are part of the app's UI.
     
   - The app's memory usage.

     - No, an app's memory usage is important but it's not something the user typically experiences as a normal part of using the app.     


.. mchoice:: mcsp-2-2-5
   :random:
   :practice: T

   Which Palette drawer (folder) contains the Player component?

   - The User Interface drawer

     - No, the User Interface drawer contains visual components like buttons, labels, and text boxes.

   - The Media drawer

     + Yes, the Media drawer has components for playing sounds and video, recording video, text-to-speech, and recognizing speech.

   - The Drawing and Animation drawer

     - No, the Drawing and Animation drawer has the Canvas component along with the ImageSprite and Ball components that live in canvases.

   - The Social Drawer

     - No, the Social drawer has components for contacts, texting, and phone calls.

.. mchoice:: mcsp-2-2-6
   :random:
   :practice: T

   Which of the following are components? (Choose all that apply.)

   - Button

     + Correct 

   - Label

     + Correct

   - Player.IsPlaying

     - No, IsPlaying is an attribute of the Player component.

   - Player

     + Correct

   - Button.Image

     - No, Button.Image refers to the Image property or attribute of the Button component.


.. mchoice:: mcsp-2-2-7
   :random:
   :practice: T

   Which of the following would be considered an event on your smart phone? (Choose all that apply.)

   - The user taps on the screen.

     + This is the Button.Click event.

   - The phone receives a text message.

     + This is a Texting.MessageReceived event.

   - The phone's location changes.

     + This is a LocationSensor.LocationChanged event.

   - The app plays a sound clip

     - This is a challenging one. The app can play a sound clip in response to an event but the playing of the sound is not considered an event itself.

   - The phone's internal clock clicks

     + This is a Clock.Timer event.

.. raw:: html
    
    <!-- Quizly -->
    
    <div><script>if (!window.quizlies) {window.quizlies={};}var quiz = {};quiz.name="quiz_pause_the_player";quiz.id="LXgF4NO50hNM";window.quizlies["quiz_pause_the_player"]= quiz;</script><script>function updateQuizlyProgressIcon(id, score) {   var qname = window.quizlies.quizname;  var iframes = document.getElementsByTagName('iframe');  var iconholder = '';  var innerHtml = '';  if (score >= 1)     innerHtml = '<img alt="Completed" class="gcb-progress-icon" src="../../_static/assets/img/completed.png" title="Completed">';  else    innerHtml = '<img alt="In_progress" class="gcb-progress-icon" src="../../_static/assets/img/in_progress.png" title="In progress">';  for (var i=0; i < iframes.length; i++) {     var iframe = iframes[i];    if (iframe.src.indexOf(qname) != -1) {       iconholder = iframe.previousSibling.previousSibling;      break;    }  }  if (iconholder != '')     iconholder.innerHTML = innerHtml;}</script><script> function checkAnswer(){ var quizName = window.quizlies["quizname"];var instanceid = window.quizlies[quizName].id;var result = window.quizlies[quizName].result;var workspace = window.quizlies[quizName].workspace;var score = (result) ? 1 : 0;console.log("RAM (quizly.py):  That solution was " + result);if (gcbCanRecordStudentEvents) {console.log("RAM (quizly.py): POSTing to server");console.log("RAM (quizly.py): instanceid=" + instanceid);var auditDict = {'instanceid': instanceid,'answer': result,'score': score,'type': "SaQuestion",'workspace': workspace,};gcbAudit(gcbCanRecordStudentEvents, auditDict, "tag-assessment", true);}  updateQuizlyProgressIcon(instanceid, score);}</script><div style="border: 1px solid black; margin: 5px; padding: 5px;"><div class="gcb-progress-icon-holder gcb-pull-right" id="icon-holder-quiz_pause_the_player"><img src="../../_static/assets/img/not_started.png"/></div><div class="qt-points"><em>1 point  </em></div>
    <iframe height="595" src="../../_static/assets/lib/quizly/index.html?backpack=hidden&amp;selector=hidden&amp;quizname=quiz_pause_the_player&amp;hints=true&amp;repeatable=false" style="border: 0px; margin: 1px; padding: 1px;" width="100%"></iframe></div></div>
    <div><script>if (!window.quizlies) {window.quizlies={};}var quiz = {};quiz.name="quiz_button_click_stop_player";quiz.id="BtQ8hSoGkeml";window.quizlies["quiz_button_click_stop_player"]= quiz;</script><script>function updateQuizlyProgressIcon(id, score) {   var qname = window.quizlies.quizname;  var iframes = document.getElementsByTagName('iframe');  var iconholder = '';  var innerHtml = '';  if (score >= 1)     innerHtml = '<img alt="Completed" class="gcb-progress-icon" src="../../_static/assets/img/completed.png" title="Completed">';  else    innerHtml = '<img alt="In_progress" class="gcb-progress-icon" src="../../_static/assets/img/in_progress.png" title="In progress">';  for (var i=0; i < iframes.length; i++) {     var iframe = iframes[i];    if (iframe.src.indexOf(qname) != -1) {       iconholder = iframe.previousSibling.previousSibling;      break;    }  }  if (iconholder != '')     iconholder.innerHTML = innerHtml;}</script><script> function checkAnswer(){ var quizName = window.quizlies["quizname"];var instanceid = window.quizlies[quizName].id;var result = window.quizlies[quizName].result;var workspace = window.quizlies[quizName].workspace;var score = (result) ? 1 : 0;console.log("RAM (quizly.py):  That solution was " + result);if (gcbCanRecordStudentEvents) {console.log("RAM (quizly.py): POSTing to server");console.log("RAM (quizly.py): instanceid=" + instanceid);var auditDict = {'instanceid': instanceid,'answer': result,'score': score,'type': "SaQuestion",'workspace': workspace,};gcbAudit(gcbCanRecordStudentEvents, auditDict, "tag-assessment", true);}  updateQuizlyProgressIcon(instanceid, score);}</script>
    <div style="border: 1px solid black; margin: 5px; padding: 5px;"><div class="gcb-progress-icon-holder gcb-pull-right" id="icon-holder-quiz_button_click_stop_player"><img src="../../_static/assets/img/not_started.png"/></div><div class="qt-points"><em>1 point  </em></div>
    <iframe height="595" src="../../_static/assets/lib/quizly/index.html?backpack=hidden&amp;selector=hidden&amp;quizname=quiz_button_click_stop_player&amp;hints=true&amp;repeatable=false" style="border: 0px; margin: 1px; padding: 1px;" width="100%"></iframe></div></div>

    <div class="yui-wk-div" id="portfolio">


Reflection: For Your Portfolio
--------------------------------

.. raw:: html


    <!-- 
    <h2>Reflection: For Your Portfolio</h2> -->
    
      <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1B90zQGsq4YFEUC5LZQ0MOo7t4vZoNA7WxsoBls66ft0/edit?usp=sharing" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
      <p>If you are using a Google Sites portfolio, see the videos on the <a href="https://sites.google.com/site/mobilecspportfoliohelp/home/portfolio-help" target="_blank">portfolio help page</a> on how to embed your google document in your web page.</p>

       <!-- added width, margin-left RAM: removed margin, added alignment in div tag -->
    <div style="align-items:center;">
      <iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vQK2N8f05DkZyvrk6AQdJQBXffYaEfsNxYpEFAhJp7GE2cleEs-sbeQ5OSXVMVEhsMZLd2CPw6AKBHs/pub" style="height:30em; width:100%"></iframe>

    </div>

