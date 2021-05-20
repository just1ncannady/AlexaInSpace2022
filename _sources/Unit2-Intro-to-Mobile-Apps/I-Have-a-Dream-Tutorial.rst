.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

I Have a Dream Tutorial
=======================


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
    

Introduction and Goals
-----------------------

.. raw:: html

    <p>
    <table><tbody>
    <tr><td><iframe allowfullscreen="" frameborder="0" height="420" src="https://www.youtube.com/embed/pQ0zjP-VC2E" width="315"></iframe>
    <br/>(<a href="http://www.teachertube.com/video/358482" target="_blank">Teacher Tube version</a>)</td>
    <td>
    <p><b><i>I Have a Dream!</i></b> is an educational "soundboard" app that plays the famous speech of Martin Luther King. This is a great example of a socially-useful app which provides multimedia education on African-American history and the civil rights movement.</p>
    <p><b>Learning Objectives:</b> In this lesson you will learn to</p>
    <ul>
    <li>follow an instructor-led walkthrough to create the <i>I Have a Dream</i> app on a mobile device;
        </li><li>navigate the App Inventor programming platform;
        </li><li>develop your understanding of what an App Inventor program is;
        </li><li>develop your understanding of event handlers.
        </li>
    </ul>
    <p><b>Language Objectives:</b></p>
    <ul>
    <li>I will be able to use target vocabulary, such as input, output, event handler, button, sound, and label, while describing app features and User Interface with the support of a word bank.
    </li>
    <li>I will be able to summarize event driven programming for the portfolio reflection questions with the support of concept definitions and vocabulary notes from this lesson.</li>
    </ul>
    <p><b>Lesson Resources:</b></p>
    <ul>
    <li><a href="https://docs.google.com/presentation/d/1n-K4AQ_maHcXekzcfERQ9dxj91nqv9ytwJx4ZkAp8zw/copy" target="_blank" title="">Vocabulary Notes</a></li>
    </ul>
    </td></tr>
    </tbody></table>
    <br/>
    

Learning Activities
--------------------
.. raw:: html

    <p>
    <h3>Tutorial</h3>
    <p>To get started, <a href="http://ai2.appinventor.mit.edu/?repo=templates.appinventor.mit.edu/trincoll/csp/tutorials/aias/IHaveADreamStarter.asc" target="_blank">
    open the I Have a Dream Starter project with the embedded tutorial in App Inventor</a> and login with your Google account into App Inventor.
      <!-- &lt;a target=&quot;_blank&quot; href=&quot;http://ai2.appinventor.mit.edu/?repo=templates.appinventor.mit.edu/trincoll/csp/unit2/templates/IHaveADreamStarter/IHaveADreamStarter.asc&quot;&gt;
    open the I Have a Dream Starter project in App Inventor&lt;/a&gt; -->
     Follow along with your teacher or the following video tutorial. You can also use the embedded tutorial in the template or the <a href="https://drive.google.com/open?id=1Bg64PZclbPwhFg8Qg2GZJw5hVC08tDIFBhs5bBbyves" target="_blank" title="">text-version of this tutorial</a> or the <a href="https://drive.google.com/open?id=1x9KDcEIyXwC7_h-bRJQCe-sIuXpQTGSRUnONxMs-MLA" target="_blank">short handout</a>. NOTE: The video below asks you to open a starter app, but if you
      use the link above the IHaveADreamStarter app will already be loaded and you can start following the video at time 1:12. </p>
    
.. youtube:: KDepcRIfnNs
        :width: 650
        :height: 415
        :align: center

.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    <!-- does not resize
    &lt;iframe width=&quot;700&quot; height=&quot;400&quot; src=&quot;https://www.youtube-nocookie.com/embed/KDepcRIfnNs?start=72&quot; frameborder=&quot;0&quot; allow=&quot;accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture&quot; allowfullscreen=&quot;&quot;&gt;&lt;/iframe&gt; -->
    <p>(<a href="http://www.teachertube.com/video/mobile-csp-i-have-a-dream-tutorial-437861" target="_blank" title="">Teacher Tube version</a>)</p>
    <h3>Input/Output</h3>
    <p><img src="../_static/assets/img/phoneIO.png" style="float:left;margin:2px" width="250px"/> 
    
    Our mobile devices and computers are built to interact with us. The mobile apps that you create will also communicate with users by getting <span class="hover vocab yui-wk-div" data-id="Input">input</span> from the users and displaying <span class="hover vocab yui-wk-div" data-id="Output">output</span><br/> to the users. Input  is data sent to a computer for processing by a program, and output is the data sent back from the program to the device.  Program output is usually based on a program’s input or prior state (e.g., internal values or variables). Input and output can come in many forms, such as <b>tactile</b> (for example touching a button or the device vibrating), <b>audible</b> (a sound), <b>visual</b> (an image), or <b>text</b>. Try listing all the forms of input and output in the I Have a Dream app!  </p>
    <p>Designing a good <span class="hover vocab yui-wk-div" data-id="User Interface">user interface (UI)</span> for a program is very important! User Experience (UX) designers are very much in demand. Most programs and apps these days are <span class="hover vocab yui-wk-div" data-id="Event-driven Programming">event-driven programming</span>, which means they display the UI and wait for a <span class="hover vocab yui-wk-div" data-id="User Events">user event</span>, for example for the user to touch a button as input.  In event-driven programming, program statements are executed when triggered rather than through the sequential flow of control.
    Events are triggered when a key is pressed, a mouse is clicked, a program is started by another application, etc., and they supply input data to a program and trigger different blocks of code in the program that influence its behavior.  A program needs to work for a variety of inputs and situations!</p>
    

Summary
--------

.. raw:: html

    <p>
    In this lesson, you learned how to:
      <div class="yui-wk-div" id="summarylist">
    </div>
    <br/>
    

Still Curious?
---------------

.. raw:: html

    <p>
    

Self-Check
-----------

.. raw:: html

    <p>
    <h3>Vocabulary</h3>
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
    <h3>Check Your Understanding</h3>
    <p>Complete the following self-check exercises. Please note that you should login if you want your answers saved and scored. In addition, some of these exercises will not work in Internet Explorer or Edge browsers. We recommend using Chrome.</p>
    
.. mchoice:: mcsp-2-2-1
    :random:
    :practice: T
    :answer_a: tactile
    :feedback_a: 
    :answer_b: audible
    :feedback_b: 
    :answer_c: visual
    :feedback_c: 
    :answer_d: text
    :feedback_d: 
    :correct: a

    What type of input does the I have a Dream app expect?


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


.. mchoice:: mcsp-2-2-2
    :random:
    :practice: T
    :answer_a: tactile
    :feedback_a: 
    :answer_b: audible
    :feedback_b: 
    :answer_c: visual
    :feedback_c: 
    :answer_d: text
    :feedback_d: 
    :correct: b

    What type of output does the I have a Dream app generate?


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


.. mchoice:: mcsp-2-2-3
    :random:
    :practice: T
    :answer_a: A cloud application
    :feedback_a: Yes. App Inventor is an application that runs on the world wide web (WWW) and is accessed through a Web browser. 
    :answer_b: An Integrated Development Environment (IDE)
    :feedback_b: Yes.  App Inventor is and IDE. As such, it is a collection of software tools for designing, developing, debugging, and testing mobile apps. 
    :answer_c: A software system for developing mobile apps.
    :feedback_c: Yes, App Inventor is used for building mobile apps.
    :answer_d: A programming language
    :feedback_d: Yes.  App Inventor is an example of a visual programming language. 
    :correct: a,b,c,d

    App Inventor is an example of which of the following (Choose all that apply)


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-2-2-4
    :random:
    :practice: T
    :answer_a: A button that appears on the screen. 
    :feedback_a: 
    :answer_b: An audible click that happens when the user taps the button. 
    :feedback_b: 
    :answer_c:  An error message that appears when something goes wrong.
    :feedback_c: 
    :answer_d: The app's memory usage. 
    :feedback_d: Let me add new information to help you solve this information. An app does store information in component properties and variables, but this data is hidden and not part of the UI (unless you display the information explicitly).
    :answer_e: The color of the app's background screen.
    :feedback_e: 
    :correct: a,b,c,e

    Which of the following elements would be considered part of the user interface (UI) for an app? Choose all that apply. 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-2-2-5
    :random:
    :practice: T
    :answer_a: The User Interface drawer
    :feedback_a: OK, so you didn’t get it right this time. Let’s look at this as an opportunity to learn. Try reviewing this information. The user interface drawer contains visual components like buttons, labels, and text boxes.
    :answer_b: The Media drawer
    :feedback_b: The Media drawer has components for playing sounds and video, recording video, text-to-speech, and recognizing speech.
    :answer_c: The Drawing and Animation drawer
    :feedback_c: OK, so you didn’t get it right this time. Let’s look at this as an opportunity to learn. Try reviewing this information. The drawing and animation drawer has the Canvas component along with the ImageSprite and Ball components that live in canvases.
    :answer_d: The Social Drawer
    :feedback_d: OK, so you didn’t get it right this time. Let’s look at this as an opportunity to learn. Try reviewing this information. The social drawer has components for contacts, texting, and phone calls.
    :correct: b

    Which Palette drawer (folder) contains the Player component? 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-2-2-6
    :random:
    :practice: T
    :answer_a: Button
    :feedback_a: 
    :answer_b: Label
    :feedback_b: 
    :answer_c: Player.IsPlaying
    :feedback_c: This is challenging, but rewarding! This is a property of a component, not a component
    :answer_d: Player
    :feedback_d: 
    :answer_e: Button.Image
    :feedback_e: This is challenging, but rewarding! This is a property of a component, not a component
    :correct: a,b,d

    Which of the following are components?


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-2-2-7
    :random:
    :practice: T
    :answer_a: The user taps on the screen.
    :feedback_a: This is the Button.Click event
    :answer_b: The phone receives a text message.
    :feedback_b: This is a Texting.MessageReceived event
    :answer_c: The phone's location changes.
    :feedback_c: This is a LocationSensor.LocationChanged event
    :answer_d: The app plays a sound clip
    :feedback_d: This is challenging, but rewarding! The app can play a sound clip in response to an event but the playing of the sound is not considered an event itself.
    :answer_e: The phone's internal clock ticks
    :feedback_e: This is a Clock.Timer event
    :correct: a,b,c,e

    Which of the following would be considered an event on your smart phone? Choose all that apply. 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
    
.. quizly:: mscp-2-2-8
    
    
    :quizname: quiz_pause_the_player
    
    
    
.. quizly:: mscp-2-2-9
    
    
    :quizname: quiz_button_click_stop_player
    
    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1B90zQGsq4YFEUC5LZQ0MOo7t4vZoNA7WxsoBls66ft0/edit?usp=sharing" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <p>If you are using a Google Sites portfolio, see the videos on the <a href="https://sites.google.com/site/mobilecspportfoliohelp/home/portfolio-help" target="_blank">portfolio help page</a> on how to embed your google document in your web page.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vQK2N8f05DkZyvrk6AQdJQBXffYaEfsNxYpEFAhJp7GE2cleEs-sbeQ5OSXVMVEhsMZLd2CPw6AKBHs/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    </div>
    </div>