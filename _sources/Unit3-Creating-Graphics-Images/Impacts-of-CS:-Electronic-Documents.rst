.. image:: ../../_static/MobileCSPLogo.png
    :width: 250
    :align: center

Impacts of CS: Electronic Documents
===================================

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
        generateSummary(EKmapping['3.10']);
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
        "algorithm": "An algorithm is a step-by-step procedures for solving a particular problem.",
        "analog": "An analog device or system is one that represents changing values as continuously variable physical quantities.",
        "ASCII": "ASCII, short for American Standard Code for Information Interchange, is a code for representing English characters as numbers, with each letter assigned a number from 0 to 127.",
        "cloud computing": "Cloud computing relies on sharing resources online on the Internet rather than having data and process located on a personal computer.",
        "cryptography": "Cryptography means secret writing. It is the science of protecting information by transforming it into an unreadable format.",
        "digital": "A digital system is any system based on discontinuous data or events. Computers are digital machines because at the basic level they can distinguish between just two values, 0 and 1.",
        "digital signal processing": "Digital signal processing (DSP) refers to manipulating analog information.",
        "download": "To download data is to copy data (usually an entire file) from an online source to a personal computer.",
        "lossless compression": "Lossless compression is a data compression technique in which no data are lost.",
        "lossy compression": "Lossy compression is a data compression technique in which some amount of data is lost.",
        "megabyte": "A megabyte (MB) is a unit for characterizing the amount of data. It is roughly 1 million bytes or, more precisely, 2<sup>20</sup> bytes, which is 1,048,576 bytes.",
        "megapixel": "A megapixel is one million pixels, used in reference to the resolution of a graphics device.",
        "modeling": "Modeling is the process of representing a real-world object of phenomenon as a set of mathematical equations.",
        "OCR": "Optical character recognition (OCR) is the process of reading text from paper and translating the images into a form that the computer can manipulate.",
        "pixel": "A pixel is short for a picture element, a single point in a graphic image.",
        "raster": "A raster is the rectangular area of a display screen actually being used to display images.",
        "render": "To render refers to the process of adding realism to a computer graphics by adding 3-D qualities, such as shadows and variations in color and shade.",
        "spam":"Spam is electronic junk mail or junk newsgroup postings.",
        "steganography": "Steganogrphy is the art and science of hiding information by embedding messages within other, seemingly harmless messages.",
        "upload": "To upload data means to transmit data from a computer to an online repository or service such as a bulletin board service, or drop box, or network.",
      
      };
      */
    </script>
    <h3 id="est-length">Time Estimate: 135 minutes</h3>
    <a href="http://www.bitsbook.com/wp-content/uploads/2008/12/B2B_3.pdf#page=91" target="_blank"><img align="left" hspace="10" src="../_static/assets/img/blowntobits.jpg" width="150"/></a>
    <p>Computing has transformed our lives in so many ways. And mobile computing, 
    where we are constantly connected to others and to the world via our mobile
    devices, is challenging us right now to come with 
    new norms about privacy, security, the ownership or openness of data and information,
    and other issues. </p>
    <p>Like any technology, mobile computing has both positive and 
    negative impacts. We need to reflect on these impacts in general and we also 
    need to think about the impacts we will create as we build our own mobile apps. </p>
    

Chapter Three: Ghosts in the Machine: Secrets and Surprises of Electronic Documents
------------------------------------------------------------------------------------

.. raw:: html

    <p>
    <p><a href="http://www.bitsbook.com/wp-content/uploads/2008/12/chapter3.pdf">
    Chapter Three of Blown to Bits</a> describes how digital documents, 
    including images and sounds, are represented by sequences of bits. Why do you think this chapter is called "Ghosts in the Machine"?</p>
    <p>As you learned in the previous lesson and as shown in the this diagram, the first step in representing an image is to convert it into a sequence of bits.  This is known as <i style="font-weight: bold;">modeling</i>. The model is an <i><b>abstract representation</b></i> of the original image.</p>
    <div class="yui-wk-div" style="text-align: center"><img class="yui-img selected" src="../_static/assets/img/FaceModel.PNG"/></div>
    <p><b>Activity: </b>Read Chapter Three (up to page 99) to discover what's hidden in electronic documents.</p>
    <ul>
    <li>Part 1: What You See Is Not What the Computer Knows - Read pg. 73 and 74 out loud as a class and discuss the word "redacted." Continue reading this section (up to pg. 80), using the <a href="https://docs.google.com/document/d/1yBzUmMimZ7YVF0x9osqcGRtHP-RkT46MLAjL2mzsAe0/edit?usp=sharing" target="_blank">Conversation Questions Template</a> to write down a question about 3-4 ideas that were important, surprising, or thought provoking. In small groups, discuss your questions. <p><b><i>Metadata</i></b> (data about data) is described and discussed on pg. 78-80. Here are a few additional things you should know about metadata:</p><ul><li>Metadata are used for finding, organizing, and managing information. </li> <li>Metadata can increase the effective use of data or data sets by providing additional information.</li><li> Metadata allow data to be structured and organized.<br/></li></ul>
    </li><br/><li>Part 2: Representation, Reality, and Illusion - Read pg. 80-94 and complete the <a href="https://docs.google.com/document/d/1LvLYKuRZ66FMd_BSkDVBj8rrg6YN5QbHBx8CxcPnq_Q/edit?usp=sharing" target="_blank">Now That's Surprising Template</a>. In small groups, discuss your notes.</li>
    <li>Part 3: Hiding Information in Images (pg. 95-99) is called <b><i>steganography</i></b>. First, answer the question below, then read the chapter pages as needed to help you complete <a href="https://docs.google.com/document/d/1rMlcppxtV-v9Ti7RDe6L6dlCczXXu8oQjZz8f9KLFaE/edit?usp=sharing" target="_blank">this activity</a>—you'll have an opportunity to hide your initials, or some 3-letter word, in an image. Try it, it's fun!</li>
    </ul>
    <iframe frameborder="0" height="550" marginheight="0" marginwidth="0" src="https://mobile-csp.org/webapps/stego/bitmap-editor.html" width="780"></iframe>
    

Still Curious?
---------------

.. raw:: html

    <p>
    <p>Printers sometimes add secret dots to documents when they're printed, very similar to steganography. In fact, the secret dots on a leaked, classified document were able to help the FBI identify a potential suspect. <a href="http://www.bbc.com/future/story/20170607-why-printers-add-secret-tracking-dots" target="_blank">Read more in this article from the BBC.</a></p>
    

Summary
--------

.. raw:: html

    <p>
    In this lesson, you learned how to:
      <div class="yui-wk-div" id="summarylist">
    </div>
    

Self Check
-----------

.. raw:: html

    <p>
    <p>Here is a table of the technical terms introduced in this lesson. Hover over the terms to review the definitions.</p>
    <table align="center">
    <tbody>
    <tr>
    <td><span class="hover vocab yui-wk-div" data-id="algorithm">algorithm</span>
    <br/><span class="hover vocab yui-wk-div" data-id="analog">analog</span>
    <br/><span class="hover vocab yui-wk-div" data-id="ASCII">ASCII</span>
    <br/><span class="hover vocab yui-wk-div" data-id="cloud computing">cloud computing</span>
    <br/><span class="hover vocab yui-wk-div" data-id="cryptography">cryptography</span>
    </td>
    <td><span class="hover vocab yui-wk-div" data-id="digital">digital</span>
    <br/><span class="hover vocab yui-wk-div" data-id="download">download</span>
    <br/><span class="hover vocab yui-wk-div" data-id="lossless compression">lossless compression</span>
    <br/><span class="hover vocab yui-wk-div" data-id="lossy compression">lossy compression</span>
    <br/><span class="hover vocab yui-wk-div" data-id="megabyte">megabyte</span>
    </td>
    <td><span class="hover vocab yui-wk-div" data-id="megapixel">megapixel</span>
    <br/><span class="hover vocab yui-wk-div" data-id="modeling">modeling</span>
    <br/><span class="hover vocab yui-wk-div" data-id="OCR">OCR</span>
    <br/><span class="hover vocab yui-wk-div" data-id="pixel">pixel</span>
    <br/><span class="hover vocab yui-wk-div" data-id="raster">raster</span>
    </td>
    <td><span class="hover vocab yui-wk-div" data-id="render">render</span>
    <br/><span class="hover vocab yui-wk-div" data-id="spam">spam</span>
    <br/><span class="hover vocab yui-wk-div" data-id="steganography">steganography</span>
    <br/><span class="hover vocab yui-wk-div" data-id="upload">upload</span>
    <br/><span class="hover vocab yui-wk-div" data-id=""></span>
    </td>
    </tr>
    </tbody>
    </table>
    <br/>
.. mchoice:: repl-mcsp-3-10-1
    :random:
    :practice: T
    :answer_a: (A) Determining the likelihood that the photo is a picture of the sky
    :feedback_a: 
    :answer_b: (B) Determining the likelihood that the photo was taken at a particular public event
    :feedback_b: 
    :answer_c: (C) Determining the number of people that appear in the photo
    :feedback_c: 
    :answer_d: (D) Determining the usability of the photo for projection onto a particular color background
    :feedback_d: 
    :correct: b

    AP 2021 Sample Question: A digital photo file contains data representing the level of red, green, and blue for each pixel in the photo. The file also contains metadata that describe the date andgeographic location where the photo was taken. For which of the following goals would analyzing the metadata be more appropriate than analyzing the data?


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>



Reflection: For Your Portfolio
-------------------------------

.. raw:: html

    <p><div class="yui-wk-div" id="portfolio">
    <p>Answer the following portfolio reflection questions as directed by your instructor. Questions are also available in this <a href="https://docs.google.com/document/d/1TC5ohH5TAWHqR1awhdqrDAT6Cc_sR71imfpXMo-IXNk/edit?usp=sharing" target="_blank">Google Doc</a> where you may use File/Make a Copy to make your own editable copy.</p>
    <div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="https://docs.google.com/document/d/e/2PACX-1vRE5WwinP0Koy6p8QR03Ph7VnVd2lqw-K71kNETNxqAsu1HvuTikf7BVuHHfIEu40rd1R23TecNFqpE/pub?embedded=true" style="height:30em;width:100%"></iframe></div>
    <!--  &lt;h2&gt;Homework: For Your Portfolio&lt;/h2&gt;
    
      &lt;p&gt;Create a page called &lt;b&gt;&lt;i&gt;Blown to Bits Chapter 3&lt;/i&gt;&lt;/b&gt; under the &lt;i&gt;Homework&lt;/i&gt; category of your portfolio and write answers using complete sentences to the following questions on that page.&lt;/p&gt;
      
      &lt;ol&gt;
        &lt;b&gt;Short answer:&lt;/b&gt;&lt;br&gt;
        &lt;li&gt;What is metadata? Give an example of how a piece of metadata could increase the usefulness of an image or document.&lt;/li&gt;
        &lt;li&gt;What is a model? &lt;/li&gt;
        &lt;li&gt;What&#39;s the difference between a raster image and an ASCII representation of a text document?&lt;/li&gt;
        &lt;li&gt;What are filename extensions? What are they used for?&lt;/li&gt;
        &lt;li&gt;What is lossless representation? What is lossy representation? What are the trade-offs in using each representation?&lt;/li&gt;
        &lt;li&gt;What is steganography and what is it used for? Describe in your own words the steganographic algorithm used in the activity.&lt;/li&gt;
        &lt;li&gt;&lt;i&gt;What would you have to do to delete a document from your computer so that it could not possibly be read by anyone else?&lt;/i&gt;&lt;/li&gt;
        &lt;li&gt;What is free and open source software? Provide an example.&lt;/li&gt;
        &lt;b&gt;Free Response:&lt;/b&gt;&lt;br&gt;
        &lt;li&gt;How has retouching become a controversial issue? Give an example.&lt;/li&gt;
        &lt;li&gt;Would you rather own a camera (or camera phone) with a higher number of megapixels or lower? Explain.&lt;/li&gt;
        &lt;li&gt;Other than digital images, what might be an example of a computer model? Explain your answer based on the definition of a model.&lt;/li&gt;
        &lt;li&gt;The code that implements App Inventor is open source and its impact on education is obvious.  Find another example of open source software and describe its positive impact on education, business or society.&lt;/li&gt;
      &lt;/ol&gt;-->
    </div>
    </div>