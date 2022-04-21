.. raw:: html 
.. raw:: html 

   <div class="logo-header"  id="student-logo"  > <img class="align-center" src="../_static/Mobile_CSP_Logo_White_transparent.png" width="250px"/> </div>

IP Addresses and Domain Names
=============================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
      $(document).ready(function() {
        generateSummary(EKmapping['6.04']);
        generateHovers();
        Tipped.create('.vocab', function(element) {
        var vocab = $(element).data('id');
        return vocabulary[vocab];
          }, {
            cache: false,
              position: 'topleft'
              });
      });
      
    /*  var vocabulary = {
        "host": "An Internet host computer is a computer that's connected directly to the Internet -- often a computer that provides certain services or resources.",
        "router": "A router is a device that transmits data between two different networks.",
        "IP Address":"An IP Address is a unique string of numbers separated by periods that identifies each computer using the Internet Protocol to communicate over a network.",
        "IPv4": "IP version 4 is an older 32 bit IP adress",
        "IPv6": "IP version 6 is a newer 128 bit IP address which allows for many more devices to be addressed.",
        "domain name": "An Internet domain name is a hierarchical name (such as trincoll.edu) that identifies an domain and an institution on the Internet. Top level domains include com, edu, gov.",
        "DNS": "Domain Name System (or Service or Server) is an Internet service that translates domain names into IP addresses."
      };      */
    </script>
    <h3 id="est-length">Time Estimate: 45 minutes</h3>

Introduction and Goals
-----------------------

.. raw:: html

    <p><h3>IP Addresses and Domain Names</h3>
    
    In this lesson, you will learn about <span class="hover vocab yui-wk-div" data-id='IP Address'>IP addresses</span> and <span class="hover vocab yui-wk-div" data-id='domain name'>domain names</span>. We will use a networking simulation app to explore how the <span class="hover vocab yui-wk-div" data-id='DNS'>Domain Name System (DNS)</span> is used to look up the <span class="hover vocab yui-wk-div" data-id='IP Address'>IP addresses</span> of <span class="hover vocab yui-wk-div" data-id='domain name'>domain names</span> such as google.com.<br/>
    
    <div id="bogus-div">
    <p></p>
    </div>
	<div><b>Learning Objectives:</b>&nbspI will learn to</div>
	<ul>
	<li>describe how the <span class="hover vocab yui-wk-div" data-id='DNS'>DNS</span> works and helps users connect to web servers on the Internet</li>
	</ul>
	<div><b>Language Objectives:</b>&nbspI will be able to</div>
	<ul>
	<li>use target vocabulary, such as <span class="hover vocab yui-wk-div" data-id="IP Address">IP Address</span>, <span class="hover vocab yui-wk-div" data-id="domain name">domain name</span>, and <span class="hover vocab yui-wk-div" data-id="DNS">DNS</span> while describing how networks connect, with the support of concept definitions and <a href="https://docs.google.com/presentation/d/1qwoJ0sNiiLFbv1KN_xW7yLpXUQLfYD8lxxZWPYjqdIY/copy" target="_blank" title="">vocabulary notes</a> from this lesson</li>
	</ul>


Learning Activities
--------------------

.. raw:: html

	<ul align="center" style="list-style: none; margin: 0; padding: 0; background: lightgrey">
	<li style="display: inline"><a href="https://docs.google.com/presentation/d/1S9SA6Y_SUU7o0oAbj7cpt7DGO5hgzJf7p3_vHWnCRG0/" target="_blank" title="">text-version</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="https://youtu.be/H81xmsxNdV8" target="_blank">YouTube Video Part 1</a></li>
	<li style="display: inline"> | </li>
	<li style="display: inline"><a href="https://youtu.be/rTB0KhkTMQM" target="_blank" title="">YouTube Video Part 2</a></li>
	</ul> 
	
	<br/>
	
	<p><iframe allowfullscreen="" frameborder="0" height="472" src="https://www.youtube.com/embed/H81xmsxNdV8" width="650"></iframe></p>
    <p>Before moving on to the activity below, try finding your <span class="hover vocab yui-wk-div" data-id='IP address'>IP address</span> by googling "what's my <span class="hover vocab yui-wk-div" data-id='IP Address'>IP address</span>". Try to find another <span class="hover vocab yui-wk-div" data-id='IP address'>IP address</span> for a <span class="hover vocab yui-wk-div" data-id='domain name'>domain name</span> that you know, for example google.com at a site like <a href="https://www.whois.com/whois/" target="_blank">WhoIs Lookup</a>.    </p>
	
    <h3>Networking Simulation Activities</h3>
    <p>
      In this lesson, we will use a <span class="hover vocab yui-wk-div" data-id='DNS'>DNS</span> simulator app to explore how we communicate on the Internet with IP addresses. Watch the video below about using the Mobile CSP's <span class="hover vocab yui-wk-div" data-id='DNS'>DNS</span> app.
    </p>
    <iframe allowfullscreen="" frameborder="0" height="472" src="https://www.youtube.com/embed/rTB0KhkTMQM" width="840">
    </iframe>
    <br/>
    (<a href="http://www.teachertube.com/video/mobile-csp-how-to-use-the-dns-widget-to-retrieve-and-use-ip-addresses-458219" target="_blank" title="">Teacher Tube version</a>)
          
    <br/>
    <p>
      Now that you understand how the app works, you will need to download the widget on to your tablet or Android phone. You can install the Android .apk file  for the widget by scanning the QR code below with the AI Companion app or by clicking on this link <a href="https://mobile-csp.org/DNSwidgetV13.apk" target="_blank">https://mobile-csp.org/DNSwidgetV13.apk</a> in your Android device's browser. If you are using the emulator or iOS, download  <a href="https://drive.google.com/file/d/0B4W7CJ-1czH5TF9FNHVxX1VRNmU2NS15c25CM0FaVkhLZUhF/view?resourcekey=0-FsWFIfHagRi0Qmnpa5JzlA" target="_blank">this .aia file</a>  and import into App Inventor and then connect. 
    <br/>
    </p><div class="yui-wk-div" style="text-align: center;"><img alt="APK file for DNS Widget" class="yui-img selected" src="../_static/assets/img/DNS-qr-codeV13.png" title="APK file for DNS Widget"/><br/></div>
    <p>
    </p><h4>Troubleshooting:</h4>
    <ul>
    <li style="margin-bottom: 5px;">Do not connect using the default Class Code 0. This might result in an error about the second argument of the for each list not being a list. You should get a 6 digit Class Code from your teacher and type it in. Your teacher should click on the NEW CLASS CODE button to get this code and give it to the whole class. Everyone in the class should use the same Class Code. Type in your name's first 3 or 4 letters in the Login Id before clicking on Login.</li>
    <li>If you are getting a TimeOut Exception error, CloudDB (which this app uses) might be down or too busy. You can use an
      older version of the app, v12, which uses TinyWebDB instead by typing this url on your device and installing it: <a href="https://mobile-csp.org/DNSwidgetV12.apk" target="_blank">https://mobile-csp.org/DNSwidgetV12.apk</a>. Or importing the following aia into App Inventor and building it: <a href="https://drive.google.com/file/d/0B4W7CJ-1czH5WDlMTGgzSVpKMUxfeksyb3QyWk1wNFFXam5N/view?resourcekey=0-luwNSk_mPXZV5vDLiIE9TA" target="_blank">v12 aia file</a>. The TinyWebDB server might also have traffic congestion problems. You can also try a different TinyWebDB server - the default URL in v12 is  http://westhilltinywebdb.appspot.com and you can replace it with http://tinywebdb.appinventor.mit.edu to try a different TinyWebDB server. </li>
    </ul>
    <p>
       Next, get together with two of your friends in class and do the following activities. (If you are working alone, you may have to skip some of the exercises listed but can still do a majority of the tasks described here.) </p>
    <h3>Activity 1 : Using the DNS to Retrieve and Use IP Addresses</h3>
    <ol>
    <li style="margin-bottom: 5px;">After your teacher has assigned you a class code, type that code into the class code textbox on your login screen. Your teacher will receive this code by clicking on the NEW CLASS CODE button on their own app. Only the teacher should click this button. The students in the class should all enter the same code. </li>
    <li style="margin-bottom: 5px;">If you are working on this exercise alone, you should press the <b><i>"Assign BOT"</i></b> button a dozen times before you log in to set up about a dozen or so robot users (<b><i>BOTS</i></b>) so you can practice looking up their <span class="hover vocab yui-wk-div" data-id='IP Address'>IP addresses</span>.  If you are working on this exercise as part of a class, you do not need to create any BOTS.
      </li><li style="margin-bottom: 5px;">Choose a short login name for yourself, enter it in the login box, and press the LOGIN button. An example of a good login would be three or four letters such as jim or mimi. Note that the system will append a number to your name when creating your login ID, to reduce the likelihood of you having the same login as someone else in the class. (Remember that your teacher will be checking your work at the end of this exercise, so do not use anything inappropriate for your login credentials). </li>
    <li style="margin-bottom: 5px;">Once the app confirms that you have successfully logged into the system, send a message to the <span class="hover vocab yui-wk-div" data-id='DNS'>DNS</span> asking it for the <span class="hover vocab yui-wk-div" data-id='IP Address'>IP address</span> for Amazon in this simulation. To do this, enter the <span class="hover vocab yui-wk-div" data-id='IP Address'>IP Address</span> of the <span class="hover vocab yui-wk-div" data-id='DNS'>DNS</span> seen at the top into the <b><i>"To:"</i></b> field. In the message field, enter "get amazon". Then press the <b><i>SEND</i></b> button. NOTE: When you type commands or login IDs into the Mobile CSP <span class="hover vocab yui-wk-div" data-id='DNS'>DNS</span> widget, it does not matter if you use upper or lower case characters.
    </li><li style="margin-bottom: 5px;">Using the <span class="hover vocab yui-wk-div" data-id='IP Address'>IP Address</span> you have discovered for Amazon, send Amazon a message to buy something. In the <b>"TO"</b> field of the message you will need to enter Amazon's <span class="hover vocab yui-wk-div" data-id='IP Address'>IP Address</span>. In the message body, you will need to enter <b><i>"buy X"</i></b> where X is the item you wish to purchase. Then press the <b><i>"SEND"</i></b> button.
    </li><li style="margin-bottom: 5px;">Repeat the previous step to purchase at least two more items.
    </li><li style="margin-bottom: 5px;">Once you have purchased three or more items, it is now time for you to contact one of your friends to brag about your recent purchases.  
    
    <img alt="APK file for DNS Widget" class="yui-img selected" style="float:right; margin:5px 0px 5px 5px" src="../_static/assets/img/DNSnetworkDiagram.png" title="APK file for DNS Widget"/>
	<ul>
	<li>Locate someone on the same <span class="hover vocab yui-wk-div" data-id='router'>router</span> as you.</li>
	<li>In the network diagram shown, the user (<b><i>jill30</i></b>) resides on <b><i><span class="hover vocab yui-wk-div" data-id='router'>Router</span> #7</i></b>, along with another user, <b><i>usha66</i></b>, whose <span class="hover vocab yui-wk-div" data-id='IP Address'>IP Address</span> is not known to <b><i>jill30</i></b>.</li>
	<li>These two users are not the only ones on this network. Pressing the PEERs button will reveal all the login IDs on this network.</li>
	<li>If there is no other user on your <span class="hover vocab yui-wk-div" data-id='router'>router</span> on the network diagram on your tablet's screen, you may have to skip this part of the exercise.</li>
	<li>Notice that your friend's <span class="hover vocab yui-wk-div" data-id='IP Address'>IP address</span> is initially hidden from you (marked with a <b><i>"?"</i></b>. Ask the <span class="hover vocab yui-wk-div" data-id='DNS'>DNS</span> what the <span class="hover vocab yui-wk-div" data-id='IP Address'>IP address</span> is of the person on your <span class="hover vocab yui-wk-div" data-id='router'>router</span> you wish to contact. </li>
	<li>After receiving the answer, notice that the <span class="hover vocab yui-wk-div" data-id='IP Address'>IP address</span> is now visible to you on your tablet's screen.</li>
	<li>Using this newly discovered address, send a message to this person, letting them know what items you bought from Amazon. Ask the person to send you a reply. NOTE: If the <span class="hover vocab yui-wk-div" data-id='DNS'>DNS</span> responds with <b><i>"Invalid Address"</i></b> to your request, it is likely that you have mistyped your friend's login ID.</li>
    
	</ul>
	</li><li style="margin-bottom: 5px;">Of course, on the Internet, we can communicate with anyone connected to the network, not just those on our <span class="hover vocab yui-wk-div" data-id='router'>router</span>. Now click the <b><i>"PEERS"</i></b> button on your screen. It will bring up a <b><i>LISTPICKER</i></b> which will display the login IDs of everyone in your class who is also on your network. Locate one of your friends in class who is on the network but not on your <span class="hover vocab yui-wk-div" data-id='router'>router</span> in this list and select this person. Note that the app has filled in the message fields with the <span class="hover vocab yui-wk-div" data-id='DNS'>DNS</span> address in the <b><i>"TO"</i></b> field and an appropriate <b><i>"get"</i></b> request in the message field. Simply press the <b><i>"SEND"</i></b> button to ask the <span class="hover vocab yui-wk-div" data-id='DNS'>DNS</span> to fetch the address of your friend. 
                    </li><li style="margin-bottom: 5px;">Once you have your friend's address, converse with them back and forth with a few messages describing your recent purchases. <b>Remember that all your messages are being logged and will be reviewed by your instructor at the end of this exercise.</b>
    </li><li>After you have finished these exercises, raise your hand to show your instructor your message log.
                          Once your teacher signs off on your activity, take a screenshot of your message log to submit  in your portfolio.</li>
    </ol>
    <h3>Activity 2 - The Lost Messages Problem</h3>
    <div class="pogil yui-wk-div">
    In this POGIL activity, you will work in groups of three to test what happens when two people send 
      simultaneous messages to a recipient using the Mobile CSP <span class="hover vocab yui-wk-div" data-id='DNS'>DNS</span> Simulator app. Here are the roles.
    <ul>
    <li><b>Recipient. </b> The recipient will lead this activity and will receive messages from the 
          other group members and record the results</li>
    <li><b>Sender #1.</b> Sender #1 will send one of the messages to the recipient
        </li>
    <li><b>Sender #2.</b> Sender #2 will send one of the messages to the recipient
        </li>
    </ul>
    <h3>Activity</h3>
    <p>Repeat the following activity three or more times.  Have the two senders enter the <span class="hover vocab yui-wk-div" data-id='IP Address'>IP address</span> of the 
        recipient and a <b><i>unique</i></b> message -- so that the recipient will be able to easily distinguish 
        the two messages.  Now, by coordinating verbally, have both senders press the app’s <b>SEND</b> button at 
        the same time.  For each trial, record the following results.
      </p>
    <table>
    <tbody><tr><th>Trial #</th><th>Number of Messages Received</th><th>Message received</th></tr>
    <tr><td>1</td><td>1</td><td>Hello</td></tr>
    </tbody></table>
    <h3>What you should observe</h3>
    <p>If you repeat this experiment enough times, you should observe that some messages are being lost -- 
        that is, they are not being received by the recipient.  Is that what you observed?
      </p>
    <h3>What explains this behavior</h3>
    <p>
        According to its current design, the app is using a simple TinyWebDB <i><b>mailbox</b></i> variable to store the 
        recipient’s messages.  Initially, this variable is given the value <b><i>EMPTY_MAIL_BOX</i></b> to signify that 
        there are no messages waiting for that recipient.  When the recipient receives a message, it is put 
        into the recipient’s mailbox.  A typical message might be <i><b>sender1:7.13:hello</b></i>. This means that the 
        message “hello” was sent by “sender1” at <span class="hover vocab yui-wk-div" data-id='IP Address'>IP address</span> “7.13”.   When the recipient retrieves the message 
        from mailbox, it replaces it with <i><b>EMPTY_MAIL_BOX</b></i> to signify that the mailbox is empty again.  
        In pseudocode, this is how this algorithm works.
      </p>
    <table>
    <tbody>
    <tr>
    	<th>Recipient</th></tr>
    <tr>
    	<td>
	<pre>
	mailbox ← EMPTY_MAIL_BOX
	Repeat every 3 seconds
	{
	   IF (mailbox is not EMPTY_MAIL_BOX)
	   {
		 Retrieve the message
		 mailbox ← EMPTY_MAIL_BOX
	   }
	}	</pre>
    	</td>
    </tr>
    </tbody></table>
    
    <table>
    <tbody>
    <tr>
    	<th>Sender1</th>
    </tr>
    <tr>
    	<td>
        <pre>recipient’s mailbox ← "sender1:7.13:hello"</pre>
    	</td>
    </tr>
    </tbody></table>
    
    <p>If the recipient only checks the mailbox every 3 seconds, what happens if 2 messages are sent in between the checks? If the message is stored in a single variable, the mailbox, what happens to the first value in a variable if it's reassigned a second value, for example:
    </p>
	<pre>mailbox ← x
    mailbox ← y</pre>
    <h3>Discussion Questions</h3>
    <ol>
    <li style="margin-bottom: 5px;"><b>Lost Messages.</b>  Explain why and how this design could lead to messages being lost when Sender1 
          and Sender2 send their messages at the same time.   Can you devise a sequence of events that shows that 
          the recipient receives the message from Sender2 but not Sender1? 
        </li>
    <li style="margin-bottom: 5px;"><b>(Portfolio) Simple variable vs. a list variable</b>.  The current design uses a simple variable to store 
          a string, either a message “sender1:7.13:hello”  or “EMPTY_MAIL_BOX”.   Discuss why and how a list variable 
          would be a better choice for storing the recipient’s messages. 
        </li>
    <li><b>(Portfolio) List handling algorithm</b>.  Using the following commands to insert and remove messages (msg) 
          into a list mailbox, design pseudocode algorithms for the sender and receiver. Choose one insert and one remove command from the list below and put them in the pseudocode below.
          <ul>
    <li>Insert_at_end_of_list(msg)</li>
    <li>Insert_at_front_of_list(msg)</li>
    <li>Remove_msg_at_end_of_list</li>
    <li>Remove_msg_at_front_of_list</li>
    </ul>
    
    <table>
    <tbody>
    <tr>
    	<th>Recipient</th>
    </tr>
    <tr>
    	<td>
	<pre>
	mailbox ← empty list
	Repeat every 3 seconds
	{
	   Repeat until mailbox is empty list
	   {
		  Remove_________________    
	   }   
	}</pre>
    	</td>
    </tr>
    </tbody></table>
    
    <table>
    <tbody>
    <tr>
    	<th>Sender1</th>
    </tr>
    <tr>
    	<td>
   	<pre>recipient's mailbox ← Insert___________________( "sender1:7.13:hello")</pre>
    	</td>
    </tr>
    </tbody></table>
    
	<p>Discuss your group’s algorithm in a class discussion until consensus is reached on an appropriate algorithm for this problem. Can you defend your solution to this problem by giving an non-computer analogy of a how a similar, related problem would be handled by your solution?</p>
    </li></ol>
    </div>
    

Summary
--------

.. raw:: html

    <p>
    In this lesson, you learned how to:
      <div id="summarylist">
    </div>
    

Self-Check
-----------

.. raw:: html

    <p>
    
    Here is a table of some of the technical terms discussed in this lesson. Hover over the terms to review the definitions.
    <table align="center">
    <tbody>
    <tr>
    <td><span class="hover vocab yui-wk-div" data-id="host">host</span>
    <br/><span class="hover vocab yui-wk-div" data-id="router">router</span>
    <br/><span class="hover vocab yui-wk-div" data-id="IP Address">IP address</span>
    <br/><span class="hover vocab yui-wk-div" data-id="IPv4">IPv4</span>
    <br/><span class="hover vocab yui-wk-div" data-id="IPv6">IPv6</span>
    <br/><span class="hover vocab yui-wk-div" data-id="Scalability">Scalability</span>
    <br/><span class="hover vocab yui-wk-div" data-id="domain name">domain name</span>
    <br/><span class="hover vocab yui-wk-div" data-id="DNS">DNS</span>
    </td>
    </tr>
    </tbody>
    </table>
	<br/>
    
.. mchoice:: mcsp-6-4-1
    :random:
    :practice: T
    :answer_a: is a string of bits that provides a computer's Internet address. 
    :feedback_a: 
    :answer_b: is used to route data through the Internet 
    :feedback_b: 
    :answer_c: consists of 32 bits 
    :feedback_c: 
    :answer_d: consists of 64 bits 
    :feedback_d: This is challenging, but rewarding! IPv4 addresses consist of 32 bits. 
    :correct: a,b,c

    An IPv4 address ____________________. Choose all that apply.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-6-4-2
    :random:
    :practice: T
    :answer_a: IPv4 is being replaced by IPv6 which can address many more devices.
    :feedback_a: 
    :answer_b: Soon new devices will not be able to connected to the internet as addresses run out.
    :feedback_b: 
    :answer_c: The internet will be divided into 64 separate networks each assigned a color and internet addresses will be similar to GREEN-11.22.33.44
    :feedback_c: 
    :correct: a

    IPv4 was designed to be scalable and change in size and scale to meet new demands. But IPv4 is limited to about 4 billion unique IP addresses.  What is planned to fix this as the number of devices on the internet grows beyond this.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


.. mchoice:: mcsp-6-4-3
    :random:
    :practice: T
    :answer_a: creates IP addresses for clients and servers 
    :feedback_a: If it were easy, you wouldn’t be learning anything! The DNS is a lookup service.  It doesn't create IP addresses.
    :answer_b: divides the Internet up into distinct and separate networks 
    :feedback_b: If it were easy, you wouldn’t be learning anything! The DNS is a service that pairs domain names (www.trincoll.edu) with IP addresses (157.252.176.180).
    :answer_c: is managed by a centralized server that knows all of the Internet's domain names 
    :feedback_c: If it were easy, you wouldn’t be learning anything! The DNS is a de-centralized system.  DNS servers are distributed around the Internet and they work together to resolve domain names (www.trincoll.edu) into IP addresses (157.252.176.180).
    :answer_d: translates easy-to-remember domain names into IP addresses 
    :feedback_d: That's right! When we type www.google.com into the address bar, the DNS translates www.google.com into Google's IP address (64.233.160.0) for us. It's much easier for us to remember www.google.com than for us to remember Google's IP address (64.233.160.0)!
    :correct: d

    The Domain Name System __________________. 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-6-4-4
    :random:
    :practice: T
    :answer_a:  The Domain Name Servers (DNS)
    :feedback_a: The DNS provides look-ups for IP Addresses but does NOT assign them.
    :answer_b:  The Network Service Provider
    :feedback_b: 
    :answer_c:  The Browser
    :feedback_c: 
    :answer_d:  The User
    :feedback_d: 
    :correct: b

    Which of the following entities is responsible for creating and assigning IP addresses as new users join a network?


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    <h3>Sample AP CSP Exam Question</h3>
    
.. mchoice:: mcsp-6-4-5
    :random:
    :practice: T
    :answer_a:  about.example.com
    :feedback_a: 
    :answer_b:  example.co.uk
    :feedback_b: 
    :answer_c:  example.com.org
    :feedback_c: 
    :answer_d:  example.org
    :feedback_d: 
    :correct: a

    According to the domain name system (DNS), which of the following is a subdomain of the domain example.com?


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    <br/>
    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1fVkUUFG8QpCQ0T6D85W2rY8mdug2ADdI6MIC2vIzoog/copy" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vRq5M8AQcG2OY4YZJVC2qIqVqz5mMTmr7nSh_a9eTl6TJIeSYW6MCavkoDL7iawKQnz0VuTigisatec/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    <!--Create a new page named 
    &lt;i&gt;&lt;b&gt;IP Addresses and Domain Names&lt;/b&gt;&lt;/i&gt; in your 
    portfolio and write
    brief answers to the following questions.
    
    &lt;ol&gt;
    &lt;li&gt;
    What is DNS and how does it work? How does DNS help you connect to a web server like Amazon?
    &lt;/li&gt;
      &lt;li&gt;Include a screenshot of your message log in the DNS Simulation app in Activity 1.&lt;/li&gt;
     &lt;li&gt; (POGIL)  Discuss why and how a list variable would be a better choice for storing the recipient’s multiple messages in the DNS simulation app.&lt;/li&gt;
      &lt;li&gt;
    (POGIL) Include the pseudocode algorithms you developed for the sender and receiver to handle multiple messages to a recipient.
    &lt;/li&gt;
    
    
    &lt;/ol&gt;-->
    </div>
    </div>
