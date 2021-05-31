.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Computer Networking
===================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
      $(document).ready(function() {
        generateSummary(EKmapping['6.02']);
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
        "Latency" : "a measure of the time it takes for a piece of data to reach its destination",
        "Bandwidth" : "the rate at which data is downloaded or uploaded in a network",
        "Digital Divide": "the gap between those who have access to the Internet and computers and those who do not",
        "Network" : "A computer network is a group of two or more computers that are linked together.",
        "World Wide Web" : "An Internet application that is based on the HTTP protocol.",
        "Client" : "A client is a computer or software application that requests services from a server located on the internet -- e.g., a Web browser is an example of a client.",
        "SMTP/POP" : "Simple Mail Transfer Protocol (SMTP) and Post Office Protocol (POP) are sets of rules that govern the email servcies.",
        "URI" : "Uniform Resource Identifier (URI) is WWW identier that uniquely identifies a resource on the WWW -- e.g., http://host.com'.",
        "Protocol" : "A protocol is a system of rules that govern the behavior of some system.",
        "Modem" : "A modem is a device that connects a computer to an Internet Service Provider (ISP).",
        "Ethernet" : "An ethernet is a network that uses wires to connect computers.",
        "Host" : "An Internet host computer is a computer that's connected directly to the Internet -- often a computer that provides certain services or resources.",
        "LAN" : "A local area network (LAN) connects computers within a school or home.",
        "WAN" : "A wide area network (WAN) connects devices over a broad geographic region -- e.g., a telephone network.",
        "Server" : "A server is a host that provides some kind of service -- e.g., Google's Gmail service.",
        "HTTP" : "The HyperText Transfer Protocol (HTTP) is the set of rules that governs the WWW application.",
        "HTML" : "The HyperText Markup Language (HTML) is a language for formatting Web pages.",
        "Router" : "A router is a device that transmits data between two different networks.",
        "Internet Service Provider" : "An Internet service provider (ISP) is a company that provides customers with Internet access.",
        "Wifi" : "A Wifi network uses radio waves to connect devices (computers, smart phones, printers).",
      };      */
    
    </script>
    <!-- can use: #self-check, #still-curious, .pogil, #portfolio -->
    <h3 id="est-length"><b>Time Estimate: 45 minutes</b></h3>
    

Introduction and Goals
-----------------------

.. raw:: <span class="hover vocab yui-wk-div" data-id='html'>html</span>

    <p>
    <p>
      The Internet is one of the seven Big Ideas of the CS Principles (CSP) curriculum and
      rightly so:  The Internet has had a tremendous impact on our lives and on modern society.
      Yet, despite its impact and influence, most people do not really understand what the Internet  
      is and how it works.
    </p>
    <p>
      We introduced the Internet in <a href="https://course.mobilecsp.org/mobilecsp/unit?unit=1&amp;lesson=146" target="_blank">Unit 2</a>,
      where we covered the following points:
      </p><ul>
    <li>The Internet is the global public <span class="hover vocab yui-wk-div" data-id='network'>network</span> of independent and autonomous 
          networks that are governed by the Internet <span class="hover vocab yui-wk-div" data-id='Protocol'>Protocol</span> Suite.
        </li>
    <li>The Internet is <i><b>not</b></i> the same as the <span class="hover vocab yui-wk-div" data-id='World Wide Web'>World Wide Web</span> (WWW).  The
          WWW is an application that runs on the Internet using the <span class="hover vocab yui-wk-div" data-id='HTTP'>HTTP</span> <span class="hover vocab yui-wk-div" data-id='protocol'>protocol</span>.
        </li><li>The Internet is based on <i>open (non-proprietary) standards</i>, which has
          enabled it to grow exponentially since its inception in the early 1980s. 
        </li>
    <li>The cloud is an everyday term for the Internet and/or WWW.
        </li>
    </ul>
    <p>This lesson provides a high-level overview of some of the Internet's
      and WWW's key concepts and terminology.   A follow-up lesson will go into 
      greater detail in explaining how the Internet works.
    </p>
    

Learning Activities
--------------------

.. raw:: <span class="hover vocab yui-wk-div" data-id='html'>html</span>

    <p><h3>Part 1.  Basic Concepts and Terminology</h3>
    <p>
      In Unit 2 we defined the Internet as a <i><b><span class="hover vocab yui-wk-div" data-id='network'>network</span> of disparate networks</b></i> that is governed by 
      systems of rules, known as <i><b>protocols</b></i>.  In this first presentation we'll see some 
      examples of different types of networks and we'll learn about the role
      that special devices known as <i><b>routers</b></i> play in enabling communication between different
      types of networks.
    </p>
    
    
    (<a href="https://docs.google.com/presentation/d/1tMJPSDrzOtXJFDVxkVbMvZGw-uzADpiIdM4gXe9f54I/edit#slide=id.p5" target="_blank" title="">Slides</a>)
    
    
.. youtube:: 42F4dByfRtY
        :width: 650
        :height: 415
        :align: center

.. raw:: <span class="hover vocab yui-wk-div" data-id='html'>html</span>

    <div id="bogus-div">
    <p></p>
    </div>

    (<a href="<span class="hover vocab yui-wk-div" data-id='http'>http</span>://www.teachertube.com/video/359108" target="_blank">Teacher Tube version</a>)
    
    <h3>Activity 1 </h3>
    <!-- Map no longer there --
    Explore the &lt;a href=&quot;<span class="hover vocab yui-wk-div" data-id='http'>http</span>://www.internetsociety.org/map/global-internet-report&quot; target=&quot;_blank&quot; data-saferedirecturl=&quot;https://www.google.com/url?hl=en&amp;amp;q=<span class="hover vocab yui-wk-div" data-id='http'>http</span>://www.internetsociety.org/map/global-internet-report&amp;amp;source=gmail&amp;amp;ust=1499951266125000&amp;amp;usg=AFQjCNG3EJa_opVQ6rM8gBg388P1AmsF7A&quot; style=&quot;color: rgb(17, 85, 204);&quot;&gt;Internet Society’s Interactive map&lt;/a&gt; of global internet statistics and choose different data sets from the menu at the top right to answer these questions. You may want to guess the answer in your class before checking the map. -->
    Answer the following questions in pairs, groups, or as class discussion:
    <ul>
    <li>Which country has the fastest download speeds on the Internet? Is the U.S. in the top 3? Try to guess the answers to these before looking them up on <a href="<span class="hover vocab yui-wk-div" data-id='http'>http</span>://www.speedtest.net/global-index" target="_blank">Speed Test Global Stats</a>. </li>
    <li>What is the percentage of Internet user penetration for the United States? The <b>Internet user penetration</b> is the percentage of the population that has access to and uses the Internet. Access to the Internet depends on the ability to connect a computing device to an Internet-connected device like a <span class="hover vocab yui-wk-div" data-id='router'>router</span>. Do you think we are close to 100%? Try to guess before you look online. You may get different data depending on the date of the data.  Some sources are <a href="https://en.wikipedia.org/wiki/List_of_countries_by_number_of_Internet_users" target="_blank">https://en.wikipedia.org/wiki/List_of_countries_by_number_of_Internet_users</a>, <a href="https://www.internetworldstats.com/stats.htm" target="_blank">https://www.internetworldstats.com/stats.htm</a>,  <a href="<span class="hover vocab yui-wk-div" data-id='http'>http</span>://www.internetlivestats.com/internet-users-by-country/" target="_blank">Internet Live Stats site</a> which presents  Internet penetration data by country.  </li>
    <li>Do all countries have similar Internet user penetration or is there a <b><span class="hover vocab yui-wk-div" data-id='digital divide'>digital divide</span></b> (a gap between those who have Internet access and those who don't)? How big is the <span class="hover vocab yui-wk-div" data-id='digital divide'>digital divide</span> between continents or countries? Find data online using the sources above or others to answer this question.
      </li>
    <li>What can we do to reduce the effects of the <span class="hover vocab yui-wk-div" data-id='digital divide'>digital divide</span> both locally and globallly? Discuss in your class.</li>
    </ul>
    <p>The <b><span class="hover vocab yui-wk-div" data-id='digital divide'>digital divide</span></b> refers to a gap or differing access to computing devices and the Internet based on socioeconomic, geographic, or demographic characteristics. It can affect both groups and individuals and can be affected by individuals, organizations and government actions. The <span class="hover vocab yui-wk-div" data-id='digital divide'>digital divide</span> raises issues of equity, access, and influence, both globally and locally. The <span class="hover vocab yui-wk-div" data-id='digital divide'>digital divide</span> is huge when we compare first and third world countries. But even students in the U.S. experience the <span class="hover vocab yui-wk-div" data-id='digital divide'>digital divide</span> in different schools. If you're interested in this topic, watch the National Geographic's <a href="<span class="hover vocab yui-wk-div" data-id='http'>http</span>://www.digitaldivide.com/" target="_blank" title="">Without a Net: <span class="hover vocab yui-wk-div" data-id='Digital Divide'>Digital Divide</span> documentary</a>. The documentary can also be found on <a href="https://www.youtube.com/watch?v=lBAkCgDD-BE" target="_blank" title="">YouTube</a>.   </p>
    <!-- Explore it&#39;s evolution using this 
    &lt;a href=&quot;<span class="hover vocab yui-wk-div" data-id='http'>http</span>://evolutionofweb.appspot.com/?hl=en#/growth/day&quot; target=&quot;_blank&quot;&gt;interactive graphic&lt;/a&gt;
     to see what new technologies have impacted growth.&lt;/p&gt;
    -->
    <h3>Part 2. <span class="hover vocab yui-wk-div" data-id='Client'>Client</span>/<span class="hover vocab yui-wk-div" data-id='Server'>Server</span> Model</h3>
    <p>When you are using the Internet to read email or visit a web site, your device (phone or tablet or computer)
      is playing the role of a <i><b><span class="hover vocab yui-wk-div" data-id='client'>client</span></b></i>.  It is using <span class="hover vocab yui-wk-div" data-id='client'>client</span> software, such as a web browser or email application 
      to communicate with a <i><b><span class="hover vocab yui-wk-div" data-id='server'>server</span></b></i>, which is computer on the Internet that provides a specific service, such as
      email or web browsing.  Clients and servers form a <b><span class="hover vocab yui-wk-div" data-id='computing system'>computing system</span></b> which is a group of computing devices and programs working together for a common purpose. The TCP and IP protocols <i><b>route</b></i> messages between the clients and servers finding a path from the sender to the receiver. In this next presentation we'll look at how communication occurs between a <span class="hover vocab yui-wk-div" data-id='client'>client</span>   and <span class="hover vocab yui-wk-div" data-id='server'>server</span> using the <i><b><span class="hover vocab yui-wk-div" data-id='HTTP'>HTTP</span> <span class="hover vocab yui-wk-div" data-id='Protocol'>Protocol</span></b></i>.
    </p>
      
    (<a href="https://docs.google.com/presentation/d/1tMJPSDrzOtXJFDVxkVbMvZGw-uzADpiIdM4gXe9f54I/edit#slide=id.p5" target="_blank" title="">Slides</a>)
    
    
    
.. youtube:: DDGnPTpk_G8
        :width: 650
        :height: 415
        :align: center

.. raw:: <span class="hover vocab yui-wk-div" data-id='html'>html</span>

    <div id="bogus-div">
    <p></p>
    </div>

    (<a href="<span class="hover vocab yui-wk-div" data-id='http'>http</span>://www.teachertube.com/video/359099" target="_blank">Teacher Tube version</a>)
    
    <h3>Activity 2:  <span class="hover vocab yui-wk-div" data-id='Client'>Client</span>/<span class="hover vocab yui-wk-div" data-id='Server'>Server</span> Model</h3>
    <p>
    Complete the activity in <a href="https://docs.google.com/document/d/1_98lN-rMLDScg9EPTUdFfdY36cGFd2njqkFF2NLtPSI/edit?usp=sharing" target="_blank">this worksheet</a> to review the <span class="hover vocab yui-wk-div" data-id='client'>client</span>/<span class="hover vocab yui-wk-div" data-id='server'>server</span> model.
    </p>
    <!--
    &lt;table&gt;
      &lt;tbody&gt;&lt;tr&gt;
        &lt;td&gt;The previous lecture described the &lt;i&gt;<span class="hover vocab yui-wk-div" data-id='client'>client</span>/<span class="hover vocab yui-wk-div" data-id='server'>server</span>&lt;/i&gt; model as it applies to accessing a Web page.  Our App
      Inventor programming platform is another example of this model.  Using this picture as a model, 
      work out the details of what happens when you open an existing project in App Inventor.
          &lt;ul&gt;
            &lt;li&gt;What is the <span class="hover vocab yui-wk-div" data-id='client'>client</span>?&lt;/li&gt;
            &lt;li&gt;What is the <span class="hover vocab yui-wk-div" data-id='server'>server</span>&#39;s URL?&lt;/li&gt;
            &lt;li&gt;What <span class="hover vocab yui-wk-div" data-id='protocol'>protocol</span> is being used?&lt;/li&gt;
            &lt;li&gt;What information is sent to the <span class="hover vocab yui-wk-div" data-id='server'>server</span> to request a specific project 
              and what does the <span class="hover vocab yui-wk-div" data-id='server'>server</span> send back?
            &lt;/li&gt;
          &lt;/ul&gt;
        &lt;/td&gt;
        &lt;td&gt;
          &lt;img src=&quot;assets/img/ClientServer.png&quot; align=&quot;right&quot; width=&quot;300px&quot;&gt; 
        &lt;/td&gt;
      &lt;/tr&gt;
    &lt;/tbody&gt;&lt;/table&gt;
    &lt;p&gt;&lt;/p&gt;
    -->
    <h3>Part 3. Internet Performance</h3>
    <p>In this next presentation we learn about two important measures of Internet performance.  The first, <b><i><span class="hover vocab yui-wk-div" data-id='bandwidth'>bandwidth</span></i></b>,
      refers to the amount of data that can be sent in a fixed amount of time and is usually measured in kilobits or megabits
      per second.  The second, <b><i><span class="hover vocab yui-wk-div" data-id='latency'>latency</span></i></b>, refers to how long it takes a packet of data to go from its source (e.g., 
      a <span class="hover vocab yui-wk-div" data-id='client'>client</span>) to its destination (e.g., a <span class="hover vocab yui-wk-div" data-id='server'>server</span>).   You'll be introduced to some easy-to-use tools that will enable you to
      measure <span class="hover vocab yui-wk-div" data-id='bandwidth'>bandwidth</span> and <span class="hover vocab yui-wk-div" data-id='latency'>latency</span> from your home or school networks. 
    </p>
    
    (<a href="https://docs.google.com/presentation/d/1tMJPSDrzOtXJFDVxkVbMvZGw-uzADpiIdM4gXe9f54I/edit#slide=id.p5" target="_blank" title="">Slides</a>)
    
    
.. youtube:: pg7oQhR5QX0
        :width: 650
        :height: 415
        :align: center

.. raw:: <span class="hover vocab yui-wk-div" data-id='html'>html</span>

    <div id="bogus-div">
    <p></p>
    </div>

    (<a href="<span class="hover vocab yui-wk-div" data-id='http'>http</span>://www.teachertube.com/video/359096" target="_blank">Teacher Tube version</a>)
    
    <h3>Activity 3: Measuring <span class="hover vocab yui-wk-div" data-id='Bandwidth'>Bandwidth</span> and <span class="hover vocab yui-wk-div" data-id='Latency'>Latency</span></h3>
    
    Use the <a data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=<span class="hover vocab yui-wk-div" data-id='http'>http</span>://www.bandwidthplace.com/&amp;source=gmail&amp;ust=1499951266125000&amp;usg=AFQjCNHMHLIizAlqwNGn2AsPqZzvfHye1w" href="<span class="hover vocab yui-wk-div" data-id='http'>http</span>://www.bandwidthplace.com/" style="color: rgb(17, 85, 204);" target="_blank"><span class="hover vocab yui-wk-div" data-id='http'>http</span>://www.bandwidthplace.com/</a> tool (or <a data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=<span class="hover vocab yui-wk-div" data-id='http'>http</span>://speedtest.xfinity.com/)&amp;source=gmail&amp;ust=1499951266126000&amp;usg=AFQjCNG5a3gBgWzaRAyVZaY_RjH_iMDRxg" href="<span class="hover vocab yui-wk-div" data-id='http'>http</span>://speedtest.xfinity.com/)" style="color: rgb(17, 85, 204);" target="_blank"> <span class="hover vocab yui-wk-div" data-id='http'>http</span>://speedtest.xfinity.com/)</a> to measure the <span class="hover vocab yui-wk-div" data-id='bandwidth'>bandwidth</span> and <span class="hover vocab yui-wk-div" data-id='latency'>latency</span> of your Internet connection.
    <ol>
    <li>What are the download and upload speeds for your Internet connection. Note that these <span class="hover vocab yui-wk-div" data-id='bandwidth'>bandwidth</span> are measured in megabits per second (Mbps). Why do you think Internet Service Providers (ISPs) provide different bandwidths for downloading and uploading from the Internet?</li>
    <li> Measure the <span class="hover vocab yui-wk-div" data-id='bandwidth'>bandwidth</span> at school and at home. Are they different? How do they compare to the fastest download speeds you found in Activity 1 on the <a href="<span class="hover vocab yui-wk-div" data-id='http'>http</span>://www.speedtest.net/global-index" target="_blank">Speed Test Global Stats site</a>?
      </li>
    <li>This speed test also provides a <span class="hover vocab yui-wk-div" data-id='latency'>latency</span> test using a utility called ping which returns the amount of time (usually measured in milliseconds) to send a small packet of data from one computer (the bandwidthplace <span class="hover vocab yui-wk-div" data-id='server'>server</span>) to another (your computer). What is the <span class="hover vocab yui-wk-div" data-id='latency'>latency</span> for your connection? Why is this a useful measurement?</li>
    </ol>
    <!-- 
    &lt;h3&gt;Activity 4 - Measuring <span class="hover vocab yui-wk-div" data-id='Latency'>Latency</span>&lt;/h3&gt;   
    
    As you learned in the slide presentation <span class="hover vocab yui-wk-div" data-id='latency'>latency</span> is a measure of the time
    it takes information to get from its source to its destination.
    
    &lt;ul&gt;
    &lt;li&gt;Use &lt;a target=&quot;_blank&quot; href=&quot;<span class="hover vocab yui-wk-div" data-id='http'>http</span>://centralops.net/co/&quot;&gt;Central Ops Ping tool&lt;/a&gt; to measure
    the average <span class="hover vocab yui-wk-div" data-id='latency'>latency</span> between its website and the following sites:
    &lt;ol&gt;
    &lt;li&gt;<span class="hover vocab yui-wk-div" data-id='http'>http</span>://google.com
    &lt;/li&gt;&lt;li&gt;<span class="hover vocab yui-wk-div" data-id='http'>http</span>://whitehouse.gov
    &lt;/li&gt;&lt;li&gt;<span class="hover vocab yui-wk-div" data-id='http'>http</span>://mobile-csp.org
    &lt;/li&gt;&lt;/ol&gt; 
    
    &lt;/li&gt;&lt;/ul&gt;
    -->
    <h3>Still Curious</h3>
    <ul>
    <li><a href="https://youtu.be/ICJqv0TN6-c" target="_blank">This video</a> contains a very visual example of <span class="hover vocab yui-wk-div" data-id='bandwidth'>bandwidth</span> using balloons and pipes that you could even recreate in your classroom.</li>
    <li><a href="https://youtu.be/F1a-eMF9xdY" target="_blank">This video</a> compares <span class="hover vocab yui-wk-div" data-id='bandwidth'>bandwidth</span> to vehicles such as buses and race cars. It also explains <span class="hover vocab yui-wk-div" data-id='latency'>latency</span> concepts in terms of the speed of light and queues (lines).</li>
    </ul>
    

Summary
--------

.. raw:: <span class="hover vocab yui-wk-div" data-id='html'>html</span>

    <p>
    In this lesson, you learned how to:
      <div class="yui-wk-div" id="summarylist">
    </div>
    

Self-Check
-----------

.. raw:: <span class="hover vocab yui-wk-div" data-id='html'>html</span>

    <p>
    
    Here is a table of some of the technical terms we've introduced in this
    lesson. Hover over the terms to review the definitions.
    <table align="center">
    <tbody><tr>
    <td><span class="hover vocab yui-wk-div" data-id="network">network</span>
    <br/><span class="hover vocab yui-wk-div" data-id="World Wide Web">World Wide Web</span>
    <br/><span class="hover vocab yui-wk-div" data-id="client">client</span>
    <br/><span class="hover vocab yui-wk-div" data-id="server">server</span>
    <br/><span class="hover vocab yui-wk-div" data-id="computing system">computing system</span>
    <br/><span class="hover vocab yui-wk-div" data-id="protocol">protocol</span>
    <br/><span class="hover vocab yui-wk-div" data-id="SMTP/POP">SMTP/POP</span>
    <br/><span class="hover vocab yui-wk-div" data-id="URI">URI</span>
    </td>
    <td>
    <span class="hover vocab yui-wk-div" data-id="digital divide">digital divide</span>
    <br/> <span class="hover vocab yui-wk-div" data-id="ethernet">ethernet</span>
    <br/><span class="hover vocab yui-wk-div" data-id="host">host</span>
    <br/><span class="hover vocab yui-wk-div" data-id="bandwidth">bandwidth</span>
    <br/><span class="hover vocab yui-wk-div" data-id="latency">latency</span>
    <br/><span class="hover vocab yui-wk-div" data-id="modem">modem</span>
    <br/><span class="hover vocab yui-wk-div" data-id="LAN">LAN</span>
    <br/><span class="hover vocab yui-wk-div" data-id="WAN">WAN</span>
    </td>
    <td>
    <span class="hover vocab yui-wk-div" data-id="HTTP">HTTP</span>
    <br/><span class="hover vocab yui-wk-div" data-id="HTML">HTML</span>
    <br/><span class="hover vocab yui-wk-div" data-id="router">router</span>
    <br/><span class="hover vocab yui-wk-div" data-id="routing">routing</span>
    <br/><span class="hover vocab yui-wk-div" data-id="Internet Service Provider">Internet Service Provider (ISP)</span>
    <br/><span class="hover vocab yui-wk-div" data-id="wifi">wifi</span>
    </td>
    </tr>
    </tbody></table>
    
.. mchoice:: mcsp-6-2-1
    :random:
    :practice: T
    :answer_a: True
    :feedback_a: 
    :answer_b: False
    :feedback_b: Don’t worry, it’s hard! Let’s go back and try it again.
    :correct: a

    True or False: Cloud computing is made possible by the Internet and the World Wide Web and employs a computation model known as client-server computing. 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-6-2-2
    :random:
    :practice: T
    :answer_a: a. client
    :feedback_a: 
    :answer_b: b. server
    :feedback_b: Of course it’s tough – school is here to makes our brains stronger!
    :correct: a

    A phone is an example of a __________. 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-6-2-3
    :random:
    :practice: T
    :answer_a: a. client
    :feedback_a: Of course it’s tough – school is here to makes our brains stronger!
    :answer_b: b. server
    :feedback_b: 
    :correct: b

    Google's search engine is an example of a __________. 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-6-2-4
    :random:
    :practice: T
    :answer_a: how fast your computer can connect to the Internet 
    :feedback_a: We’re in the learning zone today. Mistakes are our friends! 
    :answer_b: the amount of time it takes to send data over the Internet 
    :feedback_b: We’re in the learning zone today. Mistakes are our friends! 
    :answer_c: the average length of e-mails that you can send on a daily basis
    :feedback_c: We’re in the learning zone today. Mistakes are our friends! 
    :answer_d: the amount of data that can be sent in a fixed amount of time
    :feedback_d: That's right. Bandwidth measures how much data you can send in a given amount of time.
    :correct: d

    Bandwidth measures ___________________. 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. mchoice:: mcsp-6-2-5
    :random:
    :practice: T
    :answer_a:  the amount of time it takes to send a message over the Internet  
    :feedback_a: Right. Latency measures the amount of time, usually in milliseconds, that it takes a message to go from its source to its destination.
    :answer_b:  the average number of messages you send over the Internet in a day  
    :feedback_b: This is challenging, but rewarding! 
    :answer_c:  how much data can you send in a specific amount of time.  
    :feedback_c: This is challenging, but rewarding! 
    :answer_d:  the size of the messages that you send over the Internet 
    :feedback_d: This is challenging, but rewarding! 
    :correct: a

    Latency measures ___________________. 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


.. mchoice:: mcsp-6-2-6
    :random:
    :practice: T
    :answer_a: (A) A school allows students to bring a graphing calculator from home to complete in-class mathematics assignments.
    :feedback_a: 
    :answer_b: (B) A school allows students to bring a tablet computer to class every day to participate in graded quizzes.
    :feedback_b: 
    :answer_c: (C) A school provides a laptop or tablet computer to all students enrolled at the school.
    :feedback_c: 
    :answer_d: (D) A school recommends that all students purchase a computer with as much processing speed as possible so that projects run faster.
    :feedback_d: 
    :correct: c

    AP 2021 Sample Question: Which of the following school policies is most likely to have a positive impact on the digital divide?


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    <!-- 
    &lt;question quid=&quot;5678091720458240&quot; weight=&quot;1&quot; instanceid=&quot;FnawopZ2OTvY&quot;&gt;
    &lt;/question&gt;&lt;br&gt;
    &lt;question quid=&quot;5668235307384832&quot; weight=&quot;1&quot; instanceid=&quot;kZXOrFS4rhrH&quot;&gt;
    &lt;/question&gt;&lt;br&gt;
    &lt;question quid=&quot;5756035713204224&quot; weight=&quot;1&quot; instanceid=&quot;SwCp6lqMuPzq&quot;&gt;
    &lt;/question&gt;&lt;br&gt;
    -->
    

Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1OUV9uARx42QOwkgBvuT8Lsf5wetf1Z9LYDUbLBidR7c/edit?usp=sharing" target="_blank" title="">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vT7EkY_6ep9Idg3YusbkhiFFz33AcHh-cgeO5KJo2TKxqtsRQc200RL0wd4oZEhQdZ7-GHVrUKOD13m/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    <!--Create a page on your portfolio named &lt;i&gt;Internet Basic Concepts&lt;/i&gt; in your portfolio and answer the following questions:
    &lt;ol&gt;
     
      &lt;li&gt; What is bandwidth? What do you think affects the differences in bandwidth globally as well as in different locations in the U.S.?&lt;/li&gt;
      &lt;li&gt;
        What is latency? How does it differ from bandwidth? Why is it a useful measure?&lt;/li&gt;
    &lt;li&gt;What is the digital divide? What are some ways to reduce the effects of the digital divide?&lt;/li&gt;
      &lt;/ol&gt;-->-
    </div>
    </div>